import importlib
import json
import keyword
import os
import re
import sys
import time

from jinja2 import PackageLoader, Environment

from utils import get_lower_case_name, get_proj_path, get_py_file_pathes, handle_cls, hump2str


def gen_all_mds_path(project_path, out_put_path):
    content = os.popen('find ' + project_path + " -name '*.md'").read()
    # 排除其他的md
    mds = [md for md in content.splitlines() if not (md.endswith("CHANGELOG.md") or md.endswith("README.md"))]
    # print(len(mds))
    d = {}
    grpc = {}
    http = {}
    for i in mds:
        if "http" in i:
            kws = ["/interface/", "/admin/", "/job/"]
            for kw in kws:
                idx = i.find(kw)
                if idx == -1:
                    continue
                else:
                    rest_path = i[i.find(kw) + len(kw):]
                    service = rest_path.split("/")[0]
                    http.setdefault(service, []).append(i)
                    # http.setdefault(service, []).append(rest_path)

        elif "grpc" in i:
            for kw in ["/service/", "/interface/"]:  # 通过关键字得到path
                idx = i.find(kw)
                kw_ = kw
                if idx != -1:
                    break
            rest_path = i[idx + len(kw_):]
            service = rest_path.split("/")[0]
            grpc.setdefault(service, []).append(i)
            # grpc.setdefault(service, []).append(rest_path)
    d['http'] = http
    d['grpc'] = grpc

    # print(json.dumps(d, ensure_ascii=False, indent=4))

    with open(out_put_path, "w") as f:
        json.dump(d, f, ensure_ascii=False, indent=4)


def generate(input_json_path, output_path=None, category="grpc"):
    with open(input_json_path, "r") as f:
        c = json.load(f)

    for service in c[category]:
        service_name = service
        part_content = []
        files = c[category][service]
        for file in files:
            file_path = file
            with open(file_path, "r") as f:
                content = f.read()

            pat = re.compile('## ' + '(.*?)' + '#### 响应', re.S)
            results = pat.findall(content)

            for r in results:
                lines = r.splitlines()
                d = {"interface": lines[0], "desc": lines[1]}
                # if d['interface'] == '/live.xuserex.v1.dmConfig/WearForOld':  # debug
                #     print(1)
                method = 'grpc_call'
                for line in lines:
                    line = line.replace("||", "|")
                    if line.startswith("|") and ord('a') <= ord(line[1]) <= ord('z'):
                        # p = line
                        p = [i for i in line.split("|") if i != ""]
                        # 处理多个数据的情况
                        # 先找
                        # 再长度
                        p_field = p[0].split(' ')
                        rst = re.search('form:"' + '(.*?)' + '"', p_field[0])
                        if rst:
                            pp = rst.group(1)
                            p[0] = pp
                        elif len(p_field) == 1:
                            p[0] = p_field[0]
                        else:
                            print(d['interface'], line, file)
                        # 处理多个数据的情况 end
                        k = ["param_name", "is_required", "type"]
                        dic = dict(zip(k, p))
                        d.setdefault("params", []).append(dic)
                # print(d)
                func_name = d['interface'].split('/')[-1]

                func_name = get_lower_case_name(func_name)
                if func_name in keyword.kwlist:
                    func_name = f"{func_name}_"

                params = d.get("params")
                func_params = []
                if params:
                    for p in params:
                        param = p['param_name']
                        if param in keyword.kwlist:
                            param = f"**{param}_"
                            code_p = f"{param}"
                        elif p['is_required'] == "否":
                            code_p = f"{param}=None"
                        else:
                            code_p = f"{param}"
                        func_params.append(code_p)

                    func_params = sorted(func_params, key=lambda i: i.endswith("=None"))
                    func_params = sorted(func_params, key=lambda i: i.startswith("**"))
                    code_session = f"""
    @{method}(path="{d['interface']}")
    def {func_name}(self, {", ".join(func_params)}):
        \"\"\"{d['desc']}"\"\"\n"""
                    # print(code_session)
                    part_content.append(code_session)

            file_name = service_name.split(".")[-1]
            cls_content = f"""from tiny import grpc_call

class {file_name.capitalize().replace("-", "_")}(object):
    def __init__(self,service_name):
        self.service_name=service_name
    {"".join(part_content)}"""
            # print(cls_content)
        if output_path is None:
            venv_idx = get_proj_path().find("venv")
            if venv_idx != -1:
                output_path = get_proj_path()[:venv_idx] + 'api'
            else:
                output_path = os.getcwd() + '/api'

        if os.path.exists(output_path):
            with open(f"{output_path}/{file_name.replace('-', '_')}.py", "w") as f:
                f.write(cls_content)


def pre(spec_dir='app'):
    prj_path = "go-live"
    os.chdir(prj_path)

    os.system('git reset --hard')
    os.system('git clean -d -f')
    result = os.system('git checkout master')
    if result != 0:
        os.system('git checkout master')
    os.system('git pull -p')
    os.chdir(sys.path[0])
    return os.path.join(prj_path, spec_dir)


def gen_code(path):
    """
    通过class 和方法生成代码
    """
    paths = list(get_py_file_pathes(path))

    for file_ in paths:
        module_full_path = file_

        temp = module_full_path.split('/')
        test_module_full_name = '.'.join(temp).replace('.py', '')
        # try:
        test_module = importlib.import_module(test_module_full_name)
        # except Exception:
        #     print(test_module_full_name)

        file_data = handle_cls(test_module)
        for d in file_data['data']:
            _jinja_gen(d)


def _jinja_gen(data):
    env = Environment(
        loader=PackageLoader("data", "templates"),
        keep_trailing_newline=True,
        line_statement_prefix="##",
        line_comment_prefix="###",
        trim_blocks=True,
        lstrip_blocks=True,
    )
    t = env.get_template("test_case")

    content = t.render(data=data)
    with open(f'cases/test_{hump2str(data["cls_name"])}.py', 'w') as f:
        f.write(content)
    print(content)


if __name__ == '__main__':
    project_path = pre(spec_dir='app')
    out_put_path = "data/services.json"
    gen_all_mds_path(project_path, out_put_path)
    time.sleep(3)
    generate(out_put_path, 'src')

    time.sleep(3)
    # gencode
    gen_code('src')

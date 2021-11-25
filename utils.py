import inspect
import os


def get_lower_case_name(text):
    lst = []
    for index, char in enumerate(text):
        if char.isupper() and index != 0:
            lst.append("_")
        lst.append(char)

    return "".join(lst).lower()


def get_proj_path():
    return os.path.abspath(os.path.dirname(__file__))


def get_py_file_pathes(file_dir):
    for root, dirs, files in os.walk(file_dir):
        for f in files:
            if f.endswith(".py") and not f.startswith("__"):
                yield "/".join([root, f])


def handle_cls(test_module):
    data = dict(data=[])
    for cls_name, cls in inspect.getmembers(test_module):
        if inspect.isclass(cls):
            members = [(k, v) for k, v in inspect.getmembers(cls) if not k.startswith('__')]  # filter builtin func
            cls_d = dict(path=test_module.__name__, cls_name=cls_name)
            for func_name, func_obj in members:
                invoke_p = []
                params = inspect.signature(func_obj).parameters
                for p in params.values():
                    if p.name == 'self':
                        continue
                    if p.default:
                        invoke_p.append(f'{p}=1')
                        # print(name, sig_v)
                # print(1)

                call = f"self.mygrpc.{func_name}({','.join(invoke_p)})"
                cls_d.setdefault('interfaces', []).append(dict(name=func_name, call=call))

            data['data'].append(cls_d)
            # print(cls_d)
            # print(1)
    return data


def str2hump(text):
    """
    下划线转驼峰
    :param text: str
    :return: str
    """
    arr = filter(None, text.lower().split('_'))
    res = ''
    j = 0
    for i in arr:
        if j == 0:
            res = i
        else:
            res = res + i[0].upper() + i[1:]
        j += 1
    res_ = res[0].upper() + res[1:]
    return res_


def hump2str(text):
    """
    驼峰转下划线
    :param text: str
    :return: str
    """
    lst = []
    for index, char in enumerate(text):
        if char.isupper() and index != 0:
            lst.append("_")
        lst.append(char)
    return "".join(lst).lower()


def get_method_from_cls(cls):
    for member_name, member in inspect.getmembers(cls):
        if inspect.ismethod(member):
            if "teardown" not in member_name.lower():
                yield member
        elif member_name.startswith("test"):
            yield member

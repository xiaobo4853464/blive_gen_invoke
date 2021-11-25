from tiny import grpc_call

class Resource(object):
    def __init__(self,service_name):
        self.service_name=service_name
    
    @grpc_call(path="/xlive/resource/v1/resource/Add")
    def add(self, platform, title, type, device, startTime, endTime, imageUrl, jumpPath=None, jumpTime=None, jumpPathType=None, webJumpPath=None, webImageUrl=None):
        """###Add 添加资源接口"""

    @grpc_call(path="/xlive/resource/v1/resource/AddEx")
    def add_ex(self, platform, title, type, device, startTime, endTime, imageUrl, jumpPath=None, jumpTime=None, jumpPathType=None, webJumpPath=None, webImageUrl=None):
        """###Add 添加资源接口(不限制位置和平台)"""

    @grpc_call(path="/xlive/resource/v1/resource/Edit")
    def edit(self, platform, id, title=None, jumpPath=None, jumpTime=None, startTime=None, endTime=None, imageUrl=None, jumpPathType=None):
        """###Edit 编辑资源接口"""

    @grpc_call(path="/xlive/resource/v1/resource/Offline")
    def offline(self, platform, id):
        """###Offline 下线资源接口"""

    @grpc_call(path="/xlive/resource/v1/resource/GetList")
    def get_list(self, platform, type, page=None, pageSize=None):
        """###GetList 获取资源列表"""

    @grpc_call(path="/xlive/resource/v1/resource/GetPlatformList")
    def get_platform_list(self, type=None):
        """###获取平台列表"""

    @grpc_call(path="/xlive/resource/v1/resource/GetListEx")
    def get_list_ex(self, platform, type, page=None, pageSize=None, device_platform=None, status=None, startTime=None, endTime=None):
        """###GetListEx 获取资源列表"""

    @grpc_call(path="/xlive/resource/v1/resource/GetBossUploadUrl")
    def get_boss_upload_url(self, dir, uuid=None, expireTime=None):
        """###GetBossUploadUrl 获取boss上传文件地址"""

    @grpc_call(path="/xlive/resource/v1/resource/GetBossDownloadUrl")
    def get_boss_download_url(self, key, dir, expireTime=None):
        """### GetBossDownloadUrl 获取boss下载文件地址"""

    @grpc_call(path="/xlive/resource/v1/cDNOnline/GetHot")
    def get_hot(self, threshould=None):
        """###获取CDN热门数据"""

    @grpc_call(path="/xlive/resource/v1/timeConf/ListKey")
    def list_key(self, business_id):
        """### 查询某个业务下当前生效的key，不支持分页,仅支持少量生效key的场景"""

    @grpc_call(path="/xlive/resource/v1/timeConf/List")
    def list(self, business_id, page, page_size):
        """### 获取某个业务team的当前生效的list，支持分页功能"""

    @grpc_call(path="/xlive/resource/v1/timeConf/Get")
    def get(self, business_id, key):
        """### 查询某个业务team中某个key对应的值，不生效或者已经删除则返回"""""

    @grpc_call(path="/xlive/resource/v1/timeConf/Update")
    def update(self, business_id, key, start_time, end_time, value=None, status=None, source=None):
        """### 更新某个业务team中的扣个key对应的值，可以添加，修改，删除"""

    @grpc_call(path="/xlive/resource/v1/timeConf/NewSwitchRooms")
    def new_switch_rooms(self, switch_list):
        """### 新 获取开关房间"""

    @grpc_call(path="/xlive/resource/v1/timeConf/CacheClean")
    def cache_clean(self, business_id):
        """### 清除缓存"""

    @grpc_call(path="/xlive/resource/v1/timeConf/BatchGet")
    def batch_get(self, business_id, key):
        """### 批量获取"""

    @grpc_call(path="/xlive/resource/v1/splash/GetInfo")
    def get_info(self, platform, build):
        """###获取有效闪屏配置"""

    @grpc_call(path="/xlive/resource/v1/jumpFrom/GetByKeys")
    def get_by_keys(self, keys=None):
        """### 获取JumpFrom"""

    @grpc_call(path="/xlive/resource/v1/jumpFrom/AddJumpFrom")
    def add_jump_from(self, key=None, value=None):
        """### 新增JumpFrom"""

    @grpc_call(path="/xlive/resource/v1/jumpFrom/EditByKey")
    def edit_by_key(self, key, value=None):
        """### 编辑JumpFrom"""

    @grpc_call(path="/xlive/resource/v1/jumpFrom/GetOneByKey")
    def get_one_by_key(self, key=None):
        """### 获取JumpFrom"""

    @grpc_call(path="/xlive/resource/v1/jumpFrom/GetJumpFromByKeys")
    def get_jump_from_by_keys(self, keys=None):
        """### 提供给PHP服务或者主站"""

    @grpc_call(path="/xlive/resource/v1/banner/GetBlinkBanner")
    def get_blink_banner(self, platform, build):
        """###获取有效banner配置"""

    @grpc_call(path="/xlive/resource/v1/banner/GetBanner")
    def get_banner(self, platform, build, type):
        """###获取有效banner配置"""

    @grpc_call(path="/xlive/internal/resource/v1/titans/get_config_by_keyword")
    def get_config_by_keyword(self, team=None, keyword=None, id=None):
        """### 无标题"""

    @grpc_call(path="/xlive/internal/resource/v1/titans/set_config_by_keyword")
    def set_config_by_keyword(self, keyword, value, team=None, name=None, id=None, status=None):
        """### 无标题"""

    @grpc_call(path="/xlive/internal/resource/v1/titans/get_configs_by_params")
    def get_configs_by_params(self, page, page_size, team=None, keyword=None, name=None, status=None, id=None):
        """### 无标题"""

    @grpc_call(path="/xlive/internal/resource/v1/titans/getByTreeId")
    def get_by_tree_id(self, tree_id):
        """### 无标题"""

    @grpc_call(path="/xlive/internal/resource/v1/titans/get_configs_by_likes")
    def get_configs_by_likes(self, params):
        """### 无标题"""

    @grpc_call(path="/xlive/internal/resource/v1/titans/get_configs_by_treeIdKeys")
    def get_configs_by_tree_id_keys(self, tree_id=None, keys=None):
        """### 无标题"""

    @grpc_call(path="/xlive/resource/v1/titans/get_template_config")
    def get_template_config(self, template_id=None, tree_id=None):
        """### 获取模板下的配置，支持模板&服务条件并行"""

    @grpc_call(path="/xlive/resource/v1/titans/getByTreeIdV2")
    def get_by_tree_id_v2(self, tree_id):
        """###获取服务下的配置，返回map[string][]byte"""

    @grpc_call(path="/xlive/resource/v1/titans/getGroupList")
    def get_group_list(self, group_name=None, group_owner=None, group_status=None, page=None, page_size=None):
        """###获取集合配置的集合列表"""

    @grpc_call(path="/xlive/resource/v1/titans/getGroupConfList")
    def get_group_conf_list(self, group_id, page=None, page_size=None):
        """###获取集合配置列表"""

    @grpc_call(path="/xlive/resource/v1/titans/saveGroupConf")
    def save_group_conf(self, keyword, explanation, id=None, group_id=None, template=None, content=None, status=None, mtime=None):
        """###保存服务配置（新增或编辑）"""

    @grpc_call(path="/xlive/internal/resource/v1/titans/getMultiConfigs")
    def get_multi_configs(self, values=None):
        """### 无标题"""

    @grpc_call(path="/xlive/internal/resource/v1/titans/getServiceConfig")
    def get_service_config(self, tree_id=None):
        """### 无标题"""

    @grpc_call(path="/xlive/internal/resource/v1/titans/setServiceConfig")
    def set_service_config(self, tree_name=None, tree_path=None, tree_id=None, service=None, keyword=None, template=None, name=None, value=None, status=None, id=None, mtime=None):
        """### 无标题"""

    @grpc_call(path="/xlive/internal/resource/v1/titans/getServiceConfigList")
    def get_service_config_list(self, tree_name=None, tree_id=None, service=None, keyword=None, page=None, page_size=None, name=None, status=None):
        """### 无标题"""

    @grpc_call(path="/xlive/internal/resource/v1/titans/getTreeIds")
    def get_tree_ids(self, tree_name=None):
        """### 无标题"""

    @grpc_call(path="/xlive/internal/resource/v1/titans/getMyTreeApps")
    def get_my_tree_apps(self, node=None, team=None):
        """### 无标题"""

    @grpc_call(path="/xlive/internal/resource/v1/titans/getEasyList")
    def get_easy_list(self, id=None, page=None):
        """### 无标题"""

    @grpc_call(path="/xlive/internal/resource/v1/titans/setEasyList")
    def set_easy_list(self, id=None):
        """### 无标题"""

    @grpc_call(path="/xlive/internal/resource/v1/titans/syncServiceConfig")
    def sync_service_config(self, tree_name=None, tree_path=None, tree_id=None, service=None, keyword=None, template=None, name=None, value=None, status=None, id=None, mtime=None):
        """### 无标题"""

    @grpc_call(path="/xlive/resource/v1/abtest/GetABConfList")
    def get_a_b_conf_list(self, page=None, page_size=None, status=None, module_name=None):
        """### 获取AB实验模块配置列表"""

    @grpc_call(path="/xlive/resource/v1/abtest/GetABRuleList")
    def get_a_b_rule_list(self, conf_id, page=None, page_size=None, parent_id=None, status=None):
        """### 获取AB实验规则列表"""

    @grpc_call(path="/xlive/resource/v1/abtest/SetABConf")
    def set_a_b_conf(self, module_name, module_info, id=None, operator=None, sid=None):
        """### 新增/编辑模块配置"""

    @grpc_call(path="/xlive/resource/v1/abtest/SetABRule")
    def set_a_b_rule(self, conf_id, name, rule, id=None, operator=None, parent_id=None, sid=None):
        """### 新增/编辑规则"""

    @grpc_call(path="/xlive/resource/v1/abtest/OnOffABConf")
    def on_off_a_b_conf(self, id, status, operator=None):
        """### 模块配置上下线"""

    @grpc_call(path="/xlive/resource/v1/abtest/OnOffABRule")
    def on_off_a_b_rule(self, id, status, conf_id, operator=None):
        """### 规则上下线"""

    @grpc_call(path="/xlive/resource/v1/abtest/GetABTestRules")
    def get_a_b_test_rules(self, module_name=None, module_info=None):
        """### 拉AB实验的规则"""

    @grpc_call(path="/xlive/resource/v1/liveCheck/LiveCheck")
    def live_check(self, platform, system, mobile):
        """###客户端获取能否直播接口"""

    @grpc_call(path="/xlive/resource/v1/liveCheck/AddLiveCheck")
    def add_live_check(self, live_check):
        """###后台添加能否直播设备黑名单"""

    @grpc_call(path="/xlive/resource/v1/kv/saveDepartment")
    def save_department(self, department_name, department_owner, id=None):
        """###保存部门 （新增or编辑，编辑传id）"""

    @grpc_call(path="/xlive/resource/v1/kv/delDepartment")
    def del_department(self, id, is_del):
        """###删除部门"""

    @grpc_call(path="/xlive/resource/v1/kv/getBusinessList")
    def get_business_list(self, department_id, page=None, page_size=None, status=None):
        """###获取业务列表"""

    @grpc_call(path="/xlive/resource/v1/kv/saveBusiness")
    def save_business(self, department_id, key, business_name, business_owner, status, id=None):
        """###保存业务"""

    @grpc_call(path="/xlive/resource/v1/kv/getOnlineBusinessByDepartmentId")
    def get_online_business_by_department_id(self, department_id=None):
        """###根据部门id获取全部上线中的业务列表"""

    @grpc_call(path="/xlive/resource/v1/kv/bindBusiness")
    def bind_business(self, conf_id, conf_desc, department_id, business_id, is_bind=None):
        """###绑定业务"""

    @grpc_call(path="/xlive/resource/v1/kv/getConfList")
    def get_conf_list(self, department_id=None, business_id=None, conf_name=None, page=None, page_size=None):
        """###获取业务配置列表"""

    @grpc_call(path="/xlive/resource/v1/kv/getConfDetail")
    def get_conf_detail(self, conf_id=None):
        """###获取配置详情"""

    @grpc_call(path="/xlive/resource/v1/kv/getBindDetail")
    def get_bind_detail(self, conf_id=None):
        """### 获取绑定详情"""

    @grpc_call(path="/xlive/resource/v1/kv/getClientConfList")
    def get_client_conf_list(self, business_id, status=None, operator=None, page=None, page_size=None, is_need_conf=None):
        """###获取客户端配置列表"""

    @grpc_call(path="/xlive/resource/v1/kv/saveClientConf")
    def save_client_conf(self, business_id, desc, creater, department_id, id=None, start_time=None, end_time=None, status=None, conf_data=None, rule=None, conf_comment=None, mtime=None, multi_app=None):
        """###保存客户端配置"""

    @grpc_call(path="/xlive/resource/v1/kv/getClientConfDetail")
    def get_client_conf_detail(self, id=None):
        """###获取客户端配置详情"""

    @grpc_call(path="/xlive/resource/v1/kv/getClientConf")
    def get_client_conf(self, department_id, business_id, conf_name=None, uid=None, build=None, platform=None, mobi_app=None, buvid=None, ip=None):
        """###后台预览 验证配置"""

    @grpc_call(path="/xlive/resource/v1/kv/getOnlineClientConf")
    def get_online_client_conf(self, page, page_size):
        """### 获取所有上线客户端配置"""

    @grpc_call(path="/xlive/resource/v2/userResource/Add")
    def add(self, res_type, title, url, weight, creator, show_text=None):
        """###Add 添加资源接口"""

    @grpc_call(path="/xlive/resource/v2/userResource/Edit")
    def edit(self, res_type, custom_id, title=None, url=None, weight=None, show_text=None):
        """###Edit 编辑现有资源"""

    @grpc_call(path="/xlive/resource/v2/userResource/Query")
    def query(self, res_type, custom_id):
        """###Query 请求单个资源"""

    @grpc_call(path="/xlive/resource/v2/userResource/List")
    def list(self, res_type, page=None, page_size=None):
        """###List 获取资源列表"""

    @grpc_call(path="/xlive/resource/v2/userResource/SetStatus")
    def set_status(self, res_type, custom_id, status):
        """###SetStatus 更改资源状态"""

    @grpc_call(path="/xlive/resource/v2/userResource/MutipleQuery")
    def mutiple_query(self, res_type, custom_ids):
        """###MutipleQuery 请求单个或多个资源详情"""

    @grpc_call(path="/xlive/resource/v2/comment/addCommentSubject")
    def add_comment_subject(self, mid=None):
        """### addCommentSubject 新建评论区"""

    @grpc_call(path="/xlive/resource/v2/comment/sendEmail")
    def send_email(self, context):
        """### addCommentSubject 新建评论区"""

    @grpc_call(path="/xlive/resource/v2/sendEmail/sendEmail")
    def send_email(self, to_address, head, content, cc_address=None):
        """### sendEmail 发送邮件"""

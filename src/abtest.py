from tiny import grpc_call

class Abtest(object):
    def __init__(self,service_name):
        self.service_name=service_name
    
    @grpc_call(path="/live.abtest.jumpfrom/AddNewSource")
    def add_new_source(self, source_one_title, source_two_title, prefix):
        """### 新增来源"""

    @grpc_call(path="/live.abtest.jumpfrom/GetJumpFromList")
    def get_jump_from_list(self, page, page_size, source_one_title=None, source_two_title=None, jumpfrom_id=None, entry_from=None, order=None):
        """### jumpfrom列表"""

    @grpc_call(path="/live.abtest.jumpfrom/GetJumpFrom")
    def get_jump_from(self, id):
        """### jumpfrom info"""

    @grpc_call(path="/live.abtest.jumpfrom/SetJumpFrom")
    def set_jump_from(self, jumpfrom_id, entry_from, source_one_title, source_two_title, source_three_title, source_desc, report_type, id=None, tapd_url=None, img=None, aggregated_field=None):
        """### add / edit"""

    @grpc_call(path="/live.abtest.jumpfrom/GetMaxByPrefix")
    def get_max_by_prefix(self, prefix=None):
        """### 根据前缀获取最大值"""

    @grpc_call(path="/live.abtest.jumpfrom/GetSearchResult")
    def get_search_result(self, jumpfrom_id=None):
        """### 搜索框联想查询"""

    @grpc_call(path="/live.abtest.jumpfrom/GetJumpFromByKeys")
    def get_jump_from_by_keys(self, keys=None):
        """### 提供给PHP服务或者主站"""

    @grpc_call(path="/live.abtest.abtest/GetExpList")
    def get_exp_list(self, page=None, page_size=None, stat=None, exp_source=None, exp_key=None, exp_name=None, namespace=None):
        """### 获取实验列表"""

    @grpc_call(path="/live.abtest.abtest/GetExpInfo")
    def get_exp_info(self, exp_id=None, version=None):
        """### 获取实验详情"""

    @grpc_call(path="/live.abtest.abtest/OnOffExp")
    def on_off_exp(self, exp_id=None, stat=None):
        """### 实验上下线"""

    @grpc_call(path="/live.abtest.abtest/GetQuotaList")
    def get_quota_list(self, version=None):
        """### 获取指标列表"""

    @grpc_call(path="/live.abtest.abtest/GetByExpKey")
    def get_by_exp_key(self, exp_key=None):
        """### 根据key拉取规则"""

    @grpc_call(path="/live.abtest.abtest/GetOnlineByExpKey")
    def get_online_by_exp_key(self, exp_key=None):
        """### 根据key拉取在线规则 切量用"""

    @grpc_call(path="/live.abtest.abtest/GetExpListByParams")
    def get_exp_list_by_params(self, namespace):
        """### 根据条件获取AB规则列表"""

    @grpc_call(path="/live.abtest.abtest/GetSimpleQuotaList")
    def get_simple_quota_list(self, version=None):
        """### 获取指标列表"""

    @grpc_call(path="/live.abtest.abtest/GetExpListByNamespace")
    def get_exp_list_by_namespace(self, namespace):
        """### 根据需求方获取AB实验信息"""

    @grpc_call(path="/live.abtest.abtest/GetSplitResultByParam")
    def get_split_result_by_param(self, uid, exp_key, buvid=None):
        """### 根据uid获取用户分流结果"""

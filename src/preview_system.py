from tiny import grpc_call

class Preview_system(object):
    def __init__(self,service_name):
        self.service_name=service_name
    
    @grpc_call(path="/live.previewsystem.background/AddMemberListType")
    def add_member_list_type(self, tag, title, meta_data, remark):
        """###===============测试账户名单相关"""

    @grpc_call(path="/live.previewsystem.background/ModifyMemberListType")
    def modify_member_list_type(self, id, title, meta_data, remark):
        """###更改测试表单类型"""

    @grpc_call(path="/live.previewsystem.background/GetMemberListType")
    def get_member_list_type(self, page, page_size, title=None):
        """###获取测试表单列表"""

    @grpc_call(path="/live.previewsystem.background/AddPreviewAccount")
    def add_preview_account(self, uid, is_all, ext_data, state, tag_list=None):
        """###===============测试账户相关"""

    @grpc_call(path="/live.previewsystem.background/DelPreviewAccount")
    def del_preview_account(self, id):
        """###删除测试账户"""

    @grpc_call(path="/live.previewsystem.background/ModifyPreviewAccount")
    def modify_preview_account(self, id, uid, is_all, ext_data, state, tag_list=None):
        """###更新测试账户"""

    @grpc_call(path="/live.previewsystem.background/GetList")
    def get_list(self, page, page_size, uid=None):
        """###获取测试账户列表"""

    @grpc_call(path="/live.previewsystem.background/GetInfo")
    def get_info(self, id):
        """###获取测试账户详情"""

    @grpc_call(path="/live.previewsystem.business_control/Get")
    def get(self, business_id=None, business_sub_id=None, room_id=None, uid=None):
        """### 查询记录"""

    @grpc_call(path="/live.previewsystem.business_control/Set")
    def set(self, dim_type=None, object_id=None, subject_id=None, business_id=None, business_sub_id=None, start_time=None, end_time=None, source=None):
        """### 新建一条记录"""

    @grpc_call(path="/live.previewsystem.business_control/SetBatch")
    def set_batch(self, dim_type=None, object_id=None, subject_ids=None, business_id=None, business_sub_id=None, start_time=None, end_time=None, source=None):
        """### 批量新建某一业务维度下的记录（未过测试）"""

    @grpc_call(path="/live.previewsystem.business_control/Del")
    def del_(self, dim_type=None, object_id=None, subject_id=None, business_id=None, business_sub_id=None):
        """### 删除记录（线上勿用）"""

    @grpc_call(path="/live.previewsystem.business_control/AddRule")
    def add_rule(self, rule_name, start_time, end_time, id_type, description=None, mem_cache=None):
        """### V2 新增一条规则"""

    @grpc_call(path="/live.previewsystem.business_control/UpdateRule")
    def update_rule(self, id, rule_name, start_time, end_time, id_type, description=None, mem_cache=None):
        """### V2 更新规则"""

    @grpc_call(path="/live.previewsystem.business_control/GetRule")
    def get_rule(self, id):
        """### V2 获取规则详情"""

    @grpc_call(path="/live.previewsystem.business_control/GetRuleList")
    def get_rule_list(self, page=None, size=None, rule_id=None, rule_name=None):
        """### V2 获取规则列表"""

    @grpc_call(path="/live.previewsystem.business_control/GetBatchAddPlanList")
    def get_batch_add_plan_list(self, page=None, size=None):
        """### V2 获取批量新增记录计划列表"""

    @grpc_call(path="/live.previewsystem.business_control/GetBatchAddPlan")
    def get_batch_add_plan(self, id):
        """### V2 获取批量新增记录计划详情"""

    @grpc_call(path="/live.previewsystem.business_control/AddBatchAddPlan")
    def add_batch_add_plan(self, rule_ids, start_time, end_time, add_type, ids, description):
        """### V2 批量新增管控记录"""

    @grpc_call(path="/live.previewsystem.business_control/CheckRule")
    def check_rule(self, rule_id, id_str):
        """### V2 检查是否在管控"""

    @grpc_call(path="/live.previewsystem.business_control/GetRecordList")
    def get_record_list(self, rule_id=None, id_str=None, last_id=None, size=None):
        """### V2 获取管控列表"""

    @grpc_call(path="/live.previewsystem.business_control/AddRecord")
    def add_record(self, rule_id, start_time, end_time, id_str, description=None):
        """### V2 新增管控记录"""

    @grpc_call(path="/live.previewsystem.business_control/UpdateRecord")
    def update_record(self, rule_id, id_str, start_time, end_time, description=None):
        """### V2 编辑单条管控记录"""

    @grpc_call(path="/live.previewsystem.business_control/DeleteRecord")
    def delete_record(self, rule_id, id_str, id=None):
        """### V2 删除管控记录"""

    @grpc_call(path="/live.previewsystem.business_control/CheckMutualBlack")
    def check_mutual_black(self, uid_a=None, uid_b=None):
        """### 查询主站黑名单"""

    @grpc_call(path="/live.previewsystem.business_control/GetBusinessList")
    def get_business_list(self, name=None, id=None):
        """### 获取业务列表，业务名称为空的时候返回所有的记录"""

    @grpc_call(path="/live.previewsystem.business_control/SetBusiness")
    def set_business(self, id=None, name=None, desc=None, status=None):
        """### 新增业务"""

    @grpc_call(path="/live.previewsystem.business_control/GetList")
    def get_list(self, dim_type=None, object_id=None, subject_id=None, business_id=None, business_sub_id=None):
        """### 管控搜索"""

    @grpc_call(path="/live.previewsystem.member/GetList")
    def get_list(self, id, size):
        """###获取预演名单配置列表"""

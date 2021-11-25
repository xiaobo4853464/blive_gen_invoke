"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""
from tiny import grpc_call


class Settlement(object):

    def __init__(self, service_name):
        self.service_name = service_name

    @grpc_call(path="/live.settlement.v1.intercept.anchorIntercept/add")
    def add(self, uid=None, remark=None, applicant=None):
        """### 添加主播拦截"""

    @grpc_call(path="/live.settlement.v1.intercept.anchorIntercept/del")
    def del_(self, id=None, applicant=None):
        """### 删除主播拦截"""

    @grpc_call(path="/live.settlement.v1.intercept.anchorIntercept/modifyRemark")
    def modify_remark(self, id=None, remark=None, applicant=None):
        """### 修改备注"""

    @grpc_call(path="/live.settlement.v1.intercept.anchorIntercept/list")
    def list(self, uid=None, page=None, size=None):
        """### 拦截列表"""

    @grpc_call(path="/live.settlement.v1.intercept.anchorIntercept/logList")
    def log_list(self, page=None, size=None, uid=None):
        """### 拦截日志列表"""

    @grpc_call(path="/live.settlement.v1.intercept.anchorIntercept/interceptHistory")
    def intercept_history(self, date=None):
        """### 拦截下载历史记录"""

    @grpc_call(path="/live.settlement.v1.intercept.anchorIntercept/addInterceptHistory")
    def add_intercept_history(self, uid=None, anchor_name=None, room_id=None, settle_type=None, hamster=None, timestamp=None, remark=None):
        """### 添加拦截拦截记录(公会用)"""

    @grpc_call(path="/live.settlement.v1.intercept.anchorIntercept/onAddAuthGuild")
    def on_add_auth_guild(self, uid=None):
        """### 当加入官方公会"""


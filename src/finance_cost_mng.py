"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""
from tiny import grpc_call


class Finance_cost_mng(object):

    def __init__(self, service_name):
        self.service_name = service_name

    @grpc_call(path="/live.financecostmng.v1.FinanceUser/GetUser")
    def get_user(self, uid=None):
        """### 查询用户信息"""


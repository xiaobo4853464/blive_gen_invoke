"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""
from tiny import grpc_call


class Order(object):

    def __init__(self, service_name):
        self.service_name = service_name

    @grpc_call(path="/live.order.v1.contract/TerminateContract")
    def terminate_contract(self, uid, goods_id, remark, ruid=None):
        """### 终止签约"""

    @grpc_call(path="/live.order.v1.contract/ChangeContractExecuteTime")
    def change_contract_execute_time(self, uid, goods_id, next_execute_time, ruid=None):
        """### 变更扣款时间 服务端内部调用"""

    @grpc_call(path="/live.order.v1.contract/ContractNotify")
    def contract_notify(self, msg_id, msg_content, p=None):
        """### 签约/解约异步回调"""

    @grpc_call(path="/live.order.v1.contract/GetContract")
    def get_contract(self, uid=None, ruid=None, goods_id=None):
        """### 查询签约信息"""

    @grpc_call(path="/live.order.v1.contract/GetPayPlatformContractStatus")
    def get_pay_platform_contract_status(self, uid=None, ruid=None, goods_id=None):
        """### 查询支付平台签约状态"""

    @grpc_call(path="/live.order.v1.contract/GetContracts")
    def get_contracts(self, uid=None, ruids=None, goods_id=None):
        """### 批量查询签约信息"""

    @grpc_call(path="/live.order.v1.contract/GetContractsByRuid")
    def get_contracts_by_ruid(self, ruid, uids, goods_id):
        """### 根据主播ID获取签约信息"""


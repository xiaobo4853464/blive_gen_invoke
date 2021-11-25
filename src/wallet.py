"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""
from tiny import grpc_call


class Wallet(object):

    def __init__(self, service_name):
        self.service_name = service_name

    @grpc_call(path="/live.xwallet.v3.ThirdAccount/get_account_info")
    def get_account_info(self, account_id):
        """###获取用户账户信息"""

    @grpc_call(path="/live.xwallet.v3.ThirdAccount/recharge")
    def recharge(self, order_id, account_id, coin, reason, timestamp):
        """###账户充值"""

    @grpc_call(path="/live.xwallet.v3.ThirdAccount/pay")
    def pay(self, order_id, account_id, coin, reason, timestamp):
        """###账户扣除"""

    @grpc_call(path="/live.xwallet.v3.ThirdAccount/query")
    def query(self, order_id):
        """###订单查询"""

    @grpc_call(path="/live.xwallet.v3.ThirdAccount/addAccount")
    def add_account(self, account_id, coin, op_type, apply_pic, apply_user, apply_remark=None):
        """###添加预存金"""

    @grpc_call(path="/live.xwallet.v3.ThirdAccount/examine")
    def examine(self, id, examine_type, reviewer):
        """###审批预存金"""

    @grpc_call(path="/live.xwallet.v3.ThirdAccount/list")
    def list(self, state=None, page=None, page_size=None, account_id=None):
        """###查询预存金列表"""


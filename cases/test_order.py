"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.order import Order


class TestOrder(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Order()

    def test_change_contract_execute_time(self):
        r = self.mygrpc.change_contract_execute_time(uid=1, goods_id=1, next_execute_time=1)
        print(r)

    def test_contract_notify(self):
        r = self.mygrpc.contract_notify(msg_id=1, msg_content=1)
        print(r)

    def test_get_contract(self):
        r = self.mygrpc.get_contract()
        print(r)

    def test_get_contracts(self):
        r = self.mygrpc.get_contracts()
        print(r)

    def test_get_contracts_by_ruid(self):
        r = self.mygrpc.get_contracts_by_ruid(ruid=1, uids=1, goods_id=1)
        print(r)

    def test_get_pay_platform_contract_status(self):
        r = self.mygrpc.get_pay_platform_contract_status()
        print(r)

    def test_terminate_contract(self):
        r = self.mygrpc.terminate_contract(uid=1, goods_id=1, remark=1)
        print(r)


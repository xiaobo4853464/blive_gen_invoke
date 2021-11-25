"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.wallet import Wallet


class TestWallet(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Wallet()

    def test_add_account(self):
        r = self.mygrpc.add_account(account_id=1, coin=1, op_type=1, apply_pic=1, apply_user=1)
        print(r)

    def test_examine(self):
        r = self.mygrpc.examine(id=1, examine_type=1, reviewer=1)
        print(r)

    def test_get_account_info(self):
        r = self.mygrpc.get_account_info(account_id=1)
        print(r)

    def test_list(self):
        r = self.mygrpc.list()
        print(r)

    def test_pay(self):
        r = self.mygrpc.pay(order_id=1, account_id=1, coin=1, reason=1, timestamp=1)
        print(r)

    def test_query(self):
        r = self.mygrpc.query(order_id=1)
        print(r)

    def test_recharge(self):
        r = self.mygrpc.recharge(order_id=1, account_id=1, coin=1, reason=1, timestamp=1)
        print(r)


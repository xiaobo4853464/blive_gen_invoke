"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.wallet import Wallet


class TestWallet(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Wallet()

    def test_add(self):
        r = self.mygrpc.add(uid=1,account_type=1,coin=1,tid=1,extend_tid=1,timestamp=1,reason=1,biz_type=1,platform=1)
        print(r)

    def test_add_account(self):
        r = self.mygrpc.add_account(account_id=1,coin=1,op_type=1,apply_pic=1,apply_user=1)
        print(r)

    def test_add_coin_stream(self):
        r = self.mygrpc.add_coin_stream(tid=1,uid=1,account_type=1,timestamp=1,platform=1,biz_type=1,extend_tid=1,reason=1,coin=1)
        print(r)

    def test_batch_get_hamster_info(self):
        r = self.mygrpc.batch_get_hamster_info()
        print(r)

    def test_batch_get_info(self):
        r = self.mygrpc.batch_get_info(uid=1)
        print(r)

    def test_deduct(self):
        r = self.mygrpc.deduct(uid=1,coin=1,tid=1,extend_tid=1,timestamp=1,reason=1,biz_type=1,platform=1)
        print(r)

    def test_deduct_hamster(self):
        r = self.mygrpc.deduct_hamster()
        print(r)

    def test_examine(self):
        r = self.mygrpc.examine(id=1,examine_type=1,reviewer=1)
        print(r)

    def test_exchange(self):
        r = self.mygrpc.exchange()
        print(r)

    def test_get_account_balance_list(self):
        r = self.mygrpc.get_account_balance_list()
        print(r)

    def test_get_account_balance_num(self):
        r = self.mygrpc.get_account_balance_num()
        print(r)

    def test_get_account_info(self):
        r = self.mygrpc.get_account_info(account_id=1)
        print(r)

    def test_get_all(self):
        r = self.mygrpc.get_all()
        print(r)

    def test_get_hamster_info(self):
        r = self.mygrpc.get_hamster_info()
        print(r)

    def test_get_hamster_info_v2(self):
        r = self.mygrpc.get_hamster_info_v2()
        print(r)

    def test_get_hamster_tid(self):
        r = self.mygrpc.get_hamster_tid()
        print(r)

    def test_get_info(self):
        r = self.mygrpc.get_info(uid=1)
        print(r)

    def test_get_streams(self):
        r = self.mygrpc.get_streams(uid=1,date=1,start_time=1,end_time=1,page=1,page_size=1)
        print(r)

    def test_get_sync(self):
        r = self.mygrpc.get_sync(uid=1)
        print(r)

    def test_get_tid(self):
        r = self.mygrpc.get_tid(uid=1,extend_tid=1,transaction_type=1,reason=1,timestamp=1)
        print(r)

    def test_get_wallet(self):
        r = self.mygrpc.get_wallet(uid=1)
        print(r)

    def test_get_wallet_info(self):
        r = self.mygrpc.get_wallet_info(uid=1)
        print(r)

    def test_list(self):
        r = self.mygrpc.list()
        print(r)

    def test_make_wallet_ceil100(self):
        r = self.mygrpc.make_wallet_ceil100(uid=1)
        print(r)

    def test_modify(self):
        r = self.mygrpc.modify()
        print(r)

    def test_pay(self):
        r = self.mygrpc.pay(order_id=1,account_id=1,coin=1,reason=1,timestamp=1)
        print(r)

    def test_query(self):
        r = self.mygrpc.query(order_id=1)
        print(r)

    def test_query_by_extend_tid(self):
        r = self.mygrpc.query_by_extend_tid(uid=1,extend_tid=1,year_month=1)
        print(r)

    def test_query_extid(self):
        r = self.mygrpc.query_extid(uid=1,extend_tid=1,timestamp=1,transaction_type=1,reason=1)
        print(r)

    def test_query_hamster_by_id(self):
        r = self.mygrpc.query_hamster_by_id()
        print(r)

    def test_query_tid(self):
        r = self.mygrpc.query_tid(tid=1)
        print(r)

    def test_recharge(self):
        r = self.mygrpc.recharge(order_id=1,account_id=1,coin=1,reason=1,timestamp=1)
        print(r)

    def test_recharge_hamster(self):
        r = self.mygrpc.recharge_hamster()
        print(r)

    def test_refund(self):
        r = self.mygrpc.refund()
        print(r)

    def test_sync_account(self):
        r = self.mygrpc.sync_account(uid=1)
        print(r)


"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.pay_play import Pay_play


class TestPay_play(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Pay_play()

    def test_buy_info(self):
        r = self.mygrpc.buy_info()
        print(r)

    def test_get_my_tickets(self):
        r = self.mygrpc.get_my_tickets(uid=1)
        print(r)

    def test_get_share_ticket(self):
        r = self.mygrpc.get_share_ticket()
        print(r)

    def test_get_ticket_detail(self):
        r = self.mygrpc.get_ticket_detail(uid=1, ticketing_id=1)
        print(r)

    def test_get_tickets_status(self):
        r = self.mygrpc.get_tickets_status()
        print(r)

    def test_live_validate(self):
        r = self.mygrpc.live_validate()
        print(r)

    def test_pre_buy(self):
        r = self.mygrpc.pre_buy(uid=1, goods_id=1, goods_num=1)
        print(r)

    def test_send_ticket(self):
        r = self.mygrpc.send_ticket(uids=1, goods_id=1, apply_name=1, reason=1, msg_id=1)
        print(r)

    def test_share_ticket(self):
        r = self.mygrpc.share_ticket()
        print(r)

    def test_suc_buy(self):
        r = self.mygrpc.suc_buy()
        print(r)

    def test_take_ticket(self):
        r = self.mygrpc.take_ticket()
        print(r)


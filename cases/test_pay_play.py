"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.pay_play import Pay_play


class TestPay_play(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Pay_play()

    def test_add_goods(self):
        r = self.mygrpc.add_goods()
        print(r)

    def test_add_live(self):
        r = self.mygrpc.add_live(room_id=1,title=1,start_time=1,end_time=1,live_pic=1,ad_pic=1,goods_link=1,goods_id=1,buy_goods_id=1)
        print(r)

    def test_apply_give_ticket(self):
        r = self.mygrpc.apply_give_ticket()
        print(r)

    def test_buy_info(self):
        r = self.mygrpc.buy_info()
        print(r)

    def test_check_pay_live_room(self):
        r = self.mygrpc.check_pay_live_room(room_id=1,start_time=1,end_time=1)
        print(r)

    def test_close_auth(self):
        r = self.mygrpc.close_auth()
        print(r)

    def test_close_buy(self):
        r = self.mygrpc.close_buy()
        print(r)

    def test_config(self):
        r = self.mygrpc.config(room_id=1,ruid=1,uid=1)
        print(r)

    def test_create_pay_live_room(self):
        r = self.mygrpc.create_pay_live_room(epid=1,face=1,title=1,room_id=1,start_time=1,end_time=1,link_url=1)
        print(r)

    def test_enable(self):
        r = self.mygrpc.enable(room_id=1,ruid=1)
        print(r)

    def test_get_all_goods_simple_info(self):
        r = self.mygrpc.get_all_goods_simple_info()
        print(r)

    def test_get_goods_list(self):
        r = self.mygrpc.get_goods_list()
        print(r)

    def test_get_live_list(self):
        r = self.mygrpc.get_live_list()
        print(r)

    def test_get_message_list(self):
        r = self.mygrpc.get_message_list(room_id=1)
        print(r)

    def test_get_my_tickets(self):
        r = self.mygrpc.get_my_tickets(uid=1)
        print(r)

    def test_get_share_ticket(self):
        r = self.mygrpc.get_share_ticket()
        print(r)

    def test_get_ticket_detail(self):
        r = self.mygrpc.get_ticket_detail(uid=1,ticketing_id=1)
        print(r)

    def test_get_tickets_status(self):
        r = self.mygrpc.get_tickets_status()
        print(r)

    def test_is_enable(self):
        r = self.mygrpc.is_enable(room_id=1,parent_area_id=1,area_id=1)
        print(r)

    def test_live_validate(self):
        r = self.mygrpc.live_validate()
        print(r)

    def test_match_info(self):
        r = self.mygrpc.match_info()
        print(r)

    def test_open_auth(self):
        r = self.mygrpc.open_auth()
        print(r)

    def test_open_buy(self):
        r = self.mygrpc.open_buy()
        print(r)

    def test_own_message_list(self):
        r = self.mygrpc.own_message_list(room_id=1,uid=1)
        print(r)

    def test_pre_buy(self):
        r = self.mygrpc.pre_buy(uid=1,goods_id=1,goods_num=1)
        print(r)

    def test_query_order(self):
        r = self.mygrpc.query_order()
        print(r)

    def test_send_ticket(self):
        r = self.mygrpc.send_ticket(uids=1,goods_id=1,apply_name=1,reason=1,msg_id=1)
        print(r)

    def test_share_ticket(self):
        r = self.mygrpc.share_ticket()
        print(r)

    def test_suc_buy(self):
        r = self.mygrpc.suc_buy()
        print(r)

    def test_support(self):
        r = self.mygrpc.support()
        print(r)

    def test_take_ticket(self):
        r = self.mygrpc.take_ticket()
        print(r)

    def test_update_goods(self):
        r = self.mygrpc.update_goods()
        print(r)

    def test_update_live(self):
        r = self.mygrpc.update_live()
        print(r)

    def test_update_pay_live_room(self):
        r = self.mygrpc.update_pay_live_room(pay_live_id=1,epid=1,face=1,title=1,room_id=1,start_time=1,end_time=1,link_url=1)
        print(r)

    def test_update_pay_live_status(self):
        r = self.mygrpc.update_pay_live_status(pay_live_id=1)
        print(r)


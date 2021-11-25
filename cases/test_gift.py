"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.gift import Gift


class TestGift(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Gift()

    def test_add_guard_sc_gift_stream(self):
        r = self.mygrpc.add_guard_sc_gift_stream(order_id=1,goods_id=1,uid=1,ruid=1,total_coin=1,goods_num=1,pay_coin=1,platform=1,timestamp=1,msg_id=1)
        print(r)

    def test_add_special_plan(self):
        r = self.mygrpc.add_special_plan(biz_type=1,relevance_id=1,gift_list=1,online_time=1,offline_time=1,comment=1)
        print(r)

    def test_add_user_gold_package(self):
        r = self.mygrpc.add_user_gold_package(uid=1,gift_id=1,incr_gift_num=1,gift_price=1,expireat=1,biz_type=1,biz_extra=1)
        print(r)

    def test_bag_delete_task(self):
        r = self.mygrpc.bag_delete_task()
        print(r)

    def test_bag_info_admin(self):
        r = self.mygrpc.bag_info_admin()
        print(r)

    def test_bag_list(self):
        r = self.mygrpc.bag_list()
        print(r)

    def test_bag_reduce(self):
        r = self.mygrpc.bag_reduce()
        print(r)

    def test_clear_bag_dot(self):
        r = self.mygrpc.clear_bag_dot(uid=1)
        print(r)

    def test_close_config(self):
        r = self.mygrpc.close_config()
        print(r)

    def test_daily_bag(self):
        r = self.mygrpc.daily_bag()
        print(r)

    def test_delete_gift(self):
        r = self.mygrpc.delete_gift(gift_id=1)
        print(r)

    def test_discount_gift_list(self):
        r = self.mygrpc.discount_gift_list()
        print(r)

    def test_get_bag_dot(self):
        r = self.mygrpc.get_bag_dot(uid=1)
        print(r)

    def test_get_bag_list_by_uid(self):
        r = self.mygrpc.get_bag_list_by_uid(uid=1)
        print(r)

    def test_get_blind_gift_stream(self):
        r = self.mygrpc.get_blind_gift_stream(uid=1)
        print(r)

    def test_get_childrem_stream_file(self):
        r = self.mygrpc.get_childrem_stream_file()
        print(r)

    def test_get_config(self):
        r = self.mygrpc.get_config()
        print(r)

    def test_get_delete_tips(self):
        r = self.mygrpc.get_delete_tips(gift_id=1)
        print(r)

    def test_get_gift_info_by_id(self):
        r = self.mygrpc.get_gift_info_by_id(gift_id=1)
        print(r)

    def test_get_gift_list(self):
        r = self.mygrpc.get_gift_list()
        print(r)

    def test_get_gift_list_by_id(self):
        r = self.mygrpc.get_gift_list_by_id(gift_id=1)
        print(r)

    def test_get_gift_rank(self):
        r = self.mygrpc.get_gift_rank()
        print(r)

    def test_get_gift_rank_v2(self):
        r = self.mygrpc.get_gift_rank_v2()
        print(r)

    def test_get_gift_record(self):
        r = self.mygrpc.get_gift_record()
        print(r)

    def test_get_gift_stat(self):
        r = self.mygrpc.get_gift_stat()
        print(r)

    def test_get_gift_stat_v2(self):
        r = self.mygrpc.get_gift_stat_v2()
        print(r)

    def test_get_gift_statistics_total(self):
        r = self.mygrpc.get_gift_statistics_total(uid=1)
        print(r)

    def test_get_gift_stream(self):
        r = self.mygrpc.get_gift_stream()
        print(r)

    def test_get_gift_stream_v2(self):
        r = self.mygrpc.get_gift_stream_v2()
        print(r)

    def test_get_last_config(self):
        r = self.mygrpc.get_last_config()
        print(r)

    def test_get_last_send_gift(self):
        r = self.mygrpc.get_last_send_gift(room_id=1,uid=1)
        print(r)

    def test_get_list(self):
        r = self.mygrpc.get_list(page_num=1,page_size=1)
        print(r)

    def test_get_panel_tab(self):
        r = self.mygrpc.get_panel_tab(platform=1,room_id=1)
        print(r)

    def test_get_room_gift_and_bag_ids(self):
        r = self.mygrpc.get_room_gift_and_bag_ids(platform=1)
        print(r)

    def test_get_room_valid_gift_id(self):
        r = self.mygrpc.get_room_valid_gift_id(platform=1,room_id=1)
        print(r)

    def test_get_send_gift_stream(self):
        r = self.mygrpc.get_send_gift_stream()
        print(r)

    def test_get_special_plan_list(self):
        r = self.mygrpc.get_special_plan_list(page=1)
        print(r)

    def test_get_special_probability(self):
        r = self.mygrpc.get_special_probability(config_id=1,dimension=1,dimension_id=1)
        print(r)

    def test_get_stat(self):
        r = self.mygrpc.get_stat(id=1)
        print(r)

    def test_get_stream_by_order_id(self):
        r = self.mygrpc.get_stream_by_order_id(order_id=1,order_date=1)
        print(r)

    def test_get_stream_by_tid(self):
        r = self.mygrpc.get_stream_by_tid(tid=1,order_date=1)
        print(r)

    def test_gift_config(self):
        r = self.mygrpc.gift_config()
        print(r)

    def test_gift_memory_list(self):
        r = self.mygrpc.gift_memory_list(room_id=1)
        print(r)

    def test_gold_package_stream(self):
        r = self.mygrpc.gold_package_stream()
        print(r)

    def test_handle_gift_stat(self):
        r = self.mygrpc.handle_gift_stat(ruid=1,gift_id=1,gift_num=1,timestamp=1,msg_id=1)
        print(r)

    def test_join_fans_gift_info(self):
        r = self.mygrpc.join_fans_gift_info(platform=1,room_id=1)
        print(r)

    def test_live_discount_gift_list(self):
        r = self.mygrpc.live_discount_gift_list(platform=1,room_id=1)
        print(r)

    def test_live_gift_config(self):
        r = self.mygrpc.live_gift_config(platform=1)
        print(r)

    def test_live_room_gift_list(self):
        r = self.mygrpc.live_room_gift_list(platform=1,room_id=1)
        print(r)

    def test_my_tv_count(self):
        r = self.mygrpc.my_tv_count(uid=1)
        print(r)

    def test_offline_special_plan(self):
        r = self.mygrpc.offline_special_plan(plan_id=1)
        print(r)

    def test_prduce_childrem_stream(self):
        r = self.mygrpc.prduce_childrem_stream()
        print(r)

    def test_preview_room_gift_list(self):
        r = self.mygrpc.preview_room_gift_list(platform=1,room_id=1)
        print(r)

    def test_room_gift_list(self):
        r = self.mygrpc.room_gift_list()
        print(r)

    def test_room_gift_list_by_vote(self):
        r = self.mygrpc.room_gift_list_by_vote(room_id=1,area_parent_id=1,area_id=1)
        print(r)

    def test_send_combo_end(self):
        r = self.mygrpc.send_combo_end(uid=1,ruid=1,room_id=1,gift_id=1,gift_num=1,price=1,msg_id=1)
        print(r)

    def test_set_special_probability(self):
        r = self.mygrpc.set_special_probability(config_id=1,dimension=1,dimension_id=1,start_time=1,end_time=1,sp_probability=1)
        print(r)

    def test_set_vip_month_bag(self):
        r = self.mygrpc.set_vip_month_bag(uid=1)
        print(r)

    def test_silver_package_stream(self):
        r = self.mygrpc.silver_package_stream()
        print(r)

    def test_sms_reward(self):
        r = self.mygrpc.sms_reward()
        print(r)

    def test_special_plan(self):
        r = self.mygrpc.special_plan(biz_type=1,gift_list=1,online_time=1,offline_time=1,comment=1)
        print(r)

    def test_special_plan_detail(self):
        r = self.mygrpc.special_plan_detail(plan_id=1)
        print(r)

    def test_tab_room_gift_list(self):
        r = self.mygrpc.tab_room_gift_list(platform=1,room_id=1,tab_id=1)
        print(r)

    def test_update_special_plan(self):
        r = self.mygrpc.update_special_plan(biz_type=1,relevance_id=1,gift_list=1,online_time=1,offline_time=1,comment=1,plan_id=1)
        print(r)

    def test_user_gold_package_list(self):
        r = self.mygrpc.user_gold_package_list(uid=1)
        print(r)


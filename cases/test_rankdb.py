"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.rankdb import Rankdb


class TestRankdb(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Rankdb('live.rankdb')

    def test_add_rank_black(self):
        r = self.mygrpc.add_rank_black(uids=1,rankName=1,reason=1,status=1,operator=1)
        print(r)

    def test_behavior_guard(self):
        r = self.mygrpc.behavior_guard()
        print(r)

    def test_behavior_pay_live(self):
        r = self.mygrpc.behavior_pay_live()
        print(r)

    def test_behavior_red_pocket(self):
        r = self.mygrpc.behavior_red_pocket()
        print(r)

    def test_behavior_room_cut_area(self):
        r = self.mygrpc.behavior_room_cut_area()
        print(r)

    def test_behavior_send_danmu(self):
        r = self.mygrpc.behavior_send_danmu()
        print(r)

    def test_behavior_send_gift(self):
        r = self.mygrpc.behavior_send_gift()
        print(r)

    def test_behavior_super_message(self):
        r = self.mygrpc.behavior_super_message()
        print(r)

    def test_copy_rank(self):
        r = self.mygrpc.copy_rank()
        print(r)

    def test_decr(self):
        r = self.mygrpc.decr()
        print(r)

    def test_del_(self):
        r = self.mygrpc.del_()
        print(r)

    def test_delete_module(self):
        r = self.mygrpc.delete_module(uid=1,ruid=1,business_id=1)
        print(r)

    def test_export_rank_award_sql(self):
        r = self.mygrpc.export_rank_award_sql()
        print(r)

    def test_export_rank_sql(self):
        r = self.mygrpc.export_rank_sql()
        print(r)

    def test_general_rank_auto_battle_process_incr(self):
        r = self.mygrpc.general_rank_auto_battle_process_incr()
        print(r)

    def test_general_rank_auto_fix(self):
        r = self.mygrpc.general_rank_auto_fix(source=1,msg_id=1,start_time=1,end_time=1,rank_ids=1)
        print(r)

    def test_general_rank_auto_incr(self):
        r = self.mygrpc.general_rank_auto_incr()
        print(r)

    def test_general_rank_get_conf(self):
        r = self.mygrpc.general_rank_get_conf()
        print(r)

    def test_get_anchor_intimacy_rank(self):
        r = self.mygrpc.get_anchor_intimacy_rank(medal_id=1,page=1,page_size=1)
        print(r)

    def test_get_award_config_detail(self):
        r = self.mygrpc.get_award_config_detail()
        print(r)

    def test_get_award_config_list(self):
        r = self.mygrpc.get_award_config_list()
        print(r)

    def test_get_before_hot_rank_data(self):
        r = self.mygrpc.get_before_hot_rank_data()
        print(r)

    def test_get_gold_rank(self):
        r = self.mygrpc.get_gold_rank(roomId=1,rUid=1,page=1,pageSize=1)
        print(r)

    def test_get_heart_rank(self):
        r = self.mygrpc.get_heart_rank(ruid=1,page=1,page_size=1)
        print(r)

    def test_get_heart_rank_v2(self):
        r = self.mygrpc.get_heart_rank_v2(ruid=1,page=1,page_size=1)
        print(r)

    def test_get_hot_rank_info(self):
        r = self.mygrpc.get_hot_rank_info(room_id=1,ruid=1,source=1)
        print(r)

    def test_get_hot_rank_info_new(self):
        r = self.mygrpc.get_hot_rank_info_new(room_id=1,ruid=1,source=1)
        print(r)

    def test_get_live_round_rank(self):
        r = self.mygrpc.get_live_round_rank(ruid=1,roomId=1,liveId=1,page=1,pageSize=1)
        print(r)

    def test_get_new_online_rank(self):
        r = self.mygrpc.get_new_online_rank()
        print(r)

    def test_get_online_rank(self):
        r = self.mygrpc.get_online_rank()
        print(r)

    def test_get_online_rank_count(self):
        r = self.mygrpc.get_online_rank_count(roomId=1)
        print(r)

    def test_get_rank_award_list(self):
        r = self.mygrpc.get_rank_award_list()
        print(r)

    def test_get_rank_conf_by_ids(self):
        r = self.mygrpc.get_rank_conf_by_ids()
        print(r)

    def test_get_rank_detail(self):
        r = self.mygrpc.get_rank_detail()
        print(r)

    def test_get_rank_list(self):
        r = self.mygrpc.get_rank_list()
        print(r)

    def test_get_rank_list_batch_to_sql(self):
        r = self.mygrpc.get_rank_list_batch_to_sql()
        print(r)

    def test_get_seven_day_gold_rank(self):
        r = self.mygrpc.get_seven_day_gold_rank(room_id=1,ruid=1,page=1,page_size=1)
        print(r)

    def test_get_total_medal_level_rank(self):
        r = self.mygrpc.get_total_medal_level_rank()
        print(r)

    def test_get_user_hot_rank_info(self):
        r = self.mygrpc.get_user_hot_rank_info(ruid=1,room_id=1)
        print(r)

    def test_get_user_hot_rank_settlement(self):
        r = self.mygrpc.get_user_hot_rank_settlement(ruid=1,room_id=1)
        print(r)

    def test_get_user_rank_data(self):
        r = self.mygrpc.get_user_rank_data()
        print(r)

    def test_get_user_rank_in_room(self):
        r = self.mygrpc.get_user_rank_in_room()
        print(r)

    def test_gold_and_online_seven_top(self):
        r = self.mygrpc.gold_and_online_seven_top(roomId=1)
        print(r)

    def test_incr(self):
        r = self.mygrpc.incr()
        print(r)

    def test_is_in_before_hot_rank(self):
        r = self.mygrpc.is_in_before_hot_rank()
        print(r)

    def test_online(self):
        r = self.mygrpc.online(uid=1,room_id=1,msg_id=1,time_stamp=1)
        print(r)

    def test_online_gold_total_count(self):
        r = self.mygrpc.online_gold_total_count(ruid=1)
        print(r)

    def test_receive_enter_room_message(self):
        r = self.mygrpc.receive_enter_room_message()
        print(r)

    def test_receive_live_message(self):
        r = self.mygrpc.receive_live_message()
        print(r)

    def test_receive_streamer_offline_message(self):
        r = self.mygrpc.receive_streamer_offline_message(roomId=1,ruid=1,liveId=1,timestamp=1,msgId=1)
        print(r)

    def test_refresh_user_rank(self):
        r = self.mygrpc.refresh_user_rank()
        print(r)

    def test_rem_rank_black(self):
        r = self.mygrpc.rem_rank_black(id=1)
        print(r)

    def test_top(self):
        r = self.mygrpc.top()
        print(r)

    def test_update_rank_status(self):
        r = self.mygrpc.update_rank_status()
        print(r)

    def test_user_enter_room_online_rank(self):
        r = self.mygrpc.user_enter_room_online_rank()
        print(r)

    def test_user_get_online_rank(self):
        r = self.mygrpc.user_get_online_rank()
        print(r)

    def test_user_leave_room_gold(self):
        r = self.mygrpc.user_leave_room_gold()
        print(r)

    def test_user_leave_room_online_rank(self):
        r = self.mygrpc.user_leave_room_online_rank()
        print(r)


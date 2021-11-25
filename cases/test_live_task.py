"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.live_task import Live_task


class TestLive_task(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Live_task()

    def test_api_kpl_follow(self):
        r = self.mygrpc.api_kpl_follow(ruid=1,uid=1)
        print(r)

    def test_api_kpl_index(self):
        r = self.mygrpc.api_kpl_index()
        print(r)

    def test_approval_hamster_award(self):
        r = self.mygrpc.approval_hamster_award(act_id=1,time_type=1,approver=1)
        print(r)

    def test_cfs2020_follow(self):
        r = self.mygrpc.cfs2020_follow(ruid=1,uid=1)
        print(r)

    def test_cfs2020_index(self):
        r = self.mygrpc.cfs2020_index()
        print(r)

    def test_cfs2020_send_watch_task_award(self):
        r = self.mygrpc.cfs2020_send_watch_task_award()
        print(r)

    def test_check_user_today_live(self):
        r = self.mygrpc.check_user_today_live()
        print(r)

    def test_collect_card_gifts(self):
        r = self.mygrpc.collect_card_gifts()
        print(r)

    def test_count_act_need_send_message(self):
        r = self.mygrpc.count_act_need_send_message(act_id=1,time_type=1)
        print(r)

    def test_count_user_live(self):
        r = self.mygrpc.count_user_live()
        print(r)

    def test_fix_master_support(self):
        r = self.mygrpc.fix_master_support(id_list=1,old_act_id=1,new_act_id=1)
        print(r)

    def test_frozen_hamster_record(self):
        r = self.mygrpc.frozen_hamster_record(id=1,account_status=1,approver=1)
        print(r)

    def test_general_follow(self):
        r = self.mygrpc.general_follow(ruid=1,uid=1,game_type=1)
        print(r)

    def test_general_follow_status(self):
        r = self.mygrpc.general_follow_status()
        print(r)

    def test_get_ac_task_max_level(self):
        r = self.mygrpc.get_ac_task_max_level(act_id=1,ruid=1,req_timestamp=1)
        print(r)

    def test_get_act_m4_user_in_white(self):
        r = self.mygrpc.get_act_m4_user_in_white()
        print(r)

    def test_get_act_need_send_message(self):
        r = self.mygrpc.get_act_need_send_message(act_id=1,time_type=1,page=1,page_size=1)
        print(r)

    def test_get_act_task_award(self):
        r = self.mygrpc.get_act_task_award(uid=1,act_list=1)
        print(r)

    def test_get_act_task_hamster_award(self):
        r = self.mygrpc.get_act_task_hamster_award(uid=1,act_list=1)
        print(r)

    def test_get_act_task_star_award(self):
        r = self.mygrpc.get_act_task_star_award(uid=1,act_list=1)
        print(r)

    def test_get_act_user_in_white(self):
        r = self.mygrpc.get_act_user_in_white()
        print(r)

    def test_get_act_white_users(self):
        r = self.mygrpc.get_act_white_users()
        print(r)

    def test_get_activity_pay_and_free_task(self):
        r = self.mygrpc.get_activity_pay_and_free_task()
        print(r)

    def test_get_activity_task(self):
        r = self.mygrpc.get_activity_task()
        print(r)

    def test_get_activity_task_assist(self):
        r = self.mygrpc.get_activity_task_assist()
        print(r)

    def test_get_april_superstar_task_list(self):
        r = self.mygrpc.get_april_superstar_task_list(timestamp=1)
        print(r)

    def test_get_dragon_boat_task_list(self):
        r = self.mygrpc.get_dragon_boat_task_list(timestamp=1)
        print(r)

    def test_get_finalist_task(self):
        r = self.mygrpc.get_finalist_task()
        print(r)

    def test_get_finalist_task_aid_rank(self):
        r = self.mygrpc.get_finalist_task_aid_rank()
        print(r)

    def test_get_finalist_task_pendant(self):
        r = self.mygrpc.get_finalist_task_pendant()
        print(r)

    def test_get_finalist_task_rank(self):
        r = self.mygrpc.get_finalist_task_rank()
        print(r)

    def test_get_hamster_award_detail(self):
        r = self.mygrpc.get_hamster_award_detail(act_id=1,time_type=1,page=1,page_size=1)
        print(r)

    def test_get_hamster_summary_list(self):
        r = self.mygrpc.get_hamster_summary_list(page=1,page_size=1)
        print(r)

    def test_get_master_support(self):
        r = self.mygrpc.get_master_support()
        print(r)

    def test_get_master_support_pendant(self):
        r = self.mygrpc.get_master_support_pendant(room_id=1)
        print(r)

    def test_get_master_support_report(self):
        r = self.mygrpc.get_master_support_report(uid=1,gold_actid=1,traf_actid=1)
        print(r)

    def test_get_may_sweet_task_list(self):
        r = self.mygrpc.get_may_sweet_task_list(timestamp=1)
        print(r)

    def test_get_player_list(self):
        r = self.mygrpc.get_player_list()
        print(r)

    def test_get_speical_gold_task(self):
        r = self.mygrpc.get_speical_gold_task(uid=1)
        print(r)

    def test_get_task(self):
        r = self.mygrpc.get_task()
        print(r)

    def test_get_task_award(self):
        r = self.mygrpc.get_task_award()
        print(r)

    def test_get_task_info(self):
        r = self.mygrpc.get_task_info()
        print(r)

    def test_get_task_list(self):
        r = self.mygrpc.get_task_list(page=1,page_size=1)
        print(r)

    def test_get_task_pendant(self):
        r = self.mygrpc.get_task_pendant()
        print(r)

    def test_get_task_report_detail(self):
        r = self.mygrpc.get_task_report_detail()
        print(r)

    def test_get_task_report_info(self):
        r = self.mygrpc.get_task_report_info()
        print(r)

    def test_get_user_award_sum(self):
        r = self.mygrpc.get_user_award_sum(uid=1,act_list=1)
        print(r)

    def test_get_user_join_act(self):
        r = self.mygrpc.get_user_join_act(uid=1)
        print(r)

    def test_get_user_sub_task_cnt(self):
        r = self.mygrpc.get_user_sub_task_cnt()
        print(r)

    def test_get_user_task(self):
        r = self.mygrpc.get_user_task()
        print(r)

    def test_get_user_white_max_id(self):
        r = self.mygrpc.get_user_white_max_id(act_id=1)
        print(r)

    def test_insert_white_user(self):
        r = self.mygrpc.insert_white_user()
        print(r)

    def test_join_hamster_record(self):
        r = self.mygrpc.join_hamster_record(act_id=1,delay_day=1,source_id=1,transaction_id=1,award_num=1,uid=1,bag_id=1,time_type=1,award_type=1)
        print(r)

    def test_kpl_send_follow_task_award(self):
        r = self.mygrpc.kpl_send_follow_task_award()
        print(r)

    def test_kpl_send_watch_task_award(self):
        r = self.mygrpc.kpl_send_watch_task_award()
        print(r)

    def test_reward_center_call_back(self):
        r = self.mygrpc.reward_center_call_back()
        print(r)

    def test_share(self):
        r = self.mygrpc.share()
        print(r)

    def test_share_status(self):
        r = self.mygrpc.share_status()
        print(r)

    def test_task_pendant(self):
        r = self.mygrpc.task_pendant(room_id=1)
        print(r)

    def test_zrange_user_live(self):
        r = self.mygrpc.zrange_user_live()
        print(r)


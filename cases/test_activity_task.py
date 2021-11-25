"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.activity_task import Activity_task


class TestActivity_task(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Activity_task()

    def test_act_apply_live_up(self):
        r = self.mygrpc.act_apply_live_up()
        print(r)

    def test_add_milestone_data(self):
        r = self.mygrpc.add_milestone_data(task_id=1,time_length=1,reward_type=1,reward_id=1,reward_num=1,expire_type=1)
        print(r)

    def test_add_user_act(self):
        r = self.mygrpc.add_user_act(creater=1)
        print(r)

    def test_anchor_day_plan(self):
        r = self.mygrpc.anchor_day_plan(task_id=1)
        print(r)

    def test_anchor_production_plan(self):
        r = self.mygrpc.anchor_production_plan(ruid=1)
        print(r)

    def test_anchor_task_info(self):
        r = self.mygrpc.anchor_task_info(uid=1)
        print(r)

    def test_apply_live_up(self):
        r = self.mygrpc.apply_live_up(uid=1)
        print(r)

    def test_apply_live_up3(self):
        r = self.mygrpc.apply_live_up3()
        print(r)

    def test_apply_live_up4(self):
        r = self.mygrpc.apply_live_up4()
        print(r)

    def test_apply_live_up_august(self):
        r = self.mygrpc.apply_live_up_august()
        print(r)

    def test_apply_up4_condition(self):
        r = self.mygrpc.apply_up4_condition()
        print(r)

    def test_arcs(self):
        r = self.mygrpc.arcs(aids=1)
        print(r)

    def test_batch_add_subscribe_user(self):
        r = self.mygrpc.batch_add_subscribe_user(id=1,csv_content=1)
        print(r)

    def test_batch_reserve(self):
        r = self.mygrpc.batch_reserve(uid=1,subscribe_ids=1)
        print(r)

    def test_bind_relation(self):
        r = self.mygrpc.bind_relation(activity_id=1,uid=1,share_uid=1,share_code=1,risk_param=1)
        print(r)

    def test_check_get_gift_package_condition(self):
        r = self.mygrpc.check_get_gift_package_condition(package_id=1,uid=1)
        print(r)

    def test_del_member_cache(self):
        r = self.mygrpc.del_member_cache(uid=1)
        print(r)

    def test_del_milestone_data(self):
        r = self.mygrpc.del_milestone_data(task_id=1,milestone_id=1)
        print(r)

    def test_del_subscribe_user(self):
        r = self.mygrpc.del_subscribe_user(info_id=1)
        print(r)

    def test_del_user_task_child(self):
        r = self.mygrpc.del_user_task_child(task_id=1)
        print(r)

    def test_edit_subscribe_info(self):
        r = self.mygrpc.edit_subscribe_info(subscribe_name=1,subscribe_type=1,creater=1)
        print(r)

    def test_fans_medal_query(self):
        r = self.mygrpc.fans_medal_query(ruid=1,fans_award_type=1)
        print(r)

    def test_get_act_info_and_task_list(self):
        r = self.mygrpc.get_act_info_and_task_list()
        print(r)

    def test_get_act_pool_info(self):
        r = self.mygrpc.get_act_pool_info()
        print(r)

    def test_get_act_reward(self):
        r = self.mygrpc.get_act_reward()
        print(r)

    def test_get_act_up4_info(self):
        r = self.mygrpc.get_act_up4_info()
        print(r)

    def test_get_act_up_august_info(self):
        r = self.mygrpc.get_act_up_august_info()
        print(r)

    def test_get_act_user_infos(self):
        r = self.mygrpc.get_act_user_infos(uids=1)
        print(r)

    def test_get_activity_task_info(self):
        r = self.mygrpc.get_activity_task_info()
        print(r)

    def test_get_activity_task_progress(self):
        r = self.mygrpc.get_activity_task_progress()
        print(r)

    def test_get_all_gift_package_list(self):
        r = self.mygrpc.get_all_gift_package_list(firm_name=1)
        print(r)

    def test_get_all_plan(self):
        r = self.mygrpc.get_all_plan()
        print(r)

    def test_get_anchor_info(self):
        r = self.mygrpc.get_anchor_info()
        print(r)

    def test_get_anchor_people_type(self):
        r = self.mygrpc.get_anchor_people_type(uid=1)
        print(r)

    def test_get_anchor_task(self):
        r = self.mygrpc.get_anchor_task()
        print(r)

    def test_get_anchor_task_level_info(self):
        r = self.mygrpc.get_anchor_task_level_info(task_id=1)
        print(r)

    def test_get_anchor_task_level_reward(self):
        r = self.mygrpc.get_anchor_task_level_reward(task_id=1,level=1,uid=1)
        print(r)

    def test_get_anchor_task_list_by_act_id(self):
        r = self.mygrpc.get_anchor_task_list_by_act_id(act_id=1)
        print(r)

    def test_get_anchor_task_status(self):
        r = self.mygrpc.get_anchor_task_status(ruid=1,task_id=1)
        print(r)

    def test_get_anchor_task_widget(self):
        r = self.mygrpc.get_anchor_task_widget(ruid=1,task_id=1)
        print(r)

    def test_get_award_pool_list(self):
        r = self.mygrpc.get_award_pool_list(pool_ids=1)
        print(r)

    def test_get_current_anchor_task(self):
        r = self.mygrpc.get_current_anchor_task(uid=1)
        print(r)

    def test_get_current_main_task_info_by_act_id(self):
        r = self.mygrpc.get_current_main_task_info_by_act_id(act_id=1)
        print(r)

    def test_get_current_main_task_info_by_task_id(self):
        r = self.mygrpc.get_current_main_task_info_by_task_id(task_id=1)
        print(r)

    def test_get_dragon_boat_act_progress(self):
        r = self.mygrpc.get_dragon_boat_act_progress()
        print(r)

    def test_get_join_info(self):
        r = self.mygrpc.get_join_info(uid=1)
        print(r)

    def test_get_join_type(self):
        r = self.mygrpc.get_join_type(uid=1)
        print(r)

    def test_get_level_status_by_task_id(self):
        r = self.mygrpc.get_level_status_by_task_id(task_id=1,uid=1)
        print(r)

    def test_get_live_up3_act_info(self):
        r = self.mygrpc.get_live_up3_act_info()
        print(r)

    def test_get_main_task_info_by_act_id(self):
        r = self.mygrpc.get_main_task_info_by_act_id(act_id=1)
        print(r)

    def test_get_main_task_info_by_task_id(self):
        r = self.mygrpc.get_main_task_info_by_task_id(task_id=1)
        print(r)

    def test_get_master5_pendant(self):
        r = self.mygrpc.get_master5_pendant(room_id=1)
        print(r)

    def test_get_milestone_list(self):
        r = self.mygrpc.get_milestone_list(task_id=1)
        print(r)

    def test_get_new_user_task_infinite_progress(self):
        r = self.mygrpc.get_new_user_task_infinite_progress(task_id=1)
        print(r)

    def test_get_new_user_task_info(self):
        r = self.mygrpc.get_new_user_task_info(task_id=1)
        print(r)

    def test_get_new_user_task_info_all_level(self):
        r = self.mygrpc.get_new_user_task_info_all_level(task_id=1)
        print(r)

    def test_get_new_user_task_july_star_progress(self):
        r = self.mygrpc.get_new_user_task_july_star_progress(task_id=1)
        print(r)

    def test_get_open_platform_task_reward(self):
        r = self.mygrpc.get_open_platform_task_reward(task_id=1,level=1)
        print(r)

    def test_get_original_god_task(self):
        r = self.mygrpc.get_original_god_task()
        print(r)

    def test_get_original_god_task_september(self):
        r = self.mygrpc.get_original_god_task_september()
        print(r)

    def test_get_percentage_task_target_num(self):
        r = self.mygrpc.get_percentage_task_target_num(uid=1,sub_task_id=1,cycle_id=1,level=1)
        print(r)

    def test_get_play_back_status(self):
        r = self.mygrpc.get_play_back_status(uid=1)
        print(r)

    def test_get_preheat_award(self):
        r = self.mygrpc.get_preheat_award(uid=1,stage_id=1)
        print(r)

    def test_get_preheat_info(self):
        r = self.mygrpc.get_preheat_info()
        print(r)

    def test_get_qualified_task_list_by_act_id(self):
        r = self.mygrpc.get_qualified_task_list_by_act_id(act_id=1)
        print(r)

    def test_get_rewards_by_level(self):
        r = self.mygrpc.get_rewards_by_level(act_id=1,uid=1,level=1)
        print(r)

    def test_get_rewards_list(self):
        r = self.mygrpc.get_rewards_list(act_id=1,uid=1,level=1)
        print(r)

    def test_get_share_code(self):
        r = self.mygrpc.get_share_code(activity_id=1,uid=1)
        print(r)

    def test_get_share_info(self):
        r = self.mygrpc.get_share_info(activity_id=1,share_uid=1,share_code=1)
        print(r)

    def test_get_share_status(self):
        r = self.mygrpc.get_share_status(uid=1,date=1)
        print(r)

    def test_get_subscribe_info(self):
        r = self.mygrpc.get_subscribe_info(id=1)
        print(r)

    def test_get_subscribe_info_list(self):
        r = self.mygrpc.get_subscribe_info_list(id=1,page=1,page_size=1)
        print(r)

    def test_get_subscribe_list(self):
        r = self.mygrpc.get_subscribe_list(page=1,page_size=1)
        print(r)

    def test_get_task_data_list_by_act_id(self):
        r = self.mygrpc.get_task_data_list_by_act_id(act_id=1)
        print(r)

    def test_get_task_id_list(self):
        r = self.mygrpc.get_task_id_list(task_id=1)
        print(r)

    def test_get_task_infinite_progress(self):
        r = self.mygrpc.get_task_infinite_progress(task_id=1)
        print(r)

    def test_get_task_info_by_act_id(self):
        r = self.mygrpc.get_task_info_by_act_id(act_id=1)
        print(r)

    def test_get_task_level_by_act_id(self):
        r = self.mygrpc.get_task_level_by_act_id(act_id=1)
        print(r)

    def test_get_task_level_by_task_id(self):
        r = self.mygrpc.get_task_level_by_task_id(task_id=1)
        print(r)

    def test_get_task_level_list(self):
        r = self.mygrpc.get_task_level_list(task_id=1)
        print(r)

    def test_get_task_list(self):
        r = self.mygrpc.get_task_list()
        print(r)

    def test_get_task_one(self):
        r = self.mygrpc.get_task_one()
        print(r)

    def test_get_task_reward_info(self):
        r = self.mygrpc.get_task_reward_info()
        print(r)

    def test_get_user_activity_task_award(self):
        r = self.mygrpc.get_user_activity_task_award(act_id=1,task_id=1,level_id=1,uid=1)
        print(r)

    def test_get_user_activity_task_info(self):
        r = self.mygrpc.get_user_activity_task_info()
        print(r)

    def test_get_user_activity_task_progress(self):
        r = self.mygrpc.get_user_activity_task_progress()
        print(r)

    def test_get_user_by_sub_task(self):
        r = self.mygrpc.get_user_by_sub_task(task_id=1)
        print(r)

    def test_get_user_task(self):
        r = self.mygrpc.get_user_task()
        print(r)

    def test_get_user_task_child_info(self):
        r = self.mygrpc.get_user_task_child_info(task_id=1)
        print(r)

    def test_get_user_task_child_list(self):
        r = self.mygrpc.get_user_task_child_list(task_id=1)
        print(r)

    def test_get_user_task_info(self):
        r = self.mygrpc.get_user_task_info(task_id=1)
        print(r)

    def test_get_user_task_list(self):
        r = self.mygrpc.get_user_task_list(page=1,page_size=1)
        print(r)

    def test_get_user_task_list_by_act_id(self):
        r = self.mygrpc.get_user_task_list_by_act_id(act_id=1)
        print(r)

    def test_get_user_watch_task_info(self):
        r = self.mygrpc.get_user_watch_task_info(task_id=1)
        print(r)

    def test_get_user_watch_task_list(self):
        r = self.mygrpc.get_user_watch_task_list(page=1,page_size=1)
        print(r)

    def test_get_watch_task_info(self):
        r = self.mygrpc.get_watch_task_info(task_id=1)
        print(r)

    def test_get_watch_task_status(self):
        r = self.mygrpc.get_watch_task_status(task_id=1,timestamp=1)
        print(r)

    def test_get_watch_time_level(self):
        r = self.mygrpc.get_watch_time_level()
        print(r)

    def test_init_anchor_task(self):
        r = self.mygrpc.init_anchor_task()
        print(r)

    def test_init_task_record(self):
        r = self.mygrpc.init_task_record()
        print(r)

    def test_join_activity(self):
        r = self.mygrpc.join_activity(uid=1,risk_param=1)
        print(r)

    def test_live_up_reserve_info(self):
        r = self.mygrpc.live_up_reserve_info(uid=1,sids=1)
        print(r)

    def test_modify_milestone_data(self):
        r = self.mygrpc.modify_milestone_data(task_id=1,milestone_id=1,time_length=1,reward_type=1,reward_id=1,reward_num=1,expire_type=1)
        print(r)

    def test_original_god_receive_reward(self):
        r = self.mygrpc.original_god_receive_reward(task_id=1)
        print(r)

    def test_original_god_receive_reward_september(self):
        r = self.mygrpc.original_god_receive_reward_september(task_id=1)
        print(r)

    def test_receive_prize(self):
        r = self.mygrpc.receive_prize(sub_task_id=1,level=1,uid=1)
        print(r)

    def test_receive_reward(self):
        r = self.mygrpc.receive_reward(uid=1)
        print(r)

    def test_receive_reward_record(self):
        r = self.mygrpc.receive_reward_record(uid=1)
        print(r)

    def test_receive_task_reward(self):
        r = self.mygrpc.receive_task_reward(reward_source=1,uid=1)
        print(r)

    def test_recommended_anchor_daily(self):
        r = self.mygrpc.recommended_anchor_daily(sid=1,page=1,page_size=1,live_status=1)
        print(r)

    def test_recommended_program_daily(self):
        r = self.mygrpc.recommended_program_daily(sid=1,page=1,page_size=1,live_status=1)
        print(r)

    def test_search_anchor_task(self):
        r = self.mygrpc.search_anchor_task()
        print(r)

    def test_search_user_act(self):
        r = self.mygrpc.search_user_act()
        print(r)

    def test_search_user_task(self):
        r = self.mygrpc.search_user_task()
        print(r)

    def test_send_fail_task_data(self):
        r = self.mygrpc.send_fail_task_data(task_type=1,try_time=1,source_data=1)
        print(r)

    def test_set_user_watch_task_state(self):
        r = self.mygrpc.set_user_watch_task_state(task_id=1,state=1)
        print(r)

    def test_sync_user_task_watch_conf(self):
        r = self.mygrpc.sync_user_task_watch_conf(task_id=1)
        print(r)

    def test_sync_user_task_watch_conf_new(self):
        r = self.mygrpc.sync_user_task_watch_conf_new(task_id=1)
        print(r)

    def test_sync_user_watch_conf(self):
        r = self.mygrpc.sync_user_watch_conf(task_id=1)
        print(r)

    def test_up_down_act_task(self):
        r = self.mygrpc.up_down_act_task(task_id=1)
        print(r)

    def test_up_down_task(self):
        r = self.mygrpc.up_down_task()
        print(r)

    def test_up_down_user_act_task(self):
        r = self.mygrpc.up_down_user_act_task(task_id=1)
        print(r)

    def test_up_or_down_task(self):
        r = self.mygrpc.up_or_down_task(task_id=1)
        print(r)

    def test_update_user_act(self):
        r = self.mygrpc.update_user_act(id=1,act_name=1)
        print(r)

    def test_update_user_task_info(self):
        r = self.mygrpc.update_user_task_info(start_time=1,end_time=1,creater=1)
        print(r)

    def test_user_share(self):
        r = self.mygrpc.user_share()
        print(r)

    def test_user_task_sign(self):
        r = self.mygrpc.user_task_sign()
        print(r)

    def test_watch_video_tutorial(self):
        r = self.mygrpc.watch_video_tutorial(uid=1,task_id=1,sub_task_id=1)
        print(r)


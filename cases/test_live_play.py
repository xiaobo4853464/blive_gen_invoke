"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.live_play import Live_play


class TestLive_play(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Live_play()

    def test_add(self):
        r = self.mygrpc.add(type=1,type_id=1,wish_limit=1,content=1,user_id=1,platform=1)
        print(r)

    def test_add_banner(self):
        r = self.mygrpc.add_banner()
        print(r)

    def test_add_conf(self):
        r = self.mygrpc.add_conf(type=1,online_time=1)
        print(r)

    def test_add_conf_for_gift_job(self):
        r = self.mygrpc.add_conf_for_gift_job(type=1,online_time=1)
        print(r)

    def test_add_resource(self):
        r = self.mygrpc.add_resource(title=1,left_color=1,right_color=1)
        print(r)

    def test_answer(self):
        r = self.mygrpc.answer()
        print(r)

    def test_apply_birth_party(self):
        r = self.mygrpc.apply_birth_party()
        print(r)

    def test_apply_today(self):
        r = self.mygrpc.apply_today(uid=1,date=1,operator=1)
        print(r)

    def test_audit(self):
        r = self.mygrpc.audit(ids=1,status=1)
        print(r)

    def test_available_wish_list(self):
        r = self.mygrpc.available_wish_list(ruid=1)
        print(r)

    def test_batch_publish_msg(self):
        r = self.mygrpc.batch_publish_msg(act_id=1,start_time=1,end_time=1)
        print(r)

    def test_block_room_list(self):
        r = self.mygrpc.block_room_list()
        print(r)

    def test_change_wishing_bottle_switch(self):
        r = self.mygrpc.change_wishing_bottle_switch()
        print(r)

    def test_close_banner(self):
        r = self.mygrpc.close_banner(id=1)
        print(r)

    def test_config(self):
        r = self.mygrpc.config(uid=1)
        print(r)

    def test_del_conf(self):
        r = self.mygrpc.del_conf(id=1)
        print(r)

    def test_delete(self):
        r = self.mygrpc.delete(id=1,uid=1)
        print(r)

    def test_download_machine_award_list(self):
        r = self.mygrpc.download_machine_award_list()
        print(r)

    def test_export_birth(self):
        r = self.mygrpc.export_birth()
        print(r)

    def test_finish(self):
        r = self.mygrpc.finish(id=1,uid=1)
        print(r)

    def test_get_all_window_status(self):
        r = self.mygrpc.get_all_window_status()
        print(r)

    def test_get_banner_by_id(self):
        r = self.mygrpc.get_banner_by_id(id=1)
        print(r)

    def test_get_birth_anchor_by_day(self):
        r = self.mygrpc.get_birth_anchor_by_day()
        print(r)

    def test_get_birth_list(self):
        r = self.mygrpc.get_birth_list()
        print(r)

    def test_get_birth_party(self):
        r = self.mygrpc.get_birth_party()
        print(r)

    def test_get_blood_energy(self):
        r = self.mygrpc.get_blood_energy(active_id=1,play_id=1,room_id=1)
        print(r)

    def test_get_boss(self):
        r = self.mygrpc.get_boss()
        print(r)

    def test_get_conf(self):
        r = self.mygrpc.get_conf(id=1)
        print(r)

    def test_get_conf_detail(self):
        r = self.mygrpc.get_conf_detail(id=1)
        print(r)

    def test_get_conf_list(self):
        r = self.mygrpc.get_conf_list()
        print(r)

    def test_get_event_info(self):
        r = self.mygrpc.get_event_info()
        print(r)

    def test_get_harm_award_info(self):
        r = self.mygrpc.get_harm_award_info()
        print(r)

    def test_get_info_by_gift(self):
        r = self.mygrpc.get_info_by_gift(gift_id=1,gift_name=1,gift_num=1,uid=1,room_id=1,t_id=1,uname=1,areaId=1)
        print(r)

    def test_get_last_battle_result(self):
        r = self.mygrpc.get_last_battle_result(active_id=1,play_id=1,room_id=1)
        print(r)

    def test_get_list(self):
        r = self.mygrpc.get_list(page=1)
        print(r)

    def test_get_lpl_room_play_info(self):
        r = self.mygrpc.get_lpl_room_play_info()
        print(r)

    def test_get_lpl_room_play_time(self):
        r = self.mygrpc.get_lpl_room_play_time()
        print(r)

    def test_get_luck_award_info(self):
        r = self.mygrpc.get_luck_award_info()
        print(r)

    def test_get_machine_award_info(self):
        r = self.mygrpc.get_machine_award_info()
        print(r)

    def test_get_machine_award_list(self):
        r = self.mygrpc.get_machine_award_list()
        print(r)

    def test_get_message(self):
        r = self.mygrpc.get_message()
        print(r)

    def test_get_messages_by_condition(self):
        r = self.mygrpc.get_messages_by_condition(act_id=1,ruid=1,uid=1,start_time=1,end_time=1)
        print(r)

    def test_get_msg_list(self):
        r = self.mygrpc.get_msg_list(page=1,page_size=1,act_id=1,start_time=1,end_time=1)
        print(r)

    def test_get_resou_byid(self):
        r = self.mygrpc.get_resou_byid(room_id=1,play_id=1,activity_id=1)
        print(r)

    def test_get_resource_detail(self):
        r = self.mygrpc.get_resource_detail(id=1)
        print(r)

    def test_get_score(self):
        r = self.mygrpc.get_score()
        print(r)

    def test_get_user_machine_award_list(self):
        r = self.mygrpc.get_user_machine_award_list()
        print(r)

    def test_get_user_machine_award_text(self):
        r = self.mygrpc.get_user_machine_award_text()
        print(r)

    def test_get_widget_banner_list(self):
        r = self.mygrpc.get_widget_banner_list(room_id=1,ruid=1,platform=1)
        print(r)

    def test_getanswerinfo(self):
        r = self.mygrpc.getanswerinfo()
        print(r)

    def test_hot_words(self):
        r = self.mygrpc.hot_words(uid=1)
        print(r)

    def test_is_active_battle(self):
        r = self.mygrpc.is_active_battle(active_id=1,play_id=1)
        print(r)

    def test_is_battle(self):
        r = self.mygrpc.is_battle()
        print(r)

    def test_notify(self):
        r = self.mygrpc.notify()
        print(r)

    def test_offline_conf(self):
        r = self.mygrpc.offline_conf(id=1)
        print(r)

    def test_on_battle_event(self):
        r = self.mygrpc.on_battle_event(activity_id=1,play_id=1,room_id=1,battle_id=1,battle_status=1)
        print(r)

    def test_panel_data(self):
        r = self.mygrpc.panel_data(room_id=1)
        print(r)

    def test_panel_data_v2(self):
        r = self.mygrpc.panel_data_v2(room_id=1)
        print(r)

    def test_panel_data_v3(self):
        r = self.mygrpc.panel_data_v3(room_id=1)
        print(r)

    def test_panel_hour_broadcast(self):
        r = self.mygrpc.panel_hour_broadcast()
        print(r)

    def test_panel_list(self):
        r = self.mygrpc.panel_list(page=1,page_size=1)
        print(r)

    def test_panel_list_v2(self):
        r = self.mygrpc.panel_list_v2(page=1,page_size=1)
        print(r)

    def test_processing_wish_list(self):
        r = self.mygrpc.processing_wish_list(ruid=1,platform=1)
        print(r)

    def test_query_battle_i_d(self):
        r = self.mygrpc.query_battle_i_d(activity_id=1,play_id=1,room_id=1)
        print(r)

    def test_query_battle_record(self):
        r = self.mygrpc.query_battle_record(activity_id=1,play_id=1,room_id=1)
        print(r)

    def test_search_wish_list(self):
        r = self.mygrpc.search_wish_list()
        print(r)

    def test_send_message(self):
        r = self.mygrpc.send_message()
        print(r)

    def test_send_special_effect(self):
        r = self.mygrpc.send_special_effect(effect_id=1,room_ids=1)
        print(r)

    def test_set_alert_window_show(self):
        r = self.mygrpc.set_alert_window_show()
        print(r)

    def test_set_room_block(self):
        r = self.mygrpc.set_room_block(roomid=1)
        print(r)

    def test_up_or_down_msg(self):
        r = self.mygrpc.up_or_down_msg()
        print(r)

    def test_update_banner(self):
        r = self.mygrpc.update_banner(id=1)
        print(r)

    def test_update_bind_gift_id(self):
        r = self.mygrpc.update_bind_gift_id(effect_ids=1,gift_id=1,add_or_del=1)
        print(r)

    def test_update_birth(self):
        r = self.mygrpc.update_birth()
        print(r)

    def test_update_conf(self):
        r = self.mygrpc.update_conf(type=1,online_time=1,id=1)
        print(r)

    def test_update_widget_banner(self):
        r = self.mygrpc.update_widget_banner(update_type=1,source=1)
        print(r)

    def test_wish_list(self):
        r = self.mygrpc.wish_list()
        print(r)


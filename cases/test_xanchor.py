"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.xanchor import Xanchor


class TestXanchor(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Xanchor()

    def test_add_guide(self):
        r = self.mygrpc.add_guide(type=1,link=1,cover_url=1,weight=1,title=1)
        print(r)

    def test_add_pendant_to_room(self):
        r = self.mygrpc.add_pendant_to_room(uid=1,room_id=1,module_id=1)
        print(r)

    def test_add_program(self):
        r = self.mygrpc.add_program(ruid=1,start_time=1,title=1)
        print(r)

    def test_add_push_rule(self):
        r = self.mygrpc.add_push_rule(position=1,title=1,guide_ids=1)
        print(r)

    def test_add_recommend(self):
        r = self.mygrpc.add_recommend(ruid=1,start_time=1,end_time=1)
        print(r)

    def test_add_to_calendar(self):
        r = self.mygrpc.add_to_calendar(uid=1)
        print(r)

    def test_add_white_list(self):
        r = self.mygrpc.add_white_list(ruids=1)
        print(r)

    def test_apply_revert(self):
        r = self.mygrpc.apply_revert()
        print(r)

    def test_category_list(self):
        r = self.mygrpc.category_list()
        print(r)

    def test_change_pop_conf_status(self):
        r = self.mygrpc.change_pop_conf_status(id=1,status=1)
        print(r)

    def test_create_room(self):
        r = self.mygrpc.create_room()
        print(r)

    def test_danmu_notify(self):
        r = self.mygrpc.danmu_notify()
        print(r)

    def test_del_category(self):
        r = self.mygrpc.del_category()
        print(r)

    def test_del_icon(self):
        r = self.mygrpc.del_icon()
        print(r)

    def test_del_param(self):
        r = self.mygrpc.del_param()
        print(r)

    def test_del_phone(self):
        r = self.mygrpc.del_phone()
        print(r)

    def test_del_pop_conf(self):
        r = self.mygrpc.del_pop_conf(id=1)
        print(r)

    def test_del_share_conf(self):
        r = self.mygrpc.del_share_conf(room_id=1,source_platform=1,target_platform=1)
        print(r)

    def test_del_virtual_image_model(self):
        r = self.mygrpc.del_virtual_image_model(uid=1)
        print(r)

    def test_del_white_room(self):
        r = self.mygrpc.del_white_room()
        print(r)

    def test_delete_guide(self):
        r = self.mygrpc.delete_guide(id=1)
        print(r)

    def test_delete_push_rule(self):
        r = self.mygrpc.delete_push_rule(id=1)
        print(r)

    def test_delete_recommend(self):
        r = self.mygrpc.delete_recommend(ruid=1,id=1)
        print(r)

    def test_delete_white_list(self):
        r = self.mygrpc.delete_white_list(id=1,ruid=1)
        print(r)

    def test_detach_pendant_from_room(self):
        r = self.mygrpc.detach_pendant_from_room(uid=1,room_id=1,module_id=1)
        print(r)

    def test_fetch_anchor_switch(self):
        r = self.mygrpc.fetch_anchor_switch()
        print(r)

    def test_gen_and_get_info(self):
        r = self.mygrpc.gen_and_get_info()
        print(r)

    def test_get_add_to_calendar(self):
        r = self.mygrpc.get_add_to_calendar(uid=1)
        print(r)

    def test_get_anchor_guides(self):
        r = self.mygrpc.get_anchor_guides(uid=1,position=1)
        print(r)

    def test_get_anchor_pendant_cfg(self):
        r = self.mygrpc.get_anchor_pendant_cfg(uid=1)
        print(r)

    def test_get_anchor_pendant_info(self):
        r = self.mygrpc.get_anchor_pendant_info(uid=1)
        print(r)

    def test_get_anchor_switch(self):
        r = self.mygrpc.get_anchor_switch()
        print(r)

    def test_get_anchor_tags(self):
        r = self.mygrpc.get_anchor_tags(room_ids=1)
        print(r)

    def test_get_anchor_tags_by_uids(self):
        r = self.mygrpc.get_anchor_tags_by_uids(uids=1)
        print(r)

    def test_get_anchor_tags_list(self):
        r = self.mygrpc.get_anchor_tags_list(room_ids=1)
        print(r)

    def test_get_anchor_tags_list_by_uids(self):
        r = self.mygrpc.get_anchor_tags_list_by_uids(uids=1)
        print(r)

    def test_get_background_list(self):
        r = self.mygrpc.get_background_list()
        print(r)

    def test_get_blink_virtual_matter(self):
        r = self.mygrpc.get_blink_virtual_matter(sex=1,build=1,platform=1)
        print(r)

    def test_get_category(self):
        r = self.mygrpc.get_category()
        print(r)

    def test_get_channel_id_and_cdn(self):
        r = self.mygrpc.get_channel_id_and_cdn(business_type=1,old_ch_id=1,uids=1,timeoutTime=1)
        print(r)

    def test_get_guide_count(self):
        r = self.mygrpc.get_guide_count()
        print(r)

    def test_get_guide_detail(self):
        r = self.mygrpc.get_guide_detail(id=1)
        print(r)

    def test_get_guide_list(self):
        r = self.mygrpc.get_guide_list()
        print(r)

    def test_get_history_job(self):
        r = self.mygrpc.get_history_job(job_id=1)
        print(r)

    def test_get_history_title_by_keyword(self):
        r = self.mygrpc.get_history_title_by_keyword()
        print(r)

    def test_get_icon(self):
        r = self.mygrpc.get_icon()
        print(r)

    def test_get_log_list(self):
        r = self.mygrpc.get_log_list()
        print(r)

    def test_get_mission(self):
        r = self.mygrpc.get_mission(observer_name=1)
        print(r)

    def test_get_param(self):
        r = self.mygrpc.get_param()
        print(r)

    def test_get_phone(self):
        r = self.mygrpc.get_phone()
        print(r)

    def test_get_pop_conf(self):
        r = self.mygrpc.get_pop_conf(source=1,place=1)
        print(r)

    def test_get_program_by_id(self):
        r = self.mygrpc.get_program_by_id(program_id=1)
        print(r)

    def test_get_program_info(self):
        r = self.mygrpc.get_program_info(uid=1,p_id=1,platform=1)
        print(r)

    def test_get_program_list(self):
        r = self.mygrpc.get_program_list()
        print(r)

    def test_get_push_rule_detail(self):
        r = self.mygrpc.get_push_rule_detail(id=1)
        print(r)

    def test_get_push_rule_list(self):
        r = self.mygrpc.get_push_rule_list()
        print(r)

    def test_get_re_title_job_status(self):
        r = self.mygrpc.get_re_title_job_status(job_id=1)
        print(r)

    def test_get_recommend_list(self):
        r = self.mygrpc.get_recommend_list(page=1)
        print(r)

    def test_get_room_news(self):
        r = self.mygrpc.get_room_news()
        print(r)

    def test_get_san_by_uid(self):
        r = self.mygrpc.get_san_by_uid(uid=1)
        print(r)

    def test_get_san_log_list(self):
        r = self.mygrpc.get_san_log_list(uid=1)
        print(r)

    def test_get_share_conf(self):
        r = self.mygrpc.get_share_conf(room_id=1)
        print(r)

    def test_get_status_program_by_id(self):
        r = self.mygrpc.get_status_program_by_id(uid=1,program_id=1)
        print(r)

    def test_get_stickers_by_id(self):
        r = self.mygrpc.get_stickers_by_id(id=1)
        print(r)

    def test_get_stickers_text_list(self):
        r = self.mygrpc.get_stickers_text_list()
        print(r)

    def test_get_virtual_image_all_model(self):
        r = self.mygrpc.get_virtual_image_all_model(virtual_ids=1)
        print(r)

    def test_get_virtual_image_encrypt_job(self):
        r = self.mygrpc.get_virtual_image_encrypt_job()
        print(r)

    def test_get_virtual_image_model(self):
        r = self.mygrpc.get_virtual_image_model(virtual_ids=1)
        print(r)

    def test_get_virtual_image_secret(self):
        r = self.mygrpc.get_virtual_image_secret(model_ids=1,uid=1)
        print(r)

    def test_get_virtual_image_secret_usage_record(self):
        r = self.mygrpc.get_virtual_image_secret_usage_record()
        print(r)

    def test_get_virtual_matter(self):
        r = self.mygrpc.get_virtual_matter(page=1)
        print(r)

    def test_get_virtual_position(self):
        r = self.mygrpc.get_virtual_position(page=1)
        print(r)

    def test_get_virtual_record(self):
        r = self.mygrpc.get_virtual_record()
        print(r)

    def test_get_virtual_storm_infos(self):
        r = self.mygrpc.get_virtual_storm_infos(room_id=1,area_id=1)
        print(r)

    def test_get_virtual_storm_switch(self):
        r = self.mygrpc.get_virtual_storm_switch(room_id=1)
        print(r)

    def test_get_virtual_storm_touched_times_by_day(self):
        r = self.mygrpc.get_virtual_storm_touched_times_by_day(room_id=1,area_id=1)
        print(r)

    def test_get_virtual_thermal_storm_info(self):
        r = self.mygrpc.get_virtual_thermal_storm_info(room_id=1)
        print(r)

    def test_get_virtual_thermal_storm_info_v2(self):
        r = self.mygrpc.get_virtual_thermal_storm_info_v2(room_id=1)
        print(r)

    def test_get_votes_list(self):
        r = self.mygrpc.get_votes_list(audit_model=1)
        print(r)

    def test_get_white_list(self):
        r = self.mygrpc.get_white_list(page=1)
        print(r)

    def test_get_white_room(self):
        r = self.mygrpc.get_white_room()
        print(r)

    def test_hide_virtual_mat_pos(self):
        r = self.mygrpc.hide_virtual_mat_pos(type=1,status=1,id=1)
        print(r)

    def test_hit_clarity(self):
        r = self.mygrpc.hit_clarity(platform=1,mobiApp=1,build=1,phoneCode=1,areaID=1,subAreaID=1,liveMode=1,roomID=1)
        print(r)

    def test_hit_icon(self):
        r = self.mygrpc.hit_icon(platform=1,mobiApp=1,build=1,liveMode=1)
        print(r)

    def test_icon_list(self):
        r = self.mygrpc.icon_list()
        print(r)

    def test_judge_force_new_room(self):
        r = self.mygrpc.judge_force_new_room()
        print(r)

    def test_judge_switch_new_room(self):
        r = self.mygrpc.judge_switch_new_room()
        print(r)

    def test_modify_guide_status(self):
        r = self.mygrpc.modify_guide_status(id=1,modify_status_type=1)
        print(r)

    def test_modify_push_rule_status(self):
        r = self.mygrpc.modify_push_rule_status(id=1,modify_status_type=1)
        print(r)

    def test_multi_get_room_news(self):
        r = self.mygrpc.multi_get_room_news(room_ids=1)
        print(r)

    def test_operate_vote(self):
        r = self.mygrpc.operate_vote(audit_status=1,id=1,operator=1)
        print(r)

    def test_param_list(self):
        r = self.mygrpc.param_list()
        print(r)

    def test_phone_list(self):
        r = self.mygrpc.phone_list()
        print(r)

    def test_pop_conf_list(self):
        r = self.mygrpc.pop_conf_list()
        print(r)

    def test_post_file_to_re_title(self):
        r = self.mygrpc.post_file_to_re_title(uname=1,filePath=1)
        print(r)

    def test_post_pop_status(self):
        r = self.mygrpc.post_pop_status(activity_id=1,source=1,place=1)
        print(r)

    def test_program_list_export(self):
        r = self.mygrpc.program_list_export(page=1)
        print(r)

    def test_program_subscription(self):
        r = self.mygrpc.program_subscription(subscription_id=1,type=1,program_id=1,uid=1)
        print(r)

    def test_put_full_virtual_image_encrypt_job(self):
        r = self.mygrpc.put_full_virtual_image_encrypt_job()
        print(r)

    def test_put_virtual_image_encrypt_job(self):
        r = self.mygrpc.put_virtual_image_encrypt_job()
        print(r)

    def test_query_room_status(self):
        r = self.mygrpc.query_room_status(room_id=1)
        print(r)

    def test_record_switch_new_room(self):
        r = self.mygrpc.record_switch_new_room()
        print(r)

    def test_san_list(self):
        r = self.mygrpc.san_list()
        print(r)

    def test_san_log_list(self):
        r = self.mygrpc.san_log_list(uid=1,start_time=1,end_time=1)
        print(r)

    def test_save_check_result(self):
        r = self.mygrpc.save_check_result()
        print(r)

    def test_save_virtual_record(self):
        r = self.mygrpc.save_virtual_record()
        print(r)

    def test_search_guide(self):
        r = self.mygrpc.search_guide(search_value=1)
        print(r)

    def test_share_conf_list(self):
        r = self.mygrpc.share_conf_list()
        print(r)

    def test_signal_cache(self):
        r = self.mygrpc.signal_cache()
        print(r)

    def test_submit_virtual_image_encrypt_job_status(self):
        r = self.mygrpc.submit_virtual_image_encrypt_job_status()
        print(r)

    def test_switch_mission(self):
        r = self.mygrpc.switch_mission(observer_name=1,old_mission_id=1,new_target_room_id=1)
        print(r)

    def test_update_background_item(self):
        r = self.mygrpc.update_background_item()
        print(r)

    def test_update_guide(self):
        r = self.mygrpc.update_guide(id=1,type=1,link=1,cover_url=1,weight=1,title=1)
        print(r)

    def test_update_program(self):
        r = self.mygrpc.update_program(program_id=1,ruid=1)
        print(r)

    def test_update_program_by_anchor(self):
        r = self.mygrpc.update_program_by_anchor(ruid=1,program_id=1)
        print(r)

    def test_update_push_rule(self):
        r = self.mygrpc.update_push_rule(id=1,position=1,title=1,guide_ids=1)
        print(r)

    def test_update_recommend(self):
        r = self.mygrpc.update_recommend(ruid=1,id=1)
        print(r)

    def test_update_room_news(self):
        r = self.mygrpc.update_room_news()
        print(r)

    def test_update_share_conf(self):
        r = self.mygrpc.update_share_conf(type=1,source_platform=1,target_platform=1,share_type=1,img_type=1,title_format=1,start_time=1,end_time=1)
        print(r)

    def test_update_unusual_vote_record(self):
        r = self.mygrpc.update_unusual_vote_record(uid=1)
        print(r)

    def test_update_user_san(self):
        r = self.mygrpc.update_user_san()
        print(r)

    def test_update_virtual_mat_pos(self):
        r = self.mygrpc.update_virtual_mat_pos(type=1,name=1,blink_limit=1,pink_limit=1,sex=1,sort=1,preview_pic=1)
        print(r)

    def test_update_virtual_record(self):
        r = self.mygrpc.update_virtual_record()
        print(r)

    def test_update_virtual_storm_switch(self):
        r = self.mygrpc.update_virtual_storm_switch(room_id=1)
        print(r)

    def test_update_vote_time(self):
        r = self.mygrpc.update_vote_time(id=1,type=1,uid=1)
        print(r)

    def test_white_room_list(self):
        r = self.mygrpc.white_room_list()
        print(r)


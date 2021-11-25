"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.mcn_mng import Mcn_mng


class TestMcn_mng(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Mcn_mng()

    def test_accept_invitation(self):
        r = self.mygrpc.accept_invitation(contact_id=1,uid=1)
        print(r)

    def test_add_anchor_renew_record(self):
        r = self.mygrpc.add_anchor_renew_record(uid=1,org_id=1,apply_type=1)
        print(r)

    def test_add_banner(self):
        r = self.mygrpc.add_banner(link=1,jump_link=1,start_time=1,end_time=1)
        print(r)

    def test_add_operation_log(self):
        r = self.mygrpc.add_operation_log()
        print(r)

    def test_approve(self):
        r = self.mygrpc.approve(apply_id=1)
        print(r)

    def test_cancel_anchor_auto_renew(self):
        r = self.mygrpc.cancel_anchor_auto_renew(uid=1,org_id=1)
        print(r)

    def test_check_anchor_renew(self):
        r = self.mygrpc.check_anchor_renew(uid=1)
        print(r)

    def test_check_apply_join(self):
        r = self.mygrpc.check_apply_join(uid=1)
        print(r)

    def test_check_up_file(self):
        r = self.mygrpc.check_up_file(url=1)
        print(r)

    def test_commit_apply(self):
        r = self.mygrpc.commit_apply(anchor_uid=1,code=1,org_id=1,operator_uid=1)
        print(r)

    def test_commit_quit_guild(self):
        r = self.mygrpc.commit_quit_guild(uid=1)
        print(r)

    def test_confirm_build_con(self):
        r = self.mygrpc.confirm_build_con(url=1)
        print(r)

    def test_confirm_fire_anchor(self):
        r = self.mygrpc.confirm_fire_anchor(apply_id=1,uid=1)
        print(r)

    def test_del_notice(self):
        r = self.mygrpc.del_notice(notice_id=1)
        print(r)

    def test_delete_banner(self):
        r = self.mygrpc.delete_banner()
        print(r)

    def test_delete_build_con_list(self):
        r = self.mygrpc.delete_build_con_list(id=1)
        print(r)

    def test_detail_notice(self):
        r = self.mygrpc.detail_notice(notice_id=1)
        print(r)

    def test_download_build_conn_list(self):
        r = self.mygrpc.download_build_conn_list()
        print(r)

    def test_export_anchor_list(self):
        r = self.mygrpc.export_anchor_list()
        print(r)

    def test_export_guild_anchor(self):
        r = self.mygrpc.export_guild_anchor()
        print(r)

    def test_export_live_record(self):
        r = self.mygrpc.export_live_record()
        print(r)

    def test_export_operation_log_list(self):
        r = self.mygrpc.export_operation_log_list()
        print(r)

    def test_fire_anchor(self):
        r = self.mygrpc.fire_anchor()
        print(r)

    def test_gen_guild_qr_code(self):
        r = self.mygrpc.gen_guild_qr_code(org_id=1,cooperation_duration=1,anchor_type=1,operator_uid=1,staff_uid=1)
        print(r)

    def test_get_anchor_active_events(self):
        r = self.mygrpc.get_anchor_active_events(uid=1)
        print(r)

    def test_get_anchor_apply_log(self):
        r = self.mygrpc.get_anchor_apply_log()
        print(r)

    def test_get_anchor_guild_info(self):
        r = self.mygrpc.get_anchor_guild_info(uid=1)
        print(r)

    def test_get_anchor_info(self):
        r = self.mygrpc.get_anchor_info(uids=1)
        print(r)

    def test_get_anchor_join_apply_list(self):
        r = self.mygrpc.get_anchor_join_apply_list(org_id=1)
        print(r)

    def test_get_anchor_list(self):
        r = self.mygrpc.get_anchor_list(g_id=1,page=1,page_size=1)
        print(r)

    def test_get_anchor_quit_apply_list(self):
        r = self.mygrpc.get_anchor_quit_apply_list(org_id=1,type=1)
        print(r)

    def test_get_anchor_renew_record(self):
        r = self.mygrpc.get_anchor_renew_record(apply_id=1,uid=1)
        print(r)

    def test_get_anchors_by_guild(self):
        r = self.mygrpc.get_anchors_by_guild(guild_id=1)
        print(r)

    def test_get_answer_analysis_list(self):
        r = self.mygrpc.get_answer_analysis_list(batch_id=1)
        print(r)

    def test_get_audit_list(self):
        r = self.mygrpc.get_audit_list()
        print(r)

    def test_get_banner_list(self):
        r = self.mygrpc.get_banner_list()
        print(r)

    def test_get_basic_info(self):
        r = self.mygrpc.get_basic_info(guild_id=1)
        print(r)

    def test_get_basic_info_audit(self):
        r = self.mygrpc.get_basic_info_audit(apply_id=1)
        print(r)

    def test_get_build_con_list(self):
        r = self.mygrpc.get_build_con_list()
        print(r)

    def test_get_change_log(self):
        r = self.mygrpc.get_change_log(id_type=1,id_value=1,business_type=1)
        print(r)

    def test_get_coin_chart(self):
        r = self.mygrpc.get_coin_chart()
        print(r)

    def test_get_contact_info(self):
        r = self.mygrpc.get_contact_info(uid=1)
        print(r)

    def test_get_core_data(self):
        r = self.mygrpc.get_core_data(time_range=1)
        print(r)

    def test_get_email_preview(self):
        r = self.mygrpc.get_email_preview(flow_type=1,ids=1,operator=1)
        print(r)

    def test_get_expired_anchor_detail(self):
        r = self.mygrpc.get_expired_anchor_detail()
        print(r)

    def test_get_expired_anchor_list(self):
        r = self.mygrpc.get_expired_anchor_list()
        print(r)

    def test_get_guild_by_uids(self):
        r = self.mygrpc.get_guild_by_uids(uids=1)
        print(r)

    def test_get_guild_common_data(self):
        r = self.mygrpc.get_guild_common_data()
        print(r)

    def test_get_guild_fire_anchor_info(self):
        r = self.mygrpc.get_guild_fire_anchor_info(uid=1,apply_id=1)
        print(r)

    def test_get_guild_info(self):
        r = self.mygrpc.get_guild_info()
        print(r)

    def test_get_guild_info_detail(self):
        r = self.mygrpc.get_guild_info_detail(guild_id=1)
        print(r)

    def test_get_guild_list(self):
        r = self.mygrpc.get_guild_list(page=1,page_size=1)
        print(r)

    def test_get_guild_notice(self):
        r = self.mygrpc.get_guild_notice(uid=1)
        print(r)

    def test_get_guild_qr_code(self):
        r = self.mygrpc.get_guild_qr_code(code=1)
        print(r)

    def test_get_guild_question_status(self):
        r = self.mygrpc.get_guild_question_status()
        print(r)

    def test_get_guild_renew_list(self):
        r = self.mygrpc.get_guild_renew_list(org_id=1)
        print(r)

    def test_get_guild_sign_areas(self):
        r = self.mygrpc.get_guild_sign_areas()
        print(r)

    def test_get_guild_sign_info(self):
        r = self.mygrpc.get_guild_sign_info()
        print(r)

    def test_get_income_chart(self):
        r = self.mygrpc.get_income_chart()
        print(r)

    def test_get_income_rank(self):
        r = self.mygrpc.get_income_rank()
        print(r)

    def test_get_log_type_filter(self):
        r = self.mygrpc.get_log_type_filter()
        print(r)

    def test_get_message(self):
        r = self.mygrpc.get_message(token=1)
        print(r)

    def test_get_my_anchor_data_info(self):
        r = self.mygrpc.get_my_anchor_data_info()
        print(r)

    def test_get_my_anchor_list(self):
        r = self.mygrpc.get_my_anchor_list(page=1,page_size=1)
        print(r)

    def test_get_open_anchor_chart(self):
        r = self.mygrpc.get_open_anchor_chart()
        print(r)

    def test_get_operation_log_list(self):
        r = self.mygrpc.get_operation_log_list(page=1,page_size=1)
        print(r)

    def test_get_operator_info(self):
        r = self.mygrpc.get_operator_info(flow_type=1,flow_ids=1)
        print(r)

    def test_get_person_data(self):
        r = self.mygrpc.get_person_data()
        print(r)

    def test_get_personal_chart(self):
        r = self.mygrpc.get_personal_chart(uid=1,data_type=1)
        print(r)

    def test_get_personal_rec(self):
        r = self.mygrpc.get_personal_rec(uid=1,guild_id=1)
        print(r)

    def test_get_recruit_audit(self):
        r = self.mygrpc.get_recruit_audit(apply_id=1)
        print(r)

    def test_get_recruit_info(self):
        r = self.mygrpc.get_recruit_info(guild_id=1)
        print(r)

    def test_get_relation_info(self):
        r = self.mygrpc.get_relation_info(flow_type=1)
        print(r)

    def test_get_salary_audit_list(self):
        r = self.mygrpc.get_salary_audit_list(type=1)
        print(r)

    def test_guild_fire_anchor(self):
        r = self.mygrpc.guild_fire_anchor(uid=1,org_id=1)
        print(r)

    def test_important_notice(self):
        r = self.mygrpc.important_notice(notice_id=1,operate_type=1)
        print(r)

    def test_is_guild_anchor(self):
        r = self.mygrpc.is_guild_anchor(uid=1)
        print(r)

    def test_is_master(self):
        r = self.mygrpc.is_master()
        print(r)

    def test_judge_ninety_five_anchor(self):
        r = self.mygrpc.judge_ninety_five_anchor()
        print(r)

    def test_list_notices(self):
        r = self.mygrpc.list_notices()
        print(r)

    def test_living_room_list(self):
        r = self.mygrpc.living_room_list()
        print(r)

    def test_living_room_top(self):
        r = self.mygrpc.living_room_top(uid=1,operate_type=1)
        print(r)

    def test_off_line_banner(self):
        r = self.mygrpc.off_line_banner()
        print(r)

    def test_operate_notice(self):
        r = self.mygrpc.operate_notice(notice_id=1,operate_type=1)
        print(r)

    def test_reject(self):
        r = self.mygrpc.reject(apply_id=1)
        print(r)

    def test_save_answer_info(self):
        r = self.mygrpc.save_answer_info(batch_id=1,question_id=1,options=1,choice_id=1)
        print(r)

    def test_save_message(self):
        r = self.mygrpc.save_message()
        print(r)

    def test_search_guild_anchor_uname(self):
        r = self.mygrpc.search_guild_anchor_uname(org_id=1)
        print(r)

    def test_send_sms(self):
        r = self.mygrpc.send_sms()
        print(r)

    def test_start_flow(self):
        r = self.mygrpc.start_flow(flow_type=1,ids=1,operator=1)
        print(r)

    def test_submit_guild_question(self):
        r = self.mygrpc.submit_guild_question(batch_id=1)
        print(r)

    def test_update_banner(self):
        r = self.mygrpc.update_banner(link=1,jump_link=1,start_time=1,end_time=1)
        print(r)

    def test_update_basic_info(self):
        r = self.mygrpc.update_basic_info(guild_id=1)
        print(r)

    def test_update_recruit_info(self):
        r = self.mygrpc.update_recruit_info(guild_id=1)
        print(r)


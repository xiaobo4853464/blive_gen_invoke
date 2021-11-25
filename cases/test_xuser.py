"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.xuser import Xuser


class TestXuser(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Xuser()

    def test_accept_agreement(self):
        r = self.mygrpc.accept_agreement()
        print(r)

    def test_add_guard_dress(self):
        r = self.mygrpc.add_guard_dress()
        print(r)

    def test_appoint(self):
        r = self.mygrpc.appoint(uid=1,anchor_id=1)
        print(r)

    def test_are_admin_short(self):
        r = self.mygrpc.are_admin_short(uids=1,roomid=1)
        print(r)

    def test_audit_status(self):
        r = self.mygrpc.audit_status(uid=1)
        print(r)

    def test_auth(self):
        r = self.mygrpc.auth()
        print(r)

    def test_batch_get_anchor_guard_abstract(self):
        r = self.mygrpc.batch_get_anchor_guard_abstract()
        print(r)

    def test_bind(self):
        r = self.mygrpc.bind(uid=1,room_id=1)
        print(r)

    def test_buy(self):
        r = self.mygrpc.buy(order_id=1,uid=1,ruid=1,guard_level=1,num=1,platform=1)
        print(r)

    def test_clear_u_i_d_cache(self):
        r = self.mygrpc.clear_u_i_d_cache(uid=1,magic_key=1)
        print(r)

    def test_create(self):
        r = self.mygrpc.create(room_id=1,watch_platform=1,start_time=1,end_time=1)
        print(r)

    def test_delete(self):
        r = self.mygrpc.delete(id=1)
        print(r)

    def test_dismiss(self):
        r = self.mygrpc.dismiss(uid=1,anchor_id=1)
        print(r)

    def test_edit(self):
        r = self.mygrpc.edit(id=1,room_id=1,watch_platform=1,start_time=1,end_time=1)
        print(r)

    def test_fix_sync_account_data(self):
        r = self.mygrpc.fix_sync_account_data(uid=1)
        print(r)

    def test_get_all_guards_by_u_i_d(self):
        r = self.mygrpc.get_all_guards_by_u_i_d(uid=1)
        print(r)

    def test_get_anchor_recent_top_guard(self):
        r = self.mygrpc.get_anchor_recent_top_guard(uid=1)
        print(r)

    def test_get_app_note(self):
        r = self.mygrpc.get_app_note(uid=1)
        print(r)

    def test_get_app_note_v2(self):
        r = self.mygrpc.get_app_note_v2()
        print(r)

    def test_get_buyed_guards(self):
        r = self.mygrpc.get_buyed_guards(uid=1)
        print(r)

    def test_get_by_anchor(self):
        r = self.mygrpc.get_by_anchor(uid=1)
        print(r)

    def test_get_by_room(self):
        r = self.mygrpc.get_by_room(roomid=1)
        print(r)

    def test_get_by_target_ids_batch(self):
        r = self.mygrpc.get_by_target_ids_batch(target_ids=1)
        print(r)

    def test_get_by_u_i_d_batch(self):
        r = self.mygrpc.get_by_u_i_d_batch(uids=1)
        print(r)

    def test_get_by_u_i_d_for_gift(self):
        r = self.mygrpc.get_by_u_i_d_for_gift(uid=1)
        print(r)

    def test_get_by_u_i_d_target_i_d(self):
        r = self.mygrpc.get_by_u_i_d_target_i_d(uid=1,target_id=1)
        print(r)

    def test_get_by_u_i_d_target_i_d_guards(self):
        r = self.mygrpc.get_by_u_i_d_target_i_d_guards(uid=1,target_id=1)
        print(r)

    def test_get_by_uid(self):
        r = self.mygrpc.get_by_uid(uid=1)
        print(r)

    def test_get_follow_time_by_uid_target_id(self):
        r = self.mygrpc.get_follow_time_by_uid_target_id(uid=1,target_id=1)
        print(r)

    def test_get_game_role_by_m_i_d(self):
        r = self.mygrpc.get_game_role_by_m_i_d(act_id=1,game_id=1,mid=1)
        print(r)

    def test_get_guard_num_by_u_i_ds(self):
        r = self.mygrpc.get_guard_num_by_u_i_ds(uids=1)
        print(r)

    def test_get_guard_warn(self):
        r = self.mygrpc.get_guard_warn(target_id=1)
        print(r)

    def test_get_guard_warn_list(self):
        r = self.mygrpc.get_guard_warn_list(target_id=1,type=1)
        print(r)

    def test_get_lpl_identity(self):
        r = self.mygrpc.get_lpl_identity(uid=1)
        print(r)

    def test_get_multi_user_data(self):
        r = self.mygrpc.get_multi_user_data(uids=1)
        print(r)

    def test_get_peak_by_targetid_uids(self):
        r = self.mygrpc.get_peak_by_targetid_uids(targetid=1,uids=1)
        print(r)

    def test_get_peak_by_targetid_uids_v2(self):
        r = self.mygrpc.get_peak_by_targetid_uids_v2(targetid=1,uids=1)
        print(r)

    def test_get_peak_by_u_i_d_batch(self):
        r = self.mygrpc.get_peak_by_u_i_d_batch(uids=1)
        print(r)

    def test_get_personal_dress(self):
        r = self.mygrpc.get_personal_dress()
        print(r)

    def test_get_target_guard_num(self):
        r = self.mygrpc.get_target_guard_num()
        print(r)

    def test_get_top_list_guard(self):
        r = self.mygrpc.get_top_list_guard(targetid=1)
        print(r)

    def test_get_top_list_guard_attr(self):
        r = self.mygrpc.get_top_list_guard_attr(targetid=1,sort_attr=1,page=1)
        print(r)

    def test_get_top_list_guard_v2(self):
        r = self.mygrpc.get_top_list_guard_v2(targetid=1)
        print(r)

    def test_get_user_data(self):
        r = self.mygrpc.get_user_data(uid=1)
        print(r)

    def test_get_user_data_multi(self):
        r = self.mygrpc.get_user_data_multi(uids=1,attrs=1)
        print(r)

    def test_get_user_data_multi_risk_control(self):
        r = self.mygrpc.get_user_data_multi_risk_control(uids=1,attrs=1)
        print(r)

    def test_get_user_data_risk_control(self):
        r = self.mygrpc.get_user_data_risk_control(uid=1)
        print(r)

    def test_get_user_exp(self):
        r = self.mygrpc.get_user_exp(uids=1)
        print(r)

    def test_guard_card_refresh(self):
        r = self.mygrpc.guard_card_refresh()
        print(r)

    def test_guard_change(self):
        r = self.mygrpc.guard_change()
        print(r)

    def test_guard_recycle(self):
        r = self.mygrpc.guard_recycle(order_id=1,uid=1,ruid=1,guard_level=1,num=1,platform=1)
        print(r)

    def test_info(self):
        r = self.mygrpc.info(uid=1)
        print(r)

    def test_infos(self):
        r = self.mygrpc.infos(uids=1)
        print(r)

    def test_is_admin(self):
        r = self.mygrpc.is_admin(uid=1,anchor_id=1,roomid=1)
        print(r)

    def test_is_admin_short(self):
        r = self.mygrpc.is_admin_short(uid=1,roomid=1)
        print(r)

    def test_is_any(self):
        r = self.mygrpc.is_any(uid=1)
        print(r)

    def test_is_weekly_guard(self):
        r = self.mygrpc.is_weekly_guard(level=1)
        print(r)

    def test_jump_wx_config(self):
        r = self.mygrpc.jump_wx_config(act_id=1,game_id=1,mid=1)
        print(r)

    def test_list(self):
        r = self.mygrpc.list()
        print(r)

    def test_live_tencent_game_bind_info(self):
        r = self.mygrpc.live_tencent_game_bind_info(mid=1)
        print(r)

    def test_lpl_bind(self):
        r = self.mygrpc.lpl_bind(uid=1)
        print(r)

    def test_lpl_get_log_status(self):
        r = self.mygrpc.lpl_get_log_status(uid=1,orderid=1)
        print(r)

    def test_lpl_get_token(self):
        r = self.mygrpc.lpl_get_token(uid=1)
        print(r)

    def test_m_i_d_to_open_i_d(self):
        r = self.mygrpc.m_i_d_to_open_i_d(mid=1)
        print(r)

    def test_open_i_d_to_m_i_d(self):
        r = self.mygrpc.open_i_d_to_m_i_d(openID=1)
        print(r)

    def test_pre_buy(self):
        r = self.mygrpc.pre_buy(uid=1,ruid=1,guard_level=1,num=1,platform=1,price=1,discount_price=1)
        print(r)

    def test_quick_word(self):
        r = self.mygrpc.quick_word()
        print(r)

    def test_refresh_cache(self):
        r = self.mygrpc.refresh_cache(target_id=1)
        print(r)

    def test_remove_from_guard_top(self):
        r = self.mygrpc.remove_from_guard_top()
        print(r)

    def test_resign(self):
        r = self.mygrpc.resign(roomid=1,uid=1)
        print(r)

    def test_search_for_admin(self):
        r = self.mygrpc.search_for_admin(uid=1,key_word=1)
        print(r)

    def test_sms_code(self):
        r = self.mygrpc.sms_code(game_type=1,phone=1)
        print(r)

    def test_sms_login(self):
        r = self.mygrpc.sms_login(game_type=1,phone=1,code=1)
        print(r)

    def test_uname_to_u_i_d(self):
        r = self.mygrpc.uname_to_u_i_d(uname=1)
        print(r)

    def test_user_info(self):
        r = self.mygrpc.user_info(mid=1)
        print(r)

    def test_user_info_batch(self):
        r = self.mygrpc.user_info_batch()
        print(r)

    def test_user_info_by_open_i_d(self):
        r = self.mygrpc.user_info_by_open_i_d(game_type=1,openID=1)
        print(r)

    def test_valid_list(self):
        r = self.mygrpc.valid_list(session_id=1)
        print(r)

    def test_wx_h5_handler(self):
        r = self.mygrpc.wx_h5_handler(act_id=1,game_id=1,mid=1)
        print(r)

    def test_wx_handler(self):
        r = self.mygrpc.wx_handler(act_id=1,game_id=1,mid=1)
        print(r)


"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.live_dm import Live_dm


class TestLive_dm(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Live_dm()

    def test_add_room(self):
        r = self.mygrpc.add_room(room_ids=1,list_name=1)
        print(r)

    def test_add_white_list(self):
        r = self.mygrpc.add_white_list(list_addr=1,list_name=1,list_creator=1)
        print(r)

    def test_audit_ban(self):
        r = self.mygrpc.audit_ban(uid=1,ban_days=1,operator=1,ban_evidence=1)
        print(r)

    def test_audit_ban_info(self):
        r = self.mygrpc.audit_ban_info(uid=1)
        print(r)

    def test_audit_content_conf_list(self):
        r = self.mygrpc.audit_content_conf_list()
        print(r)

    def test_ban_broadcast(self):
        r = self.mygrpc.ban_broadcast(data=1,msgtype=1,**from_=1)
        print(r)

    def test_baninfo(self):
        r = self.mygrpc.baninfo(target_id=1)
        print(r)

    def test_broad_user_lopital_a_c_k(self):
        r = self.mygrpc.broad_user_lopital_a_c_k()
        print(r)

    def test_broad_user_lopital_send(self):
        r = self.mygrpc.broad_user_lopital_send()
        print(r)

    def test_broadcast_room(self):
        r = self.mygrpc.broadcast_room(msgtype=1,cmd=1,data=1)
        print(r)

    def test_broadcast_user(self):
        r = self.mygrpc.broadcast_user()
        print(r)

    def test_create_audit_content_conf(self):
        r = self.mygrpc.create_audit_content_conf(conf_title=1,start_time=1,end_time=1)
        print(r)

    def test_danmu_report(self):
        r = self.mygrpc.danmu_report(uid=1,tuid=1,msg=1,reason=1,reason_id=1,roomid=1)
        print(r)

    def test_del_history_d_m_by_roomid(self):
        r = self.mygrpc.del_history_d_m_by_roomid(roomid=1)
        print(r)

    def test_del_single_room(self):
        r = self.mygrpc.del_single_room(room_id=1)
        print(r)

    def test_delete_audit_content_conf(self):
        r = self.mygrpc.delete_audit_content_conf(id=1)
        print(r)

    def test_entry_broadcast(self):
        r = self.mygrpc.entry_broadcast(data=1,msgtype=1,**from_=1)
        print(r)

    def test_get_audit_content_conf(self):
        r = self.mygrpc.get_audit_content_conf(id=1)
        print(r)

    def test_get_auditor_num_and_danmu_num(self):
        r = self.mygrpc.get_auditor_num_and_danmu_num(id=1)
        print(r)

    def test_get_block_info(self):
        r = self.mygrpc.get_block_info(tuid=1)
        print(r)

    def test_get_d_m_msg_by_play_back_i_d(self):
        r = self.mygrpc.get_d_m_msg_by_play_back_i_d(vid=1)
        print(r)

    def test_get_d_m_num_by_vid(self):
        r = self.mygrpc.get_d_m_num_by_vid(vid=1)
        print(r)

    def test_get_danmu_lists(self):
        r = self.mygrpc.get_danmu_lists(id=1)
        print(r)

    def test_get_history(self):
        r = self.mygrpc.get_history(roomid=1)
        print(r)

    def test_get_index_info(self):
        r = self.mygrpc.get_index_info(vid=1)
        print(r)

    def test_get_list(self):
        r = self.mygrpc.get_list(page_no=1)
        print(r)

    def test_get_manage_block_list(self):
        r = self.mygrpc.get_manage_block_list(page_no=1)
        print(r)

    def test_get_room_list(self):
        r = self.mygrpc.get_room_list()
        print(r)

    def test_get_style(self):
        r = self.mygrpc.get_style()
        print(r)

    def test_gift_broadcast(self):
        r = self.mygrpc.gift_broadcast(data=1,msgtype=1,**from_=1)
        print(r)

    def test_ignore(self):
        r = self.mygrpc.ignore(dmids=1,operator=1)
        print(r)

    def test_list_d_m(self):
        r = self.mygrpc.list_d_m(vid=1,sort=1,page=1)
        print(r)

    def test_list_report(self):
        r = self.mygrpc.list_report(status=1,page=1,reporter_target=1)
        print(r)

    def test_list_style(self):
        r = self.mygrpc.list_style()
        print(r)

    def test_list_task(self):
        r = self.mygrpc.list_task()
        print(r)

    def test_multi_block(self):
        r = self.mygrpc.multi_block(ids=1,reason=1,block_reason=1,days=1)
        print(r)

    def test_multi_ignore(self):
        r = self.mygrpc.multi_ignore(ids=1)
        print(r)

    def test_pre_check_send_msg(self):
        r = self.mygrpc.pre_check_send_msg(uid=1,roomid=1,msg=1)
        print(r)

    def test_record_send_msg(self):
        r = self.mygrpc.record_send_msg(vid=1,msg=1,roomid=1,uid=1,dmid=1)
        print(r)

    def test_report(self):
        r = self.mygrpc.report(reporter_id=1,dmid=1,vid=1,report_reason=1)
        print(r)

    def test_resume(self):
        r = self.mygrpc.resume(dmid=1)
        print(r)

    def test_search_dm_list(self):
        r = self.mygrpc.search_dm_list(begin_time=1,end_time=1)
        print(r)

    def test_set_auditor_num(self):
        r = self.mygrpc.set_auditor_num(uname=1,id=1)
        print(r)

    def test_set_room_status(self):
        r = self.mygrpc.set_room_status(room_id=1)
        print(r)

    def test_stop_task(self):
        r = self.mygrpc.stop_task()
        print(r)

    def test_udate_audit_content_conf(self):
        r = self.mygrpc.udate_audit_content_conf(id=1,conf_title=1,start_time=1,end_time=1)
        print(r)

    def test_un_block(self):
        r = self.mygrpc.un_block(tuid=1)
        print(r)


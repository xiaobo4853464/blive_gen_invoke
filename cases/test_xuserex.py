"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.xuserex import Xuserex


class TestXuserex(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Xuserex()

    def test_add(self):
        r = self.mygrpc.add(uid=1,bubble_id=1,expired_at=1,desc=1)
        print(r)

    def test_add_color(self):
        r = self.mygrpc.add_color(color=1,name=1,hint_msg=1,origin=1)
        print(r)

    def test_buy_guard(self):
        r = self.mygrpc.buy_guard(uid=1,target_id=1)
        print(r)

    def test_color_list(self):
        r = self.mygrpc.color_list(status=1)
        print(r)

    def test_config_plugs(self):
        r = self.mygrpc.config_plugs(uid=1)
        print(r)

    def test_danmaku_config(self):
        r = self.mygrpc.danmaku_config()
        print(r)

    def test_debug__clear_all_cache(self):
        r = self.mygrpc.debug__clear_all_cache(uids=1)
        print(r)

    def test_debug__clear_p_h_p_all_cache(self):
        r = self.mygrpc.debug__clear_p_h_p_all_cache(uid=1)
        print(r)

    def test_debug__get_cache(self):
        r = self.mygrpc.debug__get_cache(uids=1)
        print(r)

    def test_debug__get_p_h_p_all_cache(self):
        r = self.mygrpc.debug__get_p_h_p_all_cache(uid=1)
        print(r)

    def test_del_(self):
        r = self.mygrpc.del_()
        print(r)

    def test_del_color(self):
        r = self.mygrpc.del_color(id=1)
        print(r)

    def test_del_json_content_key(self):
        r = self.mygrpc.del_json_content_key()
        print(r)

    def test_edit_plugs(self):
        r = self.mygrpc.edit_plugs(uid=1,key=1)
        print(r)

    def test_get(self):
        r = self.mygrpc.get()
        print(r)

    def test_get_bubble(self):
        r = self.mygrpc.get_bubble(uid=1,room_id=1)
        print(r)

    def test_get_by_cid(self):
        r = self.mygrpc.get_by_cid(color_id=1)
        print(r)

    def test_get_by_u_i_d_room_i_d(self):
        r = self.mygrpc.get_by_u_i_d_room_i_d(uid=1)
        print(r)

    def test_get_d_m_config_by_group(self):
        r = self.mygrpc.get_d_m_config_by_group(room_id=1)
        print(r)

    def test_get_multi_target(self):
        r = self.mygrpc.get_multi_target()
        print(r)

    def test_get_nick_name_color(self):
        r = self.mygrpc.get_nick_name_color(uid=1)
        print(r)

    def test_get_xuser_ex_data(self):
        r = self.mygrpc.get_xuser_ex_data()
        print(r)

    def test_info_plugs(self):
        r = self.mygrpc.info_plugs(uid=1)
        print(r)

    def test_recycle(self):
        r = self.mygrpc.recycle(uid=1,source=1,type=1)
        print(r)

    def test_renew_guard(self):
        r = self.mygrpc.renew_guard(uid=1,target_id=1,guard_level=1,expired_time=1)
        print(r)

    def test_send(self):
        r = self.mygrpc.send(uid=1,source=1,type=1)
        print(r)

    def test_set_online(self):
        r = self.mygrpc.set_online(id=1)
        print(r)

    def test_set_task_finish(self):
        r = self.mygrpc.set_task_finish()
        print(r)

    def test_update_color(self):
        r = self.mygrpc.update_color(id=1,color=1,name=1,hint_msg=1,origin=1)
        print(r)

    def test_upsert_json_content(self):
        r = self.mygrpc.upsert_json_content()
        print(r)

    def test_wear(self):
        r = self.mygrpc.wear(uid=1,type=1,value=1)
        print(r)

    def test_wear_for_old(self):
        r = self.mygrpc.wear_for_old()
        print(r)


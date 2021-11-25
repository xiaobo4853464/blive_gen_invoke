"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.xfetter import Xfetter


class TestXfetter(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Xfetter()

    def test_delete_component(self):
        r = self.mygrpc.delete_component(id=1)
        print(r)

    def test_filter_offline_uids(self):
        r = self.mygrpc.filter_offline_uids(uid_list=1)
        print(r)

    def test_get_component_list(self):
        r = self.mygrpc.get_component_list(page=1,page_size=1)
        print(r)

    def test_get_follow_info(self):
        r = self.mygrpc.get_follow_info(uid=1,target_uid=1)
        print(r)

    def test_get_follow_type(self):
        r = self.mygrpc.get_follow_type()
        print(r)

    def test_get_following_streaming_rooms_app(self):
        r = self.mygrpc.get_following_streaming_rooms_app(uid=1)
        print(r)

    def test_get_released_real_time_u_i_d_list(self):
        r = self.mygrpc.get_released_real_time_u_i_d_list(id=1,page=1,page_size=1)
        print(r)

    def test_get_user_following_offline_rooms_app(self):
        r = self.mygrpc.get_user_following_offline_rooms_app(uid=1)
        print(r)

    def test_get_user_following_online_room_app_dynamic_footer_tab(self):
        r = self.mygrpc.get_user_following_online_room_app_dynamic_footer_tab(uid=1)
        print(r)

    def test_get_user_following_online_room_app_dynamic_footer_tab_with_score(self):
        r = self.mygrpc.get_user_following_online_room_app_dynamic_footer_tab_with_score(uid=1)
        print(r)

    def test_get_user_following_online_rooms(self):
        r = self.mygrpc.get_user_following_online_rooms()
        print(r)

    def test_get_user_following_online_rooms_app_dynamic(self):
        r = self.mygrpc.get_user_following_online_rooms_app_dynamic()
        print(r)

    def test_get_user_following_online_rooms_web_dynamic(self):
        r = self.mygrpc.get_user_following_online_rooms_web_dynamic()
        print(r)

    def test_get_user_following_streaming_rooms_app(self):
        r = self.mygrpc.get_user_following_streaming_rooms_app(uid=1,**from_=1)
        print(r)

    def test_get_user_live_anchor_map(self):
        r = self.mygrpc.get_user_live_anchor_map()
        print(r)

    def test_get_user_live_rooms_app(self):
        r = self.mygrpc.get_user_live_rooms_app()
        print(r)

    def test_get_user_live_rooms_web(self):
        r = self.mygrpc.get_user_live_rooms_web()
        print(r)

    def test_get_user_online_anchor_list(self):
        r = self.mygrpc.get_user_online_anchor_list()
        print(r)

    def test_get_user_online_anchor_list_historical(self):
        r = self.mygrpc.get_user_online_anchor_list_historical()
        print(r)

    def test_is_user_follow(self):
        r = self.mygrpc.is_user_follow(uid=1,target_uid=1)
        print(r)

    def test_is_user_follow_batch(self):
        r = self.mygrpc.is_user_follow_batch(uid=1,target_uid_list=1)
        print(r)

    def test_publish_real_time_u_i_d(self):
        r = self.mygrpc.publish_real_time_u_i_d(component_id=1,uid=1,show_duration=1)
        print(r)

    def test_save_component(self):
        r = self.mygrpc.save_component(room_ids=1,name=1)
        print(r)


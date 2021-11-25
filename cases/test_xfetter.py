"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.xfetter import Xfetter


class TestXfetter(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Xfetter()

    def test_get_follow_info(self):
        r = self.mygrpc.get_follow_info(uid=1, target_uid=1)
        print(r)

    def test_get_follow_type(self):
        r = self.mygrpc.get_follow_type()
        print(r)

    def test_get_user_live_anchor_map(self):
        r = self.mygrpc.get_user_live_anchor_map()
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
        r = self.mygrpc.is_user_follow(uid=1, target_uid=1)
        print(r)

    def test_is_user_follow_batch(self):
        r = self.mygrpc.is_user_follow_batch(uid=1, target_uid_list=1)
        print(r)


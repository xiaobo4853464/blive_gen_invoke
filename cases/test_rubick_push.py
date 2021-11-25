"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.rubick_push import Rubick_push


class TestRubick_push(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Rubick_push()

    def test_get_recommend_push_inner_v1(self):
        r = self.mygrpc.get_recommend_push_inner_v1()
        print(r)

    def test_get_recommend_push_v1(self):
        r = self.mygrpc.get_recommend_push_v1()
        print(r)

    def test_get_user_room_cnt(self):
        r = self.mygrpc.get_user_room_cnt()
        print(r)

    def test_reload_user_room_cnt(self):
        r = self.mygrpc.reload_user_room_cnt()
        print(r)

    def test_set_room_filter(self):
        r = self.mygrpc.set_room_filter()
        print(r)


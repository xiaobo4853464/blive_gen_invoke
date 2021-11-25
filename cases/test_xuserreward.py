"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.xuserreward import Xuserreward


class TestXuserreward(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Xuserreward()

    def test_get_front_room_icon(self):
        r = self.mygrpc.get_front_room_icon(room_id=1)
        print(r)

    def test_get_room_card_list(self):
        r = self.mygrpc.get_room_card_list(room_id=1)
        print(r)


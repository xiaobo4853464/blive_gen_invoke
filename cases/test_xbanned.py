"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.xbanned import Xbanned


class TestXbanned(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Xbanned()

    def test_get_room_silent(self):
        r = self.mygrpc.get_room_silent(room_id=1)
        print(r)

    def test_room_silent_off(self):
        r = self.mygrpc.room_silent_off(room_id=1)
        print(r)


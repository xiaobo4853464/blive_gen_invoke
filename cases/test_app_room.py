"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.app_room import App_room


class TestApp_room(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = App_room()

    def test_share_conf(self):
        r = self.mygrpc.share_conf(room_id=1,platform=1)
        print(r)


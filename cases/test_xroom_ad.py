"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.xroom_ad import Xroom_ad


class TestXroom_ad(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Xroom_ad()

    def test_check(self):
        r = self.mygrpc.check()
        print(r)

    def test_check_v2(self):
        r = self.mygrpc.check_v2(room_id=1,order_type=1)
        print(r)

    def test_get_by_cri_ids(self):
        r = self.mygrpc.get_by_cri_ids()
        print(r)


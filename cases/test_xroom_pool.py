"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.xroom_pool import Xroom_pool


class TestXroom_pool(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Xroom_pool()

    def test_fetch_cpm_v2(self):
        r = self.mygrpc.fetch_cpm_v2()
        print(r)


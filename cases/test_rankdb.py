"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.rankdb import Rankdb


class TestRankdb(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Rankdb()

    def test_delete_module(self):
        r = self.mygrpc.delete_module(uid=1, ruid=1, business_id=1)
        print(r)


"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.dao_anchor import Dao_anchor


class TestDao_anchor(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Dao_anchor()

    def test_incr_popularity(self):
        r = self.mygrpc.incr_popularity()
        print(r)


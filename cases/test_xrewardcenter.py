"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.xrewardcenter import Xrewardcenter


class TestXrewardcenter(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Xrewardcenter()

    def test_current(self):
        r = self.mygrpc.current()
        print(r)


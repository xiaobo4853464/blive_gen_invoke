"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.xuserex import Xuserex


class TestXuserex(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Xuserex()

    def test_get_nick_name_color(self):
        r = self.mygrpc.get_nick_name_color(uid=1)
        print(r)

    def test_recycle(self):
        r = self.mygrpc.recycle(uid=1, source=1, type=1)
        print(r)

    def test_send(self):
        r = self.mygrpc.send(uid=1, source=1, type=1)
        print(r)


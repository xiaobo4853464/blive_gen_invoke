"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.xlottery import Xlottery


class TestXlottery(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Xlottery()

    def test_check(self):
        r = self.mygrpc.check(roomid=1)
        print(r)

    def test_join(self):
        r = self.mygrpc.join(roomid=1, id=1, type=1)
        print(r)

    def test_join_guard(self):
        r = self.mygrpc.join_guard(roomid=1, id=1, type=1)
        print(r)

    def test_start(self):
        r = self.mygrpc.start()
        print(r)


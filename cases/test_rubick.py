"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.rubick import Rubick


class TestRubick(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Rubick()

    def test_delete(self):
        r = self.mygrpc.delete()
        print(r)

    def test_list(self):
        r = self.mygrpc.list()
        print(r)

    def test_login(self):
        r = self.mygrpc.login()
        print(r)

    def test_multi(self):
        r = self.mygrpc.multi()
        print(r)

    def test_save(self):
        r = self.mygrpc.save()
        print(r)

    def test_test(self):
        r = self.mygrpc.test()
        print(r)


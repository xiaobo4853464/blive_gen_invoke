"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.settlement import Settlement


class TestSettlement(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Settlement()

    def test_add(self):
        r = self.mygrpc.add()
        print(r)

    def test_add_intercept_history(self):
        r = self.mygrpc.add_intercept_history()
        print(r)

    def test_del_(self):
        r = self.mygrpc.del_()
        print(r)

    def test_intercept_history(self):
        r = self.mygrpc.intercept_history()
        print(r)

    def test_list(self):
        r = self.mygrpc.list()
        print(r)

    def test_log_list(self):
        r = self.mygrpc.log_list()
        print(r)

    def test_modify_remark(self):
        r = self.mygrpc.modify_remark()
        print(r)

    def test_on_add_auth_guild(self):
        r = self.mygrpc.on_add_auth_guild()
        print(r)


"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.xanchor import Xanchor


class TestXanchor(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Xanchor()

    def test_change_pop_conf_status(self):
        r = self.mygrpc.change_pop_conf_status(id=1, status=1)
        print(r)

    def test_del_pop_conf(self):
        r = self.mygrpc.del_pop_conf(id=1)
        print(r)

    def test_pop_conf_list(self):
        r = self.mygrpc.pop_conf_list()
        print(r)


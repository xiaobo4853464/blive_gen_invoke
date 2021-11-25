"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.abtest import Abtest


class TestAbtest(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Abtest()

    def test_get_by_exp_key(self):
        r = self.mygrpc.get_by_exp_key()
        print(r)

    def test_get_exp_info(self):
        r = self.mygrpc.get_exp_info()
        print(r)

    def test_get_exp_list(self):
        r = self.mygrpc.get_exp_list()
        print(r)

    def test_get_exp_list_by_namespace(self):
        r = self.mygrpc.get_exp_list_by_namespace(namespace=1)
        print(r)

    def test_get_exp_list_by_params(self):
        r = self.mygrpc.get_exp_list_by_params(namespace=1)
        print(r)

    def test_get_online_by_exp_key(self):
        r = self.mygrpc.get_online_by_exp_key()
        print(r)

    def test_get_quota_list(self):
        r = self.mygrpc.get_quota_list()
        print(r)

    def test_get_simple_quota_list(self):
        r = self.mygrpc.get_simple_quota_list()
        print(r)

    def test_get_split_result_by_param(self):
        r = self.mygrpc.get_split_result_by_param(uid=1, exp_key=1)
        print(r)

    def test_on_off_exp(self):
        r = self.mygrpc.on_off_exp()
        print(r)


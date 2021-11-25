"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.abtest import Abtest


class TestAbtest(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Abtest()

    def test_add_new_source(self):
        r = self.mygrpc.add_new_source(source_one_title=1,source_two_title=1,prefix=1)
        print(r)

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

    def test_get_jump_from(self):
        r = self.mygrpc.get_jump_from(id=1)
        print(r)

    def test_get_jump_from_by_keys(self):
        r = self.mygrpc.get_jump_from_by_keys()
        print(r)

    def test_get_jump_from_list(self):
        r = self.mygrpc.get_jump_from_list(page=1,page_size=1)
        print(r)

    def test_get_max_by_prefix(self):
        r = self.mygrpc.get_max_by_prefix()
        print(r)

    def test_get_online_by_exp_key(self):
        r = self.mygrpc.get_online_by_exp_key()
        print(r)

    def test_get_quota_list(self):
        r = self.mygrpc.get_quota_list()
        print(r)

    def test_get_search_result(self):
        r = self.mygrpc.get_search_result()
        print(r)

    def test_get_simple_quota_list(self):
        r = self.mygrpc.get_simple_quota_list()
        print(r)

    def test_get_split_result_by_param(self):
        r = self.mygrpc.get_split_result_by_param(uid=1,exp_key=1)
        print(r)

    def test_on_off_exp(self):
        r = self.mygrpc.on_off_exp()
        print(r)

    def test_set_jump_from(self):
        r = self.mygrpc.set_jump_from(jumpfrom_id=1,entry_from=1,source_one_title=1,source_two_title=1,source_three_title=1,source_desc=1,report_type=1)
        print(r)


"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.data_one_piece_task import Data_one_piece_task


class TestData_one_piece_task(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Data_one_piece_task()

    def test_add_feature(self):
        r = self.mygrpc.add_feature()
        print(r)

    def test_add_feature_as_user(self):
        r = self.mygrpc.add_feature_as_user()
        print(r)

    def test_delete_feature(self):
        r = self.mygrpc.delete_feature()
        print(r)

    def test_fea_data_sampling(self):
        r = self.mygrpc.fea_data_sampling()
        print(r)

    def test_find_group_info(self):
        r = self.mygrpc.find_group_info()
        print(r)

    def test_find_group_list(self):
        r = self.mygrpc.find_group_list()
        print(r)

    def test_fuzzy_for_fea_cn_name(self):
        r = self.mygrpc.fuzzy_for_fea_cn_name()
        print(r)

    def test_fuzzy_for_fea_id(self):
        r = self.mygrpc.fuzzy_for_fea_id()
        print(r)

    def test_fuzzy_for_fea_name(self):
        r = self.mygrpc.fuzzy_for_fea_name()
        print(r)

    def test_fuzzy_for_job_name(self):
        r = self.mygrpc.fuzzy_for_job_name()
        print(r)

    def test_search_fea_info(self):
        r = self.mygrpc.search_fea_info()
        print(r)

    def test_search_feature(self):
        r = self.mygrpc.search_feature()
        print(r)

    def test_select_feature(self):
        r = self.mygrpc.select_feature()
        print(r)

    def test_select_feature_job_list(self):
        r = self.mygrpc.select_feature_job_list()
        print(r)

    def test_test_diagnosis_callback(self):
        r = self.mygrpc.test_diagnosis_callback()
        print(r)

    def test_tool_run_bsk_job(self):
        r = self.mygrpc.tool_run_bsk_job()
        print(r)

    def test_tool_search_bsk_job(self):
        r = self.mygrpc.tool_search_bsk_job()
        print(r)

    def test_update_feature(self):
        r = self.mygrpc.update_feature()
        print(r)

    def test_update_feature_as_user(self):
        r = self.mygrpc.update_feature_as_user()
        print(r)


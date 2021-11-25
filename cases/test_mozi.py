"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.mozi import Mozi


class TestMozi(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Mozi()

    def test_get_act_center_detail(self):
        r = self.mygrpc.get_act_center_detail(act_id=1)
        print(r)

    def test_get_act_center_enter_list(self):
        r = self.mygrpc.get_act_center_enter_list()
        print(r)

    def test_get_act_center_list(self):
        r = self.mygrpc.get_act_center_list(uid=1, tab_id=1, page_index=1, page_size=1)
        print(r)

    def test_get_act_info_by_topic_ids(self):
        r = self.mygrpc.get_act_info_by_topic_ids()
        print(r)

    def test_get_act_result_detail(self):
        r = self.mygrpc.get_act_result_detail(uid=1, act_id=1)
        print(r)

    def test_get_act_sign_up_info(self):
        r = self.mygrpc.get_act_sign_up_info(uid=1, act_id=1)
        print(r)

    def test_get_topic_act_join_list(self):
        r = self.mygrpc.get_topic_act_join_list(uid=1, act_id=1, page_index=1, page_size=1)
        print(r)


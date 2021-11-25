"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.mcn_mng import Mcn_mng


class TestMcn_mng(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Mcn_mng()

    def test_del_notice(self):
        r = self.mygrpc.del_notice(notice_id=1)
        print(r)

    def test_detail_notice(self):
        r = self.mygrpc.detail_notice(notice_id=1)
        print(r)

    def test_important_notice(self):
        r = self.mygrpc.important_notice(notice_id=1, operate_type=1)
        print(r)

    def test_list_notices(self):
        r = self.mygrpc.list_notices()
        print(r)

    def test_operate_notice(self):
        r = self.mygrpc.operate_notice(notice_id=1, operate_type=1)
        print(r)


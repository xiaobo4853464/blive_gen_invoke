"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.behavior import Behavior


class TestBehavior(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Behavior()

    def test_get_award(self):
        r = self.mygrpc.get_award(ruler_id=1)
        print(r)

    def test_get_award_list(self):
        r = self.mygrpc.get_award_list(page=1, page_size=1)
        print(r)

    def test_get_award_name(self):
        r = self.mygrpc.get_award_name(award_type=1, award_id=1)
        print(r)

    def test_get_package_list(self):
        r = self.mygrpc.get_package_list(page=1, page_size=1)
        print(r)

    def test_update_award_status(self):
        r = self.mygrpc.update_award_status(id=1)
        print(r)

    def test_update_package_status(self):
        r = self.mygrpc.update_package_status(id=1)
        print(r)


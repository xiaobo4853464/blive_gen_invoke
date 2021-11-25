"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.anchor_task_center import Anchor_task_center


class TestAnchor_task_center(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Anchor_task_center()

    def test_copy_anchor_group(self):
        r = self.mygrpc.copy_anchor_group()
        print(r)

    def test_copy_anchor_member(self):
        r = self.mygrpc.copy_anchor_member()
        print(r)

    def test_del_anchor_member(self):
        r = self.mygrpc.del_anchor_member()
        print(r)

    def test_get_anchor_group(self):
        r = self.mygrpc.get_anchor_group()
        print(r)

    def test_get_anchor_group_list(self):
        r = self.mygrpc.get_anchor_group_list()
        print(r)

    def test_get_anchor_member(self):
        r = self.mygrpc.get_anchor_member()
        print(r)

    def test_get_anchor_member_list(self):
        r = self.mygrpc.get_anchor_member_list()
        print(r)

    def test_set_anchor_group(self):
        r = self.mygrpc.set_anchor_group()
        print(r)


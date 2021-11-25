"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.gift import Gift


class TestGift(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Gift()

    def test_bag_delete_task(self):
        r = self.mygrpc.bag_delete_task()
        print(r)

    def test_bag_info_admin(self):
        r = self.mygrpc.bag_info_admin()
        print(r)

    def test_bag_list(self):
        r = self.mygrpc.bag_list()
        print(r)

    def test_bag_reduce(self):
        r = self.mygrpc.bag_reduce()
        print(r)

    def test_clear_bag_dot(self):
        r = self.mygrpc.clear_bag_dot(uid=1)
        print(r)

    def test_get_bag_dot(self):
        r = self.mygrpc.get_bag_dot(uid=1)
        print(r)

    def test_get_bag_list_by_uid(self):
        r = self.mygrpc.get_bag_list_by_uid(uid=1)
        print(r)

    def test_silver_package_stream(self):
        r = self.mygrpc.silver_package_stream()
        print(r)


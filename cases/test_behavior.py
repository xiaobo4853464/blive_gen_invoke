"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.behavior import Behavior


class TestBehavior(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Behavior('live.behavior')

    def test_add_rank(self):
        r = self.mygrpc.add_rank(title=1,ruler_id=1)
        print(r)

    def test_entry_room(self):
        r = self.mygrpc.entry_room(uid=1,entry_info=1)
        print(r)

    def test_get_award(self):
        r = self.mygrpc.get_award(ruler_id=1)
        print(r)

    def test_get_award_list(self):
        r = self.mygrpc.get_award_list(page=1,page_size=1)
        print(r)

    def test_get_award_name(self):
        r = self.mygrpc.get_award_name(award_type=1,award_id=1)
        print(r)

    def test_get_bls_task(self):
        r = self.mygrpc.get_bls_task()
        print(r)

    def test_get_match_task(self):
        r = self.mygrpc.get_match_task()
        print(r)

    def test_get_package_list(self):
        r = self.mygrpc.get_package_list(page=1,page_size=1)
        print(r)

    def test_get_rank_list(self):
        r = self.mygrpc.get_rank_list(page=1,page_size=1)
        print(r)

    def test_get_rulers(self):
        r = self.mygrpc.get_rulers(page=1,page_size=1)
        print(r)

    def test_get_simple_task(self):
        r = self.mygrpc.get_simple_task()
        print(r)

    def test_get_task_award(self):
        r = self.mygrpc.get_task_award()
        print(r)

    def test_get_task_info(self):
        r = self.mygrpc.get_task_info()
        print(r)

    def test_get_task_list(self):
        r = self.mygrpc.get_task_list(page=1,page_size=1)
        print(r)

    def test_get_user_task(self):
        r = self.mygrpc.get_user_task()
        print(r)

    def test_get_user_task_status(self):
        r = self.mygrpc.get_user_task_status()
        print(r)

    def test_match_share(self):
        r = self.mygrpc.match_share()
        print(r)

    def test_match_sign(self):
        r = self.mygrpc.match_sign()
        print(r)

    def test_recycle_guard(self):
        r = self.mygrpc.recycle_guard(order_id=1,uid=1,ruid=1,total_price=1,origin_price=1,platform=1,goods_id=1,goods_num=1,parent_area_id=1,area_id=1,parent_goods_cate=1,goods_cate=1,create_time=1)
        print(r)

    def test_set_focus_master(self):
        r = self.mygrpc.set_focus_master(task_id=1,ruids=1)
        print(r)

    def test_set_user_task_status(self):
        r = self.mygrpc.set_user_task_status()
        print(r)

    def test_update_award_status(self):
        r = self.mygrpc.update_award_status(id=1)
        print(r)

    def test_update_package_status(self):
        r = self.mygrpc.update_package_status(id=1)
        print(r)

    def test_update_rank_status(self):
        r = self.mygrpc.update_rank_status(id=1)
        print(r)

    def test_update_ruler_status(self):
        r = self.mygrpc.update_ruler_status(id=1)
        print(r)


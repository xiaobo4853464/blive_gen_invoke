"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.trading import Trading


class TestTrading(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Trading()

    def test_batch_get_user_score(self):
        r = self.mygrpc.batch_get_user_score(uid=1, score_ids=1)
        print(r)

    def test_coin2_silver(self):
        r = self.mygrpc.coin2_silver()
        print(r)

    def test_coin_silver_exchange_status(self):
        r = self.mygrpc.coin_silver_exchange_status()
        print(r)

    def test_get_anchor_star_expire_info(self):
        r = self.mygrpc.get_anchor_star_expire_info(page=1, page_size=1, uid=1)
        print(r)

    def test_get_batch_score_list_by_ids(self):
        r = self.mygrpc.get_batch_score_list_by_ids(score_ids=1)
        print(r)

    def test_get_log(self):
        r = self.mygrpc.get_log()
        print(r)

    def test_get_mng_user_score_by_num(self):
        r = self.mygrpc.get_mng_user_score_by_num(page=1)
        print(r)

    def test_get_score_list(self):
        r = self.mygrpc.get_score_list(page=1)
        print(r)

    def test_get_score_list_by_id(self):
        r = self.mygrpc.get_score_list_by_id()
        print(r)

    def test_get_user_metal(self):
        r = self.mygrpc.get_user_metal(uid=1)
        print(r)

    def test_get_user_score(self):
        r = self.mygrpc.get_user_score(score_id=1, uid=1)
        print(r)

    def test_get_user_score_by_period(self):
        r = self.mygrpc.get_user_score_by_period(uid=1, start_time=1, end_time=1)
        print(r)

    def test_get_user_score_history(self):
        r = self.mygrpc.get_user_score_history(score_id=1, uid=1)
        print(r)

    def test_get_user_score_log_list(self):
        r = self.mygrpc.get_user_score_log_list()
        print(r)

    def test_get_user_score_log_status(self):
        r = self.mygrpc.get_user_score_log_status(tid=1, source=1)
        print(r)

    def test_get_user_score_log_to_b(self):
        r = self.mygrpc.get_user_score_log_to_b()
        print(r)

    def test_get_user_score_update_count(self):
        r = self.mygrpc.get_user_score_update_count(score_id=1, uid=1)
        print(r)

    def test_get_user_star_log(self):
        r = self.mygrpc.get_user_star_log(id=1, uid=1, start_time=1, end_time=1, page=1, page_size=1)
        print(r)

    def test_score_exchange(self):
        r = self.mygrpc.score_exchange(src_uid=1, src_score_id=1, src_score_num=1, src_score_source=1, dest_uid=1, dest_score_id=1, dest_score_num=1, dest_score_source=1, tid=1, platform=1)
        print(r)

    def test_score_refund(self):
        r = self.mygrpc.score_refund()
        print(r)

    def test_silver2_coin(self):
        r = self.mygrpc.silver2_coin(uid=1)
        print(r)

    def test_update_score(self):
        r = self.mygrpc.update_score()
        print(r)

    def test_update_score_status(self):
        r = self.mygrpc.update_score_status(id=1, status=1)
        print(r)

    def test_update_user_score(self):
        r = self.mygrpc.update_user_score(score_id=1, score=1, uid=1, tid=1, source=1, platform=1, context_type=1)
        print(r)

    def test_update_user_score_async(self):
        r = self.mygrpc.update_user_score_async(score_id=1, score=1, uid=1, tid=1, source=1, platform=1, context_type=1)
        print(r)

    def test_update_user_star_log(self):
        r = self.mygrpc.update_user_star_log(uid=1, log_type=1)
        print(r)


"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.recommend import Recommend


class TestRecommend(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Recommend()

    def test_clear_recommend_cache(self):
        r = self.mygrpc.clear_recommend_cache()
        print(r)

    def test_get_lr_feature_result(self):
        r = self.mygrpc.get_lr_feature_result()
        print(r)

    def test_get_recall_result(self):
        r = self.mygrpc.get_recall_result()
        print(r)

    def test_get_recommend_rooms(self):
        r = self.mygrpc.get_recommend_rooms()
        print(r)


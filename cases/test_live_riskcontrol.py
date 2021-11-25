"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.live_riskcontrol import Live_riskcontrol


class TestLive_riskcontrol(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Live_riskcontrol()

    def test_deal_popularity_feedback(self):
        r = self.mygrpc.deal_popularity_feedback()
        print(r)

    def test_get_ip_forbidden(self):
        r = self.mygrpc.get_ip_forbidden()
        print(r)

    def test_get_popularity_feedback_list(self):
        r = self.mygrpc.get_popularity_feedback_list()
        print(r)

    def test_get_popularity_is_normal(self):
        r = self.mygrpc.get_popularity_is_normal()
        print(r)

    def test_report_popularity_feedback(self):
        r = self.mygrpc.report_popularity_feedback()
        print(r)


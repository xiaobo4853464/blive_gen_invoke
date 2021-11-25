"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.live_risk_metrics import Live_risk_metrics


class TestLive_risk_metrics(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Live_risk_metrics()

    def test_get_count(self):
        r = self.mygrpc.get_count()
        print(r)

    def test_get_number(self):
        r = self.mygrpc.get_number()
        print(r)

    def test_get_string(self):
        r = self.mygrpc.get_string()
        print(r)

    def test_is_in(self):
        r = self.mygrpc.is_in()
        print(r)


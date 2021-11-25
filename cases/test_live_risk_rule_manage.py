"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.live_risk_rule_manage import Live_risk_rule_manage


class TestLive_risk_rule_manage(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Live_risk_rule_manage()

    def test_add(self):
        r = self.mygrpc.add()
        print(r)

    def test_index(self):
        r = self.mygrpc.index(id=1)
        print(r)

    def test_list(self):
        r = self.mygrpc.list()
        print(r)

    def test_model(self):
        r = self.mygrpc.model()
        print(r)

    def test_scence(self):
        r = self.mygrpc.scence()
        print(r)

    def test_start(self):
        r = self.mygrpc.start()
        print(r)

    def test_update(self):
        r = self.mygrpc.update()
        print(r)


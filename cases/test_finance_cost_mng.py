"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.finance_cost_mng import Finance_cost_mng


class TestFinance_cost_mng(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Finance_cost_mng()

    def test_get_user(self):
        r = self.mygrpc.get_user()
        print(r)


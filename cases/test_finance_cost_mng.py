"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.finance_cost_mng import Finance_cost_mng


class TestFinance_cost_mng(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Finance_cost_mng()

    def test_del_pay_record(self):
        r = self.mygrpc.del_pay_record(id=1)
        print(r)

    def test_del_settle(self):
        r = self.mygrpc.del_settle(id=1)
        print(r)

    def test_edit_pay_record(self):
        r = self.mygrpc.edit_pay_record(id=1,bus_id=1,settle_ids=1,pay_status=1,month=1,amount=1,amount_type=1,creator=1,payment_entity=1,payment_method=1)
        print(r)

    def test_edit_settle(self):
        r = self.mygrpc.edit_settle()
        print(r)

    def test_export_pay_list(self):
        r = self.mygrpc.export_pay_list()
        print(r)

    def test_export_settle(self):
        r = self.mygrpc.export_settle()
        print(r)

    def test_get_finance_pay_list(self):
        r = self.mygrpc.get_finance_pay_list(page=1,page_size=1)
        print(r)

    def test_get_user(self):
        r = self.mygrpc.get_user()
        print(r)

    def test_real_pay(self):
        r = self.mygrpc.real_pay(id=1)
        print(r)

    def test_settle_list(self):
        r = self.mygrpc.settle_list(page=1,page_size=1)
        print(r)

    def test_suject_list(self):
        r = self.mygrpc.suject_list()
        print(r)


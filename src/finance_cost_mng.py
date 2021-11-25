from tiny import grpc_call

class Finance_cost_mng(object):
    def __init__(self,service_name):
        self.service_name=service_name
    
    @grpc_call(path="/live.financecostmng.v1.FinancePay/GetFinancePayList")
    def get_finance_pay_list(self, page, page_size, creator=None, start_date=None, end_date=None, pay_num=None, up_uid=None, up_uname=None, payment_entity=None, remark=None, pay_status=None, settle_num=None):
        """### 付款单列表"""

    @grpc_call(path="/live.financecostmng.v1.FinancePay/EditPayRecord")
    def edit_pay_record(self, id, bus_id, settle_ids, pay_status, month, amount, amount_type, creator, payment_entity, payment_method, up_uid=None, remark=None, append_file=None):
        """### 编辑付款单"""

    @grpc_call(path="/live.financecostmng.v1.FinancePay/DelPayRecord")
    def del_pay_record(self, id):
        """### 删除付款单"""

    @grpc_call(path="/live.financecostmng.v1.FinancePay/ExportPayList")
    def export_pay_list(self, creator=None, start_date=None, end_date=None, pay_num=None, up_uid=None, up_uname=None, payment_entity=None, remark=None, pay_status=None, key=None):
        """### 导出付款单"""

    @grpc_call(path="/live.financecostmng.v1.FinancePay/RealPay")
    def real_pay(self, id, pay_amount=None):
        """### 财务打款"""

    @grpc_call(path="/live.financecostmng.v1.FinanceSuject/SujectList")
    def suject_list(self, suject_level=None, parent_id=None, finance_type=None):
        """### 获取科目列表"""

    @grpc_call(path="/live.financecostmng.v1.FinanceSettle/EditSettle")
    def edit_settle(self, id=None, bus_id=None, settle_type=None, stat_month=None, first_suject=None, second_suject=None, third_suject=None, up_uid=None, amount=None, amount_type=None, creator=None, remark=None, payment_entity=None, payment_method=None, append_file=None):
        """### 修改结算单"""

    @grpc_call(path="/live.financecostmng.v1.FinanceSettle/DelSettle")
    def del_settle(self, id):
        """### 删除结算单"""

    @grpc_call(path="/live.financecostmng.v1.FinanceSettle/SettleList")
    def settle_list(self, page, page_size, creator=None, start_date=None, end_date=None, settle_num=None, up_uid=None, up_uname=None, payment_entity=None, remark=None, first_suject=None, second_suject=None, third_suject=None, settle_status=None, settle_type=None):
        """### 结算单列表"""

    @grpc_call(path="/live.financecostmng.v1.FinanceSettle/ExportSettle")
    def export_settle(self, creator=None, start_date=None, end_date=None, settle_num=None, first_suject=None, second_suject=None, third_suject=None, settle_status=None, up_uid=None, up_uname=None, payment_entity=None, remark=None, key=None, settle_type=None):
        """### 导出结算单"""

    @grpc_call(path="/live.financecostmng.v1.FinanceUser/GetUser")
    def get_user(self, uid=None):
        """### 查询用户信息"""

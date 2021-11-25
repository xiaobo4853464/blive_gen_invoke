"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.order import Order


class TestOrder(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Order()

    def test_add_category(self):
        r = self.mygrpc.add_category()
        print(r)

    def test_add_goods(self):
        r = self.mygrpc.add_goods(name=1)
        print(r)

    def test_app_pay_panel(self):
        r = self.mygrpc.app_pay_panel(goods_id=1,goods_num=1,uid=1,platform=1,ip=1)
        print(r)

    def test_bank_recharge_notify(self):
        r = self.mygrpc.bank_recharge_notify(msg_id=1,msg_content=1,order_id=1)
        print(r)

    def test_can_buy(self):
        r = self.mygrpc.can_buy(goods_id=1,goods_num=1,uid=1,platform=1,ip=1)
        print(r)

    def test_change_contract_execute_time(self):
        r = self.mygrpc.change_contract_execute_time(uid=1,goods_id=1,next_execute_time=1)
        print(r)

    def test_contract_notify(self):
        r = self.mygrpc.contract_notify(msg_id=1,msg_content=1)
        print(r)

    def test_create_bank_recharge_order(self):
        r = self.mygrpc.create_bank_recharge_order(uid=1,goods_id=1,platform=1,context_type=1,context_id=1,ip=1)
        print(r)

    def test_create_contract_order(self):
        r = self.mygrpc.create_contract_order(uid=1,goods_id=1,order_id=1,contract_id=1,out_contract_id=1,price=1,execute_time=1,step=1)
        print(r)

    def test_create_expire_goods_order(self):
        r = self.mygrpc.create_expire_goods_order(pay_bag_gold=1,goods_id=1,goods_num=1,goods_price=1,goods_name=1,biz_id=1,uid=1,platform=1,ip=1,context_id=1,ts=1,relevance_order_id=1,order_id=1,bag_biz_type=1,msg_id=1)
        print(r)

    def test_create_order_relevance(self):
        r = self.mygrpc.create_order_relevance(uid=1,relevance_order_id=1,order_id=1,num=1,bag_biz_type=1,msg_id=1)
        print(r)

    def test_create_third_recharge_invoice(self):
        r = self.mygrpc.create_third_recharge_invoice(sequence_id=1,account_id=1,third_order_id=1,uid=1,invoice_price=1,invoice_title=1,apply_time=1,ip=1)
        print(r)

    def test_create_third_recharge_order(self):
        r = self.mygrpc.create_third_recharge_order(pay_cash=1,uid=1,platform=1,ip=1,context_id=1,third_order_id=1,goods_num=1)
        print(r)

    def test_delivery_for_job(self):
        r = self.mygrpc.delivery_for_job()
        print(r)

    def test_delivery_notify(self):
        r = self.mygrpc.delivery_notify()
        print(r)

    def test_download_children_recharge_stream(self):
        r = self.mygrpc.download_children_recharge_stream(uid=1,start_time=1,end_time=1)
        print(r)

    def test_edit_goods(self):
        r = self.mygrpc.edit_goods(id=1,name=1,price=1)
        print(r)

    def test_get_anchor_statistics(self):
        r = self.mygrpc.get_anchor_statistics(req_type=1,ruid=1)
        print(r)

    def test_get_anchor_statistics_v2(self):
        r = self.mygrpc.get_anchor_statistics_v2(ruid=1)
        print(r)

    def test_get_anchor_stream(self):
        r = self.mygrpc.get_anchor_stream(biz_type=1,req_type=1,ruid=1,page_size=1)
        print(r)

    def test_get_category_list(self):
        r = self.mygrpc.get_category_list()
        print(r)

    def test_get_children_recharge_stream(self):
        r = self.mygrpc.get_children_recharge_stream(uid=1,start_time=1,end_time=1,page=1,page_size=1)
        print(r)

    def test_get_children_recharge_stream_file(self):
        r = self.mygrpc.get_children_recharge_stream_file(flag=1)
        print(r)

    def test_get_contract(self):
        r = self.mygrpc.get_contract()
        print(r)

    def test_get_contract_execute_log_stream(self):
        r = self.mygrpc.get_contract_execute_log_stream()
        print(r)

    def test_get_contract_log_stream(self):
        r = self.mygrpc.get_contract_log_stream()
        print(r)

    def test_get_contract_stream(self):
        r = self.mygrpc.get_contract_stream()
        print(r)

    def test_get_contracts(self):
        r = self.mygrpc.get_contracts()
        print(r)

    def test_get_contracts_by_ruid(self):
        r = self.mygrpc.get_contracts_by_ruid(ruid=1,uids=1,goods_id=1)
        print(r)

    def test_get_goods_info(self):
        r = self.mygrpc.get_goods_info()
        print(r)

    def test_get_goods_list(self):
        r = self.mygrpc.get_goods_list()
        print(r)

    def test_get_order_stream(self):
        r = self.mygrpc.get_order_stream(page=1,page_size=1)
        print(r)

    def test_get_order_stream_by_gift(self):
        r = self.mygrpc.get_order_stream_by_gift()
        print(r)

    def test_get_order_stream_by_gift_v2(self):
        r = self.mygrpc.get_order_stream_by_gift_v2()
        print(r)

    def test_get_order_stream_by_time(self):
        r = self.mygrpc.get_order_stream_by_time(start_time=1,end_time=1,page=1,page_size=1)
        print(r)

    def test_get_order_stream_by_time_v2(self):
        r = self.mygrpc.get_order_stream_by_time_v2(start_time=1,end_time=1,start_id=1,count=1)
        print(r)

    def test_get_order_stream_by_time_v3(self):
        r = self.mygrpc.get_order_stream_by_time_v3(start_time=1,end_time=1,start_id=1,count=1)
        print(r)

    def test_get_pay_platform_contract_status(self):
        r = self.mygrpc.get_pay_platform_contract_status()
        print(r)

    def test_get_user_block_rule(self):
        r = self.mygrpc.get_user_block_rule(uid=1,platform=1)
        print(r)

    def test_goods_info(self):
        r = self.mygrpc.goods_info(goods_ids=1)
        print(r)

    def test_iap_refund_notify(self):
        r = self.mygrpc.iap_refund_notify(msg_id=1,msg_content=1)
        print(r)

    def test_order_notify(self):
        r = self.mygrpc.order_notify(msg_id=1,msg_content=1)
        print(r)

    def test_order_query(self):
        r = self.mygrpc.order_query()
        print(r)

    def test_query_third_recharge_order(self):
        r = self.mygrpc.query_third_recharge_order(uid=1,third_order_id=1,account_id=1)
        print(r)

    def test_recharge_channel(self):
        r = self.mygrpc.recharge_channel(goods_id=1,platform=1,sdk_version=1,uid=1)
        print(r)

    def test_recharge_notify(self):
        r = self.mygrpc.recharge_notify(msg_id=1,msg_content=1)
        print(r)

    def test_refund(self):
        r = self.mygrpc.refund(order_id=1,reason=1)
        print(r)

    def test_refund_notify(self):
        r = self.mygrpc.refund_notify(msg_id=1,msg_content=1,order_id=1,refund_id=1)
        print(r)

    def test_supplement(self):
        r = self.mygrpc.supplement(order_id=1,pay_list=1)
        print(r)

    def test_terminate_contract(self):
        r = self.mygrpc.terminate_contract(uid=1,goods_id=1,remark=1)
        print(r)

    def test_user_consume_recent30_day(self):
        r = self.mygrpc.user_consume_recent30_day(uid=1,ruid=1)
        print(r)


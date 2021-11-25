from tiny import grpc_call

class Order(object):
    def __init__(self,service_name):
        self.service_name=service_name
    
    @grpc_call(path="/live.order.block/getUserBlockRule")
    def get_user_block_rule(self, uid, platform):
        """### 获取用户封禁规则"""

    @grpc_call(path="/live.order.v1.goods/addGoods")
    def add_goods(self, name, price=None, currency_type=None, description=None, biz_id=None, state=None, sale_start=None, sale_end=None, image=None, service_id=None, buy_limit=None, extra_info=None, cate_id=None, parent_cate=None, support_channel=None, discount_price=None, first_price=None, signed_price=None, is_settlement=None):
        """###添加一个新商品"""

    @grpc_call(path="/live.order.v1.goods/editGoods")
    def edit_goods(self, id, name, price, currency_type=None, description=None, biz_id=None, state=None, sale_start=None, sale_end=None, image=None, service_id=None, buy_limit=None, extra_info=None, cate_id=None, parent_cate=None, support_channel=None, discount_price=None, first_price=None, signed_price=None, is_settlement=None):
        """###编辑商品信息"""

    @grpc_call(path="/live.order.v1.goods/getGoodsList")
    def get_goods_list(self, page=None, pageSize=None, start_time=None, end_time=None, state=None):
        """###获取商品列表"""

    @grpc_call(path="/live.order.v1.goods/addCategory")
    def add_category(self, parent_id=None, name=None):
        """###添加商品分类"""

    @grpc_call(path="/live.order.v1.goods/getCategoryList")
    def get_category_list(self, parent_id=None, cate_id=None):
        """###分类列表"""

    @grpc_call(path="/live.order.v1.goods/getGoodsInfo")
    def get_goods_info(self, id=None):
        """###获取商品信息接口"""

    @grpc_call(path="/live.order.order/createContractOrder")
    def create_contract_order(self, uid, goods_id, order_id, contract_id, out_contract_id, price, execute_time, step, ruid=None):
        """### 创建自动续费订单"""

    @grpc_call(path="/live.order.order/goodsInfo")
    def goods_info(self, goods_ids, uid=None, need_first_buy=None):
        """### 商品详情 适用于全部商品信息配置在商品中心"""

    @grpc_call(path="/live.order.order/canBuy")
    def can_buy(self, goods_id, goods_num, uid, platform, ip, build=None, mobile_app=None, ruid=None, parent_area_id=None, area_id=None, biz_extra=None, is_contract=None):
        """### 预检接口 检查是否可以购买"""

    @grpc_call(path="/live.order.order/orderQuery")
    def order_query(self, order_id=None):
        """### 查询订单支付结果"""

    @grpc_call(path="/live.order.order/orderNotify")
    def order_notify(self, msg_id, msg_content, order_id=None, is_first_buy=None, product_id=None, is_discount=None):
        """### 支付成功异步回调"""

    @grpc_call(path="/live.order.order/rechargeNotify")
    def recharge_notify(self, msg_id, msg_content, order_id=None, is_first_buy=None, product_id=None, is_discount=None):
        """### 充值成功异步回调"""

    @grpc_call(path="/live.order.order/bankRechargeNotify")
    def bank_recharge_notify(self, msg_id, msg_content, order_id):
        """### 银行充值成功异步回调"""

    @grpc_call(path="/live.order.order/refundNotify")
    def refund_notify(self, msg_id, msg_content, order_id, refund_id):
        """### 退款成功异步回调"""

    @grpc_call(path="/live.order.order/iapRefundNotify")
    def iap_refund_notify(self, msg_id, msg_content):
        """### iap退款异步回调"""

    @grpc_call(path="/live.order.order/refund")
    def refund(self, order_id, reason, operator=None):
        """### 退款接口"""

    @grpc_call(path="/live.order.order/deliveryNotify")
    def delivery_notify(self, order_id=None, status=None):
        """### 发货通知接口"""

    @grpc_call(path="/live.order.order/deliveryForJob")
    def delivery_for_job(self, order_id=None):
        """### 发货接口"""

    @grpc_call(path="/live.order.order/AppPayPanel")
    def app_pay_panel(self, goods_id, goods_num, uid, platform, ip, build=None, mobile_app=None, ruid=None, parent_area_id=None, area_id=None, biz_extra=None, is_contract=None, sdk_version=None):
        """### 移动端支付渠道列表"""

    @grpc_call(path="/live.order.order/supplement")
    def supplement(self, order_id, pay_list):
        """### 补单接口"""

    @grpc_call(path="/live.order.order/rechargeChannel")
    def recharge_channel(self, goods_id, platform, sdk_version, uid, mobile_app=None):
        """### 充值面板渠道列表"""

    @grpc_call(path="/live.order.order/CreateThirdRechargeOrder")
    def create_third_recharge_order(self, pay_cash, uid, platform, ip, context_id, third_order_id, goods_num):
        """### 创建代理商充值单"""

    @grpc_call(path="/live.order.order/QueryThirdRechargeOrder")
    def query_third_recharge_order(self, uid, third_order_id, account_id):
        """### 查询第三方充值订单信息"""

    @grpc_call(path="/live.order.order/CreateThirdRechargeInvoice")
    def create_third_recharge_invoice(self, sequence_id, account_id, third_order_id, uid, invoice_price, invoice_title, apply_time, ip, is_full=None):
        """### 创建第三方充值发票"""

    @grpc_call(path="/live.order.order/CreateOrderRelevance")
    def create_order_relevance(self, uid, relevance_order_id, order_id, num, bag_biz_type, msg_id):
        """### 创建订单关联记录"""

    @grpc_call(path="/live.order.order/CreateExpireGoodsOrder")
    def create_expire_goods_order(self, pay_bag_gold, goods_id, goods_num, goods_price, goods_name, biz_id, uid, platform, ip, context_id, ts, relevance_order_id, order_id, bag_biz_type, msg_id, goods_img=None, ruid=None, context_type=None, biz_extra=None):
        """### 创建过期商品订单"""

    @grpc_call(path="/live.order.order/UserConsumeRecent30Day")
    def user_consume_recent30_day(self, uid, ruid):
        """### 查询最近30天用户是否对主播有打赏(T+1), 给主站私信服务用"""

    @grpc_call(path="/live.order.order/CreateBankRechargeOrder")
    def create_bank_recharge_order(self, uid, goods_id, platform, context_type, context_id, ip, build=None, version=None, mobile_app=None, parent_area_id=None, area_id=None, biz_extra=None, goods_type=None):
        """### 创建银行充值单"""

    @grpc_call(path="/live.order.v1.stream/getContractStream")
    def get_contract_stream(self, uid=None, status=None, page=None, page_size=None):
        """### 签约流水接口"""

    @grpc_call(path="/live.order.v1.stream/getContractLogStream")
    def get_contract_log_stream(self, uid=None, ruid=None, goods_id=None, page=None, page_size=None):
        """### 签约操作日志"""

    @grpc_call(path="/live.order.v1.stream/getContractExecuteLogStream")
    def get_contract_execute_log_stream(self, contract_id=None, page=None, page_size=None):
        """### 签约扣款日志"""

    @grpc_call(path="/live.order.v1.stream/getOrderStream")
    def get_order_stream(self, page, page_size, uid=None, ruid=None, cate_id=None, status=None, start_time=None, end_time=None, parent_cate=None, order_id=None, third_order_id=None, third_recharge_order_id=None):
        """### 分页查询订单列表"""

    @grpc_call(path="/live.order.v1.stream/getAnchorStream")
    def get_anchor_stream(self, biz_type, req_type, ruid, page_size, sort_type=None, page=None):
        """### 获取收益流水列表"""

    @grpc_call(path="/live.order.v1.stream/getAnchorStatistics")
    def get_anchor_statistics(self, req_type, ruid, biz_type=None):
        """### 收益统计"""

    @grpc_call(path="/live.order.v1.stream/GetOrderStreamByTime")
    def get_order_stream_by_time(self, start_time, end_time, page, page_size, status=None, goods_ids=None):
        """### 查询一段时间内的订单记录"""

    @grpc_call(path="/live.order.v1.stream/getAnchorStatisticsV2")
    def get_anchor_statistics_v2(self, ruid, biz_type=None, parent_area_ids=None, start_time=None, end_time=None):
        """###获取主播收益统计"""

    @grpc_call(path="/live.order.v1.stream/GetOrderStreamByTimeV2")
    def get_order_stream_by_time_v2(self, start_time, end_time, start_id, count, status=None, goods_ids=None):
        """### 查询一段时间内的订单记录"""

    @grpc_call(path="/live.order.v1.stream/GetChildrenRechargeStream")
    def get_children_recharge_stream(self, uid, start_time, end_time, page, page_size):
        """### 未成年人充值"""

    @grpc_call(path="/live.order.v1.stream/DownloadChildrenRechargeStream")
    def download_children_recharge_stream(self, uid, start_time, end_time):
        """### 下载未成年人充值流水文件"""

    @grpc_call(path="/live.order.v1.stream/GetChildrenRechargeStreamFile")
    def get_children_recharge_stream_file(self, flag):
        """### 获取未成年人充值文件"""

    @grpc_call(path="/live.order.v1.stream/GetOrderStreamByGift")
    def get_order_stream_by_gift(self, uid=None, next_id=None, page_size=None):
        """###  用户消费流水  给礼物使用"""

    @grpc_call(path="/live.order.v1.stream/GetOrderStreamByGiftV2")
    def get_order_stream_by_gift_v2(self, uid=None, next_id=None, page_size=None):
        """###  用户消费流水(包含退款流水)  给礼物使用"""

    @grpc_call(path="/live.order.v1.stream/GetOrderStreamByTimeV3")
    def get_order_stream_by_time_v3(self, start_time, end_time, start_id, count, uid=None, goods_ids=None):
        """### 获取一段时间内用户订单记录"""

    @grpc_call(path="/live.order.v1.contract/TerminateContract")
    def terminate_contract(self, uid, goods_id, remark, ruid=None):
        """### 终止签约"""

    @grpc_call(path="/live.order.v1.contract/ChangeContractExecuteTime")
    def change_contract_execute_time(self, uid, goods_id, next_execute_time, ruid=None):
        """### 变更扣款时间 服务端内部调用"""

    @grpc_call(path="/live.order.v1.contract/ContractNotify")
    def contract_notify(self, msg_id, msg_content, p=None):
        """### 签约/解约异步回调"""

    @grpc_call(path="/live.order.v1.contract/GetContract")
    def get_contract(self, uid=None, ruid=None, goods_id=None):
        """### 查询签约信息"""

    @grpc_call(path="/live.order.v1.contract/GetPayPlatformContractStatus")
    def get_pay_platform_contract_status(self, uid=None, ruid=None, goods_id=None):
        """### 查询支付平台签约状态"""

    @grpc_call(path="/live.order.v1.contract/GetContracts")
    def get_contracts(self, uid=None, ruids=None, goods_id=None):
        """### 批量查询签约信息"""

    @grpc_call(path="/live.order.v1.contract/GetContractsByRuid")
    def get_contracts_by_ruid(self, ruid, uids, goods_id):
        """### 根据主播ID获取签约信息"""

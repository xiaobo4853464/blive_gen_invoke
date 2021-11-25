from tiny import grpc_call

class Wallet(object):
    def __init__(self,service_name):
        self.service_name=service_name
    
    @grpc_call(path="/live.xwallet.v1.Wallet/get_info")
    def get_info(self, uid=None, platform=None, need_metal=None):
        """### 无标题"""

    @grpc_call(path="/live.xwallet.v1.Wallet/get_all")
    def get_all(self, uid=None, platform=None, need_metal=None):
        """### 无标题"""

    @grpc_call(path="/live.xwallet.v1.Wallet/get_tid")
    def get_tid(self, service_type=None, service_params=None, biz_time=None):
        """###deprecated: 已下线"""

    @grpc_call(path="/live.xwallet.v1.Wallet/recharge")
    def recharge(self, uid=None, coin_type=None, coin_num=None, extend_tid=None, timestamp=None, transaction_id=None, biz_code=None, area=None, source=None, metadata=None, biz_source=None, biz_reason=None, version=None, platform=None):
        """###deprecated: 已下线"""

    @grpc_call(path="/live.xwallet.v1.Wallet/pay")
    def pay(self, uid=None, coin_type=None, coin_num=None, extend_tid=None, timestamp=None, transaction_id=None, biz_code=None, area=None, source=None, metadata=None, biz_source=None, biz_reason=None, version=None, platform=None):
        """###deprecated: 已下线"""

    @grpc_call(path="/live.xwallet.v1.Wallet/query")
    def query(self, uid=None, platform=None, transaction_id=None):
        """###deprecated: 已下线"""

    @grpc_call(path="/live.xwallet.v1.Wallet/queryByExtendTid")
    def query_by_extend_tid(self, uid, extend_tid, year_month, platform=None):
        """###deprecated: 已下线"""

    @grpc_call(path="/live.xwallet.v1.Wallet/modify")
    def modify(self, uid=None, coin_type=None, coin_num=None, extend_tid=None, timestamp=None, transaction_id=None, biz_code=None, area=None, source=None, metadata=None, biz_source=None, biz_reason=None, version=None, platform=None):
        """###deprecated: 已下线"""

    @grpc_call(path="/live.xwallet.v1.Wallet/exchange")
    def exchange(self, uid=None, src_coin_type=None, src_coin_num=None, dest_coin_type=None, dest_coin_num=None, extend_tid=None, timestamp=None, transaction_id=None, biz_code=None, area=None, source=None, metadata=None, biz_source=None, biz_reason=None, version=None, platform=None):
        """###deprecated: 已下线"""

    @grpc_call(path="/live.xwallet.v1.HamsterAccount/rechargeHamster")
    def recharge_hamster(self, uid=None, account_type=None, source=None, third_id=None, hamster=None, reason=None, remark=None, stream_id=None, ptime=None):
        """###充值金仓鼠"""

    @grpc_call(path="/live.xwallet.v1.HamsterAccount/deductHamster")
    def deduct_hamster(self, uid=None, account_type=None, source=None, third_id=None, hamster=None, reason=None, remark=None, stream_id=None, ptime=None):
        """###扣除金仓鼠"""

    @grpc_call(path="/live.xwallet.v1.HamsterAccount/getHamsterInfoV2")
    def get_hamster_info_v2(self, uid=None):
        """###获取账户信息（普通账户包含月账户和其他账户）"""

    @grpc_call(path="/live.xwallet.v1.HamsterAccount/getHamsterInfo")
    def get_hamster_info(self, uid=None):
        """###deprecated: 获取账户信息老接口 兼容新接口，新接口上线后可以下线（普通账户包含月账户和其他账户）"""

    @grpc_call(path="/live.xwallet.v1.HamsterAccount/batchGetHamsterInfo")
    def batch_get_hamster_info(self, uid=None):
        """###批量获取账户信息（普通账户包含月账户和其他账户） PS:不能使用，内部逻辑没实现"""

    @grpc_call(path="/live.xwallet.v1.HamsterAccount/queryHamsterById")
    def query_hamster_by_id(self, stream_id=None):
        """###根据钱包流水查询订单"""

    @grpc_call(path="/live.xwallet.v1.HamsterAccount/getHamsterTid")
    def get_hamster_tid(self, uid=None, account_type=None, source=None, third_id=None, hamster=None, reason=None, stream_type=None):
        """###获取交易单号"""

    @grpc_call(path="/live.xwallet.v1.HamsterAccount/getAccountBalanceList")
    def get_account_balance_list(self, hash=None, first_uid=None, max_record=None, account_type=None):
        """###批量获取用户指定账户余额不为0的指定账户列表信息"""

    @grpc_call(path="/live.xwallet.v1.HamsterAccount/getAccountBalanceNum")
    def get_account_balance_num(self, account_type=None):
        """###获取用户指定账户余额不为0的指定账户总数"""

    @grpc_call(path="/live.xwallet.v2.UserAccount/recharge")
    def recharge(self, uid, account_type, coin, tid, extend_tid, timestamp, reason, biz_type, platform, minus_coin=None, version=None):
        """###金瓜子充值"""

    @grpc_call(path="/live.xwallet.v2.UserAccount/pay")
    def pay(self, uid, coin, tid, extend_tid, timestamp, reason, biz_type, platform, version=None, settlement_price=None):
        """###金瓜子支付"""

    @grpc_call(path="/live.xwallet.v2.UserAccount/add_coin_stream")
    def add_coin_stream(self, tid, uid, account_type, timestamp, platform, biz_type, extend_tid, reason, coin, version=None):
        """###记录金瓜子流水"""

    @grpc_call(path="/live.xwallet.v2.UserAccount/get_info")
    def get_info(self, uid):
        """###获取用户账户信息"""

    @grpc_call(path="/live.xwallet.v2.UserAccount/batch_get_info")
    def batch_get_info(self, uid):
        """###批量获取用户账户信息"""

    @grpc_call(path="/live.xwallet.v2.UserAccount/get_tid")
    def get_tid(self, uid, extend_tid, transaction_type, reason, timestamp):
        """###获取事务Tid"""

    @grpc_call(path="/live.xwallet.v2.UserAccount/query_tid")
    def query_tid(self, tid):
        """###根据钱包Tid查询流水"""

    @grpc_call(path="/live.xwallet.v2.UserAccount/query_extid")
    def query_extid(self, uid, extend_tid, timestamp, transaction_type, reason):
        """###更具第三方Tid查询流水"""

    @grpc_call(path="/live.xwallet.v2.UserAccount/sync_account")
    def sync_account(self, uid):
        """###同步账户"""

    @grpc_call(path="/live.xwallet.v2.UserAccount/refund")
    def refund(self, tid=None, price=None):
        """###退款"""

    @grpc_call(path="/live.xwallet.v2.UserAccount/add")
    def add(self, uid, account_type, coin, tid, extend_tid, timestamp, reason, biz_type, platform, version=None):
        """###非充值类金瓜子新增"""

    @grpc_call(path="/live.xwallet.v2.UserAccount/deduct")
    def deduct(self, uid, coin, tid, extend_tid, timestamp, reason, biz_type, platform, account_type=None, version=None):
        """###非消费类金瓜子扣除"""

    @grpc_call(path="/live.xwallet.v2.UserAccount/get_streams")
    def get_streams(self, uid, date, start_time, end_time, page, page_size):
        """###账户金瓜子变动流水查询"""

    @grpc_call(path="/live.xwallet.v2.UserAccount/get_wallet")
    def get_wallet(self, uid):
        """###获取钱包数据"""

    @grpc_call(path="/live.xwallet.v2.UserAccount/get_sync")
    def get_sync(self, uid):
        """###获取钱包同步状态"""

    @grpc_call(path="/live.xwallet.v2.UserAccount/get_walletInfo")
    def get_wallet_info(self, uid, need_bp=None, platform=None):
        """###获取用户钱包余额信息"""

    @grpc_call(path="/live.xwallet.v2.UserAccount/make_walletCeil100")
    def make_wallet_ceil100(self, uid):
        """###平账用 补全金瓜子"""

    @grpc_call(path="/live.xwallet.v3.ThirdAccount/get_account_info")
    def get_account_info(self, account_id):
        """###获取用户账户信息"""

    @grpc_call(path="/live.xwallet.v3.ThirdAccount/recharge")
    def recharge(self, order_id, account_id, coin, reason, timestamp):
        """###账户充值"""

    @grpc_call(path="/live.xwallet.v3.ThirdAccount/pay")
    def pay(self, order_id, account_id, coin, reason, timestamp):
        """###账户扣除"""

    @grpc_call(path="/live.xwallet.v3.ThirdAccount/query")
    def query(self, order_id):
        """###订单查询"""

    @grpc_call(path="/live.xwallet.v3.ThirdAccount/addAccount")
    def add_account(self, account_id, coin, op_type, apply_pic, apply_user, apply_remark=None):
        """###添加预存金"""

    @grpc_call(path="/live.xwallet.v3.ThirdAccount/examine")
    def examine(self, id, examine_type, reviewer):
        """###审批预存金"""

    @grpc_call(path="/live.xwallet.v3.ThirdAccount/list")
    def list(self, state=None, page=None, page_size=None, account_id=None):
        """###查询预存金列表"""

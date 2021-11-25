"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""
from tiny import grpc_call


class Trading(object):

    def __init__(self, service_name):
        self.service_name = service_name

    @grpc_call(path="/live.trading.Score/GetScoreList")
    def get_score_list(self, page, page_size=None):
        """###后台接口"""

    @grpc_call(path="/live.trading.Score/GetScoreListById")
    def get_score_list_by_id(self, id=None):
        """### 根据id获取数值"""

    @grpc_call(path="/live.trading.Score/GetBatchScoreListByIds")
    def get_batch_score_list_by_ids(self, score_ids):
        """### 批量获取数值信息"""

    @grpc_call(path="/live.trading.Score/UpdateScore")
    def update_score(self, id=None, type=None, object_id=None, name=None, extra_json=None, start_time=None, end_time=None, object_type=None, is_forever=None, update_conf_status=None):
        """### 更新创建数值数值"""

    @grpc_call(path="/live.trading.Score/UpdateScoreStatus")
    def update_score_status(self, id, status):
        """### 数值上下线"""

    @grpc_call(path="/live.trading.Score/GetLog")
    def get_log(self, id=None, uid=None, start_time=None, end_time=None, page=None, page_size=None):
        """### 获取日志"""

    @grpc_call(path="/live.trading.Score/GetMngUserScoreByNum")
    def get_mng_user_score_by_num(self, page, id=None, start_num=None, end_num=None, page_size=None):
        """### 后台获取某个数量范围的钱包账号"""

    @grpc_call(path="/live.trading.Score/UpdateUserScore")
    def update_user_score(self, score_id, score, uid, tid, source, platform, context_type, expire=None, mobi_app=None, build=None, device=None, context_id=None, extra_data=None, update_time=None, biz_id=None, async_check=None, no_error_retry=None):
        """###前台接口"""

    @grpc_call(path="/live.trading.Score/UpdateUserScoreAsync")
    def update_user_score_async(self, score_id, score, uid, tid, source, platform, context_type, expire=None, mobi_app=None, build=None, device=None, context_id=None, extra_data=None, update_time=None, biz_id=None, async_check=None, no_error_retry=None):
        """### 异步增加分数 只能增加"""

    @grpc_call(path="/live.trading.Score/GetUserScore")
    def get_user_score(self, score_id, uid):
        """### get数值"""

    @grpc_call(path="/live.trading.Score/GetUserScoreLogStatus")
    def get_user_score_log_status(self, tid, source, uid=None, score_id=None):
        """### 根据msgId查询用户某笔兑换的状态"""

    @grpc_call(path="/live.trading.Score/GetUserScoreHistory")
    def get_user_score_history(self, score_id, uid):
        """### get用户历史消费记录"""

    @grpc_call(path="/live.trading.Score/GetUserScoreLogList")
    def get_user_score_log_list(self, id=None, uid=None, start_time=None, end_time=None, update_type=None, page=None, page_size=None):
        """### 查询某个时间段的log记录(仅限成功) 新数值查询必须要传uid scoreid"""

    @grpc_call(path="/live.trading.Score/GetUserScoreUpdateCount")
    def get_user_score_update_count(self, score_id, uid, start_time=None, end_time=None, source=None, update_type=None):
        """### 查询某个时间段发放总数"""

    @grpc_call(path="/live.trading.Score/GetUserScoreLogToB")
    def get_user_score_log_to_b(self, id=None, uid=None, start_time=None, end_time=None, start_num=None, end_num=None, source=None, sort_column=None, sort_type=None, page=None, page_size=None):
        """### 查询多维度log记录(仅限成功)"""

    @grpc_call(path="/live.trading.Score/ScoreRefund")
    def score_refund(self, scoreId=None, uid=None, tid=None, source=None, bizId=None, refundNum=None, extraData=None):
        """### 星光退款"""

    @grpc_call(path="/live.trading.Score/GetUserMetal")
    def get_user_metal(self, uid):
        """### 获取硬币"""

    @grpc_call(path="/live.trading.Score/ScoreExchange")
    def score_exchange(self, src_uid, src_score_id, src_score_num, src_score_source, dest_uid, dest_score_id, dest_score_num, dest_score_source, tid, platform, mobi_app=None, build=None, device=None, context_type=None, context_id=None, reason=None):
        """### 数值交换"""

    @grpc_call(path="/live.trading.Score/Silver2Coin")
    def silver2_coin(self, uid, silver_num=None, coin_num=None):
        """### 银瓜子换硬币"""

    @grpc_call(path="/live.trading.Score/Coin2Silver")
    def coin2_silver(self, uid=None, coinNum=None, silverNum=None, vip=None):
        """### 硬币换银瓜子"""

    @grpc_call(path="/live.trading.Score/CoinSilverExchangeStatus")
    def coin_silver_exchange_status(self, uid=None):
        """### 当日硬币,银瓜子兑换次数"""

    @grpc_call(path="/live.trading.Score/BatchGetUserScore")
    def batch_get_user_score(self, uid, score_ids):
        """### 批量获取用户score"""

    @grpc_call(path="/live.trading.Score/GetUserScoreByPeriod")
    def get_user_score_by_period(self, uid, start_time, end_time):
        """###获取一段时间内用户获取的星光（未过期）"""

    @grpc_call(path="/live.trading.Score/GetUserStarLog")
    def get_user_star_log(self, id, uid, start_time, end_time, page, page_size, update_type=None):
        """###获取一段时间内主播星光流水"""

    @grpc_call(path="/live.trading.Score/GetAnchorStarExpireInfo")
    def get_anchor_star_expire_info(self, page, page_size, uid, expire_ge=None, expire_le=None):
        """###获取一段时间内的过期星光"""

    @grpc_call(path="/live.trading.Score/UpdateUserStarLog")
    def update_user_star_log(self, uid, log_type, num=None, extra_data=None, tid=None, score_id=None, source=None):
        """###获取一段时间内的过期星光"""


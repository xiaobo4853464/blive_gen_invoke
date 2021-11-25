"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""
from tiny import grpc_call


class Income_play(object):

    def __init__(self, service_name):
        self.service_name = service_name

    @grpc_call(path="/live.incomeplay.v1.battleroyale/Gift")
    def gift(self, room_id=None, ruid=None, send_uid=None, tid=None, gift_type=None, gift_id=None, gift_num=None, coin_type=None, total_price=None, origin_price=None, create_time=None, timestamp=None, platform=None, mobi_app=None):
        """### 送礼"""

    @grpc_call(path="/live.incomeplay.v1.battleroyale/GetWidgetBanner")
    def get_widget_banner(self, ruid=None):
        """### 挂件"""

    @grpc_call(path="/live.incomeplay.v1.battleroyale/GetSeasonInfo")
    def get_season_info(self, season_id=None):
        """### 赛季信息"""

    @grpc_call(path="/live.incomeplay.v1.battleroyale/GetAnchorInfo")
    def get_anchor_info(self, room_id, season_id):
        """### 主播个人信息"""

    @grpc_call(path="/live.incomeplay.v1.battleroyale/GetRankInfo")
    def get_rank_info(self, season_id, track_id, rank_type, page_num, page_size):
        """### 获取榜单相关信息"""

    @grpc_call(path="/live.incomeplay.v1.battleroyale/GetUserRank")
    def get_user_rank(self, season_id, room_id, page_num, page_size):
        """### 用户贡献总榜"""

    @grpc_call(path="/live.incomeplay.v1.battleroyale/GetFinPKInfo")
    def get_fin_p_k_info(self, season_id, track_id):
        """### 决赛圈pk信息"""

    @grpc_call(path="/live.incomeplay.v1.battleroyale/GetAnchorPkInfo")
    def get_anchor_pk_info(self, room_id, season_id):
        """### 某个主播当前pk信息"""

    @grpc_call(path="/live.incomeplay.v1.battleroyale/GetAnchorPkHistory")
    def get_anchor_pk_history(self, room_id, season_id, page_num, page_size):
        """### 获取pk历史记录"""


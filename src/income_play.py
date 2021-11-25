from tiny import grpc_call

class Income_play(object):
    def __init__(self,service_name):
        self.service_name=service_name
    
    @grpc_call(path="/live.incomeplay.v1.interactiveGamePk/GiftsAndRoomInfo")
    def gifts_and_room_info(self, room_ids=None):
        """### 主播聚合信息接口"""

    @grpc_call(path="/live.incomeplay.v1.interactiveGamePk/GiftsInfo")
    def gifts_info(self, access_key_id=None):
        """### 互动平台礼物面板(白名单形式)"""

    @grpc_call(path="/live.incomeplay.v1.interactiveGamePk/AnchorList")
    def anchor_list(self, room_id=None):
        """### 主播面板列表"""

    @grpc_call(path="/live.incomeplay.v1.interactiveGamePk/InvitePk")
    def invite_pk(self, inviter_uid=None, invitee_room_id=None, type=None):
        """### PK邀请"""

    @grpc_call(path="/live.incomeplay.v1.interactiveGamePk/InvitePkCancel")
    def invite_pk_cancel(self, inviter_uid=None):
        """### PK邀请取消"""

    @grpc_call(path="/live.incomeplay.v1.interactiveGamePk/InvitePkResponse")
    def invite_pk_response(self, invite_id=None, type=None):
        """### PK邀请响应"""

    @grpc_call(path="/live.incomeplay.v1.interactiveGamePk/PkStat")
    def pk_stat(self, pk_id=None, room_id=None, invite_id=None):
        """### PK状态"""

    @grpc_call(path="/live.incomeplay.v1.interactiveGamePk/GamePkSwitch")
    def game_pk_switch(self, uid=None, room_id=None, platform=None, device=None):
        """### 查询玩家互动游戏PK开关"""

    @grpc_call(path="/live.incomeplay.v1.interactiveGamePk/ResetPlayerStat")
    def reset_player_stat(self, uid=None):
        """### 强制清理玩家状态"""

    @grpc_call(path="/live.incomeplay.v1.pkbattle/RandMatchJoin")
    def rand_match_join(self, uid=None, room_id=None, platform=None, battle_type=None):
        """### 加入匹配"""

    @grpc_call(path="/live.incomeplay.v1.pkbattle/RandMatchCancel")
    def rand_match_cancel(self, uid=None, room_id=None, platform=None, battle_type=None):
        """### 无标题"""

    @grpc_call(path="/live.incomeplay.v1.pkbattle/CheckSendGiftPower")
    def check_send_gift_power(self, uid=None, gift_id=None):
        """### check特权礼物权限"""

    @grpc_call(path="/live.incomeplay.v1.pkbattle/UpdateBlackList")
    def update_black_list(self, owner_id, member_id, status=None, source=None):
        """### 添加/移除 黑名单"""

    @grpc_call(path="/live.incomeplay.v1.pkbattle/GetBlackList")
    def get_black_list(self, owner_id, source=None, page=None, page_size=None):
        """### 获取某个主播的 黑名单列表"""

    @grpc_call(path="/live.incomeplay.v1.pkbattle/AutoMatchSwitchStatus")
    def auto_match_switch_status(self, ruid=None, room_id=None):
        """### 自动匹配开关状态"""

    @grpc_call(path="/live.incomeplay.v1.pkbattle/UpdateAutoMatchSwitch")
    def update_auto_match_switch(self, ruid, room_id, status=None):
        """### 更新自动匹配开关"""

    @grpc_call(path="/live.incomeplay.v1.pkbattle/BattleGift")
    def battle_gift(self, room_id=None, ruid=None, uid=None, pay_coin=None, tid=None, gift_id=None, gift_num=None, super_gift_num=None, send_uid=None, send_name=None, coin_type=None, timestamp=None, platform=None, gift_name=None, order_id=None, parent_area_id=None, area_id=None, goods_id=None):
        """### 送礼迁移"""

    @grpc_call(path="/live.incomeplay.v1.pkbattle/GetSeasonBattleRecord")
    def get_season_battle_record(self, room_id=None, season_id=None, date=None):
        """###  赛季pk记录 (用户侧)"""

    @grpc_call(path="/live.incomeplay.v1.pkbattle/GetBattlePendant")
    def get_battle_pendant(self, uid=None, ruid=None, season_id=None):
        """### 大乱斗挂件"""

    @grpc_call(path="/live.incomeplay.v1.pkbattle/GetPrevSeason")
    def get_prev_season(self, season_id=None):
        """### 获取上赛季"""

    @grpc_call(path="/live.incomeplay.v1.pkbattle/GetDailyStreakRank")
    def get_daily_streak_rank(self, season_id, timestamp=None, rank_start=None, rank_end=None, need_current_info=None, uid=None):
        """### 连胜日榜"""

    @grpc_call(path="/live.incomeplay.v1.pkbattle/GetScoreWeekRank")
    def get_score_week_rank(self, season_id, timestamp=None, rank_start=None, rank_end=None, need_current_info=None, uid=None):
        """### 积分周榜"""

    @grpc_call(path="/live.incomeplay.v1.pkbattle/GetScoreSeasonRank")
    def get_score_season_rank(self, season_id, timestamp=None, rank_start=None, rank_end=None, uid=None):
        """### 积分总榜"""

    @grpc_call(path="/live.incomeplay.v1.pkbattle/GetSeasonTask")
    def get_season_task(self, uid=None, season_id=None):
        """### 获取赛季任务"""

    @grpc_call(path="/live.incomeplay.v1.pkbattle/GetSeasonReduScoreRecord")
    def get_season_redu_score_record(self, uid=None, season_id=None):
        """### 获取赛季任务"""

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

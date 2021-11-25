from tiny import grpc_call

class Rankdb(object):
    def __init__(self,service_name):
        self.service_name=service_name
    
    @grpc_call(path="/live.rankdb.v1.RankBlackUser/addRankBlack")
    def add_rank_black(self, uids, rankName, reason, status, operator):
        """###加入黑名单"""

    @grpc_call(path="/live.rankdb.v1.RankBlackUser/remRankBlack")
    def rem_rank_black(self, id, operator=None):
        """###移除黑名单"""

    @grpc_call(path="/live.rankdb.v1.HotRank/GetHotRankInfo")
    def get_hot_rank_info(self, room_id, ruid, source, is_pre=None, area_id=None):
        """### 获取房间 热门榜排行信息 一级分区榜用"""

    @grpc_call(path="/live.rankdb.v1.HotRank/GetHotRankInfoNew")
    def get_hot_rank_info_new(self, room_id, ruid, source, is_pre=None, area_id=None, parent_area_id=None):
        """### 获取房间 热门榜排行信息 总榜/ 二级分区榜用 新"""

    @grpc_call(path="/live.rankdb.v1.HotRank/GetBeforeHotRankData")
    def get_before_hot_rank_data(self, area_parent_id=None, area_id=None):
        """### 获取房间历史热门榜排行信息 - 数据中台使用"""

    @grpc_call(path="/live.rankdb.v1.HotRank/GetUserHotRankInfo")
    def get_user_hot_rank_info(self, ruid, room_id, area_parent_id=None, area_id=None, area_parent_name=None, area_name=None, user_name=None, source=None):
        """### 获取当前房间 热门榜数据 入口展示"""

    @grpc_call(path="/live.rankdb.v1.HotRank/GetUserHotRankSettlement")
    def get_user_hot_rank_settlement(self, ruid, room_id, area_parent_id=None, area_id=None, area_parent_name=None, area_name=None, user_name=None, source=None):
        """### 获取指定场次用户的结算排名 (默认找上一场结算数据)"""

    @grpc_call(path="/live.rankdb.v1.HotRank/IsInBeforeHotRank")
    def is_in_before_hot_rank(self, topN=None):
        """### 天马热门榜角标 房间页用"""

    @grpc_call(path="/live.rankdb.v1.LiveRoundRank/GetLiveRoundRank")
    def get_live_round_rank(self, ruid, roomId, liveId, page, pageSize):
        """###获取直播单场次贡献榜"""

    @grpc_call(path="/live.rankdb.v1.SevenDayGoldRank/GetSevenDayGoldRank")
    def get_seven_day_gold_rank(self, room_id, ruid, page, page_size, uid=None):
        """### 无标题"""

    @grpc_call(path="/live.rankdb.v1.baseRank/BehaviorPayLive")
    def behavior_pay_live(self, ruid=None, goods_id=None, goods_num=None, biz_id=None, parent_area_id=None, area_id=None, uid=None, total_price=None, timestamp=None, eventId=None, eventName=None, eventVersion=None, eventData=None):
        """### 行为系统 购买付费直播"""

    @grpc_call(path="/live.rankdb.v1.baseRank/BehaviorSendGift")
    def behavior_send_gift(self, uid=None, room_id=None, ruid=None, parent_area_id=None, area_id=None, goods_id=None, gift_id=None, coin_type=None, goods_price=None, goods_num=None, total_coin=None, pay_coin=None, timestamp=None, eventId=None, eventName=None, eventVersion=None, transmit_data=None, liveId=None, settlement_coin=None):
        """### 行为系统 送礼行为"""

    @grpc_call(path="/live.rankdb.v1.baseRank/BehaviorSuperMessage")
    def behavior_super_message(self, uid=None, ruid=None, parentAreaId=None, areaId=None, platform=None, mobileApp=None, goodsId=None, goodsPrice=None, goodsNum=None, totalCoin=None, payCoin=None, timestamp=None, msgId=None, transmitData=None, liveId=None, roomId=None):
        """### 行为系统 付费留言"""

    @grpc_call(path="/live.rankdb.v1.baseRank/BehaviorGuard")
    def behavior_guard(self, uid=None, ruid=None, parentAreaId=None, areaId=None, platform=None, mobileApp=None, goodsId=None, goodsPrice=None, goodsNum=None, totalCoin=None, payCoin=None, timestamp=None, msgId=None, transmitData=None, liveId=None, roomId=None):
        """### 行为系统 大航海"""

    @grpc_call(path="/live.rankdb.v1.baseRank/BehaviorRedPocket")
    def behavior_red_pocket(self, uid=None, ruid=None, parentAreaId=None, areaId=None, platform=None, mobileApp=None, goodsId=None, goodsPrice=None, goodsNum=None, totalCoin=None, payCoin=None, timestamp=None, msgId=None, transmitData=None, liveId=None, roomId=None):
        """### 行为系统 人气红包"""

    @grpc_call(path="/live.rankdb.v1.baseRank/BehaviorRoomCutArea")
    def behavior_room_cut_area(self, room_id=None, uid=None, area_id=None, area_parent_id=None, last_area_id=None, last_area_parent_id=None, timestamp=None):
        """### 行为系统 切换分区"""

    @grpc_call(path="/live.rankdb.v1.baseRank/BehaviorSendDanmu")
    def behavior_send_danmu(self, room_id=None, ruid=None, uid=None, msg_id=None, msg_type=None, liveId=None, transmit_data=None, timestamp=None):
        """### 行为系统 发送弹幕"""

    @grpc_call(path="/live.rankdb.v1.baseRank/Decr")
    def decr(self, rank_id=None, sub_rank=None, rank_date=None, score=None, item_id=None, msg_id=None, sub_score=None):
        """### 榜单扣分"""

    @grpc_call(path="/live.rankdb.v1.baseRank/Incr")
    def incr(self, rank_id=None, sub_rank=None, score=None, item_id=None, msg_id=None, sub_score=None, rank_date=None):
        """### 榜单加分"""

    @grpc_call(path="/live.rankdb.v1.baseRank/Del")
    def del_(self, rank_id=None, sub_rank=None, item_id=None, msg_id=None, rank_date=None):
        """### 榜单删除"""

    @grpc_call(path="/live.rankdb.v1.baseRank/Top")
    def top(self, rank_id=None, sub_rank=None, start=None, end=None, rank_date=None):
        """### 榜单top"""

    @grpc_call(path="/live.rankdb.v1.GoldRank/GetGoldRank")
    def get_gold_rank(self, roomId, rUid, page, pageSize, uid=None):
        """### 无标题"""

    @grpc_call(path="/live.rankdb.v1.rankUser/Online")
    def online(self, uid, room_id, msg_id, time_stamp, target_id=None):
        """### 无标题"""

    @grpc_call(path="/live.rankdb.v1.rankUser/GetOnlineRank")
    def get_online_rank(self, room_id=None, rank_name=None, show_num=None):
        """### 无标题"""

    @grpc_call(path="/live.rankdb.v1.OnlineGoldRank/ReceiveLiveMessage")
    def receive_live_message(self, roomId=None, ruid=None, liveId=None, timestamp=None):
        """### 开播消息"""

    @grpc_call(path="/live.rankdb.v1.OnlineGoldRank/ReceiveEnterRoomMessage")
    def receive_enter_room_message(self, roomId=None, ruid=None, uid=None, timestamp=None, source=None):
        """### 进房消息"""

    @grpc_call(path="/live.rankdb.v1.OnlineGoldRank/GetUserRankInRoom")
    def get_user_rank_in_room(self, uid=None, roomId=None, ruid=None):
        """### 获取用户在某个房间是在线榜的第几名（前三名为1，2，3，否则为-1）(给弹幕用)"""

    @grpc_call(path="/live.rankdb.v1.OnlineGoldRank/GetNewOnlineRank")
    def get_new_online_rank(self, ruid=None, roomId=None, pageSize=None, page=None):
        """### 获取在线榜数据"""

    @grpc_call(path="/live.rankdb.v1.OnlineGoldRank/GetUserRankData")
    def get_user_rank_data(self, uid=None, roomId=None, ruid=None):
        """### 获取某个用户的排名分数等信息（信息更全，给网关用）"""

    @grpc_call(path="/live.rankdb.v1.OnlineGoldRank/ReceiveStreamerOfflineMessage")
    def receive_streamer_offline_message(self, roomId, ruid, liveId, timestamp, msgId):
        """### 房间关播消息"""

    @grpc_call(path="/live.rankdb.v1.OnlineGoldRank/UserLeaveRoomGold")
    def user_leave_room_gold(self, uid=None, ruid=None, roomId=None, timestamp=None, parent_area_id=None, area_id=None):
        """### 高能榜用户离场"""

    @grpc_call(path="/live.rankdb.v1.OnlineGoldRank/RefreshUserRank")
    def refresh_user_rank(self, roomId=None, ruid=None, uid=None, timestamp=None):
        """### 刷新用户排名"""

    @grpc_call(path="/live.rankdb.v1.OnlineGoldRank/OnlineGoldTotalCount")
    def online_gold_total_count(self, ruid):
        """### 贡献榜总人数"""

    @grpc_call(path="/live.rankdb.v1.OnlineRank/UserEnterRoomOnlineRank")
    def user_enter_room_online_rank(self, uid=None, ruid=None, roomId=None, timestamp=None):
        """### 用户进场"""

    @grpc_call(path="/live.rankdb.v1.OnlineRank/UserLeaveRoomOnlineRank")
    def user_leave_room_online_rank(self, uid=None, ruid=None, roomId=None, timestamp=None):
        """### 用户离场"""

    @grpc_call(path="/live.rankdb.v1.OnlineRank/UserGetOnlineRank")
    def user_get_online_rank(self, uid=None, ruid=None, roomId=None, page=None, pageSize=None):
        """### 获取排名"""

    @grpc_call(path="/live.rankdb.v1.OnlineRank/GoldAndOnlineSevenTop")
    def gold_and_online_seven_top(self, roomId, ruid=None):
        """### 贡献榜+在线榜顶部7人"""

    @grpc_call(path="/live.rankdb.v1.OnlineRank/GetOnlineRankCount")
    def get_online_rank_count(self, roomId, ruid=None):
        """### 在线榜人数"""

    @grpc_call(path="/live.rankdb.v1.TotalRank/GetTotalMedalLevelRank")
    def get_total_medal_level_rank(self, uid=None, page=None, page_size=None):
        """### 勋章等级总榜"""

    @grpc_call(path="/live.rank.v1.AnchorRank/GetHeartRank")
    def get_heart_rank(self, ruid, page, page_size, light_fans_num=None):
        """### 获取排行榜数据"""

    @grpc_call(path="/live.rank.v1.AnchorRank/GetAnchorIntimacyRank")
    def get_anchor_intimacy_rank(self, medal_id, page, page_size):
        """### 获取主播亲密度榜"""

    @grpc_call(path="/live.rank.v1.AnchorRank/GetHeartRankV2")
    def get_heart_rank_v2(self, ruid, page, page_size, light_fans_num=None):
        """### 获取排行榜数据v2"""

    @grpc_call(path="/live.rankdb.v2.generalRankFrontend/GeneralRankAutoIncr")
    def general_rank_auto_incr(self, uid=None, ruid=None, room_id=None, parent_area_id=None, area_id=None, platform=None, mobile_app=None, goods_type=None, goods_id=None, coin_type=None, goods_num=None, pay_coin=None, total_coin=None, timestamp=None, msg_id=None, source=None, rank_ids=None, gift_id=None):
        """### 通用榜单自动加分接口"""

    @grpc_call(path="/live.rankdb.v2.generalRankFrontend/GeneralRankGetConf")
    def general_rank_get_conf(self, rank_id=None):
        """### 获取榜单配置"""

    @grpc_call(path="/live.rankdb.v2.generalRankFrontend/GeneralRankAutoFix")
    def general_rank_auto_fix(self, source, msg_id, start_time, end_time, rank_ids, uids=None, ruids=None):
        """### 通用补分逻辑"""

    @grpc_call(path="/live.rankdb.v2.generalRankFrontend/GeneralRankAutoBattleProcessIncr")
    def general_rank_auto_battle_process_incr(self, uid=None, ruid=None, room_id=None, parent_area_id=None, area_id=None, platform=None, mobile_app=None, goods_type=None, goods_id=None, gift_id=None, coin_type=None, goods_num=None, pay_coin=None, total_coin=None, pk_score=None, pk_id=None, season_id=None, timestamp=None, msg_id=None, source=None, rank_ids=None):
        """### 通用榜单大乱斗进程中自动加分接口"""

    @grpc_call(path="/live.rankdb.v2.generalRankBackend/GetRankList")
    def get_rank_list(self, rank_name=None, page_index=None, page_size=None):
        """### 搜索通用榜单列表"""

    @grpc_call(path="/live.rankdb.v2.generalRankBackend/GetRankDetail")
    def get_rank_detail(self, id=None):
        """### 榜单配置详情"""

    @grpc_call(path="/live.rankdb.v2.generalRankBackend/GetAwardConfigList")
    def get_award_config_list(self, award_name=None, page_index=None, page_size=None):
        """### 搜索通用榜单奖励列表"""

    @grpc_call(path="/live.rankdb.v2.generalRankBackend/GetAwardConfigDetail")
    def get_award_config_detail(self, config_id=None):
        """### 榜单奖励配置详情"""

    @grpc_call(path="/live.rankdb.v2.generalRankBackend/ExportRankSql")
    def export_rank_sql(self, id=None):
        """### 导出榜单配置sql"""

    @grpc_call(path="/live.rankdb.v2.generalRankBackend/ExportRankAwardSql")
    def export_rank_award_sql(self, id=None):
        """### 导出榜单奖励配置sql"""

    @grpc_call(path="/live.rankdb.v2.generalRankBackend/CopyRank")
    def copy_rank(self, id=None):
        """### 复制榜单"""

    @grpc_call(path="/live.rankdb.v2.generalRankBackend/UpdateRankStatus")
    def update_rank_status(self, id=None, rank_status=None):
        """### 榜单上下线"""

    @grpc_call(path="/live.rankdb.v2.generalRankBackend/GetRankConfByIds")
    def get_rank_conf_by_ids(self, rank_ids=None):
        """### 根据ID查询榜单"""

    @grpc_call(path="/live.rankdb.v2.generalRankBackend/GetRankListBatchToSql")
    def get_rank_list_batch_to_sql(self, ids=None):
        """### 批量导出通用榜单列表数据sql"""

    @grpc_call(path="/live.rankdb.v2.generalRankBackend/GetRankAwardList")
    def get_rank_award_list(self, id=None, page=None, page_size=None):
        """### 榜单奖励中发奖结果列表"""

    @grpc_call(path="/live.rankdb.v3.BaseModule/DeleteModule")
    def delete_module(self, uid, ruid, business_id, room_id=None, reason=None):
        """### 无标题"""

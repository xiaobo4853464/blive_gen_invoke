from tiny import grpc_call

class Gift(object):
    def __init__(self,service_name):
        self.service_name=service_name
    
    @grpc_call(path="/live.xgift.v1.SpecialPlan/AddSpecialPlan")
    def add_special_plan(self, biz_type, relevance_id, gift_list, online_time, offline_time, comment, creator=None, extend_int=None):
        """### 新增特殊投放"""

    @grpc_call(path="/live.xgift.v1.SpecialPlan/UpdateSpecialPlan")
    def update_special_plan(self, biz_type, relevance_id, gift_list, online_time, offline_time, comment, plan_id, creator=None, extend_int=None):
        """### 更新投放"""

    @grpc_call(path="/live.xgift.v1.SpecialPlan/SpecialPlanDetail")
    def special_plan_detail(self, plan_id):
        """### 投放详情"""

    @grpc_call(path="/live.xgift.v1.SpecialPlan/OfflineSpecialPlan")
    def offline_special_plan(self, plan_id, creator=None):
        """### 下线"""

    @grpc_call(path="/live.xgift.v1.SpecialPlan/GetSpecialPlanList")
    def get_special_plan_list(self, page, page_size=None, search_type=None, search_content=None, biz_type=None, status=None):
        """### 投放列表"""

    @grpc_call(path="/live.xgift.v1.BlindGift/GetConfig")
    def get_config(self, id=None):
        """### 获取 盲盒礼物 配置"""

    @grpc_call(path="/live.xgift.v1.BlindGift/GetLastConfig")
    def get_last_config(self, gift_id=None):
        """### 获取 最新生效盲盒礼物 配置（给活动用）"""

    @grpc_call(path="/live.xgift.v1.BlindGift/GetList")
    def get_list(self, page_num, page_size, title=None, status=None):
        """### 配置列表"""

    @grpc_call(path="/live.xgift.v1.BlindGift/GetStat")
    def get_stat(self, id, start_date=None, end_date=None):
        """### 查询统计"""

    @grpc_call(path="/live.xgift.v1.BlindGift/CloseConfig")
    def close_config(self, id=None):
        """### 下线"""

    @grpc_call(path="/live.xgift.v1.BlindGift/SetSpecialProbability")
    def set_special_probability(self, config_id, dimension, dimension_id, start_time, end_time, sp_probability):
        """### 设置特殊概率"""

    @grpc_call(path="/live.xgift.v1.BlindGift/GetSpecialProbability")
    def get_special_probability(self, config_id, dimension, dimension_id):
        """### 获取正在使用的特殊概率"""

    @grpc_call(path="/live.xgift.v1.GiftStream/getGiftStatV2")
    def get_gift_stat_v2(self, coin_type=None, begin_time=None, end_time=None, ruid=None):
        """### 获取礼物统计详情"""

    @grpc_call(path="/live.xgift.v1.GiftStream/getGiftStat")
    def get_gift_stat(self, coin_type=None, begin_time=None, end_time=None, ruid=None):
        """### 获取礼物统计详情"""

    @grpc_call(path="/live.xgift.v1.GiftStream/handleGiftStat")
    def handle_gift_stat(self, ruid, gift_id, gift_num, timestamp, msg_id, coin_type=None, sub_type=None):
        """### 处理礼物统计"""

    @grpc_call(path="/live.xgift.v1.GiftStream/getGiftRankV2")
    def get_gift_rank_v2(self, coin_type=None, rank_type=None, type_value=None, ruid=None, page_num=None, page_size=None):
        """### 消费排行"""

    @grpc_call(path="/live.xgift.v1.GiftStream/getGiftStreamV2")
    def get_gift_stream_v2(self, page_num=None, page_size=None, coin_type=None, gift_id=None, begin_time=None, uname=None, ruid=None):
        """### 获取礼物流水列表"""

    @grpc_call(path="/live.xgift.v1.GiftStream/getBlindGiftStream")
    def get_blind_gift_stream(self, uid, next_id=None, page_size=None, month=None, gift_ids=None, start_time=None, end_time=None):
        """### 获取 盲盒 送礼记录"""

    @grpc_call(path="/live.xgift.v1.GiftStream/getGiftRank")
    def get_gift_rank(self, coin_type=None, rank_type=None, type_value=None, ruid=None, page_num=None, page_size=None):
        """### 消费排行"""

    @grpc_call(path="/live.xgift.v1.GiftStream/getGiftStream")
    def get_gift_stream(self, page_num=None, page_size=None, coin_type=None, gift_id=None, begin_time=None, uname=None, ruid=None):
        """### 获取礼物流水列表"""

    @grpc_call(path="/live.xgift.v1.GiftStream/addGuardScGiftStream")
    def add_guard_sc_gift_stream(self, order_id, goods_id, uid, ruid, total_coin, goods_num, pay_coin, platform, timestamp, msg_id, transaction_id=None, parent_area_id=None, area_id=None, mobile_app=None, build=None):
        """### 写大航海、付费留言流水"""

    @grpc_call(path="/live.xgift.v1.GiftStream/getSendGiftStream")
    def get_send_gift_stream(self, month=None, uid=None, coin_type=None, id=None, page_size=None, min_month=None):
        """### 获取送礼流水"""

    @grpc_call(path="/live.xgift.v1.GiftStream/getGiftStatisticsTotal")
    def get_gift_statistics_total(self, uid, source=None):
        """### 获取 用户 礼物消费统计"""

    @grpc_call(path="/live.xgift.v1.GoldPackage/AddUserGoldPackage")
    def add_user_gold_package(self, uid, gift_id, incr_gift_num, gift_price, expireat, biz_type, biz_extra):
        """### 添加用户金瓜子包裹"""

    @grpc_call(path="/live.xgift.v1.GoldPackage/UserGoldPackageList")
    def user_gold_package_list(self, uid, room_id=None, platform=None, build=None, mobi_app=None):
        """### 用户金瓜子包裹列表"""

    @grpc_call(path="/live.xgift.v1.Backend/deleteGift")
    def delete_gift(self, gift_id):
        """### 删除道具"""

    @grpc_call(path="/live.xgift.v1.Backend/getDeleteTips")
    def get_delete_tips(self, gift_id):
        """### 获取道具删除关联提示"""

    @grpc_call(path="/live.xgift.v1.Backend/GetGiftRecord")
    def get_gift_record(self, uid=None, ruid=None, gift_id=None, order_id=None, tid=None, begin_time=None, end_time=None, coin_type=None, status=None, page=None, page_size=None):
        """### 无标题"""

    @grpc_call(path="/live.xgift.v1.Backend/GoldPackageStream")
    def gold_package_stream(self, uid=None, gift_id=None, bag_id=None, biz_type=None, order_id=None, begin_time=None, end_time=None, page=None, page_size=None):
        """### 用户金瓜子包裹查询"""

    @grpc_call(path="/live.xgift.v1.Gift/room_gift_list")
    def room_gift_list(self, room_id=None, area_v2_parent_id=None, area_v2_id=None, platform=None, build=None, mobi_app=None):
        """### 房间礼物列表    -没有流量废弃"""

    @grpc_call(path="/live.xgift.v1.Gift/gift_config")
    def gift_config(self, platform=None, build=None):
        """### 礼物素材    -低版本留着继续用"""

    @grpc_call(path="/live.xgift.v1.Gift/discount_gift_list")
    def discount_gift_list(self, uid=None, roomid=None, area_v2_parent_id=None, area_v2_id=None, platform=None, ruid=None):
        """### 房间折扣数据   -没有流量废弃"""

    @grpc_call(path="/live.xgift.v1.Gift/daily_bag")
    def daily_bag(self, uid=None):
        """### 每日礼包"""

    @grpc_call(path="/live.xgift.v1.Gift/smsReward")
    def sms_reward(self, uid=None, card_type=None):
        """### 22,33卡兑奖接口  -主站使用"""

    @grpc_call(path="/live.xgift.v1.Gift/roomGiftListByVote")
    def room_gift_list_by_vote(self, room_id, area_parent_id, area_id, uid=None, source=None):
        """### 房间礼物列表 （投票用）  blink 调用"""

    @grpc_call(path="/live.xgift.v1.Gift/getGiftListById")
    def get_gift_list_by_id(self, gift_id, source=None):
        """### 通过id获取道具基本信息 - 内部使用"""

    @grpc_call(path="/live.xgift.v1.Gift/getGiftInfoById")
    def get_gift_info_by_id(self, gift_id, source=None):
        """### 通过id获取道具全部信息 - 内部使用 只能送礼调用"""

    @grpc_call(path="/live.xgift.v1.Gift/getRoomValidGiftId")
    def get_room_valid_gift_id(self, platform, room_id, build=None, area_parent_id=None, area_id=None, uid=None, source=None, mobi_app=None):
        """### 获取房间所有 有效道具 - 内部使用 只能送礼调用"""

    @grpc_call(path="/live.xgift.v1.Gift/giftMemoryList")
    def gift_memory_list(self, room_id):
        """### 获取房间所有 高价礼物记忆列表 - 网关集合调用"""

    @grpc_call(path="/live.xgift.v1.Gift/getStreamByOrderId")
    def get_stream_by_order_id(self, order_id, order_date):
        """### 订单id查询 送礼记录 - 订单对账使用"""

    @grpc_call(path="/live.xgift.v1.Gift/getStreamByTid")
    def get_stream_by_tid(self, tid, order_date):
        """### tid查询 送礼记录 - 对账使用"""

    @grpc_call(path="/live.xgift.v1.Gift/liveGiftConfig")
    def live_gift_config(self, platform, build=None, room_id=None, area_parent_id=None, area_id=None, uid=None, source=None, mobi_app=None):
        """### 道具素材资源-房间页"""

    @grpc_call(path="/live.xgift.v1.Gift/liveRoomGiftList")
    def live_room_gift_list(self, platform, room_id, build=None, area_parent_id=None, area_id=None, uid=None, source=None, mobi_app=None):
        """### 房间礼物列表-房间页"""

    @grpc_call(path="/live.xgift.v1.Gift/liveDiscountGiftList")
    def live_discount_gift_list(self, platform, room_id, build=None, area_parent_id=None, area_id=None, uid=None, source=None, mobi_app=None):
        """### 折扣礼物列表-房间页"""

    @grpc_call(path="/live.xgift.v1.Gift/GetPanelTab")
    def get_panel_tab(self, platform, room_id, build=None, area_parent_id=None, area_id=None, uid=None, source=None, mobi_app=None):
        """### 礼物面板tab-房间页"""

    @grpc_call(path="/live.xgift.v1.Gift/TabRoomGiftList")
    def tab_room_gift_list(self, platform, room_id, tab_id, build=None, area_parent_id=None, area_id=None, uid=None, source=None, mobi_app=None):
        """### 礼物面板投放数据-房间页"""

    @grpc_call(path="/live.xgift.v1.Gift/PreviewRoomGiftList")
    def preview_room_gift_list(self, platform, room_id, time=None, area_parent_id=None, area_id=None, uid=None, build=None, mobi_app=None):
        """### 礼物面板预览-后台使用"""

    @grpc_call(path="/live.xgift.v1.Gift/GetGiftList")
    def get_gift_list(self, resource_type=None, coin_type=None):
        """### 根据条件取所有 上线（gift_online）中的礼物列表-后台使用"""

    @grpc_call(path="/live.xgift.v1.Gift/specialPlan")
    def special_plan(self, biz_type, gift_list, online_time, offline_time, comment, room_id=None, creator=None, extend_int=None, relevance_id=None):
        """### 特殊 道具投放"""

    @grpc_call(path="/live.xgift.v1.Gift/myTvCount")
    def my_tv_count(self, uid):
        """### 获取用户 小电视道具 统计"""

    @grpc_call(path="/live.xgift.v1.Gift/JoinFansGiftInfo")
    def join_fans_gift_info(self, platform, room_id, area_parent_id=None, area_id=None, need_price=None):
        """### 入团引导道具id"""

    @grpc_call(path="/live.xgift.v1.Gift/GetRoomGiftAndBagIds")
    def get_room_gift_and_bag_ids(self, platform, build=None, room_id=None, area_parent_id=None, area_id=None, uid=None, source=None, mobi_app=None):
        """### 取房间所有有效道具ids + 所有包裹道具ids 全屏动画用"""

    @grpc_call(path="/live.xgift.v1.Gift/getLastSendGift")
    def get_last_send_gift(self, room_id, uid):
        """### 获取最后送礼标记 替换V0Gift.GetLastSendGift"""

    @grpc_call(path="/live.xgift.v1.Gift/sendComboEnd")
    def send_combo_end(self, uid, ruid, room_id, gift_id, gift_num, price, msg_id, uname=None, runame=None, combo_num=None, batch_combo_num=None, gift_name=None, action=None, start_time=None, end_time=None, guard_level=None, name_color=None, combo_total_coin=None):
        """### 发送 combo_end 广播 用于播端礼物盒子"""

    @grpc_call(path="/live.xgift.v1.Gift/setVipMonthBag")
    def set_vip_month_bag(self, uid):
        """### 设置用户月礼包状态 替换 V2Inner.SetVipMonthBag"""

    @grpc_call(path="/live.xgift.v1.ChildremStream/prduceChildremStream")
    def prduce_childrem_stream(self, uid=None, ruid=None, start_time=None, end_time=None):
        """### 生成未成年打赏文件内容并上传"""

    @grpc_call(path="/live.xgift.v1.ChildremStream/getChildremStreamFile")
    def get_childrem_stream_file(self, flag=None):
        """### 获取生成文件链接"""

    @grpc_call(path="/live.xgift.v1.Bag/BagList")
    def bag_list(self, roomid=None, uid=None, platform=None, build=None, mobi_app=None):
        """### 包裹列表"""

    @grpc_call(path="/live.xgift.v1.Bag/BagReduce")
    def bag_reduce(self, uid=None, gift_num=None, bag_id=None, gift_id=None, platform=None, biz_id=None):
        """### 提供送礼接口扣减道具"""

    @grpc_call(path="/live.xgift.v1.Bag/BagDeleteTask")
    def bag_delete_task(self, table=None, limit=None):
        """### 移除过期道具"""

    @grpc_call(path="/live.xgift.v1.Bag/BagInfoAdmin")
    def bag_info_admin(self, uid=None, next_offset=None, prev_offset=None, page_size=None, export=None):
        """### 用户包裹资产"""

    @grpc_call(path="/live.xgift.v1.Bag/ClearBagDot")
    def clear_bag_dot(self, uid):
        """### 清理包裹红点"""

    @grpc_call(path="/live.xgift.v1.Bag/GetBagDot")
    def get_bag_dot(self, uid):
        """### 获取包裹红点"""

    @grpc_call(path="/live.xgift.v1.Bag/GetBagListByUid")
    def get_bag_list_by_uid(self, uid, status=None):
        """### 用户包裹列表 后台用 （包括 金瓜子包裹、免费包裹）"""

    @grpc_call(path="/live.xgift.v1.Bag/SilverPackageStream")
    def silver_package_stream(self, uid=None, gift_id=None, bag_id=None, source=None, begin_time=None, end_time=None, page=None, page_size=None):
        """### 用户银瓜子包裹查询"""

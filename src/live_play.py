from tiny import grpc_call

class Live_play(object):
    def __init__(self,service_name):
        self.service_name=service_name
    
    @grpc_call(path="/live.liveplay.v1.WishingBottle/processing_wish_list")
    def processing_wish_list(self, ruid, platform):
        """### 主播的许愿瓶状态"""

    @grpc_call(path="/live.liveplay.v1.WishingBottle/available_wish_list")
    def available_wish_list(self, ruid):
        """### 当前未删除且未完成的愿望列表"""

    @grpc_call(path="/live.liveplay.v1.WishingBottle/change_wishing_bottle_switch")
    def change_wishing_bottle_switch(self, switch=None):
        """### 全局开关变更"""

    @grpc_call(path="/live.liveplay.v1.WishingBottle/add")
    def add(self, type, type_id, wish_limit, content, user_id, platform):
        """### 无标题"""

    @grpc_call(path="/live.liveplay.v1.WishingBottle/finish")
    def finish(self, id, uid):
        """### 完成愿望"""

    @grpc_call(path="/live.liveplay.v1.WishingBottle/delete")
    def delete(self, id, uid):
        """### 删除愿望"""

    @grpc_call(path="/live.liveplay.v1.WishingBottle/config")
    def config(self, uid):
        """### 许愿瓶配置项"""

    @grpc_call(path="/live.liveplay.v1.WishingBottle/hot_words")
    def hot_words(self, uid):
        """### 愿望热词"""

    @grpc_call(path="/live.liveplay.v1.WishingBottle/search_wish_list")
    def search_wish_list(self, status=None, page_no=None, page_size=None, time_start=None, time_end=None, content=None, uid=None, roomid=None):
        """### 带搜索功能的心愿列表"""

    @grpc_call(path="/live.liveplay.v1.WishingBottle/set_room_block")
    def set_room_block(self, roomid, status=None):
        """### 无标题"""

    @grpc_call(path="/live.liveplay.v1.WishingBottle/block_room_list")
    def block_room_list(self, roomid=None, page_no=None, page_size=None):
        """### 无标题"""

    @grpc_call(path="/live.liveplay.v1.WishingBottle/audit")
    def audit(self, ids, status, reason=None, operator=None):
        """### 无标题"""

    @grpc_call(path="/liveplay.v1.WishBottle/wishList")
    def wish_list(self, ruid=None):
        """### 无标题"""

    @grpc_call(path="/live.liveplay.Lottery/getMachineAwardList")
    def get_machine_award_list(self, page=None, act_id=None, uid=None, title=None, award_type=None, start_time=None, end_time=None, type=None):
        """### 获取小电视机甲中奖列表"""

    @grpc_call(path="/live.liveplay.Lottery/downloadMachineAwardList")
    def download_machine_award_list(self, page=None, act_id=None, uid=None, title=None, award_type=None, start_time=None, end_time=None, type=None):
        """### 下载小电视机甲中奖列表"""

    @grpc_call(path="/live.liveplay.Lottery/getMachineAwardInfo")
    def get_machine_award_info(self, uid=None, fight_id=None, room_id=None):
        """### 获取小电视机甲中奖列表"""

    @grpc_call(path="/live.liveplay.Lottery/getLuckAwardInfo")
    def get_luck_award_info(self, fight_id=None, room_id=None):
        """### 获取小电视机甲中奖列表"""

    @grpc_call(path="/live.liveplay.Lottery/getHarmAwardInfo")
    def get_harm_award_info(self, fight_id=None, room_id=None):
        """### 获取小电视机甲中奖列表"""

    @grpc_call(path="/live.liveplay.Lottery/getUserMachineAwardList")
    def get_user_machine_award_list(self, page=None, act_id=None, uid=None):
        """### 获取小电视机甲中奖列表"""

    @grpc_call(path="/live.liveplay.Lottery/getUserMachineAwardText")
    def get_user_machine_award_text(self, act_id=None, uid=None):
        """### 获取小电视机甲中奖列表"""

    @grpc_call(path="/live.liveplay.SmallTVBossBack/GetConf")
    def get_conf(self, id):
        """### 获取玩法"""

    @grpc_call(path="/live.liveplay.SmallTVBossBack/GetConfList")
    def get_conf_list(self, page=None, page_size=None):
        """### 获取玩法列表"""

    @grpc_call(path="/live.liveplay.SmallTVBossBack/DelConf")
    def del_conf(self, id):
        """### 删除"""

    @grpc_call(path="/live.liveplay.SmallTVBossBack/GetBoss")
    def get_boss(self, boss_id=None):
        """### 获取单个Boss信息"""

    @grpc_call(path="/live.liveplay.WidgetAdminService/AddBanner")
    def add_banner(self, title=None, weight=None, plan_platform=None, start_time=None, end_time=None, jump_url=None, tip_text=None, tip_text_color=None, tip_bottom_color=None, bind_id=None, extra_conf=None, type=None, stay_time=None):
        """### 新增"""

    @grpc_call(path="/live.liveplay.WidgetAdminService/UpdateBanner")
    def update_banner(self, id, title=None, weight=None, plan_platform=None, start_time=None, end_time=None, jump_url=None, tip_text=None, tip_text_color=None, tip_bottom_color=None, bind_id=None, extra_conf=None, type=None, stay_time=None):
        """### 修改"""

    @grpc_call(path="/live.liveplay.WidgetAdminService/CloseBanner")
    def close_banner(self, id):
        """### 下线"""

    @grpc_call(path="/live.liveplay.WidgetAdminService/GetList")
    def get_list(self, page, page_size=None, search_id=None, search_title=None):
        """### 获取列表"""

    @grpc_call(path="/live.liveplay.WidgetAdminService/GetBannerById")
    def get_banner_by_id(self, id):
        """### 获取某一个 挂件"""

    @grpc_call(path="/live.liveplay.FullScSpecialEffect/AddConfForGiftJob")
    def add_conf_for_gift_job(self, type, online_time, web_svga=None, horizontal_svga=None, vertical_svga=None, title=None, offline_time=None, plan_platform=None, bind_gift_ids=None):
        """### 道具洗数据脚本使用"""

    @grpc_call(path="/live.liveplay.FullScSpecialEffect/AddConf")
    def add_conf(self, type, online_time, web_svga=None, horizontal_svga=None, vertical_svga=None, web_mp4=None, web_mp4_json=None, horizontal_mp4=None, vertical_mp4=None, web_mp4_zip=None, horizontal_mp4_zip=None, vertical_mp4_zip=None, title=None, offline_time=None, plan_platform=None, web_mp4_md5=None, horizontal_mp4_md5=None, vertical_mp4_md5=None, web_mp4_common=None, horizontal_mp4_common=None, vertical_mp4_common=None, web_mp4_common_md5=None, horizontal_mp4_common_md5=None, vertical_mp4_common_md5=None, web_mp4_common_zip=None, horizontal_mp4_common_zip=None, vertical_mp4_common_zip=None, web_mp4_common_json=None, resource_type=None):
        """### 新增配置"""

    @grpc_call(path="/live.liveplay.FullScSpecialEffect/UpdateConf")
    def update_conf(self, type, online_time, id, web_svga=None, horizontal_svga=None, vertical_svga=None, web_mp4=None, web_mp4_json=None, horizontal_mp4=None, vertical_mp4=None, web_mp4_zip=None, horizontal_mp4_zip=None, vertical_mp4_zip=None, title=None, offline_time=None, plan_platform=None, bind_gift_ids=None, web_mp4_md5=None, horizontal_mp4_md5=None, vertical_mp4_md5=None, web_mp4_common=None, horizontal_mp4_common=None, vertical_mp4_common=None, web_mp4_common_md5=None, horizontal_mp4_common_md5=None, vertical_mp4_common_md5=None, web_mp4_common_zip=None, horizontal_mp4_common_zip=None, vertical_mp4_common_zip=None, web_mp4_common_json=None, resource_type=None):
        """### 修改配置 注：type不能修改"""

    @grpc_call(path="/live.liveplay.FullScSpecialEffect/GetConfList")
    def get_conf_list(self, page=None, type=None, id=None, title=None, status=None, plan_platform=None):
        """### 列表信息"""

    @grpc_call(path="/live.liveplay.FullScSpecialEffect/GetConfDetail")
    def get_conf_detail(self, id):
        """### 详细信息"""

    @grpc_call(path="/live.liveplay.FullScSpecialEffect/OfflineConf")
    def offline_conf(self, id):
        """### 下线配置"""

    @grpc_call(path="/live.liveplay.FullScSpecialEffect/UpdateBindGiftId")
    def update_bind_gift_id(self, effect_ids, gift_id, add_or_del):
        """### 更新动画绑定道具id  道具后台同步时使用 可批量（多个动画同时绑定某个 道具id） ！！后台用！！"""

    @grpc_call(path="/live.liveplay.FullScSpecialEffect/SendSpecialEffect")
    def send_special_effect(self, effect_id, room_ids):
        """### 触发特效接口"""

    @grpc_call(path="/live.liveplay.LplPaidLive/setAlertWindowShow")
    def set_alert_window_show(self, window_type=None, uid=None, timestamp=None):
        """### 设置弹窗已经展示"""

    @grpc_call(path="/live.liveplay.LplPaidLive/getLplRoomPlayInfo")
    def get_lpl_room_play_info(self, window_type=None, uid=None, timestamp=None, platform=None):
        """### 获取LPL房间播放信息"""

    @grpc_call(path="/live.liveplay.LplPaidLive/getLplRoomPlayTime")
    def get_lpl_room_play_time(self, window_type=None, uid=None, timestamp=None):
        """### 获取LPL房间可播放流长度"""

    @grpc_call(path="/live.liveplay.LplPaidLive/getAllWindowStatus")
    def get_all_window_status(self, uid=None, timestamp=None):
        """### 获取所有弹窗状态"""

    @grpc_call(path="/xlive/general-interface/v1/bnj2020/answer")
    def answer(self, answer=None, qid=None, uid=None, aid=None):
        """###答题(需要登录态)"""

    @grpc_call(path="/xlive/general-interface/v1/bnj2020/getanswerinfo")
    def getanswerinfo(self, uid=None, aid=None):
        """###获取答题信息(需要登录态)"""

    @grpc_call(path="/live.liveplay.Panel/PanelData")
    def panel_data(self, room_id, platform=None, build=None, uid=None):
        """### 获取 面板全部功能 面板功能列表 外置宣发面板"""

    @grpc_call(path="/live.liveplay.Panel/PanelDataV2")
    def panel_data_v2(self, room_id, platform=None, build=None, is_entry_room=None, room_type=None):
        """### 底部面板V2"""

    @grpc_call(path="/live.liveplay.Panel/PanelDataV3")
    def panel_data_v3(self, room_id, platform=None, build=None, is_entry_room=None, room_type=None):
        """### 面板"""

    @grpc_call(path="/live.liveplay.Panel/PanelList")
    def panel_list(self, page, page_size):
        """### 获取列表"""

    @grpc_call(path="/live.liveplay.Panel/PanelListV2")
    def panel_list_v2(self, page, page_size):
        """### 获取列表V2"""

    @grpc_call(path="/live.liveplay.Panel/PanelHourBroadcast")
    def panel_hour_broadcast(self, room_id=None, area_id=None, parent_area_id=None, title=None, note=None, operate=None, jump_url=None):
        """### 发送小时榜广播"""

    @grpc_call(path="/live.liveplay.WidgetService/GetWidgetBannerList")
    def get_widget_banner_list(self, room_id, ruid, platform, area_id=None, parent_area_id=None, build=None, mobi_app=None, source=None, special_flag=None, uid=None, page_source=None):
        """### 挂件banner接口"""

    @grpc_call(path="/live.liveplay.WidgetService/UpdateWidgetBanner")
    def update_widget_banner(self, update_type, source, broadcast_type=None, room_id=None, ruid=None, bind_id=None, sub_key=None, sub_data=None, delay=None, cache_time=None, intercept=None):
        """### 挂件更新内容"""

    @grpc_call(path="/live.liveplay.topic/GetEventInfo")
    def get_event_info(self, act_id=None):
        """### 获取 活动 信息"""

    @grpc_call(path="/live.liveplay.LiveBossPlay/GetInfoByGift")
    def get_info_by_gift(self, gift_id, gift_name, gift_num, uid, room_id, t_id, uname, areaId, gift_type=None, gift_value=None, play_id=None, activity_id=None, status=None, status_fight=None):
        """###返回礼物对应的玩法信息"""

    @grpc_call(path="/live.liveplay.LiveBossPlay/GetResouByid")
    def get_resou_byid(self, room_id, play_id, activity_id):
        """###获取入口图片资源素材"""

    @grpc_call(path="/live.liveplay.LiveBossPlay/Notify")
    def notify(self, play_id=None, activity_id=None, start_or_stop=None, ts=None):
        """###活动通知"""

    @grpc_call(path="/live.liveplay.LiveBossPlay/IsBattle")
    def is_battle(self, room_id=None):
        """###是否在战斗过程中"""

    @grpc_call(path="/live.liveplay.LiveBossPlay/GetLastBattleResult")
    def get_last_battle_result(self, active_id, play_id, room_id):
        """###上轮战斗结果"""

    @grpc_call(path="/live.liveplay.LiveBossPlay/IsActiveBattle")
    def is_active_battle(self, active_id, play_id):
        """###活动是否在战斗中"""

    @grpc_call(path="/live.liveplay.LiveBossPlay/GetBloodEnergy")
    def get_blood_energy(self, active_id, play_id, room_id):
        """### 无标题"""

    @grpc_call(path="/live.liveplay.LiveBossPlay/OnBattleEvent")
    def on_battle_event(self, activity_id, play_id, room_id, battle_id, battle_status, boss_id=None, timestamp=None, energy_level=None):
        """### 战斗事件"""

    @grpc_call(path="/live.liveplay.LiveBossPlay/QueryBattleID")
    def query_battle_i_d(self, activity_id, play_id, room_id):
        """### 获取战斗ID"""

    @grpc_call(path="/live.liveplay.LiveBossPlay/QueryBattleRecord")
    def query_battle_record(self, activity_id, play_id, room_id):
        """### 获取战斗记录"""

    @grpc_call(path="/live.liveplay.BirthParty/applyBirthParty")
    def apply_birth_party(self, uid=None, date=None):
        """### 生日会申请"""

    @grpc_call(path="/live.liveplay.BirthParty/getBirthParty")
    def get_birth_party(self, uid=None):
        """### 获取生日会详情"""

    @grpc_call(path="/live.liveplay.BirthParty/getBirthAnchorByDay")
    def get_birth_anchor_by_day(self, birthday=None):
        """### 按日期提供生日主播uid"""

    @grpc_call(path="/live.liveplay.BirthParty/getBirthList")
    def get_birth_list(self, uid=None, start_apply_date=None, end_apply_date=None, page_size=None, page=None):
        """### 生日会列表获取"""

    @grpc_call(path="/live.liveplay.BirthParty/updateBirth")
    def update_birth(self, id=None, uid=None, birthday=None, birth_push=None, is_delete=None):
        """### 生日会信息更新"""

    @grpc_call(path="/live.liveplay.BirthParty/exportBirth")
    def export_birth(self, uid=None, start_apply_date=None, end_apply_date=None):
        """### 生成导出列表"""

    @grpc_call(path="/live.liveplay.BirthParty/applyToday")
    def apply_today(self, uid, date, operator):
        """### 后台紧急申请当天生日会"""

    @grpc_call(path="/live.liveplay.FloatScResource/AddResource")
    def add_resource(self, title, left_color, right_color, type=None, face_background=None, tail_background=None):
        """### 新增飘屏资源"""

    @grpc_call(path="/live.liveplay.FloatScResource/GetResourceDetail")
    def get_resource_detail(self, id):
        """### 取飘屏资源详情"""

    @grpc_call(path="/live.liveplay.MessageWall/GetMsgList")
    def get_msg_list(self, page, page_size, act_id, start_time, end_time, ruid=None):
        """###获取消息列表"""

    @grpc_call(path="/live.liveplay.MessageWall/UpOrDownMsg")
    def up_or_down_msg(self, id=None, status=None):
        """###更新上下线状态"""

    @grpc_call(path="/live.liveplay.MessageWall/BatchPublishMsg")
    def batch_publish_msg(self, act_id, start_time, end_time, force_pub=None):
        """###批量发布留言"""

    @grpc_call(path="/live.liveplay.MessageWall/SendMessage")
    def send_message(self, ruid=None, uid=None, message=None, coin=None, act_id=None, room_id=None):
        """### 发送留言"""

    @grpc_call(path="/live.liveplay.MessageWall/GetMessage")
    def get_message(self, act_id=None):
        """### 获取留言"""

    @grpc_call(path="/live.liveplay.MessageWall/GetScore")
    def get_score(self, uid=None, ruid=None, act_id=None):
        """### 获取福气值个数"""

    @grpc_call(path="/live.liveplay.MessageWall/GetMessagesByCondition")
    def get_messages_by_condition(self, act_id, ruid, uid, start_time, end_time):
        """### 指定条件查主播所有的留言"""

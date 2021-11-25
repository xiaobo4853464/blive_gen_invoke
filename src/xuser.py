from tiny import grpc_call

class Xuser(object):
    def __init__(self,service_name):
        self.service_name=service_name
    
    @grpc_call(path="/live.xuser.v1.Guard/Buy")
    def buy(self, order_id, uid, ruid, guard_level, num, platform, source):
        """### deprecated: 已废弃，请用/live.xuser.v2.Guard/Buy"""

    @grpc_call(path="/live.xuser.v1.Guard/GetByUIDTargetID")
    def get_by_u_i_d_target_i_d(self, uid, target_id, sort_type=None):
        """### GetByUIDTargetID 获取【用户态uid】与【主播态uid】守护关系, sort_type=0 返回最高等级,默认返回最高等级"""

    @grpc_call(path="/live.xuser.v1.Guard/GetByTargetIdsBatch")
    def get_by_target_ids_batch(self, target_ids, sort_type=None):
        """### deprecated: 已废弃, 批量查询多个主播大航海数据操作无实际使用且无意义,还容易弄垮服务"""

    @grpc_call(path="/live.xuser.v1.Guard/GetByUIDForGift")
    def get_by_u_i_d_for_gift(self, uid):
        """### GetByUID 获取【用户态uid】所有的最高级一个守护,不支持批量(P0级)"""

    @grpc_call(path="/live.xuser.v1.Guard/GetByUIDBatch")
    def get_by_u_i_d_batch(self, uids):
        """### GetByUIDBatch 根据【用户态uids】获取【用户态】所有的守护,支持批量(P2级)"""

    @grpc_call(path="/live.xuser.v1.Guard/GetPeakByUIDBatch")
    def get_peak_by_u_i_d_batch(self, uids):
        """### deprecated: 已废弃，目前已经没有量使用,若需要请于服务方确认使用场景再开启"""

    @grpc_call(path="/live.xuser.v1.Guard/GetAnchorRecentTopGuard")
    def get_anchor_recent_top_guard(self, uid):
        """### GetAnchorRecentTopGuard 获取最近的总督弹窗提醒"""

    @grpc_call(path="/live.xuser.v1.Guard/GetTopListGuard")
    def get_top_list_guard(self, targetid):
        """### GetTopListGuard 获取【主播态uid】某个up主的守护排行榜"""

    @grpc_call(path="/live.xuser.v1.Guard/GetTopListGuardV2")
    def get_top_list_guard_v2(self, targetid):
        """### GetTopListGuardV2 获取【主播态uid】某个up主的守护排行榜 粉丝勋章三期新接口"""

    @grpc_call(path="/live.xuser.v1.Guard/GetGuardNumByUIDs")
    def get_guard_num_by_u_i_ds(self, uids):
        """### deprecated: 已废弃，请用/live.xuser.v1.Guard/BatchGetAnchorGuardAbstract"""

    @grpc_call(path="/live.xuser.v1.Guard/GetPeakByTargetidUids")
    def get_peak_by_targetid_uids(self, targetid, uids, read_lru_cache=None):
        """###GetPeakByTargetidUids() 获取【主播态uid】的多位【用户态uids】守护者的最高守护等级"""

    @grpc_call(path="/live.xuser.v1.Guard/ClearUIDCache")
    def clear_u_i_d_cache(self, uid, magic_key):
        """### ClearUIDCache 清除【用户态uid】cache"""

    @grpc_call(path="/live.xuser.v1.Guard/GetByUIDTargetIDGuards")
    def get_by_u_i_d_target_i_d_guards(self, uid, target_id, include_expired=None):
        """###GetByUIDTargetIDGuards 获取【用户态uid】对应【主播态uid】的所有守护信息"""

    @grpc_call(path="/live.xuser.v1.Guard/GetBuyedGuards")
    def get_buyed_guards(self, uid, page=None, pagesize=None):
        """###获取用户所有购买过的大航海列表,如果有房间正在生效,那么该房间优先展示,如果有多个房间有生效的,那么最先结束的优先展示,如果无房间正在生效,那么最近失效的优先展示"""

    @grpc_call(path="/live.xuser.v1.Guard/GetAllGuardsByUID")
    def get_all_guards_by_u_i_d(self, uid):
        """### 根据【用户态uid】获取全部守护列表,web直播中心使用"""

    @grpc_call(path="/live.xuser.v1.Guard/GetFollowTimeByUidTargetId")
    def get_follow_time_by_uid_target_id(self, uid, target_id):
        """### 根据【用户态uid targetId】陪伴时间"""

    @grpc_call(path="/live.xuser.v1.Guard/IsWeeklyGuard")
    def is_weekly_guard(self, level, sub_level=None):
        """### 判断是否周舰长"""

    @grpc_call(path="/live.xuser.v1.Guard/GetPeakByTargetidUidsV2")
    def get_peak_by_targetid_uids_v2(self, targetid, uids):
        """###GetPeakByTargetidUidsV2 获取【用户态uids】对【主播态uid】大航海守护信息"""

    @grpc_call(path="/live.xuser.v1.Guard/GetTopListGuardAttr")
    def get_top_list_guard_attr(self, targetid, sort_attr, page, page_size=None):
        """###GetTopList 获取【主播态】所有的大航海守护信息，按照特定的排序逻辑"""

    @grpc_call(path="/live.xuser.v1.Guard/BatchGetAnchorGuardAbstract")
    def batch_get_anchor_guard_abstract(self, ruids=None):
        """### BatchGetAnchorGuardAbstract 批量主播获取大航海摘要统计信息"""

    @grpc_call(path="/live.xuser.v1.Guard/GetAppNote")
    def get_app_note(self, uid):
        """### GetAppNote 获取app首页提示信息"""

    @grpc_call(path="/live.xuser.v1.Guard/GetAppNoteV2")
    def get_app_note_v2(self, uid=None, abtest=None):
        """### GetAppNoteV2 获取app首页提示信息"""

    @grpc_call(path="/live.xuser.v1.Guard/GuardCardRefresh")
    def guard_card_refresh(self, uid=None):
        """### 刷新app首页提示信息"""

    @grpc_call(path="/live.xuser.v1.Guard/RefreshCache")
    def refresh_cache(self, target_id, uid=None):
        """### 主动刷新缓存 xuser-job 使用"""

    @grpc_call(path="/live.xuser.v1.Guard/GetGuardWarn")
    def get_guard_warn(self, target_id):
        """### GetGuardWarn 获取大航海告警"""

    @grpc_call(path="/live.xuser.v1.Guard/GetGuardWarnList")
    def get_guard_warn_list(self, target_id, type, page=None, page_size=None, not_need_user=None):
        """### GetGuardWarnList 获取大航海告警列表"""

    @grpc_call(path="/live.xuser.v1.Guard/GetTargetGuardNum")
    def get_target_guard_num(self, ruid=None):
        """### 新版主播大航海人数接口"""

    @grpc_call(path="/live.xuser.v1.Guard/GetPersonalDress")
    def get_personal_dress(self, ruid=None, guard_level=None):
        """### 获取大航海装扮定制装扮配置"""

    @grpc_call(path="/live.xuser.v1.Guard/RemoveFromGuardTop")
    def remove_from_guard_top(self, uid=None, room_id=None, ruid=None):
        """### 大航海剔除榜单"""

    @grpc_call(path="/live.xuser.v1.userData/GetUserData")
    def get_user_data(self, uid, roomid=None, targetid=None, attrs=None, all_guards=None):
        """### 获取用户核心数据支持的标签有：info：用户基本信息，主要是一些主站数据；exp:用户经验的信息；vip:用户的姥爷信息,guard:用户的大航海信息,"""

    @grpc_call(path="/live.xuser.v1.userData/GetUserDataRiskControl")
    def get_user_data_risk_control(self, uid, roomid=None, targetid=None, attrs=None, all_guards=None):
        """### 接入直播间风控(头像/昵称)"""

    @grpc_call(path="/live.xuser.v1.userData/GetUserDataMultiRiskControl")
    def get_user_data_multi_risk_control(self, uids, attrs, target_id=None, room_id=None):
        """### 接入直播间风控(头像/昵称)批量"""

    @grpc_call(path="/live.xuser.v1.userData/GetMultiUserData")
    def get_multi_user_data(self, uids, target_id=None, room_id=None):
        """### TODO 切换完成后，下线该接口"""

    @grpc_call(path="/live.xuser.v1.userData/GetUserDataMulti")
    def get_user_data_multi(self, uids, attrs, target_id=None, room_id=None):
        """### 根据attr批量获取用户信息"""

    @grpc_call(path="/live.xuser.v1.UserExp/GetUserExp")
    def get_user_exp(self, uids):
        """### GetUserExpMulti 获取用户经验与等级信息,支持批量"""

    @grpc_call(path="/live.xuser.v1.lpl/GetLplIdentity")
    def get_lpl_identity(self, uid):
        """###获取用户身份"""

    @grpc_call(path="/live.xuser.v1.lpl/LplBind")
    def lpl_bind(self, uid):
        """###绑定lpl"""

    @grpc_call(path="/live.xuser.v1.lpl/LplGetToken")
    def lpl_get_token(self, uid, ignore_bind_status=None):
        """###获取lpl的token"""

    @grpc_call(path="/live.xuser.v1.lpl/LplGetLogStatus")
    def lpl_get_log_status(self, uid, orderid):
        """###查询订单流水状态"""

    @grpc_call(path="/live.xuser.v1.lpl/FixSyncAccountData")
    def fix_sync_account_data(self, uid):
        """###修数据使用的接口,其他服务谨慎调用"""

    @grpc_call(path="/live.xuser.v1.RoomAdmin/is_any")
    def is_any(self, uid):
        """### 根据登录态获取功能入口是否显示, 需要登录态"""

    @grpc_call(path="/live.xuser.v1.RoomAdmin/get_by_uid")
    def get_by_uid(self, uid, page=None):
        """### 获取用户拥有的的所有房管身份"""

    @grpc_call(path="/live.xuser.v1.RoomAdmin/resign")
    def resign(self, roomid, uid, mobile_app=None):
        """### 辞职房管"""

    @grpc_call(path="/live.xuser.v1.RoomAdmin/search_for_admin")
    def search_for_admin(self, uid, key_word):
        """### 查询需要添加的房管"""

    @grpc_call(path="/live.xuser.v1.RoomAdmin/get_by_anchor")
    def get_by_anchor(self, uid, page=None):
        """### 获取主播拥有的的所有房管"""

    @grpc_call(path="/live.xuser.v1.RoomAdmin/get_by_room")
    def get_by_room(self, roomid):
        """### 获取主播拥有的的所有房管,房间号维度"""

    @grpc_call(path="/live.xuser.v1.RoomAdmin/dismiss")
    def dismiss(self, uid, anchor_id, mobile_app=None):
        """### 撤销房管"""

    @grpc_call(path="/live.xuser.v1.RoomAdmin/appoint")
    def appoint(self, uid, anchor_id, mobile_app=None):
        """### 任命房管"""

    @grpc_call(path="/live.xuser.v1.RoomAdmin/is_admin")
    def is_admin(self, uid, anchor_id, roomid):
        """### 是否房管"""

    @grpc_call(path="/live.xuser.v1.RoomAdmin/is_admin_short")
    def is_admin_short(self, uid, roomid):
        """### 是否房管, 不额外返回用户信息, 不判断是否主播自己"""

    @grpc_call(path="/live.xuser.v1.RoomAdmin/are_admin_short")
    def are_admin_short(self, uids, roomid):
        """### 批量接口，是否房管, 不额外返回用户信息, 不判断是否主播自己"""

    @grpc_call(path="/live.xuser.v1.Account/UnameToUID")
    def uname_to_u_i_d(self, uname):
        """### 用户名称转用户uid"""

    @grpc_call(path="/live.xuser.v1.Account/AuditStatus")
    def audit_status(self, uid):
        """### 用户信息是否在审核中"""

    @grpc_call(path="/live.xuser.v1.Account/UserInfo")
    def user_info(self, mid):
        """### 获取用户信息"""

    @grpc_call(path="/live.xuser.v1.Account/UserInfoBatch")
    def user_info_batch(self, mids=None):
        """### TODO 批量获取用户信息"""

    @grpc_call(path="/live.xuser.v1.Account/MIDToOpenID")
    def m_i_d_to_open_i_d(self, mid):
        """### mid转openid"""

    @grpc_call(path="/live.xuser.v1.Account/OpenIDToMID")
    def open_i_d_to_m_i_d(self, openID):
        """### openid转mid"""

    @grpc_call(path="/live.xuser.v1.InternalRoom/List")
    def list(self, room_id=None):
        """### (mlive后台)房间列表"""

    @grpc_call(path="/live.xuser.v1.InternalRoom/Edit")
    def edit(self, id, room_id, watch_platform, start_time, end_time, watch_ip_limit=None, multi_device_limit=None, departments=None, uid_white_list=None, name_white_list=None, code_limit=None):
        """### (mlive后台)编辑房间"""

    @grpc_call(path="/live.xuser.v1.InternalRoom/Create")
    def create(self, room_id, watch_platform, start_time, end_time, watch_ip_limit=None, multi_device_limit=None, departments=None, uid_white_list=None, name_white_list=None, code_limit=None):
        """### (mlive后台)创建房间"""

    @grpc_call(path="/live.xuser.v1.InternalRoom/Delete")
    def delete(self, id):
        """### (mlive后台)删除房间"""

    @grpc_call(path="/live.xuser.v1.InternalRoom/QuickWord")
    def quick_word(self, share_id=None, oid=None, buvid=None, platform=None, share_channel=None, spm_id=None, panel_type=None, share_session_id=None, object_extra_fields=None):
        """### 无标题"""

    @grpc_call(path="/live.xuser.v1.InternalRoom/ValidList")
    def valid_list(self, session_id):
        """### 给企微里H5调用,获取用户允许访问的房间列表"""

    @grpc_call(path="/live.xuser.v1.InternalRoom/Bind")
    def bind(self, uid, room_id, token=None):
        """### 生成live_token"""

    @grpc_call(path="/live.xuser.v1.InternalRoom/Auth")
    def auth(self, uid=None, live_token=None, room_id=None, ruid=None, platform=None, ip=None, buvid=None):
        """### 鉴权"""

    @grpc_call(path="/live.xuser.v1.Bind/SmsCode")
    def sms_code(self, game_type, phone):
        """### 通过手机号发送验证码"""

    @grpc_call(path="/live.xuser.v1.Bind/SmsLogin")
    def sms_login(self, game_type, phone, code):
        """### 通过手机号码与验证码登录并获取用户mid"""

    @grpc_call(path="/live.xuser.v1.Bind/UserInfoByOpenID")
    def user_info_by_open_i_d(self, game_type, openID):
        """### 通过openid 查询用户信息"""

    @grpc_call(path="/live.xuser.v1.Bind/GetGameRoleByMID")
    def get_game_role_by_m_i_d(self, game_type, mid):
        """### 通过mid查询游戏角色"""

    @grpc_call(path="/live.xuser.v1.Bind/AcceptAgreement")
    def accept_agreement(self, mid=None):
        """### 同意协议"""

    @grpc_call(path="/live.xuser.v1.Bind/JumpWxConfig")
    def jump_wx_config(self, game_type, mid=None):
        """### 跳转微信绑定方式地址下发"""

    @grpc_call(path="/live.xuser.v1.Bind/WxHandler")
    def wx_handler(self, game_type, mid=None):
        """### 获取跳转微信绑定qq小程序相关信息"""

    @grpc_call(path="/live.xuser.v1.Bind/WxH5Handler")
    def wx_h5_handler(self, game_type, mid=None):
        """### 获取跳转微信绑定H5相关信息"""

    @grpc_call(path="/live.xuser.v1.Bind/LiveTencentGameBindInfo")
    def live_tencent_game_bind_info(self, mid, actid=None, game_id=None):
        """### 查询游戏角色信息接口, 账号组收口tx游戏绑定查询"""

    @grpc_call(path="/live.xuser.v1.Vip/Info")
    def info(self, uid):
        """### Info 返回用户vip信息"""

    @grpc_call(path="/live.xuser.v1.Vip/Buy")
    def buy(self, order_id, uid, good_id, good_num, platform, source):
        """### Buy 购买月费/年费姥爷"""

    @grpc_call(path="/live.xuser.v1.Vip/Infos")
    def infos(self, uids):
        """### Infos 批量返回用户vip信息(最多50 uids)"""

    @grpc_call(path="/live.xuser.v2.Guard/PreBuy")
    def pre_buy(self, uid, ruid, guard_level, num, platform, price, discount_price, sub_level=None, build=None, mobi_app=None, auto_renew_price=None, buy_type=None):
        """### PreBuy 购买预检 ios 5.30版本以前 及 蓝版 不打折 从pay迁移而来..."""

    @grpc_call(path="/live.xuser.v2.Guard/Buy")
    def buy(self, order_id, uid, ruid, guard_level, num, platform, sub_level=None, source=None, coin=None, original_coin=None, goods_id=None, extra_info=None):
        """### Buy 购买大航海"""

    @grpc_call(path="/live.xuser.v2.Guard/GuardRecycle")
    def guard_recycle(self, order_id, uid, ruid, guard_level, num, platform, sub_level=None, source=None, coin=None, original_coin=None, goods_id=None, extra_info=None):
        """### 大航海身份回收逻辑"""

    @grpc_call(path="/live.xuser.v2.Guard/GuardChange")
    def guard_change(self, uid=None, ruid=None, total_mariner=None, change_time=None):
        """### 大航海数量变更"""

    @grpc_call(path="/live.xuser.v2.Guard/AddGuardDress")
    def add_guard_dress(self, uid=None):
        """### 根据uid发放对应主站套装"""

    @grpc_call(path="/live.xuser.v2.bind.Bind/GetGameRoleByMID")
    def get_game_role_by_m_i_d(self, act_id, game_id, mid):
        """### 通过mid查询游戏角色"""

    @grpc_call(path="/live.xuser.v2.bind.Bind/JumpWxConfig")
    def jump_wx_config(self, act_id, game_id, mid):
        """### 跳转微信绑定方式地址下发"""

    @grpc_call(path="/live.xuser.v2.bind.Bind/WxHandler")
    def wx_handler(self, act_id, game_id, mid):
        """### 获取跳转微信绑定qq小程序相关信息"""

    @grpc_call(path="/live.xuser.v2.bind.Bind/WxH5Handler")
    def wx_h5_handler(self, act_id, game_id, mid):
        """### 获取跳转微信绑定H5相关信息"""

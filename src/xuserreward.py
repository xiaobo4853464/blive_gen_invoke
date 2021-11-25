from tiny import grpc_call

class Xuserreward(object):
    def __init__(self,service_name):
        self.service_name=service_name
    
    @grpc_call(path="/live.xuserreward.v1.AchieveManage/GetList")
    def get_list(self, id=None, title=None, category=None, subject=None, is_legend=None, page=None, page_size=None):
        """###*"""

    @grpc_call(path="/live.xuserreward.v1.AchieveManage/Add")
    def add(self, title=None, is_legend=None, descript=None, legend_descript=None, reward_style=None, achieve=None, legend_achieve=None, icon=None, condition=None, process_max=None, category=None, subject=None, auto_recv=None, sort=None, status=None):
        """###*"""

    @grpc_call(path="/live.xuserreward.v1.AchieveManage/Edit")
    def edit(self, id=None, title=None, is_legend=None, descript=None, achieve=None, reward_id=None, icon=None, condition=None, process_max=None, category=None, subject=None, auto_recv=None, sort=None, legend_descript=None, legend_achieve=None):
        """###*"""

    @grpc_call(path="/live.xuserreward.v1.AchieveManage/EditStatus")
    def edit_status(self, id=None, status=None):
        """###*"""

    @grpc_call(path="/live.xuserreward.v1.AchieveManage/SetReward")
    def set_reward(self, id=None, reward_id=None, reward_style=None, rewardsinfo=None):
        """###*"""

    @grpc_call(path="/live.xuserreward.v1.AchieveManage/GetReward")
    def get_reward(self, id=None, reward_id=None):
        """###*"""

    @grpc_call(path="/live.xuserreward.v1.BrandRoomAdmin/RoomAdd")
    def room_add(self, room_id, operator, comment=None):
        """### 添加房间白名单"""

    @grpc_call(path="/live.xuserreward.v1.BrandRoomAdmin/RoomList")
    def room_list(self, pn, ps, room_id=None):
        """### 房间查询"""

    @grpc_call(path="/live.xuserreward.v1.BrandRoomAdmin/RoomDel")
    def room_del(self, id):
        """### 删除房间白名单"""

    @grpc_call(path="/live.xuserreward.v1.BrandRoomAdmin/RoomBind")
    def room_bind(self, bind_id=None, room_id=None, card_id=None, start_time=None, end_time=None, status=None):
        """### 关联/解除关联"""

    @grpc_call(path="/live.xuserreward.v1.BrandRoomAdmin/GetRoomBind")
    def get_room_bind(self, room_id):
        """### 关联信息"""

    @grpc_call(path="/live.xuserreward.v1.BrandRoomAdmin/CardAdd")
    def card_add(self, name, icon_id, url, style, type, img, title=None, sub_title=None, btn_name=None):
        """### 新增组件"""

    @grpc_call(path="/live.xuserreward.v1.BrandRoomAdmin/CardCheck")
    def card_check(self, name):
        """### 组件检测"""

    @grpc_call(path="/live.xuserreward.v1.BrandRoomAdmin/CardList")
    def card_list(self, pn, ps, name=None):
        """### 组件查询"""

    @grpc_call(path="/live.xuserreward.v1.BrandRoomAdmin/CardEnable")
    def card_enable(self, id, status=None):
        """### 组件禁用0、启用1"""

    @grpc_call(path="/live.xuserreward.v1.BrandRoomAdmin/IconAdd")
    def icon_add(self, name, icon_url, status=None):
        """### 新增icon"""

    @grpc_call(path="/live.xuserreward.v1.BrandRoomAdmin/IconList")
    def icon_list(self, pn=None, ps=None, enable_status=None):
        """### icon列表 enable_status为1时，拉全部启用状态的icon"""

    @grpc_call(path="/live.xuserreward.v1.BrandRoomAdmin/IconEnable")
    def icon_enable(self, id, status=None):
        """### 禁用icon-0、启用-1"""

    @grpc_call(path="/live.xuserreward.EmoticonUploadAdmin/GetEmoticonList")
    def get_emoticon_list(self, type, page_index, page_size, start_time=None, end_time=None, room_id=None):
        """### 查看表情包审核列表"""

    @grpc_call(path="/live.xuserreward.EmoticonUploadAdmin/EmoticonOperation")
    def emoticon_operation(self, type, unique_id, opt_id, user_id, room_id, reason=None):
        """### 表情包通过/驳回"""

    @grpc_call(path="/live.xuserreward.EntryEffect/TrigerEntry")
    def triger_entry(self, uid, target_id, room_id, uname, face, privilege_type=None, privilege_switch=None, isadmin=None, vip=None, svip=None, vip_switch=None, medal_target_id=None, medal_level=None, medal_name=None, medal_color=None, medal_color_start=None, medal_color_end=None, medal_color_border=None, is_lighted=None, guard_level=None, special=None, icon_id=None, gold_rank=None, score=None, trigger_time=None, **from_):
        """### TrigerEntry 用户进房间,会触发横幅进场特效广播和互动区文字进场广播"""

    @grpc_call(path="/live.xuserreward.EntryEffect/TrigerEffect")
    def triger_effect(self, uid, target_id, room_id, privilege_type=None, privilege_switch=None, uname=None, face=None, gold_rank=None, trigger_time=None):
        """### TrigerEffect 单独触发用户横幅进长特效广播"""

    @grpc_call(path="/live.xuserreward.EntryEffect/TrigerWelcome")
    def triger_welcome(self, uid, roomid, ip=None, is_spread=None, spread_info=None, spread_desc=None):
        """### TrigerWelcome 单独触发用户互动区文字进场广播"""

    @grpc_call(path="/live.xuserreward.EntryEffect/TrigerFollow")
    def triger_follow(self, uid, roomid, ip=None):
        """### TrigerFollow 单独触发用户关注广播"""

    @grpc_call(path="/live.xuserreward.EntryEffect/TrigerShare")
    def triger_share(self, uid, roomid, ip=None):
        """### TrigerShare 单独触发用户分享广播"""

    @grpc_call(path="/live.xuserreward.EntryEffect/SaveEffect")
    def save_effect(self, id=None, title=None, copy_writing=None, copy_color=None, highlight_color=None, priority=None, silence_time=None, status=None, business=None, basemap_url=None, show_avatar=None, effective_time=None, web_basemap_url=None, web_effective_time=None, web_effect_close=None, web_close_time=None, comment=None):
        """### SaveEffect 后台-创建/编辑特效，以id是否为0判断是新增还是更新"""

    @grpc_call(path="/live.xuserreward.EntryEffect/EffectList")
    def effect_list(self, page=None, page_size=None):
        """### EffectList 后台-特效列表"""

    @grpc_call(path="/live.xuserreward.EntryEffect/EffectDetail")
    def effect_detail(self, id):
        """### EffectDetail 后台-特效详情"""

    @grpc_call(path="/live.xuserreward.EntryEffect/SetEffectStatus")
    def set_effect_status(self, id, status=None):
        """### SetEffectStatus 后台-特效设置状态"""

    @grpc_call(path="/live.xuserreward.EntryEffect/DeleteEffect")
    def delete_effect(self, id):
        """### DeleteEffect 后台-删除未上线特效"""

    @grpc_call(path="/live.xuserreward.EntryEffect/RemoveUserCache")
    def remove_user_cache(self, uid):
        """### 清除用户缓存"""

    @grpc_call(path="/live.xuserreward.EntryEffect/RemoveEffectCache")
    def remove_effect_cache(self, effect_id):
        """### 清除进场特效详细信息缓存"""

    @grpc_call(path="/live.xuserreward.Sign/DoSign")
    def do_sign(self, uid=None, user_ip=None, platform=None, build=None, buvid=None, userAgent=None, referer=None):
        """###web和新版app的签到"""

    @grpc_call(path="/live.xuserreward.Sign/GetLastMonthSignInfo")
    def get_last_month_sign_info(self, uid=None, stype=None):
        """###获取上个月的签到信息"""

    @grpc_call(path="/live.xuserreward.Sign/WebGetSignInfo")
    def web_get_sign_info(self, uid=None, stype=None):
        """###web端获取当月签到信息"""

    @grpc_call(path="/live.xuserreward.Sign/AppGetSignInfo")
    def app_get_sign_info(self, uid=None, stype=None):
        """###app端获取当月签到信息"""

    @grpc_call(path="/live.xuserreward.Sign/Statistic")
    def statistic(self, uid=None, ctype=None):
        """###获取签到统计信息"""

    @grpc_call(path="/live.xuserreward.Sign/ClearUserCache")
    def clear_user_cache(self, uid, year=None, month=None):
        """###清除用户缓存,用于手动修复用户脏缓存"""

    @grpc_call(path="/live.xuserreward.Sign/PlugSign")
    def plug_sign(self, uid, year=None, month=None, day=None):
        """###补签"""

    @grpc_call(path="/live.xuserreward.Sign/PlugSignReward")
    def plug_sign_reward(self, uid, vip=None, special_day=None, total_sign=None, series_sign=None, year=None, month=None, day=None):
        """###补发签到奖励"""

    @grpc_call(path="/live.xuserreward.Sign/UserSignInfo")
    def user_sign_info(self, uid, year=None, month=None):
        """###后台查询用户签到日期"""

    @grpc_call(path="/live.xuserreward.v1.Achievement/GetUserStatus")
    def get_user_status(self, uid=None):
        """### 用户成就统计"""

    @grpc_call(path="/live.xuserreward.v1.Achievement/GetAchievementList")
    def get_achievement_list(self, uid=None, type=None, status=None, category=None, keywords=None, page=None, pageSize=None):
        """### 获取用户成就列表"""

    @grpc_call(path="/live.xuserreward.v1.Achievement/AchievementReceive")
    def achievement_receive(self, uid=None, aid=None):
        """### 领取成就奖励"""

    @grpc_call(path="/live.xuserreward.v1.Achievement/AchievementAdd")
    def achievement_add(self, uid=None, aid=None):
        """### 添加用户成就"""

    @grpc_call(path="/live.xuserreward.Emoticon/GetEmoticons")
    def get_emoticons(self, uid=None, room_id=None):
        """### 获取用户表情包列表"""

    @grpc_call(path="/live.xuserreward.Emoticon/GetHotEmoticon")
    def get_hot_emoticon(self, uid=None):
        """### 获取热门的引导表情包"""

    @grpc_call(path="/live.xuserreward.Emoticon/SendDmEmoticonCheckAuth")
    def send_dm_emoticon_check_auth(self, uid=None, room_id=None, emoticon_unique=None, emoticon_id=None):
        """### 发送弹幕表情包权限校验【发送弹幕时专用】"""

    @grpc_call(path="/live.xuserreward.Emoticon/GetEmoticonsNew")
    def get_emoticons_new(self, uid=None, room_id=None):
        """### 获取用户表情包列表(新版web-ucenterv2使用)"""

    @grpc_call(path="/live.xuserreward.Emoticon/SetAnchorEmoticonGuideStep")
    def set_anchor_emoticon_guide_step(self, step, uid):
        """### 设置主播表情包引导步骤(to web-ucenter)"""

    @grpc_call(path="/live.xuserreward.Emoticon/GetAnchorEmoticonGuideStep")
    def get_anchor_emoticon_guide_step(self, uid):
        """### 获取主播表情包引导步骤(to web-ucenter)"""

    @grpc_call(path="/live.xuserreward.Emoticon/GetEmoticonJurisdiction")
    def get_emoticon_jurisdiction(self, jurisdiction_type=None, upload_type=None, uid=None):
        """### 获得表情包相关权限(to web-ucenter & 内部调用)"""

    @grpc_call(path="/live.xuserreward.Emoticon/GetAnchorEmoticionsList")
    def get_anchor_emoticions_list(self, uid=None, support_type=None):
        """### 获取主播表情包列表"""

    @grpc_call(path="/live.xuserreward.Emoticon/InsertAnchorEmoticions")
    def insert_anchor_emoticions(self, uid=None, emoji=None, icon=None, emoticon_view=None, descript=None, type=None, is_dynamic=None, in_player_area=None, width=None, height=None, level_limit=None, is_free=None, identity=None, sort=None, have_pkg=None):
        """### 上传主播表情"""

    @grpc_call(path="/live.xuserreward.Emoticon/PublishEmoticon")
    def publish_emoticon(self, uid=None, room_id=None):
        """### 发布表情包(to web-ucenter)"""

    @grpc_call(path="/live.xuserreward.Emoticon/DeleteAnchorEmoticon")
    def delete_anchor_emoticon(self, emoticon_id=None, room_id=None, uid=None):
        """### 删除主播表情包"""

    @grpc_call(path="/live.xuserreward.Emoticon/UpdatePkgInfo")
    def update_pkg_info(self, update_type, emoticon_id, emoticon_view=None, emoji=None, level=None, uid=None):
        """### 变更表情包封面/名称/等级"""

    @grpc_call(path="/live.xuserreward.Emoticon/PrivateDomainAuthentication")
    def private_domain_authentication(self, uid):
        """### UP主私域表情包功能制作权限"""

    @grpc_call(path="/live.xuserreward.Emoticon/PrivateDomainEmoticonList")
    def private_domain_emoticon_list(self, uid, target_id):
        """### 获取用户对应UP主私域表情包列表"""

    @grpc_call(path="/live.xuserreward.Emoticon/PrivateDomainEmoticonAuthentication")
    def private_domain_emoticon_authentication(self, uid, target_id, emoticon_unique):
        """### UP主私域表情鉴权"""

    @grpc_call(path="/live.xuserreward.Emoticon/PrivateDomainEmoticonListByTargetId")
    def private_domain_emoticon_list_by_target_id(self, uid):
        """### 获取up主对应的全部表情包"""

    @grpc_call(path="/live.xuserreward.Emoticon/PrivateDomainEmoticonPublish")
    def private_domain_emoticon_publish(self, uid):
        """### UP主发布表情包"""

    @grpc_call(path="/live.xuserreward.Emoticon/PrivateDomainDeleteEmoticon")
    def private_domain_delete_emoticon(self, uid, emoticon_unique=None):
        """### UP主删除表情"""

    @grpc_call(path="/live.xuserreward.Emoticon/PrivateDomainUpdateEmoticonPkgInfo")
    def private_domain_update_emoticon_pkg_info(self, uid, action_type=None, emoticon_view=None, off_line_reason=None):
        """### 变更表情包封面/表情包上下线"""

    @grpc_call(path="/live.xuserreward.UserRenewCard/add")
    def add(self, card_id, uid, expire_time, num, source):
        """### 给用户添加续期卡"""

    @grpc_call(path="/live.xuserreward.UserRenewCard/getByUid")
    def get_by_uid(self, uid):
        """### 根据uid获取道具列表"""

    @grpc_call(path="/live.xuserreward.UserRenewCard/use")
    def use(self, card_record_id, title_id, uid, num=None):
        """### 使用续期卡"""

    @grpc_call(path="/live.xuserreward.UserRenewCard/send")
    def send(self, card_record_id, send_uid, recv_uid, num=None):
        """### 转赠续期卡"""

    @grpc_call(path="/live.xuserreward.UserRenewCard/logs")
    def logs(self, uid, page=None):
        """### 日志"""

    @grpc_call(path="/live.xuserreward.TitleRenewCard/add")
    def add(self, name, duration, img_url, operator):
        """### 添加头衔续期卡"""

    @grpc_call(path="/live.xuserreward.TitleRenewCard/edit")
    def edit(self, img_url, id, operator, name=None, duration=None):
        """### 编辑头衔续期卡"""

    @grpc_call(path="/live.xuserreward.TitleRenewCard/list")
    def list(self, page=None, page_size=None):
        """### 列表"""

    @grpc_call(path="/live.xuserreward.TitleRenewCard/get")
    def get(self, id):
        """### 获取指定id信息"""

    @grpc_call(path="/live.xuserreward.Title/GetWearingTitle")
    def get_wearing_title(self, uid=None):
        """### 获取当前用户佩戴头衔信息"""

    @grpc_call(path="/live.xuserreward.Title/WearTitle")
    def wear_title(self, uid=None, tid=None, cid=None, title=None):
        """### 佩戴头衔"""

    @grpc_call(path="/live.xuserreward.Title/CancelTitle")
    def cancel_title(self, uid=None):
        """### 取消头衔佩戴"""

    @grpc_call(path="/live.xuserreward.Title/GetUserTitleList")
    def get_user_title_list(self, uid=None, normal=None, keyword=None, had=None, special=None, page=None, page_size=None):
        """### 获取用户头衔列表"""

    @grpc_call(path="/live.xuserreward.Title/GetUserLightTitle")
    def get_user_light_title(self, uid=None):
        """### 获取用户新获得头衔点亮列表"""

    @grpc_call(path="/live.xuserreward.Title/GetUserCardTitle")
    def get_user_card_title(self, uid):
        """### 获取用户用户卡配置的头衔信息【旧】【用于旧版直播间头衔墙、用户卡】"""

    @grpc_call(path="/live.xuserreward.Title/ClearLightTitle")
    def clear_light_title(self, uid=None):
        """### 用户看过新获得点亮头衔 清理redis 缓存"""

    @grpc_call(path="/live.xuserreward.Title/GetUserShowTitle")
    def get_user_show_title(self, uid=None):
        """### 获取用户对外展示头衔【区别于互动区：1、互动区展示的 2、用户卡第一位】"""

    @grpc_call(path="/live.xuserreward.Title/AddScore")
    def add_score(self, uid=None, title_id=None, score=None, is_make=None):
        """### 增加头衔积分【不要使用】"""

    @grpc_call(path="/live.xuserreward.Title/GetUserTitleAll")
    def get_user_title_all(self, uid=None, need_title_info=None):
        """### 获取用户拥有的全量头衔信息"""

    @grpc_call(path="/live.xuserreward.Title/GetUserCardTitleNew")
    def get_user_card_title_new(self, uid):
        """### 获取用户用户卡配置的头衔信息【新】【用于新版直播间头衔墙、用户卡】"""

    @grpc_call(path="/live.xuserreward.PropMailbox/list")
    def list(self, uid, page=None, page_size=None):
        """### 邮箱列表"""

    @grpc_call(path="/live.xuserreward.PropMailbox/use")
    def use(self, uid=None, mail_id=None):
        """### 领取"""

    @grpc_call(path="/live.xuserreward.PropMailbox/del")
    def del_(self, uid, mail_id=None):
        """### 删除"""

    @grpc_call(path="/live.xuserreward.PropMailbox/rebuildListCache")
    def rebuild_list_cache(self, uid):
        """### 重建信箱缓存"""

    @grpc_call(path="/live.xuserreward.TitleAdmin/DelSub")
    def del_sub(self, id=None):
        """### 删除子头衔"""

    @grpc_call(path="/live.xuserreward.TitleAdmin/DelMaster")
    def del_master(self, title_id=None):
        """### 删除头衔主头衔+子头衔"""

    @grpc_call(path="/live.xuserreward.TitleAdmin/GetByTid")
    def get_by_tid(self, title_id=None):
        """### 根据tid头衔信息"""

    @grpc_call(path="/live.xuserreward.TitleAdmin/GetById")
    def get_by_id(self, id=None):
        """### 根据主头衔主键ID获取头衔详细信息"""

    @grpc_call(path="/live.xuserreward.TitleAdmin/GetList")
    def get_list(self, page=None, title_id=None, name=None, status=None, page_size=None):
        """### 后台查询头衔列表"""

    @grpc_call(path="/live.xuserreward.TitleAdmin/SetOnline")
    def set_online(self, title_id=None):
        """### 上线头衔"""

    @grpc_call(path="/live.xuserreward.Glory/GetGloryVisible")
    def get_glory_visible(self, uid):
        """### 无标题"""

    @grpc_call(path="/live.xuserreward.Glory/GetUserCardGlory")
    def get_user_card_glory(self, uid):
        """### 获取用户用户卡配置的荣誉信息"""

    @grpc_call(path="/live.xuserreward.Glory/GetUserGloryList")
    def get_user_glory_list(self, uid, page=None, page_size=None):
        """### 获取主播荣誉信息列表:有分页"""

    @grpc_call(path="/live.xuserreward.Glory/GetUserGloryAll")
    def get_user_glory_all(self, uid):
        """### 获取主播荣誉信息列表：全量"""

    @grpc_call(path="/live.xuserreward.v1.BrandRoom/GetRoomCardList")
    def get_room_card_list(self, room_id):
        """### 查询房间卡片列表"""

    @grpc_call(path="/live.xuserreward.v1.BrandRoom/GetFrontRoomIcon")
    def get_front_room_icon(self, room_id):
        """### 查询房间互动面板icon"""

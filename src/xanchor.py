from tiny import grpc_call

class Xanchor(object):
    def __init__(self,service_name):
        self.service_name=service_name
    
    @grpc_call(path="/live.xanchor.v1.Pendant/getAnchorPendantCfg")
    def get_anchor_pendant_cfg(self, uid):
        """###主播手动打标获取配置模块名称"""

    @grpc_call(path="/live.xanchor.v1.Pendant/getAnchorPendantInfo")
    def get_anchor_pendant_info(self, uid):
        """###主播手动打标获取配置模块具体信息"""

    @grpc_call(path="/live.xanchor.v1.Pendant/addPendantToRoom")
    def add_pendant_to_room(self, uid, room_id, module_id):
        """###主播手动打标角标生效"""

    @grpc_call(path="/live.xanchor.v1.Pendant/detachPendantFromRoom")
    def detach_pendant_from_room(self, uid, room_id, module_id):
        """###主播手动打标角标失效"""

    @grpc_call(path="/live.xanchor.v1.LiveCalendar/AddWhiteList")
    def add_white_list(self, ruids):
        """### 后台 新增白名单"""

    @grpc_call(path="/live.xanchor.v1.LiveCalendar/GetWhiteList")
    def get_white_list(self, page, ruid=None, pagesize=None):
        """### 后台 搜索白名单"""

    @grpc_call(path="/live.xanchor.v1.LiveCalendar/DeleteWhiteList")
    def delete_white_list(self, id, ruid):
        """### 后台 删除白名单"""

    @grpc_call(path="/live.xanchor.v1.LiveCalendar/AddRecommend")
    def add_recommend(self, ruid, start_time, end_time, offline=None):
        """### 后台 新增推荐"""

    @grpc_call(path="/live.xanchor.v1.LiveCalendar/GetRecommendList")
    def get_recommend_list(self, page, status=None, pagesize=None):
        """### 后台 搜索推荐"""

    @grpc_call(path="/live.xanchor.v1.LiveCalendar/DeleteRecommend")
    def delete_recommend(self, ruid, id):
        """### 后台 删除推荐"""

    @grpc_call(path="/live.xanchor.v1.LiveCalendar/UpdateRecommend")
    def update_recommend(self, ruid, id, start_time=None, end_time=None, offline=None):
        """### 后台 更新推荐"""

    @grpc_call(path="/live.xanchor.v1.LiveCalendar/UpdateProgram")
    def update_program(self, program_id, ruid, is_pass=None, recommend=None):
        """### 主播态 更新节目"""

    @grpc_call(path="/live.xanchor.v1.LiveCalendar/GetProgramList")
    def get_program_list(self, page, status=None, ruid=None, start_time=None, end_time=None, pagesize=None):
        """### 用户-主播态 搜索节目"""

    @grpc_call(path="/live.xanchor.v1.LiveCalendar/ProgramListExport")
    def program_list_export(self, page, status=None, ruid=None, start_time=None, end_time=None, pagesize=None):
        """### 用户-主播态 下载节目列表"""

    @grpc_call(path="/live.xanchor.v1.LiveCalendar/AddProgram")
    def add_program(self, ruid, start_time, title):
        """### 主播态 添加节目"""

    @grpc_call(path="/live.xanchor.v1.LiveCalendar/UpdateProgramByAnchor")
    def update_program_by_anchor(self, ruid, program_id, start_time=None, title=None, is_delete=None):
        """### 主播态 更新节目"""

    @grpc_call(path="/live.xanchor.v1.LiveCalendar/GetProgramById")
    def get_program_by_id(self, program_id):
        """### 活动-检测直播日历节目是否存在"""

    @grpc_call(path="/live.xanchor.v1.LiveCalendar/GetStatusProgramById")
    def get_status_program_by_id(self, uid, program_id):
        """### 活动-检测用户的直播日历节目状态"""

    @grpc_call(path="/live.xanchor.v1.ShareConfMsg/ShareConfList")
    def share_conf_list(self, room_id=None, source_platform=None, page=None, pageSize=None):
        """###分享配置列表"""

    @grpc_call(path="/live.xanchor.v1.ShareConfMsg/UpdateShareConf")
    def update_share_conf(self, type, source_platform, target_platform, share_type, img_type, title_format, start_time, end_time, id=None, room_id=None, subtitle_format=None, status=None, tag_url=None):
        """###新增，更新分享配置"""

    @grpc_call(path="/live.xanchor.v1.ShareConfMsg/DelShareConf")
    def del_share_conf(self, room_id, source_platform, target_platform):
        """### 删除分享配置"""

    @grpc_call(path="/live.xanchor.v1.ShareConf/getShareConf")
    def get_share_conf(self, room_id, source_platform=None, target_platform=None, uid=None):
        """### 获取房间分享配置信息"""

    @grpc_call(path="/live.xanchor.v1.PreliveIcon/IconList")
    def icon_list(self, offset=None, limit=None, buildVersion=None, page=None):
        """### 无标题"""

    @grpc_call(path="/live.xanchor.v1.PreliveIcon/GetIcon")
    def get_icon(self, id=None):
        """### 无标题"""

    @grpc_call(path="/live.xanchor.v1.PreliveIcon/DelIcon")
    def del_icon(self, id=None):
        """### 无标题"""

    @grpc_call(path="/live.xanchor.v1.PreliveIcon/HitIcon")
    def hit_icon(self, platform, mobiApp, build, liveMode):
        """### --------------- 客户端 ---------------"""

    @grpc_call(path="/live.xanchor.v1.PreLiveInfo/GenAndGetInfo")
    def gen_and_get_info(self, uID=None, roomID=None, syncType=None, originRoomTitle=None, originRoomArea=None, originRoomCover=None):
        """### 无标题"""

    @grpc_call(path="/live.xanchor.v1.PreLiveInfo/CreateRoom")
    def create_room(self, uID=None, liveMode=None, syncPreLiveData=None):
        """### 无标题"""

    @grpc_call(path="/live.xanchor.v1.PreLiveInfo/SignalCache")
    def signal_cache(self, uID=None, title=None, cover=None):
        """### 无标题"""

    @grpc_call(path="/live.xanchor.v1.RoomNews/GetRoomNews")
    def get_room_news(self, room_id=None, uid=None):
        """###查询公告"""

    @grpc_call(path="/live.xanchor.v1.RoomNews/MultiGetRoomNews")
    def multi_get_room_news(self, room_ids, id_decoded=None):
        """###批量查询公告"""

    @grpc_call(path="/live.xanchor.v1.RoomNews/UpdateRoomNews")
    def update_room_news(self, room_id=None, uid=None, content=None, is_inner=None):
        """###增删改公告"""

    @grpc_call(path="/live.xanchor.v1.InteractService/GetChannelIdAndCdn")
    def get_channel_id_and_cdn(self, business_type, old_ch_id, uids, timeoutTime, rule_id=None):
        """### 获取频道ID和厂商"""

    @grpc_call(path="/live.xanchor.v1.ReHistoryTitle/getHistoryTitleByKeyword")
    def get_history_title_by_keyword(self, uname=None):
        """### 通过关键字获取相关用户列表"""

    @grpc_call(path="/live.xanchor.v1.ReHistoryTitle/getHistoryJob")
    def get_history_job(self, job_id):
        """### 查询重置任务状态"""

    @grpc_call(path="/live.xanchor.v1.ReHistoryTitle/postFileToReTitle")
    def post_file_to_re_title(self, uname, filePath):
        """### 通过上传文件重置用户Title"""

    @grpc_call(path="/live.xanchor.v1.ReHistoryTitle/getReTitleJobStatus")
    def get_re_title_job_status(self, job_id):
        """### 查询重置任务状态"""

    @grpc_call(path="/live.xanchor.v1.NpsService/getProgramInfo")
    def get_program_info(self, uid, p_id, platform):
        """### 无标题"""

    @grpc_call(path="/live.xanchor.v1.StickersMng/getStickersTextList")
    def get_stickers_text_list(self, status=None, uid=None, room_id=None, page=None, page_size=None, start_time=None, end_time=None):
        """### 获取贴纸文案审核信息"""

    @grpc_call(path="/live.xanchor.v1.SanMng/SanLogList")
    def san_log_list(self, uid, start_time, end_time, page=None, limit=None):
        """### 查询某个UID下的SAN值变动记录的list，支持分页"""

    @grpc_call(path="/live.xanchor.v1.SanMng/SanList")
    def san_list(self, roomid=None, uid=None, uname=None, page=None, limit=None):
        """### 基于筛选条件获取主播SAN值列表，支持分页"""

    @grpc_call(path="/live.xanchor.v1.SanMng/UpdateUserSan")
    def update_user_san(self, uid=None, score=None, type=None, op_from=None, reason=None, proof_img=None, proof_remark=None, admin=None, is_lock=None):
        """### 更新某个UID对应的SAN值，业务上只支持扣减。"""

    @grpc_call(path="/live.xanchor.v1.SanMng/ApplyRevert")
    def apply_revert(self, uid=None, id=None, reason=None, manager_name=None):
        """### 同意用户的申述通过，恢复用户制定扣分log下所扣的分数"""

    @grpc_call(path="/live.xanchor.v1.NpsService/FetchAnchorSwitch")
    def fetch_anchor_switch(self, uid=None, switchKeys=None):
        """### 无标题"""

    @grpc_call(path="/live.xanchor.v1.VirtualStorm/danmuNotify")
    def danmu_notify(self, room_id=None, type=None, curry_num=None, target_num=None, countdown=None, danmu_word=None, time=None):
        """### 热力风暴弹幕业务回调接口"""

    @grpc_call(path="/live.xanchor.v1.VirtualStorm/getVirtualThermalStormInfo")
    def get_virtual_thermal_storm_info(self, room_id):
        """### 查询当前房间热力信息，防止信息丢失 ，客户端需要打散请求"""

    @grpc_call(path="/live.xanchor.v1.VirtualStorm/getVirtualThermalStormInfoV2")
    def get_virtual_thermal_storm_info_v2(self, room_id):
        """### 查询当前房间热力信息，防止信息丢失 ，客户端需要打散请求"""

    @grpc_call(path="/live.xanchor.v1.VirtualStorm/getVirtualStormInfos")
    def get_virtual_storm_infos(self, room_id, area_id):
        """### 获取房间互动彩蛋相关配置（时长、目标、冷却、上限、热词列表等）"""

    @grpc_call(path="/live.xanchor.v1.VirtualStorm/getVirtualStormSwitch")
    def get_virtual_storm_switch(self, room_id, area_id=None):
        """### 获取房间互动彩蛋功能开关状态"""

    @grpc_call(path="/live.xanchor.v1.VirtualStorm/updateVirtualStormSwitch")
    def update_virtual_storm_switch(self, room_id, switch_status=None, switch_type=None):
        """### 主播修改其房间互动彩蛋功能开关"""

    @grpc_call(path="/live.xanchor.v1.VirtualStorm/getVirtualStormTouchedTimesByDay")
    def get_virtual_storm_touched_times_by_day(self, room_id, area_id, query_date=None):
        """### 查询自然日内热力风暴触发次数"""

    @grpc_call(path="/live.xanchor.v1.Vote/updateUnusualVoteRecord")
    def update_unusual_vote_record(self, uid):
        """### 播端-打开app时调用的接口 (用来干掉异常的数据)"""

    @grpc_call(path="/live.xanchor.v1.Vote/updateVoteTime")
    def update_vote_time(self, id, type, uid):
        """### 播端-开始或结束投票"""

    @grpc_call(path="/live.xanchor.v1.Vote/operateVote")
    def operate_vote(self, audit_status, id, operator, audit_reject_reason=None):
        """### 后台-投票审核操作-驳回 & 通过"""

    @grpc_call(path="/live.xanchor.v1.Vote/getVotesList")
    def get_votes_list(self, audit_model, uid=None, audit_status=None, start_time=None, end_time=None, page=None, page_size=None, vote_status=None, uname=None):
        """### 后台&播端-获取&搜索投票列表(支持id搜索)"""

    @grpc_call(path="/live.xanchor.v1.Virtual/saveVirtualRecord")
    def save_virtual_record(self, uid=None, virtual_name=None, virtual_path=None, is_three=None, virtual_id=None, preview_pic=None):
        """### 保存虚拟形象设置"""

    @grpc_call(path="/live.xanchor.v1.Virtual/getVirtualRecord")
    def get_virtual_record(self, uid=None, category=None, limit=None, platform=None):
        """### 获取虚拟形象设置"""

    @grpc_call(path="/live.xanchor.v1.Virtual/updateVirtualRecord")
    def update_virtual_record(self, type=None, virtual_name=None, virtual_id=None, uid=None, preview_pic=None):
        """### update虚拟形象"""

    @grpc_call(path="/live.xanchor.v1.Virtual/delVirtualImageModel")
    def del_virtual_image_model(self, uid, model_ids=None, virtual_id=None):
        """### 删除虚拟形象模型"""

    @grpc_call(path="/live.xanchor.v1.Virtual/getVirtualImageModel")
    def get_virtual_image_model(self, virtual_ids, scene=None):
        """### 获取虚拟形象场景模型（加密模型）"""

    @grpc_call(path="/live.xanchor.v1.Virtual/getVirtualImageAllModel")
    def get_virtual_image_all_model(self, virtual_ids, uid=None):
        """### 获取虚拟形象场景模型（加密模型）"""

    @grpc_call(path="/live.xanchor.v1.Virtual/getVirtualImageSecret")
    def get_virtual_image_secret(self, model_ids, uid, device_id=None, platform=None, live_key=None, scene=None, scene_key=None, pubkey=None, ip=None):
        """### 获取虚拟形象密钥"""

    @grpc_call(path="/live.xanchor.v1.Virtual/getVirtualImageSecretUsageRecord")
    def get_virtual_image_secret_usage_record(self, virtual_id=None, uid=None, model_id=None, platform=None, page=None, pagesize=None):
        """### 获取虚拟形象密钥使用记录"""

    @grpc_call(path="/live.xanchor.v1.Virtual/putVirtualImageEncryptJob")
    def put_virtual_image_encrypt_job(self, virtual_ids=None):
        """### 推送一条虚拟形象加密任务"""

    @grpc_call(path="/live.xanchor.v1.Virtual/getVirtualImageEncryptJob")
    def get_virtual_image_encrypt_job(self, type=None, num=None):
        """### 获取一条虚拟形象加密任务"""

    @grpc_call(path="/live.xanchor.v1.Virtual/submitVirtualImageEncryptJobStatus")
    def submit_virtual_image_encrypt_job_status(self, job_id=None, status=None):
        """### 提交虚拟形象加密任务执行结果状态"""

    @grpc_call(path="/live.xanchor.v1.Virtual/putFullVirtualImageEncryptJob")
    def put_full_virtual_image_encrypt_job(self, num=None):
        """### 提交当前存量的所有虚拟形象到加密任务队列"""

    @grpc_call(path="/live.xanchor.v1.Virtual/getBackgroundList")
    def get_background_list(self, status=None, page_num=None, room_id=None, start_time=None, end_time=None, not_mng=None, id=None, live_model=None):
        """### 获取背景图"""

    @grpc_call(path="/live.xanchor.v1.Virtual/updateBackgroundItem")
    def update_background_item(self, bg_id=None, bg_url=None, live_model=None, room_id=None, select_status=None, ai_audit=None):
        """### 保存背景图"""

    @grpc_call(path="/live.xanchor.v1.Virtual/getBlinkVirtualMatter")
    def get_blink_virtual_matter(self, sex, build, platform, mat_ids=None):
        """### 获取虚拟素材"""

    @grpc_call(path="/live.xanchor.v1.Virtual/getVirtualPosition")
    def get_virtual_position(self, page, sex=None, body=None, is_all=None, pos_id=None, pos_name=None):
        """### 后台-获取虚拟部位"""

    @grpc_call(path="/live.xanchor.v1.Virtual/getVirtualMatter")
    def get_virtual_matter(self, page, sex=None, pos_id=None, mat_ids=None, mat_name=None):
        """### 后台-获取虚拟素材"""

    @grpc_call(path="/live.xanchor.v1.Virtual/hideVirtualMatPos")
    def hide_virtual_mat_pos(self, type, status, id):
        """### 后台-素材/部位-隐藏/上架"""

    @grpc_call(path="/live.xanchor.v1.Virtual/updateVirtualMatPos")
    def update_virtual_mat_pos(self, type, name, blink_limit, pink_limit, sex, sort, preview_pic, body=None, pos_id=None, mat_url=None, old_sort_id=None, id=None, pos_type=None, change_color=None, blink_upper_limit=None, pink_upper_limit=None):
        """### 后台-素材/部位-新增/编辑"""

    @grpc_call(path="/live.xanchor.v1.AnchorSwitch/GetAnchorSwitch")
    def get_anchor_switch(self, uid=None, switchKeys=None):
        """### 获取主播开关"""

    @grpc_call(path="/live.xanchor.v1.AnchorSwitch/FetchAnchorSwitch")
    def fetch_anchor_switch(self, uid, switchKeys):
        """### 获取主播开关 业务端服务直调（接口文档：https://info.bilibili.co/pages/viewpage.action?pageId=247418844）"""

    @grpc_call(path="/live.xanchor.v1.AnchorTag/getAnchorTags")
    def get_anchor_tags(self, room_ids, attrs=None):
        """### 批量根据room_ids获取标签信息"""

    @grpc_call(path="/live.xanchor.v1.AnchorTag/getAnchorTagsByUids")
    def get_anchor_tags_by_uids(self, uids, attrs=None):
        """### 批量根据uids获取标签信息"""

    @grpc_call(path="/live.xanchor.v1.AnchorTag/getAnchorTagsList")
    def get_anchor_tags_list(self, room_ids, attrs=None):
        """### 按照标签维度分类房间"""

    @grpc_call(path="/live.xanchor.v1.AnchorTag/getAnchorTagsListByUids")
    def get_anchor_tags_list_by_uids(self, uids, attrs=None):
        """### 批量根据room_ids获取房间信息"""

    @grpc_call(path="/live.xanchor.v1.AnchorSwitchService/FetchAnchorSwitch")
    def fetch_anchor_switch(self, uid=None, switchKeys=None):
        """### 无标题"""

    @grpc_call(path="/live.xanchor.v1.PopsConf/getPopConf")
    def get_pop_conf(self, source, place, uid=None):
        """### 获取弹窗配置"""

    @grpc_call(path="/live.xanchor.v1.PopsConf/postPopStatus")
    def post_pop_status(self, activity_id, source, place, uid=None):
        """### 上报弹窗状态"""

    @grpc_call(path="/live.xanchor.v1.LiveCalendarUser/GetProgramList")
    def get_program_list(self, ruids=None, is_recommend=None, year_month_start=None, year_month_end=None):
        """### 获取节目列表"""

    @grpc_call(path="/live.xanchor.v1.LiveCalendarUser/AddToCalendar")
    def add_to_calendar(self, uid, type=None, ruids=None, ruids_must_in=None):
        """### 加入日历"""

    @grpc_call(path="/live.xanchor.v1.LiveCalendarUser/GetAddToCalendar")
    def get_add_to_calendar(self, uid):
        """### 获取加入日历uids"""

    @grpc_call(path="/live.xanchor.v1.LiveCalendarUser/ProgramSubscription")
    def program_subscription(self, subscription_id, type, program_id, uid):
        """### 节目订阅"""

    @grpc_call(path="/live.xanchor.v1.SwitchNewRoom/RecordSwitchNewRoom")
    def record_switch_new_room(self, uid=None, operation=None):
        """### 记录用户近30天内勾选新旧版直播间的行为"""

    @grpc_call(path="/live.xanchor.v1.SwitchNewRoom/JudgeSwitchNewRoom")
    def judge_switch_new_room(self, uid=None, roomID=None, areaParentID=None, areaID=None):
        """### 判断是否切为新版直播间"""

    @grpc_call(path="/live.xanchor.v1.SwitchNewRoom/JudgeForceNewRoom")
    def judge_force_new_room(self, uid=None):
        """### 判断是否已被强切为新版直播间"""

    @grpc_call(path="/live.xanchor.v1.PornCheck/SaveCheckResult")
    def save_check_result(self, roomid=None, ts=None, url=None, score=None):
        """### 上报鉴黄结果"""

    @grpc_call(path="/live.xanchor.v1.ObserverOnline/getMission")
    def get_mission(self, observer_name):
        """### 获得当前审核人员审核任务"""

    @grpc_call(path="/live.xanchor.v1.ObserverOnline/queryRoomStatus")
    def query_room_status(self, room_id):
        """### 查询房间状态"""

    @grpc_call(path="/live.xanchor.v1.ObserverOnline/switchMission")
    def switch_mission(self, observer_name, old_mission_id, new_target_room_id):
        """### 切换任务"""

    @grpc_call(path="/live.xanchor.v1.ObserverOnlineLog/getLogList")
    def get_log_list(self, room_id=None, room_type=None, observer=None, fin_status=None, label=None, start_time=None, end_time=None, page=None, pageSize=None):
        """### 获取审核日志列表"""

    @grpc_call(path="/live.xanchor.v1.Clarity/CategoryList")
    def category_list(self, offset=None, limit=None):
        """### 无标题"""

    @grpc_call(path="/live.xanchor.v1.Clarity/GetCategory")
    def get_category(self, id=None):
        """### 无标题"""

    @grpc_call(path="/live.xanchor.v1.Clarity/DelCategory")
    def del_category(self, id=None):
        """### 无标题"""

    @grpc_call(path="/live.xanchor.v1.Clarity/ParamList")
    def param_list(self, offset=None, limit=None):
        """### 无标题"""

    @grpc_call(path="/live.xanchor.v1.Clarity/GetParam")
    def get_param(self, id=None):
        """### 无标题"""

    @grpc_call(path="/live.xanchor.v1.Clarity/DelParam")
    def del_param(self, id=None):
        """### 无标题"""

    @grpc_call(path="/live.xanchor.v1.Clarity/PhoneList")
    def phone_list(self, offset=None, limit=None):
        """### 无标题"""

    @grpc_call(path="/live.xanchor.v1.Clarity/GetPhone")
    def get_phone(self, id=None):
        """### 无标题"""

    @grpc_call(path="/live.xanchor.v1.Clarity/DelPhone")
    def del_phone(self, id=None):
        """### 无标题"""

    @grpc_call(path="/live.xanchor.v1.Clarity/WhiteRoomList")
    def white_room_list(self, offset=None, limit=None):
        """### 无标题"""

    @grpc_call(path="/live.xanchor.v1.Clarity/GetWhiteRoom")
    def get_white_room(self, id=None):
        """### 无标题"""

    @grpc_call(path="/live.xanchor.v1.Clarity/DelWhiteRoom")
    def del_white_room(self, id=None):
        """### 无标题"""

    @grpc_call(path="/live.xanchor.v1.Clarity/HitClarity")
    def hit_clarity(self, platform, mobiApp, build, phoneCode, areaID, subAreaID, liveMode, roomID):
        """### --------------- 客户端 ---------------"""

    @grpc_call(path="/live.xanchor.v1.AnchorAcademy/GetGuideList")
    def get_guide_list(self, type=None, title=None, status=None, up_time_start=None, up_time_end=None, page=None, page_size=None):
        """### 攻略列表"""

    @grpc_call(path="/live.xanchor.v1.AnchorAcademy/AddGuide")
    def add_guide(self, type, link, cover_url, weight, title, up_now=None, up_date=None):
        """### 新增攻略"""

    @grpc_call(path="/live.xanchor.v1.AnchorAcademy/GetGuideDetail")
    def get_guide_detail(self, id):
        """### 攻略详情"""

    @grpc_call(path="/live.xanchor.v1.AnchorAcademy/UpdateGuide")
    def update_guide(self, id, type, link, cover_url, weight, title):
        """### 更新攻略"""

    @grpc_call(path="/live.xanchor.v1.AnchorAcademy/DeleteGuide")
    def delete_guide(self, id):
        """### 删除攻略"""

    @grpc_call(path="/live.xanchor.v1.AnchorAcademy/ModifyGuideStatus")
    def modify_guide_status(self, id, modify_status_type):
        """### 上下架攻略"""

    @grpc_call(path="/live.xanchor.v1.AnchorAcademy/SearchGuide")
    def search_guide(self, search_value, page=None, page_size=None):
        """### 根据「id/标题」搜索攻略"""

    @grpc_call(path="/live.xanchor.v1.AnchorAcademy/GetPushRuleList")
    def get_push_rule_list(self, position=None, page=None, page_size=None):
        """### 获取规则列表"""

    @grpc_call(path="/live.xanchor.v1.AnchorAcademy/AddPushRule")
    def add_push_rule(self, position, title, guide_ids, apply_all=None, features_json=None, up_now=None, up_date=None):
        """### 增加规则"""

    @grpc_call(path="/live.xanchor.v1.AnchorAcademy/GetPushRuleDetail")
    def get_push_rule_detail(self, id):
        """### 规则详情"""

    @grpc_call(path="/live.xanchor.v1.AnchorAcademy/UpdatePushRule")
    def update_push_rule(self, id, position, title, guide_ids, apply_all=None, features_json=None):
        """### 编辑规则"""

    @grpc_call(path="/live.xanchor.v1.AnchorAcademy/DeletePushRule")
    def delete_push_rule(self, id):
        """### 删除规则"""

    @grpc_call(path="/live.xanchor.v1.AnchorAcademy/ModifyPushRuleStatus")
    def modify_push_rule_status(self, id, modify_status_type):
        """### 下架规则"""

    @grpc_call(path="/live.xanchor.v1.AnchorAcademy/GetAnchorGuides")
    def get_anchor_guides(self, uid, position, page=None, page_size=None):
        """### 获取主播侧的攻略列表(规则和攻略均上线)"""

    @grpc_call(path="/live.xanchor.v1.AnchorAcademy/GetGuideCount")
    def get_guide_count(self, type=None, status=None):
        """### 攻略数量"""

    @grpc_call(path="/live.xanchor.v1.Stickers/getStickersById")
    def get_stickers_by_id(self, id, room_id=None):
        """### 根据ID列表获取贴纸信息"""

    @grpc_call(path="/live.xanchor.v1.San/getSanByUid")
    def get_san_by_uid(self, uid):
        """### 根据Uid获取主播SAN值"""

    @grpc_call(path="/live.xanchor.v1.San/getSanLogList")
    def get_san_log_list(self, uid, time=None, page=None, limit=None):
        """### 用户侧根据主播UID查询历史SAN值变动情况"""

    @grpc_call(path="/live.xanchor.v1.PopConfMng/PopConfList")
    def pop_conf_list(self, creater=None, pop_id=None, activity_name=None, status=None, source=None, place=None, start_time=None, end_time=None, page=None, page_size=None):
        """###弹窗配置列表"""

    @grpc_call(path="/live.xanchor.v1.PopConfMng/ChangePopConfStatus")
    def change_pop_conf_status(self, id, status):
        """### 更新弹窗状态"""

    @grpc_call(path="/live.xanchor.v1.PopConfMng/DelPopConf")
    def del_pop_conf(self, id):
        """### 删除弹窗配置"""

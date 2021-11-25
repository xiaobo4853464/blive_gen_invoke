from tiny import grpc_call

class Activity_task(object):
    def __init__(self,service_name):
        self.service_name=service_name
    
    @grpc_call(path="/live.activitytask.UserTask/GetUserActivityTaskInfo")
    def get_user_activity_task_info(self, act_id=None):
        """### 获取活动信息"""

    @grpc_call(path="/live.activitytask.UserTask/GetUserActivityTaskProgress")
    def get_user_activity_task_progress(self, uid=None, task_id=None):
        """### 获取进度信息"""

    @grpc_call(path="/live.activitytask.UserTask/GetUserActivityTaskAward")
    def get_user_activity_task_award(self, act_id, task_id, level_id, uid, cycle_id=None):
        """### 领取任务奖励"""

    @grpc_call(path="/live.activitytask.background/GetUserWatchTaskList")
    def get_user_watch_task_list(self, page, page_size):
        """###获取任务列表"""

    @grpc_call(path="/live.activitytask.background/AddMilestoneData")
    def add_milestone_data(self, task_id, time_length, reward_type, reward_id, reward_num, expire_type, expire_time=None, deadline=None, reward_name=None):
        """###新建里程碑数据"""

    @grpc_call(path="/live.activitytask.background/ModifyMilestoneData")
    def modify_milestone_data(self, task_id, milestone_id, time_length, reward_type, reward_id, reward_num, expire_type, expire_time=None, deadline=None, reward_name=None):
        """###更改里程碑数据"""

    @grpc_call(path="/live.activitytask.background/DelMilestoneData")
    def del_milestone_data(self, task_id, milestone_id):
        """###删除里程碑数据"""

    @grpc_call(path="/live.activitytask.background/SetUserWatchTaskState")
    def set_user_watch_task_state(self, task_id, state):
        """###任务上下线设置"""

    @grpc_call(path="/live.activitytask.background/GetUserWatchTaskInfo")
    def get_user_watch_task_info(self, task_id):
        """###获取任务信息"""

    @grpc_call(path="/live.activitytask.background/GetMilestoneList")
    def get_milestone_list(self, task_id):
        """###获取里程列表"""

    @grpc_call(path="/live.activitytask.background/SyncUserWatchConf")
    def sync_user_watch_conf(self, task_id):
        """###同步用户时长配置"""

    @grpc_call(path="/live.activitytask.AnchorTaskInfo/GetTaskDataListByActId")
    def get_task_data_list_by_act_id(self, act_id, uid=None, timestamp=None):
        """###通用任务接口----根据活动ID获取任务列表 {重型接口}"""

    @grpc_call(path="/live.activitytask.AnchorTaskInfo/GetTaskInfiniteProgress")
    def get_task_infinite_progress(self, task_id, room_id=None, uid=None, act_id=None):
        """### 获取不限关卡的任务进度，通用接口"""

    @grpc_call(path="/live.activitytask.AnchorTaskInfo/GetMainTaskInfoByTaskId")
    def get_main_task_info_by_task_id(self, task_id, ruid=None, room_id=None, timestamp=None):
        """###根据任务ID获取任务信息"""

    @grpc_call(path="/live.activitytask.AnchorTaskInfo/GetMainTaskInfoByActId")
    def get_main_task_info_by_act_id(self, act_id, ruid=None, room_id=None, timestamp=None):
        """###根据活动ID获取任务信息"""

    @grpc_call(path="/live.activitytask.AnchorTaskInfo/GetCurrentMainTaskInfoByTaskId")
    def get_current_main_task_info_by_task_id(self, task_id, ruid=None, timestamp=None):
        """###获取当前任务进度任务信息"""

    @grpc_call(path="/live.activitytask.AnchorTaskInfo/GetCurrentMainTaskInfoByActId")
    def get_current_main_task_info_by_act_id(self, act_id, ruid=None, timestamp=None):
        """###获取当前任务进度任务信息"""

    @grpc_call(path="/live.activitytask.AnchorTaskInfo/GetTaskLevelByActId")
    def get_task_level_by_act_id(self, act_id, uid=None):
        """###根据活动ID获取任务里程"""

    @grpc_call(path="/live.activitytask.AnchorTaskInfo/GetTaskLevelByTaskId")
    def get_task_level_by_task_id(self, task_id, uid=None, timestamp=None):
        """###根据任务ID获取当前里程"""

    @grpc_call(path="/live.activitytask.AnchorTaskInfo/GetAwardPoolList")
    def get_award_pool_list(self, pool_ids):
        """###获取奖池明细"""

    @grpc_call(path="/live.activitytask.AnchorTaskInfo/GetRewardsList")
    def get_rewards_list(self, act_id, uid, level):
        """###获取奖励列表"""

    @grpc_call(path="/live.activitytask.AnchorTaskInfo/GetLevelStatusByTaskId")
    def get_level_status_by_task_id(self, task_id, uid):
        """###获取等级状态"""

    @grpc_call(path="/live.activitytask.AnchorTaskInfo/GetRewardsByLevel")
    def get_rewards_by_level(self, act_id, uid, level):
        """###通过用户level领取奖励"""

    @grpc_call(path="/live.activitytask.AnchorTaskInfo/SendFailTaskData")
    def send_fail_task_data(self, task_type, try_time, source_data):
        """### 投递失败任务消息"""

    @grpc_call(path="/live.activitytask.AnchorTaskInfo/GetAnchorTaskLevelInfo")
    def get_anchor_task_level_info(self, task_id, ruid=None):
        """### 五一活动 - 获取主播任务完成列表"""

    @grpc_call(path="/live.activitytask.AnchorTaskInfo/GetAnchorTaskWidget")
    def get_anchor_task_widget(self, ruid, task_id):
        """### 五一活动 - 获取主播任务挂件信息"""

    @grpc_call(path="/live.activitytask.AnchorTaskInfo/FansMedalQuery")
    def fans_medal_query(self, ruid, fans_award_type):
        """### 五一活动 - 粉丝勋章兜底查询"""

    @grpc_call(path="/live.activitytask.AnchorTaskInfo/AnchorProductionPlan")
    def anchor_production_plan(self, ruid):
        """### 五月生产计划 -  主播挂件任务进度"""

    @grpc_call(path="/live.activitytask.AnchorTaskInfo/AnchorDayPlan")
    def anchor_day_plan(self, task_id, ruid=None):
        """### 五月生产计划 - 每日任务计划"""

    @grpc_call(path="/live.activitytask.AnchorTaskInfo/GetAnchorTaskStatus")
    def get_anchor_task_status(self, ruid, task_id):
        """### 五月生产计划 - 查询某个主播任务完成状态"""

    @grpc_call(path="/live.activitytask.AnchorTaskInfo/GetAllPlan")
    def get_all_plan(self, ruid=None):
        """### 五月生产计划  - 任务列表"""

    @grpc_call(path="/live.activitytask.AnchorTaskInfo/GetDragonBoatActProgress")
    def get_dragon_boat_act_progress(self, ruid=None):
        """### 6月龙舟活动，获取任务进度"""

    @grpc_call(path="/live.activitytask.AnchorTaskInfo/GetAnchorTaskListByActId")
    def get_anchor_task_list_by_act_id(self, act_id, uid=None):
        """### 获取主播任务进度"""

    @grpc_call(path="/live.activitytask.AnchorTaskInfo/GetAnchorTaskLevelReward")
    def get_anchor_task_level_reward(self, task_id, level, uid, award_type=None):
        """### 领取主播任务奖励"""

    @grpc_call(path="/live.activitytask.AnchorTaskInfo/GetOriginalGodTask")
    def get_original_god_task(self, ruid=None):
        """###获取原神活动任务进度8月"""

    @grpc_call(path="/live.activitytask.AnchorTaskInfo/OriginalGodReceiveReward")
    def original_god_receive_reward(self, task_id, uid=None, level=None, cycle_id=None):
        """###原神活动领取奖励8月"""

    @grpc_call(path="/live.activitytask.AnchorTaskInfo/GetOriginalGodTaskSeptember")
    def get_original_god_task_september(self, ruid=None):
        """###获取原神活动任务进度9月 由于8月和9月活动中间没有时间间隔，为了方便预演。用新的接口"""

    @grpc_call(path="/live.activitytask.AnchorTaskInfo/OriginalGodReceiveRewardSeptember")
    def original_god_receive_reward_september(self, task_id, uid=None, level=None, cycle_id=None):
        """###原神活动领取奖励9月"""

    @grpc_call(path="/live.activitytask.AnchorTaskInfo/GetQualifiedTaskListByActId")
    def get_qualified_task_list_by_act_id(self, act_id, uid=None):
        """### 获取指定人群主播任务进度"""

    @grpc_call(path="/live.activitytask.AnchorTaskBackground/GetTaskIdList")
    def get_task_id_list(self, task_id):
        """### 获取当前任务列表"""

    @grpc_call(path="/live.activitytask.AnchorTaskBackground/GetTaskLevelList")
    def get_task_level_list(self, task_id):
        """### 获取当前任务包含的等级"""

    @grpc_call(path="/live.activitytask.AnchorTaskBackground/InitAnchorTask")
    def init_anchor_task(self, task_name=None, creater=None):
        """### 初始化主播任务"""

    @grpc_call(path="/live.activitytask.AnchorTaskBackground/GetAnchorTask")
    def get_anchor_task(self, task_id=None):
        """### 获取主播任务"""

    @grpc_call(path="/live.activitytask.AnchorTaskBackground/SearchAnchorTask")
    def search_anchor_task(self, task_id=None, op_status=None, task_name=None, creater=None, page=None, page_size=None):
        """### 搜索主播任务"""

    @grpc_call(path="/live.activitytask.AnchorTaskBackground/UpDownActTask")
    def up_down_act_task(self, task_id, task_status=None):
        """### 上下线任务"""

    @grpc_call(path="/live.activitytask.AnchorTaskCenter/GetAnchorPeopleType")
    def get_anchor_people_type(self, uid, timestamp=None):
        """### 无标题"""

    @grpc_call(path="/live.activitytask.AnchorTaskCenter/AnchorTaskInfo")
    def anchor_task_info(self, uid):
        """###任务中心任务详情"""

    @grpc_call(path="/live.activitytask.AnchorTaskCenter/ReceiveRewardRecord")
    def receive_reward_record(self, uid, date_type=None, page=None, page_size=None):
        """###领奖记录"""

    @grpc_call(path="/live.activitytask.AnchorTaskCenter/ReceiveReward")
    def receive_reward(self, uid):
        """###一键领取奖励"""

    @grpc_call(path="/live.activitytask.AnchorTaskCenter/WatchVideoTutorial")
    def watch_video_tutorial(self, uid, task_id, sub_task_id):
        """###观看视频开播教程"""

    @grpc_call(path="/live.activitytask.AnchorTaskCenter/GetCurrentAnchorTask")
    def get_current_anchor_task(self, uid):
        """###返回当前进行中的任务"""

    @grpc_call(path="/live.activitytask.AnchorTaskCenter/GetPercentageTaskTargetNum")
    def get_percentage_task_target_num(self, uid, sub_task_id, cycle_id, level):
        """###获取百分比任务的真实的目标值"""

    @grpc_call(path="/live.activitytask.AnchorTaskCenterBg/InitTaskRecord")
    def init_task_record(self, task_name=None, creater=None):
        """### 初始化主播任务"""

    @grpc_call(path="/live.activitytask.AnchorTaskCenterBg/GetTaskList")
    def get_task_list(self, task_id=None, op_status=None, task_name=None, creater=None, page=None, page_size=None, people_id=None):
        """### 搜索主播任务"""

    @grpc_call(path="/live.activitytask.AnchorTaskCenterBg/UpOrDownTask")
    def up_or_down_task(self, task_id, task_status=None):
        """### 上下线任务和删除"""

    @grpc_call(path="/live.activitytask.AnchorTaskCenterBg/GetTaskOne")
    def get_task_one(self, task_id=None):
        """### 获取一条记录"""

    @grpc_call(path="/live.activitytask.LiveSubscribe/GetSubscribeList")
    def get_subscribe_list(self, page, page_size, key_word=None, subscribe_name=None, start_time=None, end_time=None):
        """### 获取直播预约活动列表"""

    @grpc_call(path="/live.activitytask.LiveSubscribe/GetSubscribeInfo")
    def get_subscribe_info(self, id):
        """### 获取直播预约活动详情"""

    @grpc_call(path="/live.activitytask.LiveSubscribe/EditSubscribeInfo")
    def edit_subscribe_info(self, subscribe_name, subscribe_type, creater, id=None, remark=None):
        """### 更新 | 新增直播预约活动"""

    @grpc_call(path="/live.activitytask.LiveSubscribe/GetSubscribeInfoList")
    def get_subscribe_info_list(self, id, page, page_size):
        """### 获取预约详情列表"""

    @grpc_call(path="/live.activitytask.LiveSubscribe/DelSubscribeUser")
    def del_subscribe_user(self, info_id):
        """### 删除预约活动主播"""

    @grpc_call(path="/live.activitytask.LiveSubscribe/BatchAddSubscribeUser")
    def batch_add_subscribe_user(self, id, csv_content):
        """### 批量导入预活动主播"""

    @grpc_call(path="/live.activitytask.LiveSubscribe/LiveUpReserveInfo")
    def live_up_reserve_info(self, uid, sids):
        """### 获取预约信息"""

    @grpc_call(path="/live.activitytask.LiveSubscribe/Arcs")
    def arcs(self, aids):
        """### 获取视频信息"""

    @grpc_call(path="/live.activitytask.LiveSubscribe/GetPlayBackStatus")
    def get_play_back_status(self, uid):
        """### 获取主播直播回放权限开启状态"""

    @grpc_call(path="/live.activitytask.LiveSubscribe/RecommendedAnchorDaily")
    def recommended_anchor_daily(self, sid, page, page_size, live_status, uid=None, start_time=None, end_time=None):
        """### 每日推荐官"""

    @grpc_call(path="/live.activitytask.LiveSubscribe/RecommendedProgramDaily")
    def recommended_program_daily(self, sid, page, page_size, live_status, uid=None, start_time=None, end_time=None):
        """### 每日节目单"""

    @grpc_call(path="/live.activitytask.LiveSubscribe/BatchReserve")
    def batch_reserve(self, uid, subscribe_ids):
        """### 批量预约"""

    @grpc_call(path="/live.activitytask.AnchorTask/GetMaster5Pendant")
    def get_master5_pendant(self, room_id):
        """### 挂件 5期"""

    @grpc_call(path="/live.activitytask.AnchorTask/GetLiveUp3ActInfo")
    def get_live_up3_act_info(self, uid=None, act_id=None):
        """### up主开播3期 获取时长信息"""

    @grpc_call(path="/live.activitytask.AnchorTask/ApplyLiveUp3")
    def apply_live_up3(self, uid=None, act_id=None):
        """### up主开播3期 报名"""

    @grpc_call(path="/live.activitytask.AnchorTask/GetActUp4Info")
    def get_act_up4_info(self, uid=None):
        """### up4期相关"""

    @grpc_call(path="/live.activitytask.AnchorTask/GetActPoolInfo")
    def get_act_pool_info(self, pool_id=None):
        """### 获取活动奖池信息"""

    @grpc_call(path="/live.activitytask.AnchorTask/ApplyLiveUp4")
    def apply_live_up4(self, uid=None):
        """### up主开播4期 报名"""

    @grpc_call(path="/live.activitytask.AnchorTask/ApplyUp4Condition")
    def apply_up4_condition(self, uid=None):
        """### up主开播4期 报名条件验证"""

    @grpc_call(path="/live.activitytask.AnchorTask/GetActUpAugustInfo")
    def get_act_up_august_info(self, uid=None):
        """### 8月up开播活动"""

    @grpc_call(path="/live.activitytask.AnchorTask/ApplyLiveUpAugust")
    def apply_live_up_august(self, uid=None):
        """### 8月up主开播 报名"""

    @grpc_call(path="/live.activitytask.AnchorTask/ActApplyLiveUp")
    def act_apply_live_up(self, uid=None, apply_id=None):
        """###up主报名"""

    @grpc_call(path="/live.activitytask.AnchorTask/GetActInfoAndTaskList")
    def get_act_info_and_task_list(self, uid=None, apply_id=None):
        """###获取报名和任务信息"""

    @grpc_call(path="/live.activitytask.task/GetWatchTaskStatus")
    def get_watch_task_status(self, task_id, timestamp, uid=None):
        """### 获取关注时长任务状态"""

    @grpc_call(path="/live.activitytask.task/UserShare")
    def user_share(self, act_id=None, room_id=None, uid=None, share_type=None):
        """### 用户分享"""

    @grpc_call(path="/live.activitytask.task/GetWatchTaskInfo")
    def get_watch_task_info(self, task_id):
        """### 获取里程奖励数据"""

    @grpc_call(path="/live.activitytask.UserTaskNew/ReceivePrize")
    def receive_prize(self, sub_task_id, level, uid, cycle_id=None):
        """### 领取任务奖励"""

    @grpc_call(path="/live.activitytask.UserTaskNew/GetNewUserTaskInfo")
    def get_new_user_task_info(self, task_id, uid=None):
        """### 获取用户任务信息"""

    @grpc_call(path="/live.activitytask.UserTaskNew/UserTaskSign")
    def user_task_sign(self, task_id=None, uid=None, r_uid=None):
        """###用户任务签到接口"""

    @grpc_call(path="/live.activitytask.UserTaskNew/GetUserTaskListByActId")
    def get_user_task_list_by_act_id(self, act_id, uid=None, r_uid=None, parent_area=None, area=None):
        """###通过活动Id 获取所有任务"""

    @grpc_call(path="/live.activitytask.UserTaskNew/GetNewUserTaskInfoAllLevel")
    def get_new_user_task_info_all_level(self, task_id, uid=None):
        """###五一活动用户图鉴任务(聚合任务)"""

    @grpc_call(path="/live.activitytask.UserTaskNew/GetUserBySubTask")
    def get_user_by_sub_task(self, task_id):
        """###五一活动完成任务用户"""

    @grpc_call(path="/live.activitytask.UserTaskNew/GetNewUserTaskInfiniteProgress")
    def get_new_user_task_infinite_progress(self, task_id, uid=None, room_id=None):
        """### 根据taskid获取用户任务进度信息"""

    @grpc_call(path="/live.activitytask.UserTaskNew/GetNewUserTaskJulyStarProgress")
    def get_new_user_task_july_star_progress(self, task_id, uid=None, room_id=None):
        """###7月星令任务"""

    @grpc_call(path="/live.activitytask.SevenMonthActivity/GetShareCode")
    def get_share_code(self, activity_id, uid):
        """###获取分享码"""

    @grpc_call(path="/live.activitytask.SevenMonthActivity/BindRelation")
    def bind_relation(self, activity_id, uid, share_uid, share_code, risk_param):
        """###绑定分享关系"""

    @grpc_call(path="/live.activitytask.SevenMonthActivity/GetShareInfo")
    def get_share_info(self, activity_id, share_uid, share_code, uid=None):
        """###获取助力信息"""

    @grpc_call(path="/live.activitytask.SevenMonthActivity/GetPreheatInfo")
    def get_preheat_info(self, uid=None):
        """###获取7月活动预热阶段信息接口"""

    @grpc_call(path="/live.activitytask.SevenMonthActivity/JoinActivity")
    def join_activity(self, uid, risk_param):
        """###参与7月活动"""

    @grpc_call(path="/live.activitytask.SevenMonthActivity/GetPreheatAward")
    def get_preheat_award(self, uid, stage_id):
        """###领取奖励"""

    @grpc_call(path="/live.activitytask.SevenMonthActivity/GetJoinType")
    def get_join_type(self, uid):
        """###获取报名状态"""

    @grpc_call(path="/live.activitytask.SevenMonthActivity/GetJoinInfo")
    def get_join_info(self, uid):
        """###获取报名信息"""

    @grpc_call(path="/live.activitytask.SevenMonthActivity/GetShareStatus")
    def get_share_status(self, uid, date):
        """###获取是否参与助力"""

    @grpc_call(path="/live.activitytask.SevenMonthActivity/DelMemberCache")
    def del_member_cache(self, uid):
        """###删除开播redis数据"""

    @grpc_call(path="/live.activitytask.SevenMonthActivity/ApplyLiveUp")
    def apply_live_up(self, uid):
        """### up主开播报名"""

    @grpc_call(path="/live.activitytask.Activity/GetAnchorInfo")
    def get_anchor_info(self, uid=None, act_id=None, date=None):
        """###获取主播身份信息"""

    @grpc_call(path="/live.activitytask.Activity/GetTaskRewardInfo")
    def get_task_reward_info(self, uid=None, act_id=None):
        """###获取活动奖励信息"""

    @grpc_call(path="/live.activitytask.Activity/GetActReward")
    def get_act_reward(self, uid=None, act_id=None):
        """###领取活动奖励"""

    @grpc_call(path="/live.activitytask.Activity/GetWatchTimeLevel")
    def get_watch_time_level(self, uid=None):
        """###获取观看时长总计里程"""

    @grpc_call(path="/live.activitytask.UserTaskBackgroundOld/AddUserAct")
    def add_user_act(self, creater, act_name=None):
        """### 增加用户活动"""

    @grpc_call(path="/live.activitytask.UserTaskBackgroundOld/SearchUserAct")
    def search_user_act(self, act_id=None, act_name=None, creater=None, page=None, page_size=None, act_status=None):
        """### 获取活动列表"""

    @grpc_call(path="/live.activitytask.UserTaskBackgroundOld/UpdateUserAct")
    def update_user_act(self, id, act_name, lock=None, act_status=None):
        """### 活动锁定操作"""

    @grpc_call(path="/live.activitytask.UserTaskBackgroundOld/GetUserTask")
    def get_user_task(self, task_id=None):
        """### 获取用户任务"""

    @grpc_call(path="/live.activitytask.UserTaskBackgroundOld/SearchUserTask")
    def search_user_task(self, task_id=None, task_status=None, task_name=None, creater=None, page=None, page_size=None, act_id=None):
        """### 搜索用户任务"""

    @grpc_call(path="/live.activitytask.UserTaskBackgroundOld/UpDownUserActTask")
    def up_down_user_act_task(self, task_id, task_status=None):
        """### 上下线任务"""

    @grpc_call(path="/live.activitytask.UserTaskBackgroundOld/GetActUserInfos")
    def get_act_user_infos(self, uids):
        """### 获取关注配置"""

    @grpc_call(path="/live.activitytask.AnchorTask/GetActivityTaskInfo")
    def get_activity_task_info(self, act_id=None):
        """### 获取活动信息"""

    @grpc_call(path="/live.activitytask.AnchorTask/GetActivityTaskProgress")
    def get_activity_task_progress(self, id=None):
        """### 获取进度信息"""

    @grpc_call(path="/live.activitytask.UserTaskBackground/GetUserTaskList")
    def get_user_task_list(self, page, page_size, title=None, task_status=None, act_title=None, creater=None):
        """### 获取当前任务列表"""

    @grpc_call(path="/live.activitytask.UserTaskBackground/GetUserTaskChildList")
    def get_user_task_child_list(self, task_id):
        """### 获取子任务列表"""

    @grpc_call(path="/live.activitytask.UserTaskBackground/GetUserTaskInfo")
    def get_user_task_info(self, task_id):
        """### 获取一个主任务详情"""

    @grpc_call(path="/live.activitytask.UserTaskBackground/GetUserTaskChildInfo")
    def get_user_task_child_info(self, task_id):
        """### 获取一个子任务详情"""

    @grpc_call(path="/live.activitytask.UserTaskBackground/UpdateUserTaskInfo")
    def update_user_task_info(self, start_time, end_time, creater, task_id=None, title=None, task_desc=None, feature_id=None, act_id=None, act_title=None):
        """### 更新和新增主任务"""

    @grpc_call(path="/live.activitytask.UserTaskBackground/UpDownTask")
    def up_down_task(self, task_id=None, task_status=None):
        """### 上下线任务"""

    @grpc_call(path="/live.activitytask.UserTaskBackground/DelUserTaskChild")
    def del_user_task_child(self, task_id):
        """### 删除一个子任务"""

    @grpc_call(path="/live.activitytask.UserTaskBackground/SyncUserTaskWatchConf")
    def sync_user_task_watch_conf(self, task_id):
        """###同步用户任务时长配置"""

    @grpc_call(path="/live.activitytask.UserTaskBackground/SyncUserTaskWatchConfNew")
    def sync_user_task_watch_conf_new(self, task_id):
        """###同步用户任务时长配置"""

    @grpc_call(path="/live.activitytask.OpenTask/GetTaskInfoByActId")
    def get_task_info_by_act_id(self, act_id, uid=None):
        """###获取任务详情"""

    @grpc_call(path="/live.activitytask.OpenTask/GetOpenPlatformTaskReward")
    def get_open_platform_task_reward(self, task_id, level, uid=None):
        """###领取游戏任务奖励"""

    @grpc_call(path="/live.activitytask.OpenTask/ReceiveTaskReward")
    def receive_task_reward(self, reward_source, uid, package_id=None, order_id=None):
        """###领取任务奖励"""

    @grpc_call(path="/live.activitytask.OpenTask/CheckGetGiftPackageCondition")
    def check_get_gift_package_condition(self, package_id, uid):
        """###奖励预检"""

    @grpc_call(path="/live.activitytask.OpenTask/GetAllGiftPackageList")
    def get_all_gift_package_list(self, firm_name):
        """###返回所有可用礼包"""

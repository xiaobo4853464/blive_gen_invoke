from tiny import grpc_call

class Anchor_task_center(object):
    def __init__(self,service_name):
        self.service_name=service_name
    
    @grpc_call(path="/live.anchortaskcenter.AnchorTaskCenterTaskConfigBg/CreateAndEditTaskGroup")
    def create_and_edit_task_group(self, title, task_group_cycle, area_ids, creator, task_group_id=None, valid_type=None, valid_date=None, remark=None, is_branch_task=None):
        """###创建和编辑任务组"""

    @grpc_call(path="/live.anchortaskcenter.AnchorTaskCenterTaskConfigBg/OnlineOrOfflineTaskGroup")
    def online_or_offline_task_group(self, task_group_id, op_status=None):
        """###上下线任务组"""

    @grpc_call(path="/live.anchortaskcenter.AnchorTaskCenterTaskConfigBg/GetTaskGroupList")
    def get_task_group_list(self, op_status=None, task_group_biz=None, task_group_id=None, title=None, creator=None, page=None, size=None):
        """###任务组列表"""

    @grpc_call(path="/live.anchortaskcenter.AnchorTaskCenterTaskConfigBg/GetTaskGroupDetail")
    def get_task_group_detail(self, task_group_id):
        """###任务组详情"""

    @grpc_call(path="/live.anchortaskcenter.AnchorTaskCenterTaskConfigBg/GetTaskGroupInfoByPeopleFlushPeriod")
    def get_task_group_info_by_people_flush_period(self, flush_period):
        """###通过人群刷新周期获取指定类型任务组"""

    @grpc_call(path="/live.anchortaskcenter.AnchorTaskCenterTaskConfigBg/DelAnchorTask")
    def del_anchor_task(self, task_id):
        """###删除主播任务"""

    @grpc_call(path="/live.anchortaskcenter.AnchorTaskCenterTaskConfigBg/CopyAnchorTask")
    def copy_anchor_task(self, task_id, task_group_id):
        """###复制主播任务"""

    @grpc_call(path="/live.anchortaskcenter.AnchorTaskCenterTaskConfigBg/OnlineOrOfflineTask")
    def online_or_offline_task(self, task_id, task_group_id, op_status=None):
        """###上下线任务"""

    @grpc_call(path="/live.anchortaskcenter.AnchorTaskCenterTaskConfigBg/GetAnchorTaskDetail")
    def get_anchor_task_detail(self, task_id):
        """###主播任务详情"""

    @grpc_call(path="/live.anchortaskcenter.AnchorTaskCenterTaskConfigBg/GetTaskGroupChildTask")
    def get_task_group_child_task(self, task_group_id):
        """###获取任务组下的所有任务"""

    @grpc_call(path="/live.anchortaskcenter.AnchorTaskCenterApi/AnchorTaskInfo")
    def anchor_task_info(self, uid, raw_platform=None, build=None):
        """###任务中心任务详情"""

    @grpc_call(path="/live.anchortaskcenter.AnchorTaskCenterApi/GetCurrentAnchorTask")
    def get_current_anchor_task(self, uid, raw_platform=None, build=None):
        """###挂件接口,获取当前进行中的任务"""

    @grpc_call(path="/live.anchortaskcenter.AnchorTaskCenterApi/ReceiveRewardRecord")
    def receive_reward_record(self, uid, date_type=None, page=None, page_size=None):
        """###领奖记录"""

    @grpc_call(path="/live.anchortaskcenter.AnchorTaskCenterApi/ReceiveReward")
    def receive_reward(self, uid):
        """###一键领取奖励"""

    @grpc_call(path="/live.anchortaskcenter.AnchorTaskCenterApi/WatchVideoTutorial")
    def watch_video_tutorial(self, uid, task_id, sub_task_id, task_group_id=None):
        """###观看视频开播教程"""

    @grpc_call(path="/live.anchortaskcenter.AnchorTaskCenterApi/GetPercentageTaskTargetNum")
    def get_percentage_task_target_num(self, uid, task_id, sub_task_id, level):
        """###获取百分比任务的真实的目标值"""

    @grpc_call(path="/live.anchortaskcenter.AnchorTaskCenterApi/GetAnchorTaskByPeopleId")
    def get_anchor_task_by_people_id(self, people_ids):
        """###获取主播所属人群下所配置的任务组任务"""

    @grpc_call(path="/live.anchortaskcenter.AnchorTaskCenterApi/AnchorNewTaskIsValid")
    def anchor_new_task_is_valid(self, uid, member_ids, timestamp=None):
        """###判断主播是否有门槛(新人)任务且是否过了有效期"""

    @grpc_call(path="/live.anchortaskcenter.AnchorMemberApi/GetMemberIdByUidAndTime")
    def get_member_id_by_uid_and_time(self, uid, timestamp=None):
        """###根据用户uid及时间获取全部人群信息"""

    @grpc_call(path="/live.anchortaskcenter.AnchorMemberApi/AnchorInMemberId")
    def anchor_in_member_id(self, uid, member_id, timestamp=None):
        """###判定用户uid是否在某一人群包"""

    @grpc_call(path="/live.anchortaskcenter.AnchorMemberApi/AnchorIsNewPeople")
    def anchor_is_new_people(self, uid, timestamp=None):
        """###判定是否新人主播"""

    @grpc_call(path="/live.anchortaskcenter.AnchorMemberApi/GetMemberIdByUidAndTimeForTask")
    def get_member_id_by_uid_and_time_for_task(self, uid, timestamp=None):
        """###根据用户uid和时间获取全部人群信息「for  任务」"""

    @grpc_call(path="/live.anchortaskcenter.AnchorMemberApi/SyncNewMember")
    def sync_new_member(self, uid, start_time=None, is_new=None):
        """###增量同步"""

    @grpc_call(path="/live.anchortaskcenter.AnchorMemberApi/AnchorInMemberIdList")
    def anchor_in_member_id_list(self, member_id_list, uid, timestamp):
        """###判定用户是否在人群列表中"""

    @grpc_call(path="/live.anchortaskcenter.AnchorMemberApi/UpdateUserProtectedPeriod")
    def update_user_protected_period(self, uid):
        """###刷新用户扶持周期"""

    @grpc_call(path="/live.anchortaskcenter.AnchorTaskCenterPeopleTaskConfigBg/DelPeopleTaskCfg")
    def del_people_task_cfg(self, people_task_id):
        """###删除人群任务配置"""

    @grpc_call(path="/live.anchortaskcenter.AnchorTaskCenterPeopleTaskConfigBg/OnlineAndOfflinePeopleTaskCfg")
    def online_and_offline_people_task_cfg(self, people_task_id, status=None):
        """###上下线人群任务配置"""

    @grpc_call(path="/live.anchortaskcenter.AnchorTaskCenterPeopleTaskConfigBg/GetPeopleTaskCfgList")
    def get_people_task_cfg_list(self, op_status=None, people_task_id=None, people_id=None, creator=None, page=None, size=None):
        """###人群任务配置列表"""

    @grpc_call(path="/live.anchortaskcenter.AnchorTaskCenterPeopleTaskConfigBg/GetPeopleTaskCfgDetail")
    def get_people_task_cfg_detail(self, people_task_id=None):
        """###人群任务配置详情"""

    @grpc_call(path="/live.anchortaskcenter.AnchorTaskCenterPeopleConfigBg/GetAnchorGroupList")
    def get_anchor_group_list(self, id=None, group_name=None, page=None, page_size=None):
        """### 获取人群组列表"""

    @grpc_call(path="/live.anchortaskcenter.AnchorTaskCenterPeopleConfigBg/GetAnchorGroup")
    def get_anchor_group(self, id=None):
        """### 获取单个人群组"""

    @grpc_call(path="/live.anchortaskcenter.AnchorTaskCenterPeopleConfigBg/SetAnchorGroup")
    def set_anchor_group(self, id=None, group_name=None, useful_life_type=None, start_time=None, end_time=None, flush_period=None, creater=None, remark=None):
        """### 新增/编辑人群组"""

    @grpc_call(path="/live.anchortaskcenter.AnchorTaskCenterPeopleConfigBg/CopyAnchorGroup")
    def copy_anchor_group(self, id=None, creater=None):
        """### 复制人群组"""

    @grpc_call(path="/live.anchortaskcenter.AnchorTaskCenterPeopleConfigBg/GetAnchorMemberList")
    def get_anchor_member_list(self, group_id=None):
        """### 获取人群包列表"""

    @grpc_call(path="/live.anchortaskcenter.AnchorTaskCenterPeopleConfigBg/GetAnchorMember")
    def get_anchor_member(self, id=None):
        """### 获取单个人群包"""

    @grpc_call(path="/live.anchortaskcenter.AnchorTaskCenterPeopleConfigBg/CopyAnchorMember")
    def copy_anchor_member(self, id=None, creater=None):
        """### 复制人群包"""

    @grpc_call(path="/live.anchortaskcenter.AnchorTaskCenterPeopleConfigBg/DelAnchorMember")
    def del_anchor_member(self, id=None, creater=None):
        """### 删除人群包"""

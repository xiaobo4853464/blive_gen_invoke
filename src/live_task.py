from tiny import grpc_call

class Live_task(object):
    def __init__(self,service_name):
        self.service_name=service_name
    
    @grpc_call(path="/live.livetask.UserTask/getUserTask")
    def get_user_task(self, id=None, uid=None, timestamp=None):
        """### 获取用户任务"""

    @grpc_call(path="/live.livetask.UserTask/GetTaskAward")
    def get_task_award(self, id=None, uid=None):
        """### 获取任务奖励"""

    @grpc_call(path="/live.livetask.UserTask/getActivityTask")
    def get_activity_task(self, act_type=None, act_id=None, uid=None, is_owner=None):
        """### 获取活动任务"""

    @grpc_call(path="/live.livetask.UserTask/getActivityPayAndFreeTask")
    def get_activity_pay_and_free_task(self, act_type=None, act_id=None, uid=None, is_owner=None):
        """### 获取活动任务"""

    @grpc_call(path="/live.livetask.UserTask/getActivityTaskAssist")
    def get_activity_task_assist(self, act_type=None, act_id=None, uid=None, timestamp=None):
        """### 获取活动任务应援"""

    @grpc_call(path="/live.livetask.UserTask/GetTaskReportInfo")
    def get_task_report_info(self, act_id=None, timestamp=None, uid=None):
        """### 任务挂件"""

    @grpc_call(path="/live.livetask.UserTask/GetTaskReportDetail")
    def get_task_report_detail(self, act_id=None, uid=None, timestamp=None):
        """### 任务挂件"""

    @grpc_call(path="/live.livetask.UserTask/TaskPendant")
    def task_pendant(self, room_id):
        """### 任务挂件"""

    @grpc_call(path="/live.livetask.UserTask/getUserSubTaskCnt")
    def get_user_sub_task_cnt(self, id=None, timestamp=None, uid=None):
        """### 获取用户任务"""

    @grpc_call(path="/live.livetask.UserTask/getMasterSupport")
    def get_master_support(self, act_type=None, act_id=None, uid=None, is_owner=None):
        """### 获取用户任务"""

    @grpc_call(path="/live.livetask.UserTask/getActUserInWhite")
    def get_act_user_in_white(self, act_id=None, uid=None, timestamp=None):
        """### 获取用户是否在活动白名单"""

    @grpc_call(path="/live.livetask.UserTask/getActWhiteUsers")
    def get_act_white_users(self, act_id=None, page=None, page_size=None):
        """### 获取活动白名单列表"""

    @grpc_call(path="/live.livetask.UserTask/GetMasterSupportPendant")
    def get_master_support_pendant(self, room_id):
        """### 主播助力任务挂件"""

    @grpc_call(path="/live.livetask.UserTask/GetAcTaskMaxLevel")
    def get_ac_task_max_level(self, act_id, ruid, req_timestamp):
        """### 获取活动完成最高等级"""

    @grpc_call(path="/live.livetask.UserTask/FixMasterSupport")
    def fix_master_support(self, id_list, old_act_id, new_act_id):
        """### 修改主播扶持任务脏ruid"""

    @grpc_call(path="/live.livetask.UserTask/RewardCenterCallBack")
    def reward_center_call_back(self, transaction_id=None, result_code=None, result_msg=None):
        """### 奖励中心回调"""

    @grpc_call(path="/live.livetask.UserTask/GetMasterSupportReport")
    def get_master_support_report(self, uid, gold_actid, traf_actid, timestamp=None):
        """### 主播扶持日报信息"""

    @grpc_call(path="/live.livetask.UserTask/GetUserJoinAct")
    def get_user_join_act(self, uid, time_type=None):
        """### 获取主播参加的活动id"""

    @grpc_call(path="/live.livetask.UserTask/GetUserAwardSum")
    def get_user_award_sum(self, uid, act_list, award_type=None, current_time=None):
        """### 获取活动奖励数据"""

    @grpc_call(path="/live.livetask.UserTask/GetActNeedSendMessage")
    def get_act_need_send_message(self, act_id, time_type, page, page_size):
        """### 获取活动需要发送私信的人"""

    @grpc_call(path="/live.livetask.UserTask/CountActNeedSendMessage")
    def count_act_need_send_message(self, act_id, time_type):
        """### 获取活动需要发送私信的人总数"""

    @grpc_call(path="/live.livetask.UserTask/GetActTaskAward")
    def get_act_task_award(self, uid, act_list, award_type=None, current_time=None):
        """### 领取活动奖励，例如星光，金仓鼠"""

    @grpc_call(path="/live.livetask.UserTask/GetUserWhiteMaxId")
    def get_user_white_max_id(self, act_id):
        """### 获取白名单最大id"""

    @grpc_call(path="/live.livetask.UserTask/CheckUserTodayLive")
    def check_user_today_live(self, time_type=None, uid_list=None):
        """### check主播是否开播过"""

    @grpc_call(path="/live.livetask.UserTask/GetActTaskStarAward")
    def get_act_task_star_award(self, uid, act_list, award_type=None, current_time=None, source_id=None, extra_data=None):
        """### 领取星光奖励"""

    @grpc_call(path="/live.livetask.UserTask/GetActTaskHamsterAward")
    def get_act_task_hamster_award(self, uid, act_list, award_type=None, current_time=None):
        """### 领取金仓鼠奖励"""

    @grpc_call(path="/live.livetask.UserTask/InsertWhiteUser")
    def insert_white_user(self, uids=None, act_id=None):
        """### 添加白名单"""

    @grpc_call(path="/live.livetask.UserTask/CountUserLive")
    def count_user_live(self, time_type=None):
        """### 获取开播总数"""

    @grpc_call(path="/live.livetask.UserTask/ZrangeUserLive")
    def zrange_user_live(self, page=None, page_size=None, time_type=None):
        """### 获取开播成员"""

    @grpc_call(path="/live.livetask.UserTask/GetActM4UserInWhite")
    def get_act_m4_user_in_white(self, act_id=None, uid=None):
        """### 是否在主播扶持4期"""

    @grpc_call(path="/live.livetask.UserTask/GetPlayerList")
    def get_player_list(self, page=None, page_size=None):
        """###获取在播列表"""

    @grpc_call(path="/live.livetask.UserTask/GetSpeicalGoldTask")
    def get_speical_gold_task(self, uid):
        """###获取特殊金瓜子任务"""

    @grpc_call(path="/live.livetask.DragonBoat/GetDragonBoatTaskList")
    def get_dragon_boat_task_list(self, timestamp, uid=None):
        """###获取用户任务列表"""

    @grpc_call(path="/live.livetask.MatchTask/ApiKplIndex")
    def api_kpl_index(self, uid=None):
        """###----------------------------------------kpl2020秋季赛"""

    @grpc_call(path="/live.livetask.MatchTask/ApiKplFollow")
    def api_kpl_follow(self, ruid, uid):
        """### 关注主播"""

    @grpc_call(path="/live.livetask.MatchTask/KplSendWatchTaskAward")
    def kpl_send_watch_task_award(self, uid=None, date=None):
        """### 完成关注时长任务发奖"""

    @grpc_call(path="/live.livetask.MatchTask/KplSendFollowTaskAward")
    def kpl_send_follow_task_award(self, uid=None, ruid=None):
        """### 完成关注主播任务发奖"""

    @grpc_call(path="/live.livetask.MatchTask/Cfs2020Index")
    def cfs2020_index(self, uid=None):
        """###----------------------------------------cfs2020"""

    @grpc_call(path="/live.livetask.MatchTask/Cfs2020SendWatchTaskAward")
    def cfs2020_send_watch_task_award(self, uid=None, timestamp=None):
        """### 获取观赛任务状态 & 主播列表"""

    @grpc_call(path="/live.livetask.MatchTask/Cfs2020Follow")
    def cfs2020_follow(self, ruid, uid):
        """### 关注主播"""

    @grpc_call(path="/live.livetask.MatchTask/GeneralFollow")
    def general_follow(self, ruid, uid, game_type):
        """### 通用关注"""

    @grpc_call(path="/live.livetask.MatchTask/GeneralFollowStatus")
    def general_follow_status(self, uid=None, game_type=None):
        """### 无标题"""

    @grpc_call(path="/live.livetask.MatchTask/Share")
    def share(self, uid=None, game_type=None):
        """### 通用分享"""

    @grpc_call(path="/live.livetask.MatchTask/ShareStatus")
    def share_status(self, uid=None, game_type=None):
        """### 通用分享"""

    @grpc_call(path="/live.livetask.HamsterApprove/GetHamsterSummaryList")
    def get_hamster_summary_list(self, page, page_size, start_day=None, end_day=None, act_name=None):
        """### 金仓鼠汇总记录"""

    @grpc_call(path="/live.livetask.HamsterApprove/ApprovalHamsterAward")
    def approval_hamster_award(self, act_id, time_type, approver):
        """### 审批金仓鼠发放"""

    @grpc_call(path="/live.livetask.HamsterApprove/GetHamsterAwardDetail")
    def get_hamster_award_detail(self, act_id, time_type, page, page_size, uid=None, task_id=None, account_status=None):
        """### 金仓鼠奖励明细"""

    @grpc_call(path="/live.livetask.HamsterApprove/JoinHamsterRecord")
    def join_hamster_record(self, act_id, delay_day, source_id, transaction_id, award_num, uid, bag_id, time_type, award_type, task_id=None):
        """### 新增金仓鼠奖励记录"""

    @grpc_call(path="/live.livetask.HamsterApprove/FrozenHamsterRecord")
    def frozen_hamster_record(self, id, account_status, approver):
        """### 冻结金仓鼠发放记录"""

    @grpc_call(path="/live.livetask.AprilSuperstar/GetAprilSuperstarTaskList")
    def get_april_superstar_task_list(self, timestamp, uid=None):
        """###获取四月星势力用户任务列表"""

    @grpc_call(path="/live.livetask.TaskBackend/getTaskList")
    def get_task_list(self, page, page_size):
        """### 获取任务列表"""

    @grpc_call(path="/live.livetask.TaskBackend/getTaskInfo")
    def get_task_info(self, id=None):
        """### 添加任务详细信息"""

    @grpc_call(path="/live.livetask.CollectCard/CollectCardGifts")
    def collect_card_gifts(self, uid=None):
        """### 获取用户奖励"""

    @grpc_call(path="/live.livetask.MaySweet/GetMaySweetTaskList")
    def get_may_sweet_task_list(self, timestamp, uid=None):
        """###获取用户任务列表"""

    @grpc_call(path="/live.livetask.Bls2020/GetTask")
    def get_task(self, uid=None, room_id=None):
        """### 获取用户任务"""

    @grpc_call(path="/live.livetask.Bls2020/GetTaskPendant")
    def get_task_pendant(self, uid=None, room_id=None):
        """### 主播助力任务挂件"""

    @grpc_call(path="/live.livetask.Bls2020/GetFinalistTask")
    def get_finalist_task(self, uid=None, room_id=None):
        """### 获取入围赛任务进度"""

    @grpc_call(path="/live.livetask.Bls2020/GetFinalistTaskPendant")
    def get_finalist_task_pendant(self, uid=None, room_id=None):
        """### 入围赛挂件"""

    @grpc_call(path="/live.livetask.Bls2020/GetFinalistTaskRank")
    def get_finalist_task_rank(self, team_id=None, page=None):
        """### 入围赛榜单 (只展示当天)"""

    @grpc_call(path="/live.livetask.Bls2020/GetFinalistTaskAidRank")
    def get_finalist_task_aid_rank(self, ruid=None, room_id=None):
        """### 入围赛应援榜"""

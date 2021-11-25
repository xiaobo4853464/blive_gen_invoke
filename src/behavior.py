from tiny import grpc_call

class Behavior(object):
    def __init__(self,service_name):
        self.service_name=service_name
    
    @grpc_call(path="/live.behavior.UserTask/getTaskList")
    def get_task_list(self, page, page_size):
        """### 添加任务"""

    @grpc_call(path="/live.behavior.UserTask/getTaskInfo")
    def get_task_info(self, id=None):
        """### 添加任务"""

    @grpc_call(path="/live.behavior.UserTask/getUserTask")
    def get_user_task(self, id=None, uid=None):
        """### 获取用户任务"""

    @grpc_call(path="/live.behavior.UserTask/getUserTaskStatus")
    def get_user_task_status(self, id=None, uid=None):
        """### 获取用户任务"""

    @grpc_call(path="/live.behavior.UserTask/GetTaskAward")
    def get_task_award(self, id=None, uid=None):
        """### 获取任务奖励"""

    @grpc_call(path="/live.behavior.UserTask/GetBlsTask")
    def get_bls_task(self, room_id=None, uid=None):
        """### 获取任务奖励"""

    @grpc_call(path="/live.behavior.UserTask/setFocusMaster")
    def set_focus_master(self, task_id, ruids):
        """### 设置关注主播"""

    @grpc_call(path="/live.behavior.UserTask/setUserTaskStatus")
    def set_user_task_status(self, id=None, uid=None, status=None):
        """### 无标题"""

    @grpc_call(path="/live.behavior.UserTask/GetSimpleTask")
    def get_simple_task(self, id=None, uid=None):
        """### 获取赛事任务"""

    @grpc_call(path="/live.behavior.UserTask/GetMatchTask")
    def get_match_task(self, game_type=None, task_type=None, uid=None):
        """### 获取赛事任务"""

    @grpc_call(path="/live.behavior.UserTask/MatchSign")
    def match_sign(self, game_type=None, uid=None):
        """### 赛事签到"""

    @grpc_call(path="/live.behavior.UserTask/MatchShare")
    def match_share(self, game_type=None, uid=None):
        """### 赛事分享"""

    @grpc_call(path="/live.behavior.rank/add_rank")
    def add_rank(self, title, ruler_id, id=None, master_rank_list=None, user_rank_list=None, rank_score_type=None, rank_score_extra=None):
        """### 添加榜单"""

    @grpc_call(path="/live.behavior.rank/get_rank_list")
    def get_rank_list(self, page, page_size):
        """### 获取榜单列表"""

    @grpc_call(path="/live.behavior.rank/update_rank_status")
    def update_rank_status(self, id, status=None):
        """### 更新榜单列表状态"""

    @grpc_call(path="/live.behavior.behavior/get_rulers")
    def get_rulers(self, page, page_size):
        """### 获取规则列表"""

    @grpc_call(path="/live.behavior.behavior/update_ruler_status")
    def update_ruler_status(self, id, status=None):
        """### 更新规则列表状态"""

    @grpc_call(path="/live.behavior.behavior/EntryRoom")
    def entry_room(self, uid, entry_info):
        """### 用户进场"""

    @grpc_call(path="/live.behavior.behavior/RecycleGuard")
    def recycle_guard(self, order_id, uid, ruid, total_price, origin_price, platform, goods_id, goods_num, parent_area_id, area_id, parent_goods_cate, goods_cate, create_time, mobile_app=None):
        """### 回收大航海权益"""

    @grpc_call(path="/live.behavior.reward/get_award")
    def get_award(self, ruler_id):
        """### 获取奖励详情"""

    @grpc_call(path="/live.behavior.reward/get_award_name")
    def get_award_name(self, award_type, award_id):
        """### 获取奖励名称"""

    @grpc_call(path="/live.behavior.reward/get_award_list")
    def get_award_list(self, page, page_size):
        """### 获取奖励列表"""

    @grpc_call(path="/live.behavior.reward/update_award_status")
    def update_award_status(self, id, status=None):
        """### 更新规则列表状态"""

    @grpc_call(path="/live.behavior.reward/get_package_list")
    def get_package_list(self, page, page_size):
        """### 获取奖励打包列表"""

    @grpc_call(path="/live.behavior.reward/update_package_status")
    def update_package_status(self, id, status=None):
        """### 更新打包列表状态"""

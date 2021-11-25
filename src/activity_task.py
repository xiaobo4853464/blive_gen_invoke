"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""
from tiny import grpc_call


class Activity_task(object):

    def __init__(self, service_name):
        self.service_name = service_name

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


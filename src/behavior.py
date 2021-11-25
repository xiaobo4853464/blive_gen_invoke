"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""
from tiny import grpc_call


class Behavior(object):

    def __init__(self, service_name):
        self.service_name = service_name

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


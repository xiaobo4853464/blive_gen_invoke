"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""
from tiny import grpc_call


class Live_reward(object):

    def __init__(self, service_name):
        self.service_name = service_name

    @grpc_call(path="/live.reward.userItem/UpdateUserItem")
    def update_user_item(self, item_id, num, uid, tid, source, expire=None, target_uid=None, target_parent_area_id=None, target_area_id=None, target_other=None, platform=None, mobi_app=None, build=None, device=None, context_type=None, context_id=None, extra_data=None, update_time=None):
        """### 修改物品数量"""

    @grpc_call(path="/live.reward.userItem/GetUserItem")
    def get_user_item(self, item_id, uid, target_uid=None, target_parent_area_id=None, target_area_id=None, target_other=None):
        """### get物品数量"""

    @grpc_call(path="/live.reward.userItem/GetLogForUser")
    def get_log_for_user(self, item_id=None, uid=None, start_time=None, end_time=None, page=None, page_size=None, target_uid=None, target_parent_area_id=None, target_area_id=None, target_other=None, target_otupdate_typeher=None):
        """### 获取日志(用户态，给用户自己看的)"""


"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""
from tiny import grpc_call


class Rubick_push(object):

    def __init__(self, service_name):
        self.service_name = service_name

    @grpc_call(path="/live.rubickpush.RecommendPushV1/get_recommend_push_v1")
    def get_recommend_push_v1(self, uid=None, room_id=None, sid=None, is_special=None):
        """### 房间推荐推送专用接口"""

    @grpc_call(path="/live.rubickpush.RecommendPushV1/get_recommend_push_inner_v1")
    def get_recommend_push_inner_v1(self, uid=None, room_list=None, sid=None):
        """### 房间推荐推送端内专用接口"""

    @grpc_call(path="/live.rubickpush.RecommendPushV1/reload_user_room_cnt")
    def reload_user_room_cnt(self, gap=None):
        """### 手动重新加载"""

    @grpc_call(path="/live.rubickpush.RecommendPushV1/get_user_room_cnt")
    def get_user_room_cnt(self, uid=None):
        """### 手动获取"""

    @grpc_call(path="/live.rubickpush.RecommendPushV1/set_room_filter")
    def set_room_filter(self, room_id=None, start_time=None, end_time=None, source=None, source_id=None):
        """### 过滤付费课堂"""


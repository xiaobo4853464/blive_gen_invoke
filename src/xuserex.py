"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""
from tiny import grpc_call


class Xuserex(object):

    def __init__(self, service_name):
        self.service_name = service_name

    @grpc_call(path="/live.xuserex.v1.UserColor/GetNickNameColor")
    def get_nick_name_color(self, uid, room_id=None):
        """### 获取用户昵称颜色"""

    @grpc_call(path="/live.xuserex.v1.UserColor/Send")
    def send(self, uid, source, type, room_id=None, color=None, weight=None, add_time=None, expired_time=None):
        """### 向用户下发颜色"""

    @grpc_call(path="/live.xuserex.v1.UserColor/Recycle")
    def recycle(self, uid, source, type, room_id=None, color=None, weight=None, add_time=None, expired_time=None):
        """### 回收颜色"""


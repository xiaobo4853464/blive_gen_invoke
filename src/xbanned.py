"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""
from tiny import grpc_call


class Xbanned(object):

    def __init__(self, service_name):
        self.service_name = service_name

    @grpc_call(path="/live.xbanned.v2.silent/GetRoomSilent")
    def get_room_silent(self, room_id):
        """### 超管获取房间禁言"""

    @grpc_call(path="/live.xbanned.v2.silent/RoomSilentOff")
    def room_silent_off(self, room_id):
        """### 关闭超管房间禁言"""


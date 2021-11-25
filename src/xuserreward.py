"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""
from tiny import grpc_call


class Xuserreward(object):

    def __init__(self, service_name):
        self.service_name = service_name

    @grpc_call(path="/live.xuserreward.v1.BrandRoom/GetRoomCardList")
    def get_room_card_list(self, room_id):
        """### 查询房间卡片列表"""

    @grpc_call(path="/live.xuserreward.v1.BrandRoom/GetFrontRoomIcon")
    def get_front_room_icon(self, room_id):
        """### 查询房间互动面板icon"""


"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""
from tiny import grpc_call


class Xrewardcenter(object):

    def __init__(self, service_name):
        self.service_name = service_name

    @grpc_call(path="/live.xrewardcenter.v2.Skin/Current")
    def current(self, room_id=None, skin_platform=None, skin_version=None, area_v2_parent_id=None, area_v2_id=None, device=None, build=None, mobi_app=None):
        """### 获取当前房间的皮肤"""


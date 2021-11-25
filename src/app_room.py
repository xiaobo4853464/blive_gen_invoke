"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""
from tiny import grpc_call


class App_room(object):

    def __init__(self, service_name):
        self.service_name = service_name

    @grpc_call(path="/xlive/app-room/v1/share/shareConf")
    def share_conf(self, room_id, platform, target_platform=None, entry_from=None, req_biz=None):
        """### 房间分享信息"""


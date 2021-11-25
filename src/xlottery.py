"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""
from tiny import grpc_call


class Xlottery(object):

    def __init__(self, service_name):
        self.service_name = service_name

    @grpc_call(path="/live.xlottery.v1.Guard/Start")
    def start(self, uid=None, ruid=None, roomid=None, privilege=None, playflowID=None, sub_level=None, msg_id=None):
        """### 开启抽奖"""

    @grpc_call(path="/live.xlottery.v1.Guard/Join")
    def join(self, roomid, id, type, uid=None):
        """### 加入抽奖"""

    @grpc_call(path="/live.xlottery.v1.Guard/Check")
    def check(self, roomid, uid=None, isGetUser=None, isGetPayFlow=None):
        """### 房间页是否有抽奖"""

    @grpc_call(path="/live.xlottery.v1.Guard/JoinGuard")
    def join_guard(self, roomid, id, type, uid=None):
        """### 新版即时抽奖"""


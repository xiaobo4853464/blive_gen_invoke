"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""
from tiny import grpc_call


class Live_dm(object):

    def __init__(self, service_name):
        self.service_name = service_name

    @grpc_call(path="/live.livedm.v1.CM/EntryBroadcast")
    def entry_broadcast(self, data, msgtype, uid=None, roomid=None, area2id=None, area1id=None, ignore_room=None, timepoint=None, vid=None, cmd=None, **from_):
        """### 无标题"""

    @grpc_call(path="/live.livedm.v1.CM/BanBroadcast")
    def ban_broadcast(self, data, msgtype, uid=None, roomid=None, area2id=None, area1id=None, ignore_room=None, timepoint=None, vid=None, cmd=None, **from_):
        """### 无标题"""

    @grpc_call(path="/live.livedm.v1.CM/GiftBroadcast")
    def gift_broadcast(self, data, msgtype, uid=None, roomid=None, area2id=None, area1id=None, ignore_room=None, timepoint=None, vid=None, cmd=None, **from_):
        """### 无标题"""

    @grpc_call(path="/live.livedm.v1.CM/BroadcastRoom")
    def broadcast_room(self, msgtype, cmd, data, ignore_room=None, roomids=None, zone_id=None, group=None, from_room=None, additional_room_id=None):
        """###房间级别广播"""

    @grpc_call(path="/live.livedm.v1.CM/BroadcastUser")
    def broadcast_user(self, msgtype=None, user_ids=None, message=None, group=None, cmd=None, from_room=None):
        """###用户级别广播"""

    @grpc_call(path="/live.livedm.v1.CM/BroadUserLopitalACK")
    def broad_user_lopital_a_c_k(self, sequence=None, ack=None, uid=None):
        """###用户消息必答ACK"""

    @grpc_call(path="/live.livedm.v1.CM/BroadUserLopitalSend")
    def broad_user_lopital_send(self, user_id=None, message=None, group=None, cmd=None, from_room=None, ack=None):
        """###必答用户消息"""


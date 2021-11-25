"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""
from tiny import grpc_call


class Xfetter(object):

    def __init__(self, service_name):
        self.service_name = service_name

    @grpc_call(path="/live.xfetter.relation/GetUserOnlineAnchorList")
    def get_user_online_anchor_list(self, uid=None, uip=None, is_https=None, req_biz=None, platform=None, build=None, device_name=None, last_request_timestamp=None, limitation=None, network=None, header_ishttps=None):
        """### GetUserOnlineAnchorList 获取某一用户首页在线主播列表 (客户端)"""

    @grpc_call(path="/live.xfetter.relation/GetFollowType")
    def get_follow_type(self, uid=None):
        """### GetFollowType 获取某一用户调用关系链"""

    @grpc_call(path="/live.xfetter.relation/GetUserOnlineAnchorListHistorical")
    def get_user_online_anchor_list_historical(self, uid=None, uip=None, is_https=None, req_biz=None, platform=None, build=None, device_name=None, last_request_timestamp=None, limitation=None, network=None, header_ishttps=None):
        """### GetUserOnlineAnchorListHistorical 获取某一用户首页在线主播列表（历史版本客户端）"""

    @grpc_call(path="/live.xfetter.relation/GetUserLiveRoomsWeb")
    def get_user_live_rooms_web(self, uid=None, page=None, pagesize=None, sort_type=None):
        """### GetUserLiveRoomsWeb 获取某一用户关注主播在播列表（Web端）"""

    @grpc_call(path="/live.xfetter.relation/GetUserLiveAnchorMap")
    def get_user_live_anchor_map(self, uid=None):
        """### GetUserLiveAnchorMap 获取某一用户关注主播信息Map"""

    @grpc_call(path="/live.xfetter.relation/GetFollowInfo")
    def get_follow_info(self, uid, target_uid, is_need_fan_count=None, is_need_attention_count=None):
        """### 获取用户与目标用户的关系以及目标用户的粉丝数和关注数(粉丝数和关注数可选)"""

    @grpc_call(path="/live.xfetter.relation/IsUserFollow")
    def is_user_follow(self, uid, target_uid):
        """### 获取用户与目标用户的关系"""

    @grpc_call(path="/live.xfetter.relation/IsUserFollowBatch")
    def is_user_follow_batch(self, uid, target_uid_list):
        """### 获取用户与目标用户列表的关系"""


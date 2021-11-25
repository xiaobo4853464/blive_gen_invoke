from tiny import grpc_call

class Xfetter(object):
    def __init__(self,service_name):
        self.service_name=service_name
    
    @grpc_call(path="/live.xfetter.ComponentMng/GetComponentList")
    def get_component_list(self, page, page_size):
        """### 获取通用关注组件列表"""

    @grpc_call(path="/live.xfetter.ComponentMng/SaveComponent")
    def save_component(self, room_ids, name, id=None, button_color=None):
        """### 保存（新增/更新）通用关注组件配置"""

    @grpc_call(path="/live.xfetter.ComponentMng/DeleteComponent")
    def delete_component(self, id):
        """### 删除通用关注组件配置"""

    @grpc_call(path="/live.xfetter.ComponentMng/GetReleasedRealTimeUIDList")
    def get_released_real_time_u_i_d_list(self, id, page, page_size):
        """### 获取实时发布中已发布uid列表"""

    @grpc_call(path="/live.xfetter.ComponentMng/PublishRealTimeUID")
    def publish_real_time_u_i_d(self, component_id, uid, show_duration):
        """### 实时发布中发布uid"""

    @grpc_call(path="/live.xfetter.Fetter/GetUserLiveRoomsApp")
    def get_user_live_rooms_app(self, uid=None, uip=None, is_https=None, req_biz=None, platform=None, build=None, device_name=None, last_request_timestamp=None, limitation=None, network=None, header_ishttps=None):
        """### APP端动态获取关注的开播直播间、Q值排序"""

    @grpc_call(path="/live.xfetter.Fetter/GetFollowingStreamingRoomsApp")
    def get_following_streaming_rooms_app(self, uid, score_type=None, max_count=None, buvid=None):
        """### APP首页用户关注开播卡片灰度策略排序"""

    @grpc_call(path="/live.xfetter.Fetter/GetUserFollowingStreamingRoomsApp")
    def get_user_following_streaming_rooms_app(self, uid, buvid=None, offset=None, num=None, score_type=None, **from_):
        """### APP首页用户关注开播卡片排序"""

    @grpc_call(path="/live.xfetter.Fetter/GetUserFollowingOfflineRoomsApp")
    def get_user_following_offline_rooms_app(self, uid, offset=None, num=None):
        """### APP首页用户关注未开播卡片排序"""

    @grpc_call(path="/live.xfetter.Fetter/GetUserFollowingOnlineRooms")
    def get_user_following_online_rooms(self, uid=None, uip=None, is_https=None, req_biz=None, platform=None, build=None, device_name=None, limitation=None, network=None, buvid=None):
        """### 获取用户当前关注在播房间信息列表（无排序）"""

    @grpc_call(path="/live.xfetter.Fetter/GetUserFollowingOnlineRoomsAppDynamic")
    def get_user_following_online_rooms_app_dynamic(self, uid=None, uip=None, is_https=None, req_biz=None, platform=None, build=None, device_name=None, limitation=None, network=None, buvid=None):
        """### App 动态首页获取用户当前关注在播房间信息列表灰度策略排序"""

    @grpc_call(path="/live.xfetter.Fetter/GetUserFollowingOnlineRoomsWebDynamic")
    def get_user_following_online_rooms_web_dynamic(self, uid=None, page=None, pagesize=None, sort_type=None):
        """### Web 动态首页获取用户当前关注在播房间信息列表灰度策略排序"""

    @grpc_call(path="/live.xfetter.Fetter/GetUserFollowingOnlineRoomAppDynamicFooterTab")
    def get_user_following_online_room_app_dynamic_footer_tab(self, uid, platform=None, device=None):
        """### App 底tab获取一个用户当前关注的在播房间"""

    @grpc_call(path="/live.xfetter.Fetter/GetUserFollowingOnlineRoomAppDynamicFooterTabWithScore")
    def get_user_following_online_room_app_dynamic_footer_tab_with_score(self, uid, platform=None, device=None):
        """### App 底tab获取一个用户当前关注的在播房间主播uid和对应算法打分"""

    @grpc_call(path="/live.xfetter.Fetter/FilterOfflineUids")
    def filter_offline_uids(self, uid_list):
        """### 过滤未开播的uid"""

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

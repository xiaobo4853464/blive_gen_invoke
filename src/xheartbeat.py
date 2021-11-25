from tiny import grpc_call

class Xheartbeat(object):
    def __init__(self,service_name):
        self.service_name=service_name
    
    @grpc_call(path="/live.xheartbeat.v1.heartbeat/HeartBeat")
    def heart_beat(self, platform, buvid, room_id, parent_id, area_id, timestamp, secret_key, sign, watch_time, client_ts, uuid=None, seq_id=None, uid=None, target_id=None, target_level=None, jump_from=None, gu_id=None, play_type=None, play_url=None, s_time=None, data_behavior_id=None, data_source_id=None, up_session=None, visit_id=None, watch_status=None, click_id=None, session_id=None, player_type=None, version=None, build=None, mobi_app=None, ip=None):
        """###处理正常心跳"""

    @grpc_call(path="/live.xheartbeat.v1.heartbeat/MobileExit")
    def mobile_exit(self, platform, buvid, room_id, parent_id, area_id, timestamp, secret_key, sign, watch_time, client_ts, uuid=None, seq_id=None, uid=None, is_patch=None, target_id=None, target_level=None, jump_from=None, gu_id=None, play_type=None, play_url=None, s_time=None, data_behavior_id=None, data_source_id=None, up_session=None, visit_id=None, watch_status=None, click_id=None, session_id=None, player_type=None, version=None, ip=None):
        """###处理App退出,新版本废弃使用"""

    @grpc_call(path="/live.xheartbeat.v1.heartbeat/GetUserWatchTime")
    def get_user_watch_time(self, uid, atype=None, aid=None, roomid=None, areaid2=None, areaid1=None, series=None, need_bitset=None):
        """###获取用户观看时长"""

    @grpc_call(path="/live.xheartbeat.v1.heartbeat/BatchGetUserWatchTime")
    def batch_get_user_watch_time(self, uid, roomid=None, series=None):
        """###批量获取用户观看时长"""

    @grpc_call(path="/live.xheartbeat.v1.heartbeat/GetWatchTaskConfList")
    def get_watch_task_conf_list(self, task_id=None, activity_ids=None):
        """### 获取当前的观看任务列表"""

    @grpc_call(path="/live.xheartbeat.v1.heartbeat/UpdateBaseTaskConfStatusOff")
    def update_base_task_conf_status_off(self, activity_id, channel_id):
        """### 更新状态"""

    @grpc_call(path="/live.xheartbeat.v1.heartbeat/GetBaseTaskConfList")
    def get_base_task_conf_list(self, activity_id, channel_id):
        """### 获取当前的基础任务列表"""

    @grpc_call(path="/live.xheartbeat.v1.heartbeat/GetUserTotalWatchTime")
    def get_user_total_watch_time(self, uid, room_id, start_ts, end_ts):
        """###获取用户一段时间的累积观看时长"""

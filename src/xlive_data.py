from tiny import grpc_call

class Xlive_data(object):
    def __init__(self,service_name):
        self.service_name=service_name
    
    @grpc_call(path="/live.xlivedata.v1.settlement/LiveKeyByTimeId")
    def live_key_by_time_id(self, uid=None, start_time=None, end_time=None):
        """### starttime < 开播时间/切场次 < endtime"""

    @grpc_call(path="/live.xlivedata.v1.record/GetLastLiveInfo")
    def get_last_live_info(self, roomids=None):
        """### 无标题"""

    @grpc_call(path="/live.xlivedata.v1.record/GetTotalLiveTime")
    def get_total_live_time(self, room_id=None):
        """### 无标题"""

    @grpc_call(path="/live.xlivedata.v1.record/GetLiveInfoByLiveKey")
    def get_live_info_by_live_key(self, room_id, live_key):
        """### 无标题"""

    @grpc_call(path="/live.xlivedata.v1.record/GetLiveInfoByDate")
    def get_live_info_by_date(self, room_id, start_date, end_date, area_v2_parent_id=None, area_v2_id=None, area_parent_ids=None, except_area_v2_ids=None, day_hour=None, effective_time=None, need_cache=None, area_ids=None):
        """### GetLiveInfoByDate 根据日期获取主播直播信息"""

    @grpc_call(path="/live.xlivedata.v1.record/GetValidLiveInfo")
    def get_valid_live_info(self, room_id=None, date=None, start_date=None, end_date=None, area_v2_parent_ids=None, area_v2_ids=None):
        """### GetValidLiveInfo 获取有效开播信息"""

    @grpc_call(path="/live.xlivedata.v1.record/GetRealTimeLiveInfo")
    def get_real_time_live_info(self, roomids=None, except_area_parent_ids=None, except_area_ids=None):
        """### 获取主播当天实时直播时长信息"""

    @grpc_call(path="/live.xlivedata.v1.record/GetRealTimeLiveInfoExceptAreaIds")
    def get_real_time_live_info_except_area_ids(self, start_time, end_time, roomids=None, area_parent_ids=None, except_area_ids=None):
        """### 指定一级分区排除二级分区"""

    @grpc_call(path="/live.xlivedata.v1.record/GetRealTimeLiveInfoByAreaIds")
    def get_real_time_live_info_by_area_ids(self, start_time, end_time, roomids=None, area_ids=None):
        """### 获取主播当天指定二级分区的实时直播时长信息"""

    @grpc_call(path="/live.xlivedata.v1.record/GetLiveDetails")
    def get_live_details(self, start_time, end_time, roomids=None):
        """### GetLiveDetails 获取有效直播详情"""

    @grpc_call(path="/live.xlivedata.v1.record/GetLiveKeyByTime")
    def get_live_key_by_time(self, room_id, start_time, end_time):
        """### 查询 live_room_flow.ap_room_flow_0 表"""

    @grpc_call(path="/live.xlivedata.v1.record/GetHistory")
    def get_history(self, live_ids):
        """### GetHistory 获取历史直播卡片信息"""

    @grpc_call(path="/live.xlivedata.v1.record/GetRoomEfDays")
    def get_room_ef_days(self, room_ids, type=None):
        """### GetRoomEfDays 获取某个时间段内主播的有效直播天数"""

    @grpc_call(path="/live.xlivedata.v1.record/GetDau")
    def get_dau(self, room_id, date, start_date=None, end_date=None):
        """### GetDau 获取房间dau数据"""

    @grpc_call(path="/live.xlivedata.v1.record/GetRecordList")
    def get_record_list(self, start_date, end_date, roomid=None, area_ids=None, uid=None):
        """### 获取主播在指定分区、指定时间段的直播记录"""

    @grpc_call(path="/live.xlivedata.v1.record/GetRecordListPage")
    def get_record_list_page(self, start_date, end_date, roomid=None, validate:"required"=None, page_size=None):
        """### 获取主播在指定时间段的直播记录(有分页 没有分区筛选)"""

    @grpc_call(path="/live.xlivedata.v1.record/GetRecordListNew")
    def get_record_list_new(self, start_date, end_date, roomid=None, area_ids=None, uid=None):
        """### 获取主播在对应时间段内的直播数据"""

    @grpc_call(path="/live.xlivedata.v1.record/GetFirstRecordByLiveId")
    def get_first_record_by_live_id(self, uid, live_id):
        """### 根据liveid获主播最近一条开播数据"""

    @grpc_call(path="/live.xlivedata.v1.record/GetSubByLiveId")
    def get_sub_by_live_id(self, live_id, uid):
        """### 根据liveid获主播sub_sessions_key"""

    @grpc_call(path="/live.xlivedata.v1.record/GetBroadcastCountByRoomId")
    def get_broadcast_count_by_room_id(self, room_id=None, start_date=None, end_date=None):
        """### 根据roomId获取主播时间段内的开播次数"""

    @grpc_call(path="/live.xlivedata.v1.anchortag/GetAnchorList")
    def get_anchor_list(self, page_number, page_size, parent_area_id, area_id, type=None, uid=None, uname=None, room_id=None):
        """### 根据一级分区和二级分区ID获取符合打标准入标准的分区主播列表"""

    @grpc_call(path="/live.xlivedata.v1.anchortag/GetAnchorTagList")
    def get_anchor_tag_list(self, parent_area_id, area_id, uid):
        """### 根据一级分区和二级分区ID获取该分区下标签列表，返回分区"""

    @grpc_call(path="/live.xlivedata.v1.anchortag/GetNextUntagAnchor")
    def get_next_untag_anchor(self, parent_area_id, area_id, uid=None):
        """### 获取“下一个”未打标的主播"""

    @grpc_call(path="/live.xlivedata.v1.anchortag/LockAnchorTagEdit")
    def lock_anchor_tag_edit(self, uid, parent_area_id, area_id, last_operate_ts):
        """### 获取编辑锁"""

    @grpc_call(path="/live.xlivedata.v1.anchortag/LockHoldHeartBeat")
    def lock_hold_heart_beat(self, uid, parent_area_id, area_id, last_operate_ts):
        """### 持锁心跳，每30秒请求一次，以便服务端确保持锁人活着，超时未收到心跳就释放锁"""

    @grpc_call(path="/live.xlivedata.v1.anchortag/UnlockAnchorTagEdit")
    def unlock_anchor_tag_edit(self, uid, parent_area_id, area_id):
        """### 释放编辑锁"""

    @grpc_call(path="/live.xlivedata.v1.live/RegisterLiveTimeMileStone")
    def register_live_time_mile_stone(self, source_identify, start_at, end_at, notify_live_time_before_finish, task_type, mile_stone_value, specific_parent_area_ids=None, specific_area_ids=None, except_area_ids=None, specific_platforms=None, description=None):
        """### 注册里程碑事件"""

    @grpc_call(path="/live.xlivedata.v1.live/UpdateLiveTimeMileStone")
    def update_live_time_mile_stone(self, mile_stone_id, source_identify, update_fields, is_delete=None, specific_parent_area_ids=None, specific_area_ids=None, except_area_ids=None, specific_platforms=None, start_at=None, end_at=None, notify_live_time_before_finish=None, task_type=None, description=None, mile_stone_value=None):
        """### 更新"""

    @grpc_call(path="/live.xlivedata.v1.live/AllLiveTimeMileStone")
    def all_live_time_mile_stone(self, all=None, time=None):
        """### 里程碑事件列表 start <= now << end"""

    @grpc_call(path="/live.xlivedata.v1.Chemcenser/GetPopulationByStreamerEvent")
    def get_population_by_streamer_event(self, interacting_event=None):
        """### GetPopulationByStreamerEvent 获取当前进行各个交互事件的主播人数。"""

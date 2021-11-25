from tiny import grpc_call

class Dao_anchor(object):
    def __init__(self,service_name):
        self.service_name=service_name
    
    @grpc_call(path="/live.daoanchor.v1.DaoAnchor/FetchRoomByIDs")
    def fetch_room_by_i_ds(self, room_ids=None, uids=None, fields=None, default_fields=None):
        """### 查询房间信息"""

    @grpc_call(path="/live.daoanchor.v1.DaoAnchor/RoomOnlineListByArea")
    def room_online_list_by_area(self, area_ids=None):
        """### 分区在线房间列表(只返回room_id列表，不传分区，默认查找所有)"""

    @grpc_call(path="/live.daoanchor.v1.DaoAnchor/RoomOnlineInfoByArea")
    def room_online_info_by_area(self, live_parent_area_ids=None, live_area_ids=None, fields=None, not_filter_offline_area=None):
        """### 分区在线房间信息列表(返回房间在播列表房间信息，不传分区号默认查找所有)"""

    @grpc_call(path="/live.daoanchor.v1.DaoAnchor/RoomOnlineListFromDB")
    def room_online_list_from_d_b(self, filterLocked=None, filterHiddened=None):
        """### 获取在播列表from DB (room-service切读专用,若需要用到其他业务，请提前联系服务负责人)"""

    @grpc_call(path="/live.daoanchor.v1.DaoAnchor/RoomCreate")
    def room_create(self, uid, room_id=None):
        """### 房间创建"""

    @grpc_call(path="/live.daoanchor.v1.DaoAnchor/RoomUpdate")
    def room_update(self, fields, room_id, title=None, cover=None, tags=None, background=None, description=None, live_start_time=None, live_screen_type=None, lock_status=None, lock_time=None, hidden_time=None, area_id=None, anchor_round_switch=None, anchor_record_switch=None, live_type=None, room_shield=None):
        """### 房间信息更新"""

    @grpc_call(path="/live.daoanchor.v1.DaoAnchor/RoomExtendUpdate")
    def room_extend_update(self, fields, room_id, keyframe=None, danmu_count=None, popularity_count=None, audience_count=None, gift_count=None, gift_gold_amount=None, gift_gold_count=None, live_id=None, first_live_time=None, short_id=None, sub_session_key=None, live_info=None, app_background=None):
        """### 房间扩展信息更新"""

    @grpc_call(path="/live.daoanchor.v1.DaoAnchor/RoomExtendIncre")
    def room_extend_incre(self, req_id, fields, room_id, danmu_count=None, popularity_count=None, audience_count=None, gift_count=None, gift_gold_amount=None, gift_gold_count=None):
        """### 房间信息增量更新"""

    @grpc_call(path="/live.daoanchor.v1.DaoAnchor/RoomTagCreate")
    def room_tag_create(self, room_id, tag_id, tag_sub_id=None, tag_value=None, tag_ext=None, tag_expire_at=None):
        """### 房间Tag创建"""

    @grpc_call(path="/live.daoanchor.v1.DaoAnchor/AnchorUpdate")
    def anchor_update(self, fields, uid, profile_type=None, san_score=None, round_status=None, record_status=None, exp=None):
        """### 主播信息更新"""

    @grpc_call(path="/live.daoanchor.v1.DaoAnchor/AnchorIncre")
    def anchor_incre(self, req_id, fields, uid, san_score=None, exp=None):
        """### 主播信息增量更新"""

    @grpc_call(path="/live.daoanchor.v1.DaoAnchor/FetchAreas")
    def fetch_areas(self, area_id=None, show_all=None):
        """### 根据父分区号查询子分区"""

    @grpc_call(path="/live.daoanchor.v1.DaoAnchor/DeleteTagByID")
    def delete_tag_by_i_d(self, room_id, tag_id, tag_sub_id):
        """### 删除某房间的一个标签"""

    @grpc_call(path="/live.daoanchor.v1.DaoAnchor/PendantCreate")
    def pendant_create(self, type, name, priority, position=None, bg_color=None, bg_pic=None):
        """### 创建/注册房间角标挂件（type & name 唯一确定一个 pendant）"""

    @grpc_call(path="/live.daoanchor.v1.DaoAnchor/PendantAddToRoom")
    def pendant_add_to_room(self, type, name, priority, room_id, expire_at, position=None, bg_color=None, bg_pic=None, value=None, area_id=None, increase_ttl=None):
        """### 仅用于为当前 RoomService 添加角标挂件提供双写支持"""

    @grpc_call(path="/live.daoanchor.v1.DaoAnchor/GetTagListByRoomId")
    def get_tag_list_by_room_id(self, room_id=None):
        """### 获取房间的所有标签"""

    @grpc_call(path="/live.daoanchor.v1.DaoAnchor/PendantUpdate")
    def pendant_update(self, id, position=None, priority=None, bg_color=None, bg_pic=None):
        """###更新角标"""

    @grpc_call(path="/live.daoanchor.v1.DaoAnchor/PendantQuery")
    def pendant_query(self, id=None, type=None, name=None, position=None, priority=None, page=None, page_size=None):
        """###查询角标"""

    @grpc_call(path="/live.daoanchor.v1.DaoAnchor/QueryAreaInfo")
    def query_area_info(self, old_area_ids=None, new_area_ids=None):
        """### 根据分区ID得到分区的信息, 支持新分区(二级分区)和老分区"""

    @grpc_call(path="/live.daoanchor.v1.DaoAnchor/AddPendantToRoom")
    def add_pendant_to_room(self, room_id, pendant_id, expire_at, value=None, area_id=None, increase_ttl=None):
        """### 为房间创建角标数据"""

    @grpc_call(path="/live.daoanchor.v1.DaoAnchor/GetTagRoomList")
    def get_tag_room_list(self, tag_id, tag_sub_id, page, page_size):
        """### 根据 tag_id tag_sub_id 获取房间列表(批次间返回的数据有可能会少量重复，建议调用方去重)"""

    @grpc_call(path="/live.daoanchor.v1.DaoAnchor/FlushCacheById")
    def flush_cache_by_id(self, room_id, table_name, uid=None):
        """### del房间缓存, 目前只给job调用"""

    @grpc_call(path="/live.daoanchor.v1.DaoAnchor/GetAllPendantList")
    def get_all_pendant_list(self, room_ids):
        """### 批量获取直播间的角标信息，不过滤优先级"""

    @grpc_call(path="/live.daoanchor.v1.Popularity/GetPopularityByRoomIds")
    def get_popularity_by_room_ids(self, roomIds=None):
        """### GetPopularityByRoomIds 获取房间实时人气值"""

    @grpc_call(path="/live.daoanchor.v0.Popularity/IncrPopularity")
    def incr_popularity(self, total_coin=None, coin_type=None, room_id=None):
        """### IncrPopularity 增加人气值"""

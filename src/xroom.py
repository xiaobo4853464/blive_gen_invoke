"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""
from tiny import grpc_call


class Xroom(object):

    def __init__(self, service_name):
        self.service_name = service_name

    @grpc_call(path="/live.xroom.v1.ShortIdMng/shortIdList")
    def short_id_list(self, status=None, short_id=None, short_id_range_start=None, short_id_range_end=None, page=None, pagesize=None):
        """###短号库存列表"""

    @grpc_call(path="/live.xroom.v1.ShortIdMng/shortIdAdd")
    def short_id_add(self, short_id, action_user=None):
        """###短号库存添加"""

    @grpc_call(path="/live.xroom.v1.ShortIdMng/shortIdDel")
    def short_id_del(self, short_id, action_user=None):
        """###短号库存删除"""

    @grpc_call(path="/live.xroom.v1.ShortIdMng/shortIdInfo")
    def short_id_info(self, short_id):
        """###手动输入短位号时，查询短位号信息"""

    @grpc_call(path="/live.xroom.v1.ShortIdMng/shortRoomList")
    def short_room_list(self, status=None, short_id=None, short_id_range_start=None, short_id_range_end=None, page=None, pagesize=None, roomid=None, valid_type=None):
        """###短号管理列表"""

    @grpc_call(path="/live.xroom.v1.ShortIdMng/shortRoomAdd")
    def short_room_add(self, short_id, roomid, valid_type, apply_reason=None, operate_user_name=None, start_time=None, end_time=None):
        """###添加短号"""

    @grpc_call(path="/live.xroom.v1.ShortIdMng/shortRoomBack")
    def short_room_back(self, short_id, end_reason, status=None, roomid=None, uid=None, operate_user_name=None):
        """###回收短号"""

    @grpc_call(path="/live.xroom.v1.ShortIdMng/roomIdAndShortIdInfo")
    def room_id_and_short_id_info(self, roomid):
        """###新增或续约短位号时，房间号信息和短位号信息展示"""

    @grpc_call(path="/live.xroom.v1.ShortIdMng/shortRoomListExport")
    def short_room_list_export(self, status=None, short_id=None, short_id_range_start=None, short_id_range_end=None, page=None, pagesize=None, roomid=None, valid_type=None):
        """###短位号管理页面导出接口"""

    @grpc_call(path="/live.xroom.v1.ShortIdMng/shortIdListExport")
    def short_id_list_export(self, status=None, short_id=None, short_id_range_start=None, short_id_range_end=None, page=None, pagesize=None):
        """###短位号库存页面导出接口"""


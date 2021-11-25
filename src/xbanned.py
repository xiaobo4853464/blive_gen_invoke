from tiny import grpc_call

class Xbanned(object):
    def __init__(self,service_name):
        self.service_name=service_name
    
    @grpc_call(path="/live.xbanned.v1.silent/GetRoomSilent")
    def get_room_silent(self, room_id):
        """### 获取房间禁言"""

    @grpc_call(path="/live.xbanned.v1.silent/RoomSilent")
    def room_silent(self, room_id, type, uid, minute=None, level=None, mobi_app=None):
        """### 设置房间禁言"""

    @grpc_call(path="/live.xbanned.v1.silent/RoomLiveOff")
    def room_live_off(self, room_id):
        """### 关播时调用，清除一些数据，如禁言信息"""

    @grpc_call(path="/live.xbanned.v1.silent/IsBlockUser")
    def is_block_user(self, uid, roomid, type=None):
        """### 查询是否被主播禁言"""

    @grpc_call(path="/live.xbanned.v1.silent/GetBlockListSimple")
    def get_block_list_simple(self, room_id, pn, ps):
        """### 过缓存的主播禁言名单（非后台用）"""

    @grpc_call(path="/live.xbanned.v1.silent/AddSilentUser")
    def add_silent_user(self, tuid, room_id, hour, uid=None, mobi_app=None, op_type=None):
        """### 用户禁言"""

    @grpc_call(path="/live.xbanned.v1.silent/DelSilentUser")
    def del_silent_user(self, tuid, room_id, uid=None, mobi_app=None, op_type=None):
        """### 解禁"""

    @grpc_call(path="/live.xbanned.v1.silent/GetSilentUserList")
    def get_silent_user_list(self, room_id, pn, ps, uid=None, search=None, op_type=None):
        """### 用户禁言列表"""

    @grpc_call(path="/live.xbanned.v1.namelist/Verify")
    def verify(self, uid, type):
        """### 是否在名单里"""

    @grpc_call(path="/live.xbanned.v1.namelist/AdminList")
    def admin_list(self, uid, type, page, size):
        """### 后台管理-查询列表"""

    @grpc_call(path="/live.xbanned.v1.namelist/AdminDel")
    def admin_del(self, uid, type, sub_type=None):
        """### 后台管理-删除列表"""

    @grpc_call(path="/live.xbanned.v1.SiteBlock/IsSiteBlockUser")
    def is_site_block_user(self, uid):
        """### 是否被封禁的用户，包了一层Verify"""

    @grpc_call(path="/live.xbanned.v1.SiteBlock/GetSiteBlockStatus")
    def get_site_block_status(self, uid):
        """### 获取封禁状态"""

    @grpc_call(path="/live.xbanned.v1.SiteBlock/UnBlock")
    def un_block(self, uid, mobi_app=None):
        """### 解封"""

    @grpc_call(path="/live.xbanned.v1.SiteBlock/GetManageList")
    def get_manage_list(self, pn, ps, uid=None):
        """### 获取列表"""

    @grpc_call(path="/live.xbanned.v1.SiteBlock/MultiAddBlock")
    def multi_add_block(self, days, uids=None, mobi_app=None):
        """### 批量封禁"""

    @grpc_call(path="/live.xbanned.v1.user/Verify")
    def verify(self, uid, biz_code, roomid=None):
        """### 无标题"""

    @grpc_call(path="/live.xbanned.v1.user/IsSiteBlockUser")
    def is_site_block_user(self, uid):
        """### 是否被封禁的用户，包了一层Verify"""

    @grpc_call(path="/live.xbanned.v1.Black/GetBlackList")
    def get_black_list(self, uid, pn=None, ps=None):
        """### 主站拉黑获取接口"""

    @grpc_call(path="/live.xbanned.v1.Black/AddBlack")
    def add_black(self, uid, tuid, spmid=None, mobi_app=None):
        """### 主站拉黑接口"""

    @grpc_call(path="/live.xbanned.v1.Black/DelBlack")
    def del_black(self, uid, tuid, spmid=None, mobi_app=None):
        """### 主站删除拉黑接口"""

    @grpc_call(path="/live.xbanned.v1.Black/IsBlackUser")
    def is_black_user(self, uid, tuid):
        """### 无标题"""

    @grpc_call(path="/live.xbanned.v1.shield/Filter")
    def filter(self, area, message, mid, uip, id=None, oid=None, keys=None):
        """### 接主站屏蔽词"""

    @grpc_call(path="/live.xbanned.v1.shield/Hit")
    def hit(self, area, msg, type_id=None):
        """### 主站屏蔽词命中"""

    @grpc_call(path="/live.xbanned.v1.shield/ShieldContent")
    def shield_content(self, uid, content):
        """### 主播或者后台设置的屏蔽词"""

    @grpc_call(path="/live.xbanned.v1.shield/GetShieldInfo")
    def get_shield_info(self, uid, is_mobile=None):
        """### 获取屏蔽信息"""

    @grpc_call(path="/live.xbanned.v1.shield/GetShieldUser")
    def get_shield_user(self, uid):
        """### 获取被屏蔽用户信息"""

    @grpc_call(path="/live.xbanned.v1.shield/GetDanmuShield")
    def get_danmu_shield(self, uid):
        """### 弹幕屏蔽规则"""

    @grpc_call(path="/live.xbanned.v1.shield/IsShieldUser")
    def is_shield_user(self, uid, target_uid):
        """### 是否被屏蔽"""

    @grpc_call(path="/live.xbanned.v1.shield/GetAdminShieldRule")
    def get_admin_shield_rule(self, room_id=None):
        """### 运营规则查询"""

    @grpc_call(path="/live.xbanned.v1.shield/AddShieldKeyword")
    def add_shield_keyword(self, keyword, room_id=None, uid=None, mobi_app=None, op_type=None):
        """### 添加屏蔽词"""

    @grpc_call(path="/live.xbanned.v1.shield/DelShieldKeyword")
    def del_shield_keyword(self, keyword, room_id=None, uid=None, mobi_app=None, op_type=None):
        """### 删除屏蔽词"""

    @grpc_call(path="/live.xbanned.v1.shield/GetKeywordList")
    def get_keyword_list(self, uid=None, room_id=None, is_mobile=None, op_type=None):
        """### 获取屏蔽词列表 room_id==0获取用户屏蔽词，room_id!=0房间屏蔽词"""

    @grpc_call(path="/live.xbanned.v2.silent/GetRoomSilent")
    def get_room_silent(self, room_id):
        """### 超管获取房间禁言"""

    @grpc_call(path="/live.xbanned.v2.silent/RoomSilentOff")
    def room_silent_off(self, room_id):
        """### 关闭超管房间禁言"""

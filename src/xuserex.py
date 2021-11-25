from tiny import grpc_call

class Xuserex(object):
    def __init__(self,service_name):
        self.service_name=service_name
    
    @grpc_call(path="/live.xuserex.v1.ConfDepot/get")
    def get(self, uid=None, target_id=None, type=None):
        """###* 查看用户配置"""

    @grpc_call(path="/live.xuserex.v1.ConfDepot/get_multi_target")
    def get_multi_target(self, uid=None, target_list=None, type=None):
        """###* 同个uid 同个type 多个targetid"""

    @grpc_call(path="/live.xuserex.v1.ConfDepot/del")
    def del_(self, uid=None, target_id=None, type=None):
        """###* 删除用户配置"""

    @grpc_call(path="/live.xuserex.v1.ConfDepot/delJsonContentKey")
    def del_json_content_key(self, uid=None, target_id=None, type=None, contentKey=None):
        """### 删除json类型content某个key"""

    @grpc_call(path="/live.xuserex.v1.ConfDepot/upsertJsonContent")
    def upsert_json_content(self, uid=None, target_id=None, type=None, contentKey=None, contentValue=None):
        """### 无标题"""

    @grpc_call(path="/live.xuserex.v1.RoomNotice/buy_guard")
    def buy_guard(self, uid, target_id):
        """### deprecated: 功能移除"""

    @grpc_call(path="/live.xuserex.v1.RoomNotice/set_task_finish")
    def set_task_finish(self, result=None):
        """### deprecated: 功能移除"""

    @grpc_call(path="/live.xuserex.v1.RoomNotice/renew_guard")
    def renew_guard(self, uid, target_id, guard_level, expired_time, auto_renew=None):
        """### 续费大航海提示"""

    @grpc_call(path="/live.xuserex.v1.Labs/InfoPlugs")
    def info_plugs(self, uid):
        """### Info 返回用户配置信息"""

    @grpc_call(path="/live.xuserex.v1.Labs/ConfigPlugs")
    def config_plugs(self, uid):
        """### Config 返回用户配置信息"""

    @grpc_call(path="/live.xuserex.v1.Labs/EditPlugs")
    def edit_plugs(self, uid, key, status=None, option=None):
        """### Edit 用户修改配置信息"""

    @grpc_call(path="/live.xuserex.v1.dmConfMng/GetByCid")
    def get_by_cid(self, color_id):
        """### 根据颜色id获取颜色信息"""

    @grpc_call(path="/live.xuserex.v1.dmConfMng/AddColor")
    def add_color(self, color, name, hint_msg, origin, weight=None, start_time=None, end_time=None, url=None, is_expire=None):
        """### 后台添加新弹幕颜色"""

    @grpc_call(path="/live.xuserex.v1.dmConfMng/DelColor")
    def del_color(self, id):
        """### 后台删除弹幕颜色"""

    @grpc_call(path="/live.xuserex.v1.dmConfMng/SetOnline")
    def set_online(self, id):
        """### 上线弹幕颜色"""

    @grpc_call(path="/live.xuserex.v1.dmConfMng/UpdateColor")
    def update_color(self, id, color, name, hint_msg, origin, weight=None, start_time=None, end_time=None, url=None, is_expire=None):
        """### 后台编辑弹幕颜色"""

    @grpc_call(path="/live.xuserex.v1.dmConfMng/ColorList")
    def color_list(self, page, page_size, name=None, color_id=None, status=None):
        """### 查询弹幕颜色"""

    @grpc_call(path="/live.xuserex.v1.dmConfig/GetByUIDRoomID")
    def get_by_u_i_d_room_i_d(self, uid=None, roomid=None):
        """### 元数据|根据uids获取全局或房间弹幕配置(长度、模式、颜色)"""

    @grpc_call(path="/live.xuserex.v1.dmConfig/WearForOld")
    def wear_for_old(self, uid=None, mode=None, roomid=None, color=None):
        """### 兼容接口,切换配置"""

    @grpc_call(path="/live.xuserex.v1.dmConfig/DanmakuConfig")
    def danmaku_config(self, roomid=None):
        """### 业务数据,迁移user-ex移动端获取弹幕配置接口"""

    @grpc_call(path="/live.xuserex.v1.dmConfig/GetDMConfigByGroup")
    def get_d_m_config_by_group(self, room_id, type=None, uid=None):
        """### 业务数据,迁移web端+app端获取弹幕配置接口, 使用group分类"""

    @grpc_call(path="/live.xuserex.v1.dmConfig/ColorList")
    def color_list(self, status):
        """### 查询后台弹幕颜色列表"""

    @grpc_call(path="/live.xuserex.v1.dmConfig/Add")
    def add(self, uid, type=None, value=None, roomid=None, expire_time=None):
        """### 更新弹幕属性"""

    @grpc_call(path="/live.xuserex.v1.dmConfig/Recycle")
    def recycle(self, uid, type=None, value=None, roomid=None, expire_time=None):
        """### 回收弹幕属性"""

    @grpc_call(path="/live.xuserex.v1.dmConfig/Wear")
    def wear(self, uid, type, value, roomid=None):
        """### 佩戴弹幕属性"""

    @grpc_call(path="/live.xuserex.v1.dmConfig/Debug_GetCache")
    def debug__get_cache(self, uids):
        """###  [Debug 内部调试接口]获取Cache和DB中的弹幕配置部分并解析"""

    @grpc_call(path="/live.xuserex.v1.dmConfig/Debug_ClearAllCache")
    def debug__clear_all_cache(self, uids):
        """###  [Debug 内部调试接口]清除所有cache"""

    @grpc_call(path="/live.xuserex.v1.dmConfig/Debug_ClearPHPAllCache")
    def debug__clear_p_h_p_all_cache(self, uid, type=None, value=None, roomid=None):
        """###  [Debug 内部调试接口]清除PHP所有cache"""

    @grpc_call(path="/live.xuserex.v1.dmConfig/Debug_GetPHPAllCache")
    def debug__get_p_h_p_all_cache(self, uid, type=None, value=None, roomid=None):
        """###  [Debug 内部调试接口]获取PHP所有cache"""

    @grpc_call(path="/live.xuserex.v1.xuserexData/GetXuserExData")
    def get_xuser_ex_data(self, uid=None, roomid=None, targetid=None, needBuyGuardNotice=None):
        """### 获取用户额外信息"""

    @grpc_call(path="/live.xuserex.v1.Bubble/GetBubble")
    def get_bubble(self, uid, room_id, category=None, sub_category=None):
        """### 根据用户id 房间号, 分区号, 子分区号获取当前生效最高等级的气泡框"""

    @grpc_call(path="/live.xuserex.v1.Bubble/GetByUIDRoomID")
    def get_by_u_i_d_room_i_d(self, uid, room_id=None, guard_level=None, bubble_id=None):
        """### 根据uid,room_id查询气泡框"""

    @grpc_call(path="/live.xuserex.v1.Bubble/Add")
    def add(self, uid, bubble_id, expired_at, desc, category=None, sub_category=None, room_id=None, weight=None):
        """### 添加气泡框"""

    @grpc_call(path="/live.xuserex.v1.Bubble/Recycle")
    def recycle(self, uid, bubble_id, expired_at, desc, category=None, sub_category=None, room_id=None, weight=None):
        """### 回收气泡框"""

    @grpc_call(path="/live.xuserex.v1.UserColor/GetNickNameColor")
    def get_nick_name_color(self, uid, room_id=None):
        """### 获取用户昵称颜色"""

    @grpc_call(path="/live.xuserex.v1.UserColor/Send")
    def send(self, uid, source, type, room_id=None, color=None, weight=None, add_time=None, expired_time=None):
        """### 向用户下发颜色"""

    @grpc_call(path="/live.xuserex.v1.UserColor/Recycle")
    def recycle(self, uid, source, type, room_id=None, color=None, weight=None, add_time=None, expired_time=None):
        """### 回收颜色"""

from tiny import grpc_call

class Live_dm(object):
    def __init__(self,service_name):
        self.service_name=service_name
    
    @grpc_call(path="/live.livedm.v1.DMReport/DanmuReport")
    def danmu_report(self, uid, tuid, msg, reason, reason_id, roomid, file_id=None, dm_type=None, img_url=None):
        """###服务相关接口"""

    @grpc_call(path="/live.livedm.v1.DMReport/GetList")
    def get_list(self, page_no, status=None, type=None, uid=None, uname=None, msg=None, start_time=None, end_time=None, id=None, block_reason=None, roomid=None, dm_type=None):
        """###后台相关接口"""

    @grpc_call(path="/live.livedm.v1.DMReport/MultiIgnore")
    def multi_ignore(self, ids, operate_user_name=None):
        """### 批量忽略"""

    @grpc_call(path="/live.livedm.v1.DMReport/MultiBlock")
    def multi_block(self, ids, reason, block_reason, days, operate_user_name=None):
        """### 批量封禁"""

    @grpc_call(path="/live.livedm.v1.DMReport/UnBlock")
    def un_block(self, tuid):
        """### 解封"""

    @grpc_call(path="/live.livedm.v1.DMReport/GetBlockInfo")
    def get_block_info(self, tuid, id=None):
        """###  获取用户被封禁记录"""

    @grpc_call(path="/live.livedm.v1.DMReport/GetManageBlockList")
    def get_manage_block_list(self, page_no, uid=None, uname=None):
        """### 获取封禁记录"""

    @grpc_call(path="/live.livedm.v1.manager/report")
    def report(self, reporter_id, dmid, vid, report_reason):
        """### 前端举报"""

    @grpc_call(path="/live.livedm.v1.manager/listDM")
    def list_d_m(self, vid, sort, page, sender_id=None, key_word=None, dmstatus=None, pagesize=None):
        """### (弹幕管理)后台获取某个直播回放的弹幕列表"""

    @grpc_call(path="/live.livedm.v1.manager/listReport")
    def list_report(self, status, page, reporter_target, pagesize=None, start_time=None, end_time=None, id=None, name=None, key_word=None):
        """### (举报管理)后台根据举报弹幕处理状态获取列表"""

    @grpc_call(path="/live.livedm.v1.manager/baninfo")
    def baninfo(self, target_id):
        """### (通用)获取用户封禁信息"""

    @grpc_call(path="/live.livedm.v1.manager/ignore")
    def ignore(self, dmids, operator):
        """### (举报管理)后台忽略举报"""

    @grpc_call(path="/live.livedm.v1.manager/resume")
    def resume(self, dmid):
        """### (弹幕管理)删除后恢复"""

    @grpc_call(path="/live.livedm.v1.DM/GetHistory")
    def get_history(self, roomid, scene=None):
        """###获取弹幕历史"""

    @grpc_call(path="/live.livedm.v1.DM/DelHistoryDMByRoomid")
    def del_history_d_m_by_roomid(self, roomid):
        """###删除历史弹幕"""

    @grpc_call(path="/live.livedm.v1.DM/AuditContentConfList")
    def audit_content_conf_list(self, page=None, pagesize=None):
        """###后台相关接口"""

    @grpc_call(path="/live.livedm.v1.DM/CreateAuditContentConf")
    def create_audit_content_conf(self, conf_title, start_time, end_time, conf_type=None, roomids=None):
        """###新增先审后发配置"""

    @grpc_call(path="/live.livedm.v1.DM/UdateAuditContentConf")
    def udate_audit_content_conf(self, id, conf_title, start_time, end_time, conf_type=None, roomids=None):
        """###修改先审后发配置"""

    @grpc_call(path="/live.livedm.v1.DM/DeleteAuditContentConf")
    def delete_audit_content_conf(self, id):
        """###删除先审后发配置"""

    @grpc_call(path="/live.livedm.v1.DM/GetAuditContentConf")
    def get_audit_content_conf(self, id):
        """###查询先审后发配置"""

    @grpc_call(path="/live.livedm.v1.DM/SetAuditorNum")
    def set_auditor_num(self, uname, id):
        """###注册审核人数"""

    @grpc_call(path="/live.livedm.v1.DM/GetAuditorNumAndDanmuNum")
    def get_auditor_num_and_danmu_num(self, id):
        """###获取当前审核人数以及弹幕池弹幕数量"""

    @grpc_call(path="/live.livedm.v1.DM/GetDanmuLists")
    def get_danmu_lists(self, id):
        """###获取待审核弹幕列表"""

    @grpc_call(path="/live.livedm.v1.DM/AuditBan")
    def audit_ban(self, uid, ban_days, operator, ban_evidence, operate_reason=None):
        """### rpc SetDanmuSendList (SetDanmuSendListReq) returns (google.protobuf.Empty){"""

    @grpc_call(path="/live.livedm.v1.DM/AuditBanInfo")
    def audit_ban_info(self, uid):
        """### 先审后发后获取用户封禁信息"""

    @grpc_call(path="/live.livedm.v1.DM/PreCheckSendMsg")
    def pre_check_send_msg(self, uid, roomid, msg, ip=None, msgtype=None):
        """### 弹幕内容预请求"""

    @grpc_call(path="/live.livedm.v1.WL/AddWhiteList")
    def add_white_list(self, list_addr, list_name, list_creator):
        """###添加白名单"""

    @grpc_call(path="/live.livedm.v1.WL/AddRoom")
    def add_room(self, room_ids, list_name, status=None, operator=None):
        """###添加房间白名单"""

    @grpc_call(path="/live.livedm.v1.WL/GetRoomList")
    def get_room_list(self, room_ids=None, page=None, page_size=None):
        """###查询房间白名单"""

    @grpc_call(path="/live.livedm.v1.WL/SetRoomStatus")
    def set_room_status(self, room_id, status=None, operator=None):
        """###设置单个房间白名单"""

    @grpc_call(path="/live.livedm.v1.WL/DelSingleRoom")
    def del_single_room(self, room_id, list_name=None, operator=None):
        """###删除对应房间的白名单信息"""

    @grpc_call(path="/live.livedm.v1.NoticeMsg/ListStyle")
    def list_style(self, page=None, pagesize=None):
        """###获取配置列表"""

    @grpc_call(path="/live.livedm.v1.NoticeMsg/GetStyle")
    def get_style(self, id=None):
        """###获取指定样式的详细配置"""

    @grpc_call(path="/live.livedm.v1.NoticeMsg/StopTask")
    def stop_task(self, id=None):
        """###停止任务"""

    @grpc_call(path="/live.livedm.v1.NoticeMsg/ListTask")
    def list_task(self, finished=None, page=None, pagesize=None):
        """###列出任务列表"""

    @grpc_call(path="/live.livedm.v1.PlayBack/getIndexInfo")
    def get_index_info(self, vid):
        """###获取回放页互动信息"""

    @grpc_call(path="/live.livedm.v1.PlayBack/getDMMsgByPlayBackID")
    def get_d_m_msg_by_play_back_i_d(self, vid, index=None):
        """###获取指定分段回访页信息"""

    @grpc_call(path="/live.livedm.v1.PlayBack/recordSendMsg")
    def record_send_msg(self, vid, msg, roomid, uid, dmid, bubble=None, ts=None, risk_result=None):
        """### 发送弹幕"""

    @grpc_call(path="/live.livedm.v1.PlayBack/getDMNumByVid")
    def get_d_m_num_by_vid(self, vid):
        """### 通过vid 获取弹幕数量"""

    @grpc_call(path="/live.livedm.v1.PlayBack/SearchDmList")
    def search_dm_list(self, begin_time, end_time, mid=None, room_id=None, msg=None, audit_res=None, audit_reason=None, page=None, page_size=None):
        """### 弹幕es数据搜索"""

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

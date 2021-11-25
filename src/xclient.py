from tiny import grpc_call

class Xclient(object):
    def __init__(self,service_name):
        self.service_name=service_name
    
    @grpc_call(path="/live.xclient.v1.Blink/Add")
    def add(self, title, type, device, startTime, endTime, imageUrl, webImageUrl=None, jumpPath=None, jumpTime=None, jumpPathType=None, webJumpPath=None, list_type=None, list_id=None, priority=None):
        """###Add 添加资源接口"""

    @grpc_call(path="/live.xclient.v1.Blink/Edit")
    def edit(self, id, jumpPathType=None, title=None, jumpPath=None, jumpTime=None, startTime=None, endTime=None, imageUrl=None, list_type=None, list_id=None, priority=None, type=None, device=None):
        """###Edit 编辑资源接口"""

    @grpc_call(path="/live.xclient.v1.Blink/Offline")
    def offline(self, id):
        """###Offline 下线资源接口"""

    @grpc_call(path="/live.xclient.v1.Blink/GetList")
    def get_list(self, type, page=None, pageSize=None, device_platform=None, status=None, startTime=None, endTime=None):
        """###GetList 获取资源列表"""

    @grpc_call(path="/live.xclient.v1.Blink/GetPlatformList")
    def get_platform_list(self, type=None):
        """###获取平台列表"""

    @grpc_call(path="/live.xclient.v1.Blink/GetInfo")
    def get_info(self, platform, build=None, uid=None, type=None):
        """###获取有效闪屏配置"""

    @grpc_call(path="/live.xclient.v1.Banner/getBanner")
    def get_banner(self, location, platform, module=None, position=None, build=None, uid=None, positions=None):
        """### 获取在线banner"""

    @grpc_call(path="/live.xclient.v1.Banner/GetJudgmentList")
    def get_judgment_list(self, creator=None, title=None, bannerId=None, status=None, location=None, start_time=None, end_time=None, page=None, page_size=None, username=None, platform=None):
        """### 获取待审核列表"""

    @grpc_call(path="/live.xclient.v1.Banner/BannerJudgment")
    def banner_judgment(self, username, id, reason=None, reason_id=None, **pass_):
        """### 审核员审核记录"""

    @grpc_call(path="/live.xclient.v1.Banner/UnJudgeBannerCount")
    def un_judge_banner_count(self, username=None):
        """### 获取用户创建的未通过的banner数量"""

    @grpc_call(path="/live.xclient.v1.Banner/GetJudgeInfo")
    def get_judge_info(self, banner_id=None):
        """### 获取单条banner的审核详情"""

    @grpc_call(path="/live.xclient.v1.Tab/mobileTab")
    def mobile_tab(self, roomid=None, uid=None):
        """###获取移动端tab"""

    @grpc_call(path="/live.xclient.v1.Tab/webTab")
    def web_tab(self, roomid=None, uid=None):
        """###获取web端tab"""

    @grpc_call(path="/live.xclient.v1.Tab/list")
    def list(self, roomid=None, sort=None, page=None, pagesize=None):
        """###获取所有tab列表"""

    @grpc_call(path="/live.xclient.v1.Tab/off")
    def off(self, roomid):
        """###下线某个tab恢复默认"""

    @grpc_call(path="/live.xclient.v1.Tab/getAllTabs")
    def get_all_tabs(self, roomid):
        """###获取某个房间所有的tab"""

    @grpc_call(path="/live.xclient.v1.Tab/sort")
    def sort(self, roomid, order=None):
        """###房间tab排序"""

    @grpc_call(path="/live.xclient.v1.Tab/filterTabByRoom")
    def filter_tab_by_room(self, room_id, filter_tab, start_time, end_time, source, source_id):
        """###批量房间屏蔽tab"""

    @grpc_call(path="/live.xclient.v1.activity/getActivity")
    def get_activity(self, uid=None, **from_):
        """### 无标题"""

    @grpc_call(path="/live.xclient.v1.BuildConn/getBuildConnList")
    def get_build_conn_list(self, uid=None, username=None, start_time=None, end_time=None, page=None, page_size=None):
        """### 获取建联列表"""

    @grpc_call(path="/live.xclient.v1.BuildConn/downloadBuildConnList")
    def download_build_conn_list(self, uid=None, username=None, start_time=None, end_time=None, page=None, page_size=None):
        """### 下载建联数据"""

    @grpc_call(path="/live.xclient.v1.BuildConn/acceptInvitation")
    def accept_invitation(self, uid=None, username=None, contact=None, parent_area_id=None):
        """### 保存建联数据"""

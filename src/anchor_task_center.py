"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""
from tiny import grpc_call


class Anchor_task_center(object):

    def __init__(self, service_name):
        self.service_name = service_name

    @grpc_call(path="/live.anchortaskcenter.AnchorTaskCenterPeopleConfigBg/GetAnchorGroupList")
    def get_anchor_group_list(self, id=None, group_name=None, page=None, page_size=None):
        """### 获取人群组列表"""

    @grpc_call(path="/live.anchortaskcenter.AnchorTaskCenterPeopleConfigBg/GetAnchorGroup")
    def get_anchor_group(self, id=None):
        """### 获取单个人群组"""

    @grpc_call(path="/live.anchortaskcenter.AnchorTaskCenterPeopleConfigBg/SetAnchorGroup")
    def set_anchor_group(self, id=None, group_name=None, useful_life_type=None, start_time=None, end_time=None, flush_period=None, creater=None, remark=None):
        """### 新增/编辑人群组"""

    @grpc_call(path="/live.anchortaskcenter.AnchorTaskCenterPeopleConfigBg/CopyAnchorGroup")
    def copy_anchor_group(self, id=None, creater=None):
        """### 复制人群组"""

    @grpc_call(path="/live.anchortaskcenter.AnchorTaskCenterPeopleConfigBg/GetAnchorMemberList")
    def get_anchor_member_list(self, group_id=None):
        """### 获取人群包列表"""

    @grpc_call(path="/live.anchortaskcenter.AnchorTaskCenterPeopleConfigBg/GetAnchorMember")
    def get_anchor_member(self, id=None):
        """### 获取单个人群包"""

    @grpc_call(path="/live.anchortaskcenter.AnchorTaskCenterPeopleConfigBg/CopyAnchorMember")
    def copy_anchor_member(self, id=None, creater=None):
        """### 复制人群包"""

    @grpc_call(path="/live.anchortaskcenter.AnchorTaskCenterPeopleConfigBg/DelAnchorMember")
    def del_anchor_member(self, id=None, creater=None):
        """### 删除人群包"""


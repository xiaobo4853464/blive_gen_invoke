"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""
from tiny import grpc_call


class Xclient(object):

    def __init__(self, service_name):
        self.service_name = service_name

    @grpc_call(path="/live.xclient.v1.BuildConn/getBuildConnList")
    def get_build_conn_list(self, uid=None, username=None, start_time=None, end_time=None, page=None, page_size=None):
        """### 获取建联列表"""

    @grpc_call(path="/live.xclient.v1.BuildConn/downloadBuildConnList")
    def download_build_conn_list(self, uid=None, username=None, start_time=None, end_time=None, page=None, page_size=None):
        """### 下载建联数据"""

    @grpc_call(path="/live.xclient.v1.BuildConn/acceptInvitation")
    def accept_invitation(self, uid=None, username=None, contact=None, parent_area_id=None):
        """### 保存建联数据"""


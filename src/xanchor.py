"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""
from tiny import grpc_call


class Xanchor(object):

    def __init__(self, service_name):
        self.service_name = service_name

    @grpc_call(path="/live.xanchor.v1.PopConfMng/PopConfList")
    def pop_conf_list(self, creater=None, pop_id=None, activity_name=None, status=None, source=None, place=None, start_time=None, end_time=None, page=None, page_size=None):
        """###弹窗配置列表"""

    @grpc_call(path="/live.xanchor.v1.PopConfMng/ChangePopConfStatus")
    def change_pop_conf_status(self, id, status):
        """### 更新弹窗状态"""

    @grpc_call(path="/live.xanchor.v1.PopConfMng/DelPopConf")
    def del_pop_conf(self, id):
        """### 删除弹窗配置"""


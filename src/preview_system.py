"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""
from tiny import grpc_call


class Preview_system(object):

    def __init__(self, service_name):
        self.service_name = service_name

    @grpc_call(path="/live.previewsystem.member/GetList")
    def get_list(self, id, size):
        """###获取预演名单配置列表"""


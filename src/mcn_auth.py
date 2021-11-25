"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""
from tiny import grpc_call


class Mcn_auth(object):

    def __init__(self, service_name):
        self.service_name = service_name

    @grpc_call(path="/live.mcnauth.Wechat/Bind")
    def bind(self, openid, wechat_name=None):
        """###绑定"""

    @grpc_call(path="/live.mcnauth.Wechat/Unbind")
    def unbind(self, uid):
        """###解绑"""


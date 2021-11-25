"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""
from tiny import grpc_call


class Xrobot(object):

    def __init__(self, service_name):
        self.service_name = service_name

    @grpc_call(path="/live.xrobot.v1.WxServAccountService/GetWxUserInfo")
    def get_wx_user_info(self, code):
        """###通过用户授权的code获取用户信息"""

    @grpc_call(path="/live.xrobot.v1.WxServAccountService/GetWechatBindInfo")
    def get_wechat_bind_info(self, code):
        """### 通过code获取用户关注订阅号信息"""


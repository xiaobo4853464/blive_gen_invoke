"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""
from tiny import grpc_call


class Artemis(object):

    def __init__(self, service_name):
        self.service_name = service_name

    @grpc_call(path="/live.artemis.v1.Bind/TxUserInfoByOpenID")
    def tx_user_info_by_open_i_d(self, openID, gameType=None, gameId=None, actId=None):
        """###腾讯 通过openId 获取游戏信息"""

    @grpc_call(path="/live.artemis.v1.Bind/TxH5BindHandler")
    def tx_h5_bind_handler(self, gameType, uid):
        """###腾讯 H5跳转绑定页逻辑"""

    @grpc_call(path="/live.artemis.v1.Bind/TxBindHandler")
    def tx_bind_handler(self, uid, gameType=None, gameId=None):
        """###腾讯 小程序跳转绑定页逻辑"""


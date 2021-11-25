from tiny import grpc_call

class Artemis(object):
    def __init__(self,service_name):
        self.service_name=service_name
    
    @grpc_call(path="/live.artemis.v1.Common/GetUserInfo")
    def get_user_info(self, uid, attrs=None):
        """###获取用户信息"""

    @grpc_call(path="/live.artemis.v1.Common/TxLiveLinkCommonV1")
    def tx_live_link_common_v1(self, apiName=None, loginType=None, gameId=None, actId=None, openId=None, flowId=None, serialCode=None, reqTimestamp=None):
        """###腾讯通用请求 1.1版本"""

    @grpc_call(path="/live.artemis.v1.Common/TxLiveLinkCommonV2")
    def tx_live_link_common_v2(self, apiName=None, loginType=None, gameId=None, actId=None, openId=None, flowId=None, serialCode=None, reqTimestamp=None):
        """###腾讯通用请求 2.0版本"""

    @grpc_call(path="/live.artemis.v1.Bind/TxUserInfoByOpenID")
    def tx_user_info_by_open_i_d(self, openID, gameType=None, gameId=None, actId=None):
        """###腾讯 通过openId 获取游戏信息"""

    @grpc_call(path="/live.artemis.v1.Bind/TxH5BindHandler")
    def tx_h5_bind_handler(self, gameType, uid):
        """###腾讯 H5跳转绑定页逻辑"""

    @grpc_call(path="/live.artemis.v1.Bind/TxBindHandler")
    def tx_bind_handler(self, uid, gameType=None, gameId=None):
        """###腾讯 小程序跳转绑定页逻辑"""

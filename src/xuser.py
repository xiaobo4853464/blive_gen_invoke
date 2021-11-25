"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""
from tiny import grpc_call


class Xuser(object):

    def __init__(self, service_name):
        self.service_name = service_name

    @grpc_call(path="/live.xuser.v2.bind.Bind/GetGameRoleByMID")
    def get_game_role_by_m_i_d(self, act_id, game_id, mid):
        """### 通过mid查询游戏角色"""

    @grpc_call(path="/live.xuser.v2.bind.Bind/JumpWxConfig")
    def jump_wx_config(self, act_id, game_id, mid):
        """### 跳转微信绑定方式地址下发"""

    @grpc_call(path="/live.xuser.v2.bind.Bind/WxHandler")
    def wx_handler(self, act_id, game_id, mid):
        """### 获取跳转微信绑定qq小程序相关信息"""

    @grpc_call(path="/live.xuser.v2.bind.Bind/WxH5Handler")
    def wx_h5_handler(self, act_id, game_id, mid):
        """### 获取跳转微信绑定H5相关信息"""


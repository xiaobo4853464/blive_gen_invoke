from tiny import grpc_call

class Xrobot(object):
    def __init__(self,service_name):
        self.service_name=service_name
    
    @grpc_call(path="/live.xrobot.v1.SendMessage/sendTextMessage")
    def send_text_message(self, robot_name, content=None, name=None):
        """###主播手动打标获取配置模块名称"""

    @grpc_call(path="/live.xrobot.v1.SendMessage/sendMdMessage")
    def send_md_message(self, robot_name, content=None):
        """###机器人发消息"""

    @grpc_call(path="/live.xrobot.v1.WeChatService/VerifyURL")
    def verify_u_r_l(self, msg_signature, timestamp, nonce, echostr, app_name=None):
        """### 验证URL有效性"""

    @grpc_call(path="/live.xrobot.v1.WeChatService/ReceiveMessage")
    def receive_message(self, msg_signature=None, timestamp=None, nonce=None, xml=None, app_name=None):
        """### 消息回调"""

    @grpc_call(path="/live.xrobot.v1.WxServAccountService/GetWxUserInfo")
    def get_wx_user_info(self, code):
        """###通过用户授权的code获取用户信息"""

    @grpc_call(path="/live.xrobot.v1.WxServAccountService/GetWechatBindInfo")
    def get_wechat_bind_info(self, code):
        """### 通过code获取用户关注订阅号信息"""

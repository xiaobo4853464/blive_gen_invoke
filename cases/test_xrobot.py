"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.xrobot import Xrobot


class TestXrobot(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Xrobot()

    def test_get_wechat_bind_info(self):
        r = self.mygrpc.get_wechat_bind_info(code=1)
        print(r)

    def test_get_wx_user_info(self):
        r = self.mygrpc.get_wx_user_info(code=1)
        print(r)

    def test_receive_message(self):
        r = self.mygrpc.receive_message()
        print(r)

    def test_send_md_message(self):
        r = self.mygrpc.send_md_message(robot_name=1)
        print(r)

    def test_send_text_message(self):
        r = self.mygrpc.send_text_message(robot_name=1)
        print(r)

    def test_verify_u_r_l(self):
        r = self.mygrpc.verify_u_r_l(msg_signature=1,timestamp=1,nonce=1,echostr=1)
        print(r)


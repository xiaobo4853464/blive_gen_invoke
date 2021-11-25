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


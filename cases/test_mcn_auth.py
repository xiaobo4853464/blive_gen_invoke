"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.mcn_auth import Mcn_auth


class TestMcn_auth(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Mcn_auth()

    def test_bind(self):
        r = self.mygrpc.bind(openid=1)
        print(r)

    def test_unbind(self):
        r = self.mygrpc.unbind(uid=1)
        print(r)


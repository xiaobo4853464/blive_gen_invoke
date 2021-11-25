"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.xcaptcha import Xcaptcha


class TestXcaptcha(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Xcaptcha()

    def test_check(self):
        r = self.mygrpc.check(anti=1,uid=1)
        print(r)

    def test_create(self):
        r = self.mygrpc.create()
        print(r)

    def test_getcode(self):
        r = self.mygrpc.getcode(uid=1,ip=1,referer=1,ua=1,path=1)
        print(r)

    def test_midcheck(self):
        r = self.mygrpc.midcheck(uid=1,path=1)
        print(r)

    def test_verify(self):
        r = self.mygrpc.verify(uid=1)
        print(r)

    def test_verifycode(self):
        r = self.mygrpc.verifycode(uid=1,ip=1,referer=1,ua=1,type=1,path=1,data=1)
        print(r)


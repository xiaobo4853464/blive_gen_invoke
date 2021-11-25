"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""
from tiny import grpc_call


class Xcaptcha(object):

    def __init__(self, service_name):
        self.service_name = service_name

    @grpc_call(path="/live.xcaptcha.v1.xVerifycode/Midcheck")
    def midcheck(self, uid, path, risk=None):
        """###中间件检查用户状态"""

    @grpc_call(path="/live.xcaptcha.v1.xVerifycode/Getcode")
    def getcode(self, uid, ip, referer, ua, path, live=None, show=None, gee=None):
        """###前端获取验证码"""

    @grpc_call(path="/live.xcaptcha.v1.xVerifycode/Verifycode")
    def verifycode(self, uid, ip, referer, ua, type, path, data):
        """###前端验证验证码"""


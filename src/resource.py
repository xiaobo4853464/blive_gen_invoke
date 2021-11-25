"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""
from tiny import grpc_call


class Resource(object):

    def __init__(self, service_name):
        self.service_name = service_name

    @grpc_call(path="/xlive/resource/v2/sendEmail/sendEmail")
    def send_email(self, to_address, head, content, cc_address=None):
        """### sendEmail 发送邮件"""


"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""
from tiny import grpc_call


class Mcn_mng(object):

    def __init__(self, service_name):
        self.service_name = service_name

    @grpc_call(path="/live.mcnmng.v1.Notice/DelNotice")
    def del_notice(self, notice_id, uid=None):
        """###删除公告"""

    @grpc_call(path="/live.mcnmng.v1.Notice/DetailNotice")
    def detail_notice(self, notice_id, uid=None):
        """###查看公告"""

    @grpc_call(path="/live.mcnmng.v1.Notice/ImportantNotice")
    def important_notice(self, notice_id, operate_type):
        """###是否重要"""

    @grpc_call(path="/live.mcnmng.v1.Notice/OperateNotice")
    def operate_notice(self, notice_id, operate_type):
        """###上线、下线"""

    @grpc_call(path="/live.mcnmng.v1.Notice/ListNotices")
    def list_notices(self, category=None, status=None, important=None, title=None, notice_id=None, start_time=None, end_time=None, page=None, page_size=None, order_by=None, uid=None):
        """###公告列表"""


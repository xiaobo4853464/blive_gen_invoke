"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""
from tiny import grpc_call


class Live_riskcontrol(object):

    def __init__(self, service_name):
        self.service_name = service_name

    @grpc_call(path="/live.riskcontrol.v1.IsForbidden/GetIpForbidden")
    def get_ip_forbidden(self, uri=None, ip=None):
        """### 无标题"""

    @grpc_call(path="/live.riskcontrol.v1.IsForbidden/GetPopularityIsNormal")
    def get_popularity_is_normal(self, roomid=None, fb_type=None):
        """### 无标题"""

    @grpc_call(path="/live.riskcontrol.v1.IsForbidden/ReportPopularityFeedback")
    def report_popularity_feedback(self, roomid=None, begin_time=None, end_time=None):
        """### 无标题"""

    @grpc_call(path="/live.riskcontrol.v1.IsForbidden/DealPopularityFeedback")
    def deal_popularity_feedback(self, id=None, result=None, reason=None):
        """### 无标题"""

    @grpc_call(path="/live.riskcontrol.v1.IsForbidden/GetPopularityFeedbackList")
    def get_popularity_feedback_list(self, status=None, roomid=None, page_index=None, page_size=None):
        """### 无标题"""


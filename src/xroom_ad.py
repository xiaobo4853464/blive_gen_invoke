"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""
from tiny import grpc_call


class Xroom_ad(object):

    def __init__(self, service_name):
        self.service_name = service_name

    @grpc_call(path="/live.xroomad.AdOrder/Check")
    def check(self, order_id=None, room_id=None, order_type=None, child_order_id=None):
        """###校验接口"""

    @grpc_call(path="/live.xroomad.AdOrder/GetByCriIds")
    def get_by_cri_ids(self, cri_ids=None):
        """###批量通过创意id获取订单ID和roomid"""


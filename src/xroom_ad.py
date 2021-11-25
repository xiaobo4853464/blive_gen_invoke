from tiny import grpc_call

class Xroom_ad(object):
    def __init__(self,service_name):
        self.service_name=service_name
    
    @grpc_call(path="/live.xroomad.ad/Check")
    def check(self, order_id=None, room_id=None, order_type=None, child_order_id=None):
        """###校验接口"""

    @grpc_call(path="/live.xroomad.ad/GetByCriIds")
    def get_by_cri_ids(self, cri_ids=None):
        """###批量通过创意id获取订单ID和roomid"""

    @grpc_call(path="/live.xroomad.ad/CheckV2")
    def check_v2(self, room_id, order_type, channel_ids=None):
        """###校验接口 v2版本"""

    @grpc_call(path="/live.xroomad.AdOrder/Check")
    def check(self, order_id=None, room_id=None, order_type=None, child_order_id=None):
        """###校验接口"""

    @grpc_call(path="/live.xroomad.AdOrder/GetByCriIds")
    def get_by_cri_ids(self, cri_ids=None):
        """###批量通过创意id获取订单ID和roomid"""

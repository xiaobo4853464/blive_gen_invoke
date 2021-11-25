"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""
from tiny import grpc_call


class Rankdb(object):

    def __init__(self, service_name):
        self.service_name = service_name

    @grpc_call(path="/live.rankdb.v3.BaseModule/DeleteModule")
    def delete_module(self, uid, ruid, business_id, room_id=None, reason=None):
        """### 无标题"""


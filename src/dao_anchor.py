"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""
from tiny import grpc_call


class Dao_anchor(object):

    def __init__(self, service_name):
        self.service_name = service_name

    @grpc_call(path="/live.daoanchor.v0.Popularity/IncrPopularity")
    def incr_popularity(self, total_coin=None, coin_type=None, room_id=None):
        """### IncrPopularity 增加人气值"""


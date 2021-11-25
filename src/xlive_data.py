"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""
from tiny import grpc_call


class Xlive_data(object):

    def __init__(self, service_name):
        self.service_name = service_name

    @grpc_call(path="/live.xlivedata.v1.Chemcenser/GetPopulationByStreamerEvent")
    def get_population_by_streamer_event(self, interacting_event=None):
        """### GetPopulationByStreamerEvent 获取当前进行各个交互事件的主播人数。"""


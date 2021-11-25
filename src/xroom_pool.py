from tiny import grpc_call

class Xroom_pool(object):
    def __init__(self,service_name):
        self.service_name=service_name
    
    @grpc_call(path="/live.xroompool.Pool/FetchCpmV2")
    def fetch_cpm_v2(self, channel_ids=None):
        """###直播AI 获取推广池 按照子订单渠道维度"""

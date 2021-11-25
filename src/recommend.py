from tiny import grpc_call

class Recommend(object):
    def __init__(self,service_name):
        self.service_name=service_name
    
    @grpc_call(path="/live.recommend.v1.Recommend/clear_recommend_cache")
    def clear_recommend_cache(self, uid=None, buvid=None):
        """### 清空推荐缓存，清空推荐过的集合"""

    @grpc_call(path="/live.recommend.v1.Recommend/get_recommend_rooms")
    def get_recommend_rooms(self, uid=None, count=None, exist_ids=None, buvid=None, sid=None, parent_area_id=None, area_id=None):
        """### 房间推荐接口"""

    @grpc_call(path="/live.recommend.v1.Recommend/get_recall_result")
    def get_recall_result(self, uid=None):
        """### 获取召回源的接口(调试)"""

    @grpc_call(path="/live.recommend.v1.Recommend/get_lr_feature_result")
    def get_lr_feature_result(self, uid=None):
        """### 获取房间特征向量接口(调试)"""

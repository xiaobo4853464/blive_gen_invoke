"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""
from tiny import grpc_call


class Mozi(object):

    def __init__(self, service_name):
        self.service_name = service_name

    @grpc_call(path="/live.mozi.actCenter/GetActCenterEnterList")
    def get_act_center_enter_list(self, uid=None):
        """### 活动中心入口列表接口"""

    @grpc_call(path="/live.mozi.actCenter/GetActCenterList")
    def get_act_center_list(self, uid, tab_id, page_index, page_size):
        """### 活动列表接口"""

    @grpc_call(path="/live.mozi.actCenter/GetActCenterDetail")
    def get_act_center_detail(self, act_id):
        """### 活动详情接口"""

    @grpc_call(path="/live.mozi.actCenter/GetActSignUpInfo")
    def get_act_sign_up_info(self, uid, act_id):
        """### 报名信息查询接口"""

    @grpc_call(path="/live.mozi.actCenter/GetActResultDetail")
    def get_act_result_detail(self, uid, act_id):
        """### 活动结果页查询接口"""

    @grpc_call(path="/live.mozi.actCenter/GetTopicActJoinList")
    def get_topic_act_join_list(self, uid, act_id, page_index, page_size):
        """### 话题活动参与记录接口"""

    @grpc_call(path="/live.mozi.actCenter/GetActInfoByTopicIds")
    def get_act_info_by_topic_ids(self, topic_id=None):
        """### 根据话题查询活动信息"""


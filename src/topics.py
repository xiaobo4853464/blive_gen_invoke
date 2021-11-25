"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""
from tiny import grpc_call


class Topics(object):

    def __init__(self, service_name):
        self.service_name = service_name

    @grpc_call(path="/live.topics.v1.topic/AddTopic")
    def add_topic(self, name, creator, cover=None, content=None, start_time=None, end_time=None, jump_content=None, jump_link=None, is_forever=None):
        """### AddTopic 新增话题"""

    @grpc_call(path="/live.topics.v1.topic/UpdateTopic")
    def update_topic(self, topic_id, cover=None, content=None, start_time=None, end_time=None, jump_content=None, jump_link=None, is_forever=None):
        """### UpdateTopic 更新话题信息"""

    @grpc_call(path="/live.topics.v1.topic/GetTopicList")
    def get_topic_list(self, topic_id=None, topic_name=None, creator=None, page=None, page_size=None):
        """### GetTopicList 分页获取话题列表"""

    @grpc_call(path="/live.topics.v1.topic/GetAllTopics")
    def get_all_topics(self, filter_offline=None):
        """### GetAllTopics 获取全量话题"""

    @grpc_call(path="/live.topics.v1.topic/GetTopic")
    def get_topic(self, topic_id, filter_offline=None):
        """### GetTopic 获取话题信息"""

    @grpc_call(path="/live.topics.v1.topic/GetMultiTopics")
    def get_multi_topics(self, topic_ids, filter_offline=None):
        """### GetMultiTopics 批量获取话题信息"""

    @grpc_call(path="/live.topics.v1.topic/BindLiveTopic")
    def bind_live_topic(self, room_id, live_id, topic_id=None):
        """### BindLiveTopic 开播关联话题"""

    @grpc_call(path="/live.topics.v1.topic/IsUserJoinAct")
    def is_user_join_act(self, uid, act_ids, min_live_time=None):
        """### IsUserJoinAct 批量查询主播是否参与过指定的话题活动"""

    @grpc_call(path="/live.topics.v1.topic/GetActRecords")
    def get_act_records(self, uid=None, act_id=None, min_live_time=None, page=None, page_size=None):
        """### GetActRecords 查询主播参与话题活动记录"""

    @grpc_call(path="/live.topics.v1.topic/CountTopicParticipant")
    def count_topic_participant(self, topic_ids):
        """### CountTopicParticipant 统计话题参与人数"""

    @grpc_call(path="/live.topics.v1.topic/GetAllTopicsByPage")
    def get_all_topics_by_page(self, page=None, page_size=None, topic_id=None):
        """### GetAllTopicsByPage 分页获取全量话题（带排序）"""

    @grpc_call(path="/live.topics.v1.topic/GetTopicRoom")
    def get_topic_room(self, topic_id):
        """### GetTopicRoom 查询话题下的在播房间"""

    @grpc_call(path="/live.topics.v1.topic/GetTopicByRoom")
    def get_topic_by_room(self, room_id):
        """### GetTopicByRoom 根据在播房间号查询话题"""

    @grpc_call(path="/live.topics.v1.topic/GetTopicAct")
    def get_topic_act(self, topic_id):
        """### GetTopicAct 获取话题详情(带活动信息)"""

    @grpc_call(path="/live.topics.v1.topic/GetSortedTopicsList")
    def get_sorted_topics_list(self, page=None, page_size=None):
        """### GetSortedTopicsList 获取排序话题列表"""

    @grpc_call(path="/live.topics.v1.topic/UpdateTopicWeight")
    def update_topic_weight(self, topic_id=None, sort_weight=None):
        """### UpdateTopicWeight 更新话题权重"""

    @grpc_call(path="/live.topics.v1.topic/GetTopicByUidAndLiveKey")
    def get_topic_by_uid_and_live_key(self, uid, live_key):
        """### 通过uid和live_key获取有效话题id"""


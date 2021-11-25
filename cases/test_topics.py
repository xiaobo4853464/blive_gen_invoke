"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.topics import Topics


class TestTopics(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Topics()

    def test_add_topic(self):
        r = self.mygrpc.add_topic(name=1, creator=1)
        print(r)

    def test_bind_live_topic(self):
        r = self.mygrpc.bind_live_topic(room_id=1, live_id=1)
        print(r)

    def test_count_topic_participant(self):
        r = self.mygrpc.count_topic_participant(topic_ids=1)
        print(r)

    def test_get_act_records(self):
        r = self.mygrpc.get_act_records()
        print(r)

    def test_get_all_topics(self):
        r = self.mygrpc.get_all_topics()
        print(r)

    def test_get_all_topics_by_page(self):
        r = self.mygrpc.get_all_topics_by_page()
        print(r)

    def test_get_multi_topics(self):
        r = self.mygrpc.get_multi_topics(topic_ids=1)
        print(r)

    def test_get_sorted_topics_list(self):
        r = self.mygrpc.get_sorted_topics_list()
        print(r)

    def test_get_topic(self):
        r = self.mygrpc.get_topic(topic_id=1)
        print(r)

    def test_get_topic_act(self):
        r = self.mygrpc.get_topic_act(topic_id=1)
        print(r)

    def test_get_topic_by_room(self):
        r = self.mygrpc.get_topic_by_room(room_id=1)
        print(r)

    def test_get_topic_by_uid_and_live_key(self):
        r = self.mygrpc.get_topic_by_uid_and_live_key(uid=1, live_key=1)
        print(r)

    def test_get_topic_list(self):
        r = self.mygrpc.get_topic_list()
        print(r)

    def test_get_topic_room(self):
        r = self.mygrpc.get_topic_room(topic_id=1)
        print(r)

    def test_is_user_join_act(self):
        r = self.mygrpc.is_user_join_act(uid=1, act_ids=1)
        print(r)

    def test_update_topic(self):
        r = self.mygrpc.update_topic(topic_id=1)
        print(r)

    def test_update_topic_weight(self):
        r = self.mygrpc.update_topic_weight()
        print(r)


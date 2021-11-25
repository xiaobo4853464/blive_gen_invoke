"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.live_play import Live_play


class TestLive_play(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Live_play()

    def test_batch_publish_msg(self):
        r = self.mygrpc.batch_publish_msg(act_id=1, start_time=1, end_time=1)
        print(r)

    def test_get_message(self):
        r = self.mygrpc.get_message()
        print(r)

    def test_get_messages_by_condition(self):
        r = self.mygrpc.get_messages_by_condition(act_id=1, ruid=1, uid=1, start_time=1, end_time=1)
        print(r)

    def test_get_msg_list(self):
        r = self.mygrpc.get_msg_list(page=1, page_size=1, act_id=1, start_time=1, end_time=1)
        print(r)

    def test_get_score(self):
        r = self.mygrpc.get_score()
        print(r)

    def test_send_message(self):
        r = self.mygrpc.send_message()
        print(r)

    def test_up_or_down_msg(self):
        r = self.mygrpc.up_or_down_msg()
        print(r)


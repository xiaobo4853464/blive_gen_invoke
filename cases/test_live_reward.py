"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.live_reward import Live_reward


class TestLive_reward(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Live_reward()

    def test_get_log_for_user(self):
        r = self.mygrpc.get_log_for_user()
        print(r)

    def test_get_user_item(self):
        r = self.mygrpc.get_user_item(item_id=1, uid=1)
        print(r)

    def test_update_user_item(self):
        r = self.mygrpc.update_user_item(item_id=1, num=1, uid=1, tid=1, source=1)
        print(r)


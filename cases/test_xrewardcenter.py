"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.xrewardcenter import Xrewardcenter


class TestXrewardcenter(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Xrewardcenter()

    def test_add_reward(self):
        r = self.mygrpc.add_reward(reward_id=1,roomid=1,source=1,uid=1,order_id=1)
        print(r)

    def test_cancel_reward(self):
        r = self.mygrpc.cancel_reward()
        print(r)

    def test_current(self):
        r = self.mygrpc.current()
        print(r)

    def test_get(self):
        r = self.mygrpc.get(id=1)
        print(r)

    def test_get_pools(self):
        r = self.mygrpc.get_pools()
        print(r)

    def test_grant_bag_reward(self):
        r = self.mygrpc.grant_bag_reward()
        print(r)

    def test_has_expire(self):
        r = self.mygrpc.has_expire(user_id=1)
        print(r)

    def test_is_viewed(self):
        r = self.mygrpc.is_viewed(uid=1)
        print(r)

    def test_list(self):
        r = self.mygrpc.list()
        print(r)

    def test_my_reward(self):
        r = self.mygrpc.my_reward(uid=1)
        print(r)

    def test_reissue_reward(self):
        r = self.mygrpc.reissue_reward()
        print(r)

    def test_reward_list(self):
        r = self.mygrpc.reward_list(type=1,reward_type=1,user_id=1)
        print(r)

    def test_reward_send_status(self):
        r = self.mygrpc.reward_send_status()
        print(r)

    def test_room_head_box(self):
        r = self.mygrpc.room_head_box()
        print(r)

    def test_room_skin(self):
        r = self.mygrpc.room_skin()
        print(r)

    def test_set(self):
        r = self.mygrpc.set(name=1,reward_config=1)
        print(r)

    def test_use_record(self):
        r = self.mygrpc.use_record(uid=1)
        print(r)

    def test_use_reward(self):
        r = self.mygrpc.use_reward(record_id=1,type=1,user_id=1)
        print(r)


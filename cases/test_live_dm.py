"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.live_dm import Live_dm


class TestLive_dm(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Live_dm()

    def test_ban_broadcast(self):
        r = self.mygrpc.ban_broadcast(data=1, msgtype=1, **{"from": 1})
        print(r)

    def test_broad_user_lopital_a_c_k(self):
        r = self.mygrpc.broad_user_lopital_a_c_k()
        print(r)

    def test_broad_user_lopital_send(self):
        r = self.mygrpc.broad_user_lopital_send()
        print(r)

    def test_broadcast_room(self):
        r = self.mygrpc.broadcast_room(msgtype=1, cmd=1, data=1)
        print(r)

    def test_broadcast_user(self):
        r = self.mygrpc.broadcast_user()
        print(r)

    def test_entry_broadcast(self):
        r = self.mygrpc.entry_broadcast(data=1, msgtype=1, **{"from": 1})
        print(r)

    def test_gift_broadcast(self):
        r = self.mygrpc.gift_broadcast(data=1, msgtype=1, **{"from": 1})
        print(r)


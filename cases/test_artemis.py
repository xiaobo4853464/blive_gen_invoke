"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.artemis import Artemis


class TestArtemis(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Artemis()

    def test_get_user_info(self):
        r = self.mygrpc.get_user_info(uid=1)
        print(r)

    def test_tx_bind_handler(self):
        r = self.mygrpc.tx_bind_handler(uid=1)
        print(r)

    def test_tx_h5_bind_handler(self):
        r = self.mygrpc.tx_h5_bind_handler(gameType=1,uid=1)
        print(r)

    def test_tx_live_link_common_v1(self):
        r = self.mygrpc.tx_live_link_common_v1()
        print(r)

    def test_tx_live_link_common_v2(self):
        r = self.mygrpc.tx_live_link_common_v2()
        print(r)

    def test_tx_user_info_by_open_i_d(self):
        r = self.mygrpc.tx_user_info_by_open_i_d(openID=1)
        print(r)


"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.xuser import Xuser


class TestXuser(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Xuser()

    def test_get_game_role_by_m_i_d(self):
        r = self.mygrpc.get_game_role_by_m_i_d(act_id=1, game_id=1, mid=1)
        print(r)

    def test_jump_wx_config(self):
        r = self.mygrpc.jump_wx_config(act_id=1, game_id=1, mid=1)
        print(r)

    def test_wx_h5_handler(self):
        r = self.mygrpc.wx_h5_handler(act_id=1, game_id=1, mid=1)
        print(r)

    def test_wx_handler(self):
        r = self.mygrpc.wx_handler(act_id=1, game_id=1, mid=1)
        print(r)


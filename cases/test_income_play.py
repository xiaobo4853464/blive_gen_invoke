"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.income_play import Income_play


class TestIncome_play(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Income_play()

    def test_get_anchor_info(self):
        r = self.mygrpc.get_anchor_info(room_id=1, season_id=1)
        print(r)

    def test_get_anchor_pk_history(self):
        r = self.mygrpc.get_anchor_pk_history(room_id=1, season_id=1, page_num=1, page_size=1)
        print(r)

    def test_get_anchor_pk_info(self):
        r = self.mygrpc.get_anchor_pk_info(room_id=1, season_id=1)
        print(r)

    def test_get_fin_p_k_info(self):
        r = self.mygrpc.get_fin_p_k_info(season_id=1, track_id=1)
        print(r)

    def test_get_rank_info(self):
        r = self.mygrpc.get_rank_info(season_id=1, track_id=1, rank_type=1, page_num=1, page_size=1)
        print(r)

    def test_get_season_info(self):
        r = self.mygrpc.get_season_info()
        print(r)

    def test_get_user_rank(self):
        r = self.mygrpc.get_user_rank(season_id=1, room_id=1, page_num=1, page_size=1)
        print(r)

    def test_get_widget_banner(self):
        r = self.mygrpc.get_widget_banner()
        print(r)

    def test_gift(self):
        r = self.mygrpc.gift()
        print(r)


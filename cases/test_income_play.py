"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.income_play import Income_play


class TestIncome_play(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Income_play()

    def test_anchor_list(self):
        r = self.mygrpc.anchor_list()
        print(r)

    def test_auto_match_switch_status(self):
        r = self.mygrpc.auto_match_switch_status()
        print(r)

    def test_battle_gift(self):
        r = self.mygrpc.battle_gift()
        print(r)

    def test_check_send_gift_power(self):
        r = self.mygrpc.check_send_gift_power()
        print(r)

    def test_game_pk_switch(self):
        r = self.mygrpc.game_pk_switch()
        print(r)

    def test_get_anchor_info(self):
        r = self.mygrpc.get_anchor_info(room_id=1,season_id=1)
        print(r)

    def test_get_anchor_pk_history(self):
        r = self.mygrpc.get_anchor_pk_history(room_id=1,season_id=1,page_num=1,page_size=1)
        print(r)

    def test_get_anchor_pk_info(self):
        r = self.mygrpc.get_anchor_pk_info(room_id=1,season_id=1)
        print(r)

    def test_get_battle_pendant(self):
        r = self.mygrpc.get_battle_pendant()
        print(r)

    def test_get_black_list(self):
        r = self.mygrpc.get_black_list(owner_id=1)
        print(r)

    def test_get_daily_streak_rank(self):
        r = self.mygrpc.get_daily_streak_rank(season_id=1)
        print(r)

    def test_get_fin_p_k_info(self):
        r = self.mygrpc.get_fin_p_k_info(season_id=1,track_id=1)
        print(r)

    def test_get_prev_season(self):
        r = self.mygrpc.get_prev_season()
        print(r)

    def test_get_rank_info(self):
        r = self.mygrpc.get_rank_info(season_id=1,track_id=1,rank_type=1,page_num=1,page_size=1)
        print(r)

    def test_get_score_season_rank(self):
        r = self.mygrpc.get_score_season_rank(season_id=1)
        print(r)

    def test_get_score_week_rank(self):
        r = self.mygrpc.get_score_week_rank(season_id=1)
        print(r)

    def test_get_season_battle_record(self):
        r = self.mygrpc.get_season_battle_record()
        print(r)

    def test_get_season_info(self):
        r = self.mygrpc.get_season_info()
        print(r)

    def test_get_season_redu_score_record(self):
        r = self.mygrpc.get_season_redu_score_record()
        print(r)

    def test_get_season_task(self):
        r = self.mygrpc.get_season_task()
        print(r)

    def test_get_user_rank(self):
        r = self.mygrpc.get_user_rank(season_id=1,room_id=1,page_num=1,page_size=1)
        print(r)

    def test_get_widget_banner(self):
        r = self.mygrpc.get_widget_banner()
        print(r)

    def test_gift(self):
        r = self.mygrpc.gift()
        print(r)

    def test_gifts_and_room_info(self):
        r = self.mygrpc.gifts_and_room_info()
        print(r)

    def test_gifts_info(self):
        r = self.mygrpc.gifts_info()
        print(r)

    def test_invite_pk(self):
        r = self.mygrpc.invite_pk()
        print(r)

    def test_invite_pk_cancel(self):
        r = self.mygrpc.invite_pk_cancel()
        print(r)

    def test_invite_pk_response(self):
        r = self.mygrpc.invite_pk_response()
        print(r)

    def test_pk_stat(self):
        r = self.mygrpc.pk_stat()
        print(r)

    def test_rand_match_cancel(self):
        r = self.mygrpc.rand_match_cancel()
        print(r)

    def test_rand_match_join(self):
        r = self.mygrpc.rand_match_join()
        print(r)

    def test_reset_player_stat(self):
        r = self.mygrpc.reset_player_stat()
        print(r)

    def test_update_auto_match_switch(self):
        r = self.mygrpc.update_auto_match_switch(ruid=1,room_id=1)
        print(r)

    def test_update_black_list(self):
        r = self.mygrpc.update_black_list(owner_id=1,member_id=1)
        print(r)


"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.xactivity import Xactivity


class TestXactivity(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Xactivity()

    def test_a_g_awards_list(self):
        r = self.mygrpc.a_g_awards_list()
        print(r)

    def test_a_g_box_lottery(self):
        r = self.mygrpc.a_g_box_lottery()
        print(r)

    def test_a_g_get_user_star_token(self):
        r = self.mygrpc.a_g_get_user_star_token()
        print(r)

    def test_a_g_lottery(self):
        r = self.mygrpc.a_g_lottery()
        print(r)

    def test_a_g_lottery_lucky_guys_log(self):
        r = self.mygrpc.a_g_lottery_lucky_guys_log()
        print(r)

    def test_a_g_open_free_guard(self):
        r = self.mygrpc.a_g_open_free_guard()
        print(r)

    def test_a_g_receive_awards(self):
        r = self.mygrpc.a_g_receive_awards()
        print(r)

    def test_a_g_share_act(self):
        r = self.mygrpc.a_g_share_act()
        print(r)

    def test_act_data_card_valid_state(self):
        r = self.mygrpc.act_data_card_valid_state(uid=1)
        print(r)

    def test_act_result_data(self):
        r = self.mygrpc.act_result_data(act_id=1,uid=1)
        print(r)

    def test_act_sign_up_data(self):
        r = self.mygrpc.act_sign_up_data(act_id=1,uid=1)
        print(r)

    def test_activity_full_init(self):
        r = self.mygrpc.activity_full_init(act_id=1)
        print(r)

    def test_activity_half_init(self):
        r = self.mygrpc.activity_half_init(act_id=1,room_id=1)
        print(r)

    def test_activity_index(self):
        r = self.mygrpc.activity_index()
        print(r)

    def test_activity_index_v2(self):
        r = self.mygrpc.activity_index_v2()
        print(r)

    def test_activity_index_v3(self):
        r = self.mygrpc.activity_index_v3()
        print(r)

    def test_activity_index_v4(self):
        r = self.mygrpc.activity_index_v4()
        print(r)

    def test_activity_sign_up(self):
        r = self.mygrpc.activity_sign_up(act_id=1,ruid=1)
        print(r)

    def test_activity_video_p_k_incr(self):
        r = self.mygrpc.activity_video_p_k_incr()
        print(r)

    def test_add_account_bind_info(self):
        r = self.mygrpc.add_account_bind_info()
        print(r)

    def test_add_user_award(self):
        r = self.mygrpc.add_user_award()
        print(r)

    def test_anchor_set_complete(self):
        r = self.mygrpc.anchor_set_complete()
        print(r)

    def test_anchor_set_enable(self):
        r = self.mygrpc.anchor_set_enable()
        print(r)

    def test_anchor_set_game_info(self):
        r = self.mygrpc.anchor_set_game_info()
        print(r)

    def test_april_bonus21_p_k_log(self):
        r = self.mygrpc.april_bonus21_p_k_log()
        print(r)

    def test_april_bonus21_tab(self):
        r = self.mygrpc.april_bonus21_tab()
        print(r)

    def test_april_bonus_rank_delete(self):
        r = self.mygrpc.april_bonus_rank_delete()
        print(r)

    def test_april_bonus_withdraw(self):
        r = self.mygrpc.april_bonus_withdraw()
        print(r)

    def test_august_master_info(self):
        r = self.mygrpc.august_master_info(room_id=1)
        print(r)

    def test_august_pendant(self):
        r = self.mygrpc.august_pendant(room_id=1)
        print(r)

    def test_august_pendant_pk(self):
        r = self.mygrpc.august_pendant_pk(room_id=1)
        print(r)

    def test_august_pendant_rank(self):
        r = self.mygrpc.august_pendant_rank(room_id=1)
        print(r)

    def test_august_user_rank(self):
        r = self.mygrpc.august_user_rank(room_id=1,page=1)
        print(r)

    def test_b_l_s2021_pre_star_wish(self):
        r = self.mygrpc.b_l_s2021_pre_star_wish()
        print(r)

    def test_b_l_s2021_pre_star_wish_log(self):
        r = self.mygrpc.b_l_s2021_pre_star_wish_log()
        print(r)

    def test_b_l_s2021_v_s_rank_wheel_data(self):
        r = self.mygrpc.b_l_s2021_v_s_rank_wheel_data()
        print(r)

    def test_b_l_s21_parent_area_p_k_list(self):
        r = self.mygrpc.b_l_s21_parent_area_p_k_list()
        print(r)

    def test_battle_list(self):
        r = self.mygrpc.battle_list()
        print(r)

    def test_behavior_change_play_status(self):
        r = self.mygrpc.behavior_change_play_status()
        print(r)

    def test_behavior_send_gift(self):
        r = self.mygrpc.behavior_send_gift()
        print(r)

    def test_bls2020_area_apply_change(self):
        r = self.mygrpc.bls2020_area_apply_change(team_id=1)
        print(r)

    def test_bls2020_area_change_status(self):
        r = self.mygrpc.bls2020_area_change_status()
        print(r)

    def test_bls2020_area_master_info(self):
        r = self.mygrpc.bls2020_area_master_info(act_id=1,room_id=1)
        print(r)

    def test_bls2020_area_spc_master_info(self):
        r = self.mygrpc.bls2020_area_spc_master_info(act_id=1,room_id=1)
        print(r)

    def test_bls2020_guild_rank_index(self):
        r = self.mygrpc.bls2020_guild_rank_index()
        print(r)

    def test_bls2020_guild_rank_list(self):
        r = self.mygrpc.bls2020_guild_rank_list()
        print(r)

    def test_bls2020_m_v_p_rank(self):
        r = self.mygrpc.bls2020_m_v_p_rank()
        print(r)

    def test_bls2020_master_info(self):
        r = self.mygrpc.bls2020_master_info()
        print(r)

    def test_bls2020_personal_apply(self):
        r = self.mygrpc.bls2020_personal_apply()
        print(r)

    def test_bls2020_personal_apply_index(self):
        r = self.mygrpc.bls2020_personal_apply_index()
        print(r)

    def test_bls2020_personal_master_info(self):
        r = self.mygrpc.bls2020_personal_master_info(room_id=1,apply_complete=1)
        print(r)

    def test_bls2020_semifinal_aid_rank(self):
        r = self.mygrpc.bls2020_semifinal_aid_rank(page=1)
        print(r)

    def test_bls2020_semifinal_info(self):
        r = self.mygrpc.bls2020_semifinal_info()
        print(r)

    def test_bls2020_semifinal_master_rank(self):
        r = self.mygrpc.bls2020_semifinal_master_rank(act_id=1,name=1,page=1)
        print(r)

    def test_bls2020_semifinal_pendant(self):
        r = self.mygrpc.bls2020_semifinal_pendant()
        print(r)

    def test_bls2020_spec_get_act_id(self):
        r = self.mygrpc.bls2020_spec_get_act_id()
        print(r)

    def test_bls2020_spec_rank_top_text(self):
        r = self.mygrpc.bls2020_spec_rank_top_text()
        print(r)

    def test_bls21_area_receive_rewards(self):
        r = self.mygrpc.bls21_area_receive_rewards()
        print(r)

    def test_bls21_big_player_data(self):
        r = self.mygrpc.bls21_big_player_data()
        print(r)

    def test_bls_big_area_force_switch(self):
        r = self.mygrpc.bls_big_area_force_switch()
        print(r)

    def test_bls_life_sub_area(self):
        r = self.mygrpc.bls_life_sub_area()
        print(r)

    def test_bls_life_sub_list(self):
        r = self.mygrpc.bls_life_sub_list()
        print(r)

    def test_box_info(self):
        r = self.mygrpc.box_info()
        print(r)

    def test_compound_gift_list(self):
        r = self.mygrpc.compound_gift_list()
        print(r)

    def test_do_compound_gift(self):
        r = self.mygrpc.do_compound_gift(uid=1,giftId=1)
        print(r)

    def test_exchange_kanban(self):
        r = self.mygrpc.exchange_kanban()
        print(r)

    def test_fireworks_init(self):
        r = self.mygrpc.fireworks_init()
        print(r)

    def test_follow(self):
        r = self.mygrpc.follow()
        print(r)

    def test_follow2(self):
        r = self.mygrpc.follow2()
        print(r)

    def test_follow2_task(self):
        r = self.mygrpc.follow2_task()
        print(r)

    def test_full_init(self):
        r = self.mygrpc.full_init()
        print(r)

    def test_genshin_get_thumbs_up_status(self):
        r = self.mygrpc.genshin_get_thumbs_up_status()
        print(r)

    def test_genshin_special_task_receive_reward(self):
        r = self.mygrpc.genshin_special_task_receive_reward()
        print(r)

    def test_genshin_thumbs_up(self):
        r = self.mygrpc.genshin_thumbs_up()
        print(r)

    def test_get_account_bind_info(self):
        r = self.mygrpc.get_account_bind_info()
        print(r)

    def test_get_act_period_team_config(self):
        r = self.mygrpc.get_act_period_team_config()
        print(r)

    def test_get_act_score(self):
        r = self.mygrpc.get_act_score(act_id=1,uid=1)
        print(r)

    def test_get_act_user_award_num(self):
        r = self.mygrpc.get_act_user_award_num()
        print(r)

    def test_get_activity_award_list(self):
        r = self.mygrpc.get_activity_award_list()
        print(r)

    def test_get_activity_info(self):
        r = self.mygrpc.get_activity_info()
        print(r)

    def test_get_activity_list(self):
        r = self.mygrpc.get_activity_list()
        print(r)

    def test_get_area_team_by_room_id(self):
        r = self.mygrpc.get_area_team_by_room_id(act_id=1,room_id=1,period=1,area_id=1,parent_area_id=1)
        print(r)

    def test_get_award_config(self):
        r = self.mygrpc.get_award_config()
        print(r)

    def test_get_award_list(self):
        r = self.mygrpc.get_award_list()
        print(r)

    def test_get_bind_infos_by_openid(self):
        r = self.mygrpc.get_bind_infos_by_openid()
        print(r)

    def test_get_bls2020_area_pendant(self):
        r = self.mygrpc.get_bls2020_area_pendant(room_id=1)
        print(r)

    def test_get_bls2020_buff(self):
        r = self.mygrpc.get_bls2020_buff()
        print(r)

    def test_get_bls2020_final_master_info(self):
        r = self.mygrpc.get_bls2020_final_master_info()
        print(r)

    def test_get_bls2020_finalist_pendant(self):
        r = self.mygrpc.get_bls2020_finalist_pendant(room_id=1,act_id=1)
        print(r)

    def test_get_bls2020_parent_area_pendant(self):
        r = self.mygrpc.get_bls2020_parent_area_pendant(room_id=1)
        print(r)

    def test_get_bls2020_personal_pendant(self):
        r = self.mygrpc.get_bls2020_personal_pendant(room_id=1)
        print(r)

    def test_get_bls2020_ready_pendant(self):
        r = self.mygrpc.get_bls2020_ready_pendant(room_id=1)
        print(r)

    def test_get_bls2020_spec_area_pendant(self):
        r = self.mygrpc.get_bls2020_spec_area_pendant(room_id=1)
        print(r)

    def test_get_bls2020_ultimate_master_aid_rank(self):
        r = self.mygrpc.get_bls2020_ultimate_master_aid_rank(act_id=1,room_id=1)
        print(r)

    def test_get_bls2020_ultimate_master_info(self):
        r = self.mygrpc.get_bls2020_ultimate_master_info()
        print(r)

    def test_get_bls2020_ultimate_pendant(self):
        r = self.mygrpc.get_bls2020_ultimate_pendant(room_id=1)
        print(r)

    def test_get_bls2020parea_master_info(self):
        r = self.mygrpc.get_bls2020parea_master_info()
        print(r)

    def test_get_buff_info(self):
        r = self.mygrpc.get_buff_info()
        print(r)

    def test_get_content_info(self):
        r = self.mygrpc.get_content_info(id=1)
        print(r)

    def test_get_content_infos(self):
        r = self.mygrpc.get_content_infos(act_id=1)
        print(r)

    def test_get_content_list(self):
        r = self.mygrpc.get_content_list(page=1)
        print(r)

    def test_get_cur_act_time(self):
        r = self.mygrpc.get_cur_act_time()
        print(r)

    def test_get_lanturn2021_pendant(self):
        r = self.mygrpc.get_lanturn2021_pendant(act_id=1,room_id=1,ruid=1)
        print(r)

    def test_get_march_blind_gift2021_pendant(self):
        r = self.mygrpc.get_march_blind_gift2021_pendant(act_id=1,room_id=1,ruid=1)
        print(r)

    def test_get_master_promotion_status(self):
        r = self.mygrpc.get_master_promotion_status(act_id=1,uid=1)
        print(r)

    def test_get_multiple_widget_banner(self):
        r = self.mygrpc.get_multiple_widget_banner(room_id=1,ruid=1)
        print(r)

    def test_get_parea_master_battle_info(self):
        r = self.mygrpc.get_parea_master_battle_info()
        print(r)

    def test_get_parea_master_battle_list(self):
        r = self.mygrpc.get_parea_master_battle_list()
        print(r)

    def test_get_promotion_status(self):
        r = self.mygrpc.get_promotion_status(act_id=1)
        print(r)

    def test_get_rank_config(self):
        r = self.mygrpc.get_rank_config()
        print(r)

    def test_get_rank_data_list(self):
        r = self.mygrpc.get_rank_data_list()
        print(r)

    def test_get_rank_info(self):
        r = self.mygrpc.get_rank_info()
        print(r)

    def test_get_rank_tab(self):
        r = self.mygrpc.get_rank_tab()
        print(r)

    def test_get_rank_tab_config(self):
        r = self.mygrpc.get_rank_tab_config()
        print(r)

    def test_get_rank_tab_info(self):
        r = self.mygrpc.get_rank_tab_info()
        print(r)

    def test_get_rank_tab_list(self):
        r = self.mygrpc.get_rank_tab_list()
        print(r)

    def test_get_room_queue(self):
        r = self.mygrpc.get_room_queue()
        print(r)

    def test_get_sep_rank_pendant(self):
        r = self.mygrpc.get_sep_rank_pendant(room_id=1)
        print(r)

    def test_get_sign_up_team(self):
        r = self.mygrpc.get_sign_up_team()
        print(r)

    def test_get_team_by_room(self):
        r = self.mygrpc.get_team_by_room(act_id=1,period=1,room_id=1)
        print(r)

    def test_get_user_apply_data_by_type(self):
        r = self.mygrpc.get_user_apply_data_by_type()
        print(r)

    def test_get_user_kanban(self):
        r = self.mygrpc.get_user_kanban()
        print(r)

    def test_get_widget_banner(self):
        r = self.mygrpc.get_widget_banner(act_id=1,room_id=1,ruid=1)
        print(r)

    def test_get_winter_vacation2021_pendant(self):
        r = self.mygrpc.get_winter_vacation2021_pendant(room_id=1)
        print(r)

    def test_goods_exchange(self):
        r = self.mygrpc.goods_exchange(id=1,act_id=1,uid=1)
        print(r)

    def test_goods_exchange_list(self):
        r = self.mygrpc.goods_exchange_list(act_id=1)
        print(r)

    def test_guild_buff_info(self):
        r = self.mygrpc.guild_buff_info()
        print(r)

    def test_half_init(self):
        r = self.mygrpc.half_init()
        print(r)

    def test_index(self):
        r = self.mygrpc.index()
        print(r)

    def test_index_july(self):
        r = self.mygrpc.index_july()
        print(r)

    def test_index_june(self):
        r = self.mygrpc.index_june()
        print(r)

    def test_j_s_awards_list(self):
        r = self.mygrpc.j_s_awards_list()
        print(r)

    def test_j_s_get_user_star_token(self):
        r = self.mygrpc.j_s_get_user_star_token()
        print(r)

    def test_j_s_lottery(self):
        r = self.mygrpc.j_s_lottery()
        print(r)

    def test_j_s_open_star_token(self):
        r = self.mygrpc.j_s_open_star_token()
        print(r)

    def test_j_s_receive_awards(self):
        r = self.mygrpc.j_s_receive_awards()
        print(r)

    def test_j_s_share_act(self):
        r = self.mygrpc.j_s_share_act()
        print(r)

    def test_july_carnival_score_log(self):
        r = self.mygrpc.july_carnival_score_log()
        print(r)

    def test_july_pendant(self):
        r = self.mygrpc.july_pendant(room_id=1)
        print(r)

    def test_july_rank_area_sign(self):
        r = self.mygrpc.july_rank_area_sign()
        print(r)

    def test_july_rank_battery_reward(self):
        r = self.mygrpc.july_rank_battery_reward()
        print(r)

    def test_july_rank_luck_dog(self):
        r = self.mygrpc.july_rank_luck_dog()
        print(r)

    def test_july_rank_parent_area_sign(self):
        r = self.mygrpc.july_rank_parent_area_sign()
        print(r)

    def test_july_rank_task(self):
        r = self.mygrpc.july_rank_task()
        print(r)

    def test_july_rank_task_upgrade(self):
        r = self.mygrpc.july_rank_task_upgrade(**from_=1)
        print(r)

    def test_july_star_token_score_log(self):
        r = self.mygrpc.july_star_token_score_log()
        print(r)

    def test_july_star_tx_status(self):
        r = self.mygrpc.july_star_tx_status()
        print(r)

    def test_lanturn21_apply(self):
        r = self.mygrpc.lanturn21_apply(ruid=1)
        print(r)

    def test_lanturn21_apply_status(self):
        r = self.mygrpc.lanturn21_apply_status(ruid=1)
        print(r)

    def test_lanturn21_apply_switch(self):
        r = self.mygrpc.lanturn21_apply_switch(ruid=1)
        print(r)

    def test_lanturn21_lucky_user_rank(self):
        r = self.mygrpc.lanturn21_lucky_user_rank(room_id=1)
        print(r)

    def test_lanturn21_master_info(self):
        r = self.mygrpc.lanturn21_master_info(room_id=1,period=1)
        print(r)

    def test_lanturn21_promoted_masters(self):
        r = self.mygrpc.lanturn21_promoted_masters(team=1)
        print(r)

    def test_march_blind_gift_apply(self):
        r = self.mygrpc.march_blind_gift_apply(ruid=1,team=1)
        print(r)

    def test_march_blind_gift_get_team(self):
        r = self.mygrpc.march_blind_gift_get_team(ruid=1)
        print(r)

    def test_march_blind_gift_master_info(self):
        r = self.mygrpc.march_blind_gift_master_info(ruid=1,room_id=1)
        print(r)

    def test_march_blind_gift_status(self):
        r = self.mygrpc.march_blind_gift_status(ruid=1)
        print(r)

    def test_match_room_info(self):
        r = self.mygrpc.match_room_info()
        print(r)

    def test_match_room_status(self):
        r = self.mygrpc.match_room_status()
        print(r)

    def test_may_sweet_token(self):
        r = self.mygrpc.may_sweet_token()
        print(r)

    def test_msg_wall_get_user_rank(self):
        r = self.mygrpc.msg_wall_get_user_rank(room_id=1,act_id=1)
        print(r)

    def test_nov_anchor_act_score_log(self):
        r = self.mygrpc.nov_anchor_act_score_log()
        print(r)

    def test_nov_drifting_bottle_open(self):
        r = self.mygrpc.nov_drifting_bottle_open()
        print(r)

    def test_nov_drifting_bottle_pool(self):
        r = self.mygrpc.nov_drifting_bottle_pool()
        print(r)

    def test_nov_drifting_bottle_throw(self):
        r = self.mygrpc.nov_drifting_bottle_throw()
        print(r)

    def test_oct21_red_leaf_draw_bag(self):
        r = self.mygrpc.oct21_red_leaf_draw_bag(uid=1,pool_id=1,pool_version=1,draw_num=1,ruid=1)
        print(r)

    def test_oct21_red_leaf_new_guide(self):
        r = self.mygrpc.oct21_red_leaf_new_guide()
        print(r)

    def test_oct21_red_leaf_pool_info(self):
        r = self.mygrpc.oct21_red_leaf_pool_info(pool_id=1)
        print(r)

    def test_oct21_red_leaf_pool_list(self):
        r = self.mygrpc.oct21_red_leaf_pool_list(start_pool_id=1)
        print(r)

    def test_oct_national_achievement_receive(self):
        r = self.mygrpc.oct_national_achievement_receive()
        print(r)

    def test_oct_national_gift_wall(self):
        r = self.mygrpc.oct_national_gift_wall()
        print(r)

    def test_open_box(self):
        r = self.mygrpc.open_box(uid=1,boxId=1)
        print(r)

    def test_play_with_rank(self):
        r = self.mygrpc.play_with_rank(page=1)
        print(r)

    def test_query_fans_medal_redis(self):
        r = self.mygrpc.query_fans_medal_redis()
        print(r)

    def test_rank_top_n_june(self):
        r = self.mygrpc.rank_top_n_june()
        print(r)

    def test_room_index_july(self):
        r = self.mygrpc.room_index_july(act_id=1,room_id=1)
        print(r)

    def test_s_g_awards_list(self):
        r = self.mygrpc.s_g_awards_list()
        print(r)

    def test_s_g_get_user_star_token(self):
        r = self.mygrpc.s_g_get_user_star_token()
        print(r)

    def test_s_g_lottery(self):
        r = self.mygrpc.s_g_lottery()
        print(r)

    def test_s_g_lottery_lucky_guys_log(self):
        r = self.mygrpc.s_g_lottery_lucky_guys_log()
        print(r)

    def test_s_g_open_free_guard(self):
        r = self.mygrpc.s_g_open_free_guard()
        print(r)

    def test_s_g_receive_awards(self):
        r = self.mygrpc.s_g_receive_awards()
        print(r)

    def test_s_g_share_act(self):
        r = self.mygrpc.s_g_share_act()
        print(r)

    def test_s_g_task_infos(self):
        r = self.mygrpc.s_g_task_infos()
        print(r)

    def test_send_free_gift(self):
        r = self.mygrpc.send_free_gift(uid=1,order_id=1)
        print(r)

    def test_send_gold_coin_gift(self):
        r = self.mygrpc.send_gold_coin_gift(uid=1,order_id=1)
        print(r)

    def test_sep21_topic_pre_apply(self):
        r = self.mygrpc.sep21_topic_pre_apply()
        print(r)

    def test_sep21_topic_receive_award(self):
        r = self.mygrpc.sep21_topic_receive_award()
        print(r)

    def test_sep21_topic_task_info(self):
        r = self.mygrpc.sep21_topic_task_info()
        print(r)

    def test_sep_act_pool_info(self):
        r = self.mygrpc.sep_act_pool_info()
        print(r)

    def test_sep_act_task_upgrade(self):
        r = self.mygrpc.sep_act_task_upgrade()
        print(r)

    def test_sep_act_use_card(self):
        r = self.mygrpc.sep_act_use_card()
        print(r)

    def test_sep_act_user_task_info(self):
        r = self.mygrpc.sep_act_user_task_info()
        print(r)

    def test_sep_m_a_bag_lottery(self):
        r = self.mygrpc.sep_m_a_bag_lottery(id=1,uid=1,act_id=1,**from_=1)
        print(r)

    def test_sign_up(self):
        r = self.mygrpc.sign_up()
        print(r)

    def test_skybox2021_draw(self):
        r = self.mygrpc.skybox2021_draw(room_id=1,pool_id=1,uid=1)
        print(r)

    def test_skybox2021_draw_ten(self):
        r = self.mygrpc.skybox2021_draw_ten(room_id=1,pool_id=1,uid=1)
        print(r)

    def test_snow_enjoy_draw_bag(self):
        r = self.mygrpc.snow_enjoy_draw_bag(uid=1,pool_id=1,pool_version=1,draw_num=1,ruid=1,pool_type=1)
        print(r)

    def test_snow_enjoy_new_guide(self):
        r = self.mygrpc.snow_enjoy_new_guide()
        print(r)

    def test_snow_enjoy_pool_info(self):
        r = self.mygrpc.snow_enjoy_pool_info(pool_id=1,pool_type=1)
        print(r)

    def test_snow_enjoy_pool_list(self):
        r = self.mygrpc.snow_enjoy_pool_list(start_pool_id=1,pool_type=1)
        print(r)

    def test_spring_festival2021_master_info(self):
        r = self.mygrpc.spring_festival2021_master_info(room_id=1)
        print(r)

    def test_spring_festival2021_period_one_apply(self):
        r = self.mygrpc.spring_festival2021_period_one_apply(ruid=1)
        print(r)

    def test_spring_festival2021_period_one_apply_status(self):
        r = self.mygrpc.spring_festival2021_period_one_apply_status(ruid=1)
        print(r)

    def test_spring_festival2021_period_three_apply(self):
        r = self.mygrpc.spring_festival2021_period_three_apply(ruid=1)
        print(r)

    def test_summer2021_get_score(self):
        r = self.mygrpc.summer2021_get_score()
        print(r)

    def test_summer2021_get_sign_up_team(self):
        r = self.mygrpc.summer2021_get_sign_up_team()
        print(r)

    def test_team_battle_info(self):
        r = self.mygrpc.team_battle_info(act_id=1,period=1,data_key=1)
        print(r)

    def test_token_infos(self):
        r = self.mygrpc.token_infos()
        print(r)

    def test_un_bind_by_uid(self):
        r = self.mygrpc.un_bind_by_uid()
        print(r)

    def test_update_user_apply(self):
        r = self.mygrpc.update_user_apply()
        print(r)

    def test_user_box_status(self):
        r = self.mygrpc.user_box_status(uid=1)
        print(r)

    def test_user_in_queue(self):
        r = self.mygrpc.user_in_queue()
        print(r)

    def test_user_set_game_info(self):
        r = self.mygrpc.user_set_game_info()
        print(r)

    def test_video_pk_s2_join(self):
        r = self.mygrpc.video_pk_s2_join()
        print(r)

    def test_video_pk_s2_p_k_log(self):
        r = self.mygrpc.video_pk_s2_p_k_log()
        print(r)

    def test_video_pk_s2_rank_params(self):
        r = self.mygrpc.video_pk_s2_rank_params()
        print(r)

    def test_video_pk_s2_withdraw(self):
        r = self.mygrpc.video_pk_s2_withdraw()
        print(r)

    def test_watch_task(self):
        r = self.mygrpc.watch_task()
        print(r)

    def test_watch_task_index(self):
        r = self.mygrpc.watch_task_index()
        print(r)

    def test_winter_vacation21_apply(self):
        r = self.mygrpc.winter_vacation21_apply(ruid=1)
        print(r)

    def test_winter_vacation21_apply_status(self):
        r = self.mygrpc.winter_vacation21_apply_status(ruid=1)
        print(r)

    def test_winter_vacation21_apply_switch(self):
        r = self.mygrpc.winter_vacation21_apply_switch(ruid=1)
        print(r)

    def test_winter_vacation21_master_info(self):
        r = self.mygrpc.winter_vacation21_master_info(room_id=1,period=1)
        print(r)

    def test_winter_vacation21_promoted_masters(self):
        r = self.mygrpc.winter_vacation21_promoted_masters(team=1)
        print(r)


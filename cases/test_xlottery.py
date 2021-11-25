"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.xlottery import Xlottery


class TestXlottery(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Xlottery()

    def test_add(self):
        r = self.mygrpc.add(award_name=1,award_num=1,duration=1)
        print(r)

    def test_add_award(self):
        r = self.mygrpc.add_award()
        print(r)

    def test_award_record(self):
        r = self.mygrpc.award_record(page=1)
        print(r)

    def test_be_old(self):
        r = self.mygrpc.be_old()
        print(r)

    def test_can_start(self):
        r = self.mygrpc.can_start()
        print(r)

    def test_check(self):
        r = self.mygrpc.check(roomid=1)
        print(r)

    def test_check3(self):
        r = self.mygrpc.check3(roomid=1)
        print(r)

    def test_check_t_v(self):
        r = self.mygrpc.check_t_v(roomid=1)
        print(r)

    def test_d_b_conf(self):
        r = self.mygrpc.d_b_conf()
        print(r)

    def test_danmu_add(self):
        r = self.mygrpc.danmu_add(roomid=1,duration=1,award_name=1,award_num=1,award_image=1)
        print(r)

    def test_danmu_check(self):
        r = self.mygrpc.danmu_check(roomid=1)
        print(r)

    def test_danmu_gift_list_by_room_i_d(self):
        r = self.mygrpc.danmu_gift_list_by_room_i_d(roomid=1)
        print(r)

    def test_danmu_join(self):
        r = self.mygrpc.danmu_join(id=1)
        print(r)

    def test_danmu_list(self):
        r = self.mygrpc.danmu_list(page=1)
        print(r)

    def test_danmu_name(self):
        r = self.mygrpc.danmu_name()
        print(r)

    def test_danmu_start(self):
        r = self.mygrpc.danmu_start()
        print(r)

    def test_danmu_update(self):
        r = self.mygrpc.danmu_update(status=1,id=1,roomid=1)
        print(r)

    def test_danmu_win_users(self):
        r = self.mygrpc.danmu_win_users(id=1)
        print(r)

    def test_delete_coin(self):
        r = self.mygrpc.delete_coin(id=1)
        print(r)

    def test_delete_pool(self):
        r = self.mygrpc.delete_pool(id=1)
        print(r)

    def test_delete_pool_prize(self):
        r = self.mygrpc.delete_pool_prize(id=1)
        print(r)

    def test_delete_white_anchor(self):
        r = self.mygrpc.delete_white_anchor(anchor_uid=1)
        print(r)

    def test_done(self):
        r = self.mygrpc.done(id=1)
        print(r)

    def test_draw(self):
        r = self.mygrpc.draw()
        print(r)

    def test_draw_prize(self):
        r = self.mygrpc.draw_prize(uid=1,gift_id=1,anchor_id=1,room_id=1,third_id=1,continuous_num=1,lottery_time=1,platform=1,lottrty_id=1)
        print(r)

    def test_export_excel(self):
        r = self.mygrpc.export_excel(ex_code_id=1,type=1)
        print(r)

    def test_get_award(self):
        r = self.mygrpc.get_award(roomid=1,raffleId=1,type=1)
        print(r)

    def test_get_award_pool_info(self):
        r = self.mygrpc.get_award_pool_info(room_id=1,act_id=1)
        print(r)

    def test_get_capsule_info(self):
        r = self.mygrpc.get_capsule_info(**from_=1)
        print(r)

    def test_get_capsule_info_by_id(self):
        r = self.mygrpc.get_capsule_info_by_id(**from_=1)
        print(r)

    def test_get_check_lottery_list(self):
        r = self.mygrpc.get_check_lottery_list(status=1,page=1,page_size=1)
        print(r)

    def test_get_coin_detail(self):
        r = self.mygrpc.get_coin_detail()
        print(r)

    def test_get_coin_gift(self):
        r = self.mygrpc.get_coin_gift()
        print(r)

    def test_get_coin_list(self):
        r = self.mygrpc.get_coin_list(page=1,page_size=1)
        print(r)

    def test_get_coupon_list(self):
        r = self.mygrpc.get_coupon_list()
        print(r)

    def test_get_current_task(self):
        r = self.mygrpc.get_current_task()
        print(r)

    def test_get_detail(self):
        r = self.mygrpc.get_detail(**from_=1)
        print(r)

    def test_get_exchange_code_info(self):
        r = self.mygrpc.get_exchange_code_info(ex_ids=1)
        print(r)

    def test_get_fleet_lottery(self):
        r = self.mygrpc.get_fleet_lottery(uid=1)
        print(r)

    def test_get_list(self):
        r = self.mygrpc.get_list(page=1,page_size=1)
        print(r)

    def test_get_lottery_res(self):
        r = self.mygrpc.get_lottery_res(draw_id=1,uid=1)
        print(r)

    def test_get_lottery_result_list(self):
        r = self.mygrpc.get_lottery_result_list(page=1,page_size=1)
        print(r)

    def test_get_lottery_user_list(self):
        r = self.mygrpc.get_lottery_user_list(lottery_id=1)
        print(r)

    def test_get_one_record(self):
        r = self.mygrpc.get_one_record()
        print(r)

    def test_get_plan(self):
        r = self.mygrpc.get_plan(id=1)
        print(r)

    def test_get_pool_detail(self):
        r = self.mygrpc.get_pool_detail(pool_id=1)
        print(r)

    def test_get_pool_list(self):
        r = self.mygrpc.get_pool_list(page=1,page_size=1)
        print(r)

    def test_get_pool_prize(self):
        r = self.mygrpc.get_pool_prize(pool_id=1)
        print(r)

    def test_get_pool_prize_by_pool(self):
        r = self.mygrpc.get_pool_prize_by_pool(pool_id=1)
        print(r)

    def test_get_pool_status(self):
        r = self.mygrpc.get_pool_status()
        print(r)

    def test_get_prize_by_ids(self):
        r = self.mygrpc.get_prize_by_ids(ids=1)
        print(r)

    def test_get_prize_list_by_type(self):
        r = self.mygrpc.get_prize_list_by_type()
        print(r)

    def test_get_prize_type(self):
        r = self.mygrpc.get_prize_type()
        print(r)

    def test_get_product_list(self):
        r = self.mygrpc.get_product_list(page=1,page_size=1)
        print(r)

    def test_get_room_activity_by_roomid(self):
        r = self.mygrpc.get_room_activity_by_roomid()
        print(r)

    def test_get_skin_list(self):
        r = self.mygrpc.get_skin_list(page=1,page_size=1)
        print(r)

    def test_get_special_skin(self):
        r = self.mygrpc.get_special_skin(roomId=1)
        print(r)

    def test_get_status(self):
        r = self.mygrpc.get_status()
        print(r)

    def test_get_user_award(self):
        r = self.mygrpc.get_user_award()
        print(r)

    def test_get_user_award_list(self):
        r = self.mygrpc.get_user_award_list(uid=1)
        print(r)

    def test_get_user_award_log_by_pool_id(self):
        r = self.mygrpc.get_user_award_log_by_pool_id()
        print(r)

    def test_get_user_coin_num(self):
        r = self.mygrpc.get_user_coin_num(uid=1,coin_id=1)
        print(r)

    def test_get_user_info_list(self):
        r = self.mygrpc.get_user_info_list()
        print(r)

    def test_get_white_list(self):
        r = self.mygrpc.get_white_list(page=1,page_size=1)
        print(r)

    def test_gifts(self):
        r = self.mygrpc.gifts(roomid=1)
        print(r)

    def test_give_address_info(self):
        r = self.mygrpc.give_address_info(id=1,address=1)
        print(r)

    def test_has_record(self):
        r = self.mygrpc.has_record()
        print(r)

    def test_info(self):
        r = self.mygrpc.info(roomid=1)
        print(r)

    def test_info_list(self):
        r = self.mygrpc.info_list(page=1,page_size=1,ex_code_id=1)
        print(r)

    def test_join(self):
        r = self.mygrpc.join(roomid=1,id=1,type=1)
        print(r)

    def test_join2(self):
        r = self.mygrpc.join2(id=1)
        print(r)

    def test_join_guard(self):
        r = self.mygrpc.join_guard(roomid=1,id=1,type=1)
        print(r)

    def test_join_p_k(self):
        r = self.mygrpc.join_p_k(id=1)
        print(r)

    def test_join_t_v(self):
        r = self.mygrpc.join_t_v(roomid=1,id=1,type=1)
        print(r)

    def test_notice(self):
        r = self.mygrpc.notice(raffleId=1,type=1)
        print(r)

    def test_open_capsule(self):
        r = self.mygrpc.open_capsule()
        print(r)

    def test_open_capsule_by_id(self):
        r = self.mygrpc.open_capsule_by_id()
        print(r)

    def test_open_capsule_by_id_with_multi_pool(self):
        r = self.mygrpc.open_capsule_by_id_with_multi_pool(**from_=1)
        print(r)

    def test_open_capsule_by_pool(self):
        r = self.mygrpc.open_capsule_by_pool()
        print(r)

    def test_open_capsule_by_type(self):
        r = self.mygrpc.open_capsule_by_type()
        print(r)

    def test_rand_time(self):
        r = self.mygrpc.rand_time(id=1)
        print(r)

    def test_recall(self):
        r = self.mygrpc.recall(id=1)
        print(r)

    def test_record(self):
        r = self.mygrpc.record(page=1)
        print(r)

    def test_red_pocket_check(self):
        r = self.mygrpc.red_pocket_check()
        print(r)

    def test_red_pocket_create(self):
        r = self.mygrpc.red_pocket_create()
        print(r)

    def test_red_pocket_get_award_list(self):
        r = self.mygrpc.red_pocket_get_award_list()
        print(r)

    def test_red_pocket_get_list(self):
        r = self.mygrpc.red_pocket_get_list(page=1,page_size=1)
        print(r)

    def test_red_pocket_get_result(self):
        r = self.mygrpc.red_pocket_get_result()
        print(r)

    def test_red_pocket_pre_check(self):
        r = self.mygrpc.red_pocket_pre_check(uid=1,amount=1,biz_extra=1)
        print(r)

    def test_red_pocket_trigger(self):
        r = self.mygrpc.red_pocket_trigger(id=1)
        print(r)

    def test_red_pocket_update(self):
        r = self.mygrpc.red_pocket_update(id=1,entry_type=1,delay_receive_time=1)
        print(r)

    def test_red_pocket_update_status(self):
        r = self.mygrpc.red_pocket_update_status(id=1,status=1)
        print(r)

    def test_reduce_user_capsule(self):
        r = self.mygrpc.reduce_user_capsule(uid=1,coin_id=1,count=1,platform=1)
        print(r)

    def test_send_award_by_capsule_id(self):
        r = self.mygrpc.send_award_by_capsule_id(uid=1,capsule_id=1,award_type=1,award_num=1)
        print(r)

    def test_send_award_cdk(self):
        r = self.mygrpc.send_award_cdk(uid=1,ex_id=1,award_num=1)
        print(r)

    def test_send_cdk(self):
        r = self.mygrpc.send_cdk()
        print(r)

    def test_set_end(self):
        r = self.mygrpc.set_end(id=1)
        print(r)

    def test_start(self):
        r = self.mygrpc.start()
        print(r)

    def test_stop(self):
        r = self.mygrpc.stop(id=1)
        print(r)

    def test_super_u_i_d(self):
        r = self.mygrpc.super_u_i_d(uids=1)
        print(r)

    def test_update_award_status(self):
        r = self.mygrpc.update_award_status()
        print(r)

    def test_update_coin_config(self):
        r = self.mygrpc.update_coin_config(title=1,change_num=1,start_time=1,end_time=1,gift_type=1)
        print(r)

    def test_update_coin_status(self):
        r = self.mygrpc.update_coin_status(id=1)
        print(r)

    def test_update_info(self):
        r = self.mygrpc.update_info(ex_code_name=1,ac_name=1,ac_link_web=1,ac_link_mobile=1)
        print(r)

    def test_update_plan_status(self):
        r = self.mygrpc.update_plan_status()
        print(r)

    def test_update_pool(self):
        r = self.mygrpc.update_pool(title=1,start_time=1,end_time=1,rule=1)
        print(r)

    def test_update_pool_prize(self):
        r = self.mygrpc.update_pool_prize(type=1)
        print(r)

    def test_update_pool_status(self):
        r = self.mygrpc.update_pool_status(id=1)
        print(r)

    def test_update_product(self):
        r = self.mygrpc.update_product()
        print(r)

    def test_update_product_status(self):
        r = self.mygrpc.update_product_status()
        print(r)

    def test_update_skin(self):
        r = self.mygrpc.update_skin(title=1,roomIds=1,startTime=1,endTime=1)
        print(r)

    def test_update_skin_status(self):
        r = self.mygrpc.update_skin_status(id=1)
        print(r)

    def test_update_status(self):
        r = self.mygrpc.update_status(id=1)
        print(r)

    def test_winner_group_info(self):
        r = self.mygrpc.winner_group_info()
        print(r)


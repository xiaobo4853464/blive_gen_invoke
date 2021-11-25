"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.settlement import Settlement


class TestSettlement(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Settlement()

    def test_add(self):
        r = self.mygrpc.add()
        print(r)

    def test_add_apply(self):
        r = self.mygrpc.add_apply()
        print(r)

    def test_add_intercept_history(self):
        r = self.mygrpc.add_intercept_history()
        print(r)

    def test_add_rate_config(self):
        r = self.mygrpc.add_rate_config()
        print(r)

    def test_add_withdraw_monthly(self):
        r = self.mygrpc.add_withdraw_monthly()
        print(r)

    def test_apply_withdraw(self):
        r = self.mygrpc.apply_withdraw()
        print(r)

    def test_apply_withdraw_new(self):
        r = self.mygrpc.apply_withdraw_new()
        print(r)

    def test_batch_add_apply(self):
        r = self.mygrpc.batch_add_apply()
        print(r)

    def test_batch_modify_apply(self):
        r = self.mygrpc.batch_modify_apply()
        print(r)

    def test_cancel_withdraw(self):
        r = self.mygrpc.cancel_withdraw()
        print(r)

    def test_check_b_add_apply(self):
        r = self.mygrpc.check_b_add_apply()
        print(r)

    def test_check_b_modify_apply(self):
        r = self.mygrpc.check_b_modify_apply()
        print(r)

    def test_del_(self):
        r = self.mygrpc.del_()
        print(r)

    def test_del_rate_config(self):
        r = self.mygrpc.del_rate_config()
        print(r)

    def test_delete_rule(self):
        r = self.mygrpc.delete_rule()
        print(r)

    def test_examine(self):
        r = self.mygrpc.examine()
        print(r)

    def test_examine_delay(self):
        r = self.mygrpc.examine_delay()
        print(r)

    def test_examine_money_limit(self):
        r = self.mygrpc.examine_money_limit()
        print(r)

    def test_get_anchor_in_grey(self):
        r = self.mygrpc.get_anchor_in_grey()
        print(r)

    def test_get_anchor_income(self):
        r = self.mygrpc.get_anchor_income()
        print(r)

    def test_get_anchor_info(self):
        r = self.mygrpc.get_anchor_info()
        print(r)

    def test_get_apply(self):
        r = self.mygrpc.get_apply()
        print(r)

    def test_get_big_withdraw_list(self):
        r = self.mygrpc.get_big_withdraw_list()
        print(r)

    def test_get_by_uid_month(self):
        r = self.mygrpc.get_by_uid_month()
        print(r)

    def test_get_coin_by_tids(self):
        r = self.mygrpc.get_coin_by_tids()
        print(r)

    def test_get_coin_stream(self):
        r = self.mygrpc.get_coin_stream()
        print(r)

    def test_get_delay_list(self):
        r = self.mygrpc.get_delay_list()
        print(r)

    def test_get_hamster_by_day(self):
        r = self.mygrpc.get_hamster_by_day()
        print(r)

    def test_get_hamster_change_by_third_id(self):
        r = self.mygrpc.get_hamster_change_by_third_id()
        print(r)

    def test_get_hamster_change_record(self):
        r = self.mygrpc.get_hamster_change_record()
        print(r)

    def test_get_hamster_change_records(self):
        r = self.mygrpc.get_hamster_change_records()
        print(r)

    def test_get_money_limit_list(self):
        r = self.mygrpc.get_money_limit_list()
        print(r)

    def test_get_rate_list_by_type(self):
        r = self.mygrpc.get_rate_list_by_type()
        print(r)

    def test_get_rule(self):
        r = self.mygrpc.get_rule()
        print(r)

    def test_get_rule_by_id(self):
        r = self.mygrpc.get_rule_by_id()
        print(r)

    def test_get_running_withdraw(self):
        r = self.mygrpc.get_running_withdraw()
        print(r)

    def test_get_settlement_type(self):
        r = self.mygrpc.get_settlement_type()
        print(r)

    def test_get_streamer_total_profits(self):
        r = self.mygrpc.get_streamer_total_profits(uids=1,time_start=1,time_end=1)
        print(r)

    def test_get_withdraw_apply(self):
        r = self.mygrpc.get_withdraw_apply()
        print(r)

    def test_get_withdraw_apply_record(self):
        r = self.mygrpc.get_withdraw_apply_record()
        print(r)

    def test_get_withdraw_config(self):
        r = self.mygrpc.get_withdraw_config()
        print(r)

    def test_get_withdraw_status(self):
        r = self.mygrpc.get_withdraw_status()
        print(r)

    def test_gethamster_no_op(self):
        r = self.mygrpc.gethamster_no_op()
        print(r)

    def test_gift_stream_account_type(self):
        r = self.mygrpc.gift_stream_account_type()
        print(r)

    def test_intercept_history(self):
        r = self.mygrpc.intercept_history()
        print(r)

    def test_list(self):
        r = self.mygrpc.list()
        print(r)

    def test_log_list(self):
        r = self.mygrpc.log_list()
        print(r)

    def test_modify_apply(self):
        r = self.mygrpc.modify_apply()
        print(r)

    def test_modify_delay(self):
        r = self.mygrpc.modify_delay()
        print(r)

    def test_modify_money_limit(self):
        r = self.mygrpc.modify_money_limit()
        print(r)

    def test_modify_remark(self):
        r = self.mygrpc.modify_remark()
        print(r)

    def test_modify_settle_type_for_month(self):
        r = self.mygrpc.modify_settle_type_for_month()
        print(r)

    def test_modify_settlement_type(self):
        r = self.mygrpc.modify_settlement_type()
        print(r)

    def test_on_add_auth_guild(self):
        r = self.mygrpc.on_add_auth_guild()
        print(r)

    def test_pass_(self):
        r = self.mygrpc.pass_()
        print(r)

    def test_pass_all(self):
        r = self.mygrpc.pass_all()
        print(r)

    def test_pre_deduct(self):
        r = self.mygrpc.pre_deduct(transaction_id=1,uid=1,hamster=1,deduct_type=1,reason=1)
        print(r)

    def test_query(self):
        r = self.mygrpc.query(transaction_id=1,timestamp=1)
        print(r)

    def test_rate_list(self):
        r = self.mygrpc.rate_list()
        print(r)

    def test_reject(self):
        r = self.mygrpc.reject()
        print(r)

    def test_revenue_detail(self):
        r = self.mygrpc.revenue_detail(ruid=1,date=1)
        print(r)

    def test_revoke(self):
        r = self.mygrpc.revoke()
        print(r)

    def test_revoke_delay(self):
        r = self.mygrpc.revoke_delay()
        print(r)

    def test_revoke_money_limit(self):
        r = self.mygrpc.revoke_money_limit()
        print(r)

    def test_salary(self):
        r = self.mygrpc.salary(transaction_id=1,code=1,uid=1,salary=1,timestamp=1)
        print(r)

    def test_save_big_withdraw(self):
        r = self.mygrpc.save_big_withdraw()
        print(r)

    def test_update_rate_config(self):
        r = self.mygrpc.update_rate_config()
        print(r)

    def test_withdraw_notify(self):
        r = self.mygrpc.withdraw_notify(msg_id=1,msg_content=1)
        print(r)

    def test_withdraw_refund(self):
        r = self.mygrpc.withdraw_refund(refund_stream_id=1,stream_id=1,wallet_id=1,uid=1,amount=1)
        print(r)

    def test_withdraw_status_manage(self):
        r = self.mygrpc.withdraw_status_manage(raw_data=1,next_status=1)
        print(r)


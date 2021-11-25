"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.live_reward import Live_reward


class TestLive_reward(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Live_reward()

    def test_act_list(self):
        r = self.mygrpc.act_list()
        print(r)

    def test_act_score_detail(self):
        r = self.mygrpc.act_score_detail()
        print(r)

    def test_act_score_list(self):
        r = self.mygrpc.act_score_list()
        print(r)

    def test_act_score_save(self):
        r = self.mygrpc.act_score_save()
        print(r)

    def test_add_sub_stock(self):
        r = self.mygrpc.add_sub_stock()
        print(r)

    def test_apply_reward(self):
        r = self.mygrpc.apply_reward()
        print(r)

    def test_apply_reward_log(self):
        r = self.mygrpc.apply_reward_log()
        print(r)

    def test_batch_export_sql(self):
        r = self.mygrpc.batch_export_sql()
        print(r)

    def test_check_import_award_items(self):
        r = self.mygrpc.check_import_award_items()
        print(r)

    def test_config_copy(self):
        r = self.mygrpc.config_copy()
        print(r)

    def test_config_detail(self):
        r = self.mygrpc.config_detail()
        print(r)

    def test_config_list(self):
        r = self.mygrpc.config_list()
        print(r)

    def test_config_save(self):
        r = self.mygrpc.config_save()
        print(r)

    def test_create_order(self):
        r = self.mygrpc.create_order(key=1,platform=1,receiver_name=1,phone=1,province=1,city=1,addr_detail=1,ip=1,uid=1)
        print(r)

    def test_delete(self):
        r = self.mygrpc.delete()
        print(r)

    def test_delete_award(self):
        r = self.mygrpc.delete_award()
        print(r)

    def test_doc_config_batch_to_sql(self):
        r = self.mygrpc.doc_config_batch_to_sql()
        print(r)

    def test_doc_detail(self):
        r = self.mygrpc.doc_detail()
        print(r)

    def test_doc_list(self):
        r = self.mygrpc.doc_list()
        print(r)

    def test_doc_save(self):
        r = self.mygrpc.doc_save()
        print(r)

    def test_doc_switch_status(self):
        r = self.mygrpc.doc_switch_status()
        print(r)

    def test_exchange_award(self):
        r = self.mygrpc.exchange_award()
        print(r)

    def test_exchange_award_list(self):
        r = self.mygrpc.exchange_award_list(act_id=1)
        print(r)

    def test_export_order(self):
        r = self.mygrpc.export_order()
        print(r)

    def test_export_sql(self):
        r = self.mygrpc.export_sql()
        print(r)

    def test_get_all_item_list(self):
        r = self.mygrpc.get_all_item_list()
        print(r)

    def test_get_doc_content(self):
        r = self.mygrpc.get_doc_content()
        print(r)

    def test_get_json_content(self):
        r = self.mygrpc.get_json_content()
        print(r)

    def test_get_log_for_user(self):
        r = self.mygrpc.get_log_for_user()
        print(r)

    def test_get_order(self):
        r = self.mygrpc.get_order(order_id=1)
        print(r)

    def test_get_order_by_id(self):
        r = self.mygrpc.get_order_by_id(id=1,uid=1)
        print(r)

    def test_get_order_detail(self):
        r = self.mygrpc.get_order_detail()
        print(r)

    def test_get_order_list(self):
        r = self.mygrpc.get_order_list()
        print(r)

    def test_get_order_list_for_mlive(self):
        r = self.mygrpc.get_order_list_for_mlive()
        print(r)

    def test_get_reward_config_list(self):
        r = self.mygrpc.get_reward_config_list()
        print(r)

    def test_get_score_id(self):
        r = self.mygrpc.get_score_id()
        print(r)

    def test_get_user_item(self):
        r = self.mygrpc.get_user_item(item_id=1,uid=1)
        print(r)

    def test_import_(self):
        r = self.mygrpc.import_()
        print(r)

    def test_import_award_items(self):
        r = self.mygrpc.import_award_items()
        print(r)

    def test_import_order(self):
        r = self.mygrpc.import_order()
        print(r)

    def test_init_data(self):
        r = self.mygrpc.init_data()
        print(r)

    def test_json_config_batch_to_sql(self):
        r = self.mygrpc.json_config_batch_to_sql()
        print(r)

    def test_json_detail(self):
        r = self.mygrpc.json_detail()
        print(r)

    def test_json_list(self):
        r = self.mygrpc.json_list()
        print(r)

    def test_json_save(self):
        r = self.mygrpc.json_save()
        print(r)

    def test_json_switch_status(self):
        r = self.mygrpc.json_switch_status()
        print(r)

    def test_list(self):
        r = self.mygrpc.list(act_id=1,pool_id=1,page=1,size=1)
        print(r)

    def test_lottery_log(self):
        r = self.mygrpc.lottery_log()
        print(r)

    def test_my_award_list(self):
        r = self.mygrpc.my_award_list()
        print(r)

    def test_my_award_log(self):
        r = self.mygrpc.my_award_log()
        print(r)

    def test_order_detail(self):
        r = self.mygrpc.order_detail(id=1)
        print(r)

    def test_order_list(self):
        r = self.mygrpc.order_list()
        print(r)

    def test_order_list_item(self):
        r = self.mygrpc.order_list_item()
        print(r)

    def test_product_list(self):
        r = self.mygrpc.product_list()
        print(r)

    def test_product_list_item(self):
        r = self.mygrpc.product_list_item()
        print(r)

    def test_query_job_status(self):
        r = self.mygrpc.query_job_status()
        print(r)

    def test_real_award_get_pro_award_info(self):
        r = self.mygrpc.real_award_get_pro_award_info()
        print(r)

    def test_real_award_item_delete(self):
        r = self.mygrpc.real_award_item_delete()
        print(r)

    def test_real_award_item_download(self):
        r = self.mygrpc.real_award_item_download()
        print(r)

    def test_real_award_item_list(self):
        r = self.mygrpc.real_award_item_list()
        print(r)

    def test_real_award_item_save(self):
        r = self.mygrpc.real_award_item_save()
        print(r)

    def test_real_award_product_list(self):
        r = self.mygrpc.real_award_product_list()
        print(r)

    def test_real_award_product_log_list(self):
        r = self.mygrpc.real_award_product_log_list()
        print(r)

    def test_real_award_project_add(self):
        r = self.mygrpc.real_award_project_add()
        print(r)

    def test_real_award_project_change(self):
        r = self.mygrpc.real_award_project_change()
        print(r)

    def test_real_award_project_list(self):
        r = self.mygrpc.real_award_project_list()
        print(r)

    def test_real_award_project_property_delete(self):
        r = self.mygrpc.real_award_project_property_delete()
        print(r)

    def test_real_award_project_property_list(self):
        r = self.mygrpc.real_award_project_property_list()
        print(r)

    def test_real_award_project_property_save(self):
        r = self.mygrpc.real_award_project_property_save()
        print(r)

    def test_refund(self):
        r = self.mygrpc.refund()
        print(r)

    def test_reward_conf(self):
        r = self.mygrpc.reward_conf()
        print(r)

    def test_reward_data(self):
        r = self.mygrpc.reward_data()
        print(r)

    def test_reward_item_list(self):
        r = self.mygrpc.reward_item_list()
        print(r)

    def test_reward_package_conf(self):
        r = self.mygrpc.reward_package_conf()
        print(r)

    def test_save_award_list(self):
        r = self.mygrpc.save_award_list(award_data=1,uid=1)
        print(r)

    def test_save_order(self):
        r = self.mygrpc.save_order(id=1)
        print(r)

    def test_save_order_award(self):
        r = self.mygrpc.save_order_award(order_award_pkid=1)
        print(r)

    def test_send_reward(self):
        r = self.mygrpc.send_reward()
        print(r)

    def test_set_addr(self):
        r = self.mygrpc.set_addr()
        print(r)

    def test_update_user_item(self):
        r = self.mygrpc.update_user_item(item_id=1,num=1,uid=1,tid=1,source=1)
        print(r)


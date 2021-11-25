"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.mozi import Mozi


class TestMozi(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Mozi()

    def test_act_sign_up_list_batch_to_sql(self):
        r = self.mygrpc.act_sign_up_list_batch_to_sql()
        print(r)

    def test_batch_export_sql(self):
        r = self.mygrpc.batch_export_sql()
        print(r)

    def test_batch_get_user_sign_up(self):
        r = self.mygrpc.batch_get_user_sign_up()
        print(r)

    def test_batch_import_template_user_sign_up(self):
        r = self.mygrpc.batch_import_template_user_sign_up()
        print(r)

    def test_batch_update_user_sign_up(self):
        r = self.mygrpc.batch_update_user_sign_up()
        print(r)

    def test_batch_user_re_spawn_sign_up(self):
        r = self.mygrpc.batch_user_re_spawn_sign_up()
        print(r)

    def test_batch_user_sign_up(self):
        r = self.mygrpc.batch_user_sign_up()
        print(r)

    def test_delete_user_sign_up_info(self):
        r = self.mygrpc.delete_user_sign_up_info()
        print(r)

    def test_diff_set_sign_up(self):
        r = self.mygrpc.diff_set_sign_up()
        print(r)

    def test_export_act_sign_up_user_list(self):
        r = self.mygrpc.export_act_sign_up_user_list()
        print(r)

    def test_get_act_center_detail(self):
        r = self.mygrpc.get_act_center_detail(act_id=1)
        print(r)

    def test_get_act_center_enter_list(self):
        r = self.mygrpc.get_act_center_enter_list()
        print(r)

    def test_get_act_center_list(self):
        r = self.mygrpc.get_act_center_list(uid=1,tab_id=1,page_index=1,page_size=1)
        print(r)

    def test_get_act_detail(self):
        r = self.mygrpc.get_act_detail()
        print(r)

    def test_get_act_info_by_topic_ids(self):
        r = self.mygrpc.get_act_info_by_topic_ids()
        print(r)

    def test_get_act_list(self):
        r = self.mygrpc.get_act_list()
        print(r)

    def test_get_act_list_batch_to_sql(self):
        r = self.mygrpc.get_act_list_batch_to_sql()
        print(r)

    def test_get_act_result_detail(self):
        r = self.mygrpc.get_act_result_detail(uid=1,act_id=1)
        print(r)

    def test_get_act_sign_up_by_id(self):
        r = self.mygrpc.get_act_sign_up_by_id()
        print(r)

    def test_get_act_sign_up_info(self):
        r = self.mygrpc.get_act_sign_up_info(uid=1,act_id=1)
        print(r)

    def test_get_act_sign_up_list(self):
        r = self.mygrpc.get_act_sign_up_list()
        print(r)

    def test_get_act_sign_up_msg_by_id(self):
        r = self.mygrpc.get_act_sign_up_msg_by_id()
        print(r)

    def test_get_act_sort_list(self):
        r = self.mygrpc.get_act_sort_list()
        print(r)

    def test_get_all_user_by_id(self):
        r = self.mygrpc.get_all_user_by_id()
        print(r)

    def test_get_all_user_by_uids(self):
        r = self.mygrpc.get_all_user_by_uids()
        print(r)

    def test_get_all_user_count_by_id(self):
        r = self.mygrpc.get_all_user_count_by_id()
        print(r)

    def test_get_all_user_sign_up(self):
        r = self.mygrpc.get_all_user_sign_up()
        print(r)

    def test_get_anchor_sign_up_msg_by_uid(self):
        r = self.mygrpc.get_anchor_sign_up_msg_by_uid()
        print(r)

    def test_get_auto_sign_up_config_by_id(self):
        r = self.mygrpc.get_auto_sign_up_config_by_id()
        print(r)

    def test_get_auto_sign_up_config_list(self):
        r = self.mygrpc.get_auto_sign_up_config_list()
        print(r)

    def test_get_auto_sign_up_config_log_list(self):
        r = self.mygrpc.get_auto_sign_up_config_log_list()
        print(r)

    def test_get_battle_config_info(self):
        r = self.mygrpc.get_battle_config_info(id=1)
        print(r)

    def test_get_battle_config_list(self):
        r = self.mygrpc.get_battle_config_list()
        print(r)

    def test_get_battle_round_config_frontend(self):
        r = self.mygrpc.get_battle_round_config_frontend(config_id=1)
        print(r)

    def test_get_battle_round_info_frontend(self):
        r = self.mygrpc.get_battle_round_info_frontend(config_id=1,session=1)
        print(r)

    def test_get_effect_act_list(self):
        r = self.mygrpc.get_effect_act_list()
        print(r)

    def test_get_operation_act_detail(self):
        r = self.mygrpc.get_operation_act_detail()
        print(r)

    def test_get_operation_act_list(self):
        r = self.mygrpc.get_operation_act_list()
        print(r)

    def test_get_round_list(self):
        r = self.mygrpc.get_round_list(config_id=1)
        print(r)

    def test_get_sub_list(self):
        r = self.mygrpc.get_sub_list()
        print(r)

    def test_get_topic_act_join_list(self):
        r = self.mygrpc.get_topic_act_join_list(uid=1,act_id=1,page_index=1,page_size=1)
        print(r)

    def test_get_user_sign_status(self):
        r = self.mygrpc.get_user_sign_status()
        print(r)

    def test_get_user_sign_status_batch_sign_ids(self):
        r = self.mygrpc.get_user_sign_status_batch_sign_ids()
        print(r)

    def test_query_job_status(self):
        r = self.mygrpc.query_job_status()
        print(r)

    def test_round_export(self):
        r = self.mygrpc.round_export(config_id=1)
        print(r)

    def test_round_import(self):
        r = self.mygrpc.round_import(config_id=1,csv_content=1)
        print(r)

    def test_save_battle_config(self):
        r = self.mygrpc.save_battle_config(start_time=1,num=1,score_type=1)
        print(r)

    def test_sign_up(self):
        r = self.mygrpc.sign_up()
        print(r)

    def test_update_act_conf_status(self):
        r = self.mygrpc.update_act_conf_status()
        print(r)

    def test_update_act_sign_up(self):
        r = self.mygrpc.update_act_sign_up()
        print(r)

    def test_update_act_status(self):
        r = self.mygrpc.update_act_status()
        print(r)

    def test_update_act_time_conf(self):
        r = self.mygrpc.update_act_time_conf()
        print(r)

    def test_update_act_weight(self):
        r = self.mygrpc.update_act_weight()
        print(r)

    def test_update_auto_sign_up_config_status(self):
        r = self.mygrpc.update_auto_sign_up_config_status()
        print(r)

    def test_update_battle_config_status(self):
        r = self.mygrpc.update_battle_config_status(id=1)
        print(r)

    def test_update_round(self):
        r = self.mygrpc.update_round()
        print(r)

    def test_update_sign_up_team_by_uid(self):
        r = self.mygrpc.update_sign_up_team_by_uid()
        print(r)

    def test_update_sub_act_status(self):
        r = self.mygrpc.update_sub_act_status()
        print(r)

    def test_update_user_sign_up_info(self):
        r = self.mygrpc.update_user_sign_up_info()
        print(r)


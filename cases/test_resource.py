"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.resource import Resource


class TestResource(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Resource()

    def test_add(self):
        r = self.mygrpc.add(res_type=1,title=1,url=1,weight=1,creator=1)
        print(r)

    def test_add_comment_subject(self):
        r = self.mygrpc.add_comment_subject()
        print(r)

    def test_add_ex(self):
        r = self.mygrpc.add_ex(platform=1,title=1,type=1,device=1,startTime=1,endTime=1,imageUrl=1)
        print(r)

    def test_add_jump_from(self):
        r = self.mygrpc.add_jump_from()
        print(r)

    def test_add_live_check(self):
        r = self.mygrpc.add_live_check(live_check=1)
        print(r)

    def test_batch_get(self):
        r = self.mygrpc.batch_get(business_id=1,key=1)
        print(r)

    def test_bind_business(self):
        r = self.mygrpc.bind_business(conf_id=1,conf_desc=1,department_id=1,business_id=1)
        print(r)

    def test_cache_clean(self):
        r = self.mygrpc.cache_clean(business_id=1)
        print(r)

    def test_del_department(self):
        r = self.mygrpc.del_department(id=1,is_del=1)
        print(r)

    def test_edit(self):
        r = self.mygrpc.edit(res_type=1,custom_id=1)
        print(r)

    def test_edit_by_key(self):
        r = self.mygrpc.edit_by_key(key=1)
        print(r)

    def test_get(self):
        r = self.mygrpc.get(business_id=1,key=1)
        print(r)

    def test_get_a_b_conf_list(self):
        r = self.mygrpc.get_a_b_conf_list()
        print(r)

    def test_get_a_b_rule_list(self):
        r = self.mygrpc.get_a_b_rule_list(conf_id=1)
        print(r)

    def test_get_a_b_test_rules(self):
        r = self.mygrpc.get_a_b_test_rules()
        print(r)

    def test_get_banner(self):
        r = self.mygrpc.get_banner(platform=1,build=1,type=1)
        print(r)

    def test_get_bind_detail(self):
        r = self.mygrpc.get_bind_detail()
        print(r)

    def test_get_blink_banner(self):
        r = self.mygrpc.get_blink_banner(platform=1,build=1)
        print(r)

    def test_get_boss_download_url(self):
        r = self.mygrpc.get_boss_download_url(key=1,dir=1)
        print(r)

    def test_get_boss_upload_url(self):
        r = self.mygrpc.get_boss_upload_url(dir=1)
        print(r)

    def test_get_business_list(self):
        r = self.mygrpc.get_business_list(department_id=1)
        print(r)

    def test_get_by_keys(self):
        r = self.mygrpc.get_by_keys()
        print(r)

    def test_get_by_tree_id(self):
        r = self.mygrpc.get_by_tree_id(tree_id=1)
        print(r)

    def test_get_by_tree_id_v2(self):
        r = self.mygrpc.get_by_tree_id_v2(tree_id=1)
        print(r)

    def test_get_client_conf(self):
        r = self.mygrpc.get_client_conf(department_id=1,business_id=1)
        print(r)

    def test_get_client_conf_detail(self):
        r = self.mygrpc.get_client_conf_detail()
        print(r)

    def test_get_client_conf_list(self):
        r = self.mygrpc.get_client_conf_list(business_id=1)
        print(r)

    def test_get_conf_detail(self):
        r = self.mygrpc.get_conf_detail()
        print(r)

    def test_get_conf_list(self):
        r = self.mygrpc.get_conf_list()
        print(r)

    def test_get_config_by_keyword(self):
        r = self.mygrpc.get_config_by_keyword()
        print(r)

    def test_get_configs_by_likes(self):
        r = self.mygrpc.get_configs_by_likes(params=1)
        print(r)

    def test_get_configs_by_params(self):
        r = self.mygrpc.get_configs_by_params(page=1,page_size=1)
        print(r)

    def test_get_configs_by_tree_id_keys(self):
        r = self.mygrpc.get_configs_by_tree_id_keys()
        print(r)

    def test_get_easy_list(self):
        r = self.mygrpc.get_easy_list()
        print(r)

    def test_get_group_conf_list(self):
        r = self.mygrpc.get_group_conf_list(group_id=1)
        print(r)

    def test_get_group_list(self):
        r = self.mygrpc.get_group_list()
        print(r)

    def test_get_hot(self):
        r = self.mygrpc.get_hot()
        print(r)

    def test_get_info(self):
        r = self.mygrpc.get_info(platform=1,build=1)
        print(r)

    def test_get_jump_from_by_keys(self):
        r = self.mygrpc.get_jump_from_by_keys()
        print(r)

    def test_get_list(self):
        r = self.mygrpc.get_list(platform=1,type=1)
        print(r)

    def test_get_list_ex(self):
        r = self.mygrpc.get_list_ex(platform=1,type=1)
        print(r)

    def test_get_multi_configs(self):
        r = self.mygrpc.get_multi_configs()
        print(r)

    def test_get_my_tree_apps(self):
        r = self.mygrpc.get_my_tree_apps()
        print(r)

    def test_get_one_by_key(self):
        r = self.mygrpc.get_one_by_key()
        print(r)

    def test_get_online_business_by_department_id(self):
        r = self.mygrpc.get_online_business_by_department_id()
        print(r)

    def test_get_online_client_conf(self):
        r = self.mygrpc.get_online_client_conf(page=1,page_size=1)
        print(r)

    def test_get_platform_list(self):
        r = self.mygrpc.get_platform_list()
        print(r)

    def test_get_service_config(self):
        r = self.mygrpc.get_service_config()
        print(r)

    def test_get_service_config_list(self):
        r = self.mygrpc.get_service_config_list()
        print(r)

    def test_get_template_config(self):
        r = self.mygrpc.get_template_config()
        print(r)

    def test_get_tree_ids(self):
        r = self.mygrpc.get_tree_ids()
        print(r)

    def test_list(self):
        r = self.mygrpc.list(res_type=1)
        print(r)

    def test_list_key(self):
        r = self.mygrpc.list_key(business_id=1)
        print(r)

    def test_live_check(self):
        r = self.mygrpc.live_check(platform=1,system=1,mobile=1)
        print(r)

    def test_mutiple_query(self):
        r = self.mygrpc.mutiple_query(res_type=1,custom_ids=1)
        print(r)

    def test_new_switch_rooms(self):
        r = self.mygrpc.new_switch_rooms(switch_list=1)
        print(r)

    def test_offline(self):
        r = self.mygrpc.offline(platform=1,id=1)
        print(r)

    def test_on_off_a_b_conf(self):
        r = self.mygrpc.on_off_a_b_conf(id=1,status=1)
        print(r)

    def test_on_off_a_b_rule(self):
        r = self.mygrpc.on_off_a_b_rule(id=1,status=1,conf_id=1)
        print(r)

    def test_query(self):
        r = self.mygrpc.query(res_type=1,custom_id=1)
        print(r)

    def test_save_business(self):
        r = self.mygrpc.save_business(department_id=1,key=1,business_name=1,business_owner=1,status=1)
        print(r)

    def test_save_client_conf(self):
        r = self.mygrpc.save_client_conf(business_id=1,desc=1,creater=1,department_id=1)
        print(r)

    def test_save_department(self):
        r = self.mygrpc.save_department(department_name=1,department_owner=1)
        print(r)

    def test_save_group_conf(self):
        r = self.mygrpc.save_group_conf(keyword=1,explanation=1)
        print(r)

    def test_send_email(self):
        r = self.mygrpc.send_email(to_address=1,head=1,content=1)
        print(r)

    def test_set_a_b_conf(self):
        r = self.mygrpc.set_a_b_conf(module_name=1,module_info=1)
        print(r)

    def test_set_a_b_rule(self):
        r = self.mygrpc.set_a_b_rule(conf_id=1,name=1,rule=1)
        print(r)

    def test_set_config_by_keyword(self):
        r = self.mygrpc.set_config_by_keyword(keyword=1,value=1)
        print(r)

    def test_set_easy_list(self):
        r = self.mygrpc.set_easy_list()
        print(r)

    def test_set_service_config(self):
        r = self.mygrpc.set_service_config()
        print(r)

    def test_set_status(self):
        r = self.mygrpc.set_status(res_type=1,custom_id=1,status=1)
        print(r)

    def test_sync_service_config(self):
        r = self.mygrpc.sync_service_config()
        print(r)

    def test_update(self):
        r = self.mygrpc.update(business_id=1,key=1,start_time=1,end_time=1)
        print(r)


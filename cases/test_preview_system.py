"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.preview_system import Preview_system


class TestPreview_system(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Preview_system()

    def test_add_batch_add_plan(self):
        r = self.mygrpc.add_batch_add_plan(rule_ids=1,start_time=1,end_time=1,add_type=1,ids=1,description=1)
        print(r)

    def test_add_member_list_type(self):
        r = self.mygrpc.add_member_list_type(tag=1,title=1,meta_data=1,remark=1)
        print(r)

    def test_add_preview_account(self):
        r = self.mygrpc.add_preview_account(uid=1,is_all=1,ext_data=1,state=1)
        print(r)

    def test_add_record(self):
        r = self.mygrpc.add_record(rule_id=1,start_time=1,end_time=1,id_str=1)
        print(r)

    def test_add_rule(self):
        r = self.mygrpc.add_rule(rule_name=1,start_time=1,end_time=1,id_type=1)
        print(r)

    def test_check_mutual_black(self):
        r = self.mygrpc.check_mutual_black()
        print(r)

    def test_check_rule(self):
        r = self.mygrpc.check_rule(rule_id=1,id_str=1)
        print(r)

    def test_del_(self):
        r = self.mygrpc.del_()
        print(r)

    def test_del_preview_account(self):
        r = self.mygrpc.del_preview_account(id=1)
        print(r)

    def test_delete_record(self):
        r = self.mygrpc.delete_record(rule_id=1,id_str=1)
        print(r)

    def test_get(self):
        r = self.mygrpc.get()
        print(r)

    def test_get_batch_add_plan(self):
        r = self.mygrpc.get_batch_add_plan(id=1)
        print(r)

    def test_get_batch_add_plan_list(self):
        r = self.mygrpc.get_batch_add_plan_list()
        print(r)

    def test_get_business_list(self):
        r = self.mygrpc.get_business_list()
        print(r)

    def test_get_info(self):
        r = self.mygrpc.get_info(id=1)
        print(r)

    def test_get_list(self):
        r = self.mygrpc.get_list(id=1,size=1)
        print(r)

    def test_get_member_list_type(self):
        r = self.mygrpc.get_member_list_type(page=1,page_size=1)
        print(r)

    def test_get_record_list(self):
        r = self.mygrpc.get_record_list()
        print(r)

    def test_get_rule(self):
        r = self.mygrpc.get_rule(id=1)
        print(r)

    def test_get_rule_list(self):
        r = self.mygrpc.get_rule_list()
        print(r)

    def test_modify_member_list_type(self):
        r = self.mygrpc.modify_member_list_type(id=1,title=1,meta_data=1,remark=1)
        print(r)

    def test_modify_preview_account(self):
        r = self.mygrpc.modify_preview_account(id=1,uid=1,is_all=1,ext_data=1,state=1)
        print(r)

    def test_set(self):
        r = self.mygrpc.set()
        print(r)

    def test_set_batch(self):
        r = self.mygrpc.set_batch()
        print(r)

    def test_set_business(self):
        r = self.mygrpc.set_business()
        print(r)

    def test_update_record(self):
        r = self.mygrpc.update_record(rule_id=1,id_str=1,start_time=1,end_time=1)
        print(r)

    def test_update_rule(self):
        r = self.mygrpc.update_rule(id=1,rule_name=1,start_time=1,end_time=1,id_type=1)
        print(r)


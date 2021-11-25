"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.mcn_auth import Mcn_auth


class TestMcn_auth(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Mcn_auth()

    def test_add_org(self):
        r = self.mygrpc.add_org(org_id=1,org_name=1,creator_uid=1)
        print(r)

    def test_add_super_admin(self):
        r = self.mygrpc.add_super_admin(org_id=1,uid=1)
        print(r)

    def test_add_user(self):
        r = self.mygrpc.add_user(org_id=1,uid=1,uname=1,parent_uid=1,role_id=1,operator_uid=1)
        print(r)

    def test_bind(self):
        r = self.mygrpc.bind(openid=1)
        print(r)

    def test_get_all_valid_staff(self):
        r = self.mygrpc.get_all_valid_staff()
        print(r)

    def test_get_anchor_list(self):
        r = self.mygrpc.get_anchor_list(org_id=1,superior_uid=1)
        print(r)

    def test_get_anchor_staff_info(self):
        r = self.mygrpc.get_anchor_staff_info(uids=1)
        print(r)

    def test_get_auth_mng_list(self):
        r = self.mygrpc.get_auth_mng_list(org_id=1)
        print(r)

    def test_get_auth_user_info(self):
        r = self.mygrpc.get_auth_user_info(org_id=1,superior_uid=1,inferior_uid=1)
        print(r)

    def test_get_broker_role_by_uids(self):
        r = self.mygrpc.get_broker_role_by_uids()
        print(r)

    def test_get_guild_super_admins(self):
        r = self.mygrpc.get_guild_super_admins(org_id=1)
        print(r)

    def test_get_guild_user_list(self):
        r = self.mygrpc.get_guild_user_list(page=1,page_size=1,org_id=1)
        print(r)

    def test_get_mcn_auth_by_type_and_sort_id(self):
        r = self.mygrpc.get_mcn_auth_by_type_and_sort_id(auth_type=1,sort_id=1)
        print(r)

    def test_get_org_ids_by_uid(self):
        r = self.mygrpc.get_org_ids_by_uid(uid=1)
        print(r)

    def test_get_role_auth_list(self):
        r = self.mygrpc.get_role_auth_list(org_id=1,selected_role_id=1)
        print(r)

    def test_get_role_list(self):
        r = self.mygrpc.get_role_list(org_id=1)
        print(r)

    def test_get_sub_structure(self):
        r = self.mygrpc.get_sub_structure(org_id=1,uid=1)
        print(r)

    def test_get_sub_structure_user_list(self):
        r = self.mygrpc.get_sub_structure_user_list(org_id=1,uid=1)
        print(r)

    def test_get_sub_user_and_anchor_count(self):
        r = self.mygrpc.get_sub_user_and_anchor_count(org_id=1,uid=1)
        print(r)

    def test_get_sub_user_auth_list(self):
        r = self.mygrpc.get_sub_user_auth_list(org_id=1,superior_uid=1,inferior_uid=1)
        print(r)

    def test_get_user_auth_list(self):
        r = self.mygrpc.get_user_auth_list(org_id=1,uid=1)
        print(r)

    def test_get_user_detail_in_transfer(self):
        r = self.mygrpc.get_user_detail_in_transfer(org_id=1,uid=1)
        print(r)

    def test_get_user_list(self):
        r = self.mygrpc.get_user_list(org_id=1)
        print(r)

    def test_get_user_list_by_permission(self):
        r = self.mygrpc.get_user_list_by_permission(permission=1)
        print(r)

    def test_get_user_list_by_role_id(self):
        r = self.mygrpc.get_user_list_by_role_id(org_id=1,role_id=1)
        print(r)

    def test_has_permission(self):
        r = self.mygrpc.has_permission(org_id=1,uid=1,route=1)
        print(r)

    def test_login(self):
        r = self.mygrpc.login(uid=1)
        print(r)

    def test_migrate_anchor_to_other(self):
        r = self.mygrpc.migrate_anchor_to_other(org_id=1,final_uid=1,uid=1)
        print(r)

    def test_migrate_staff_to_other(self):
        r = self.mygrpc.migrate_staff_to_other(org_id=1,uid=1,final_uid=1)
        print(r)

    def test_modify_guild_super_admin(self):
        r = self.mygrpc.modify_guild_super_admin(org_id=1,old_uid=1,new_uid=1,editor_name=1)
        print(r)

    def test_move_user(self):
        r = self.mygrpc.move_user(uid=1,parent_uid=1,org_id=1,operator_uid=1)
        print(r)

    def test_multi_add_user(self):
        r = self.mygrpc.multi_add_user(org_id=1,file_url=1,uid=1,operator_uid=1)
        print(r)

    def test_multi_update_anchor(self):
        r = self.mygrpc.multi_update_anchor(org_id=1,staff_uid=1,anchor_uid_list=1,operator_uid=1)
        print(r)

    def test_remove_anchor(self):
        r = self.mygrpc.remove_anchor(anchor_uid=1)
        print(r)

    def test_remove_guild_user(self):
        r = self.mygrpc.remove_guild_user(org_id=1,uid=1,transfer_uid=1,editor_name=1)
        print(r)

    def test_remove_super_admin(self):
        r = self.mygrpc.remove_super_admin(org_id=1,uid=1)
        print(r)

    def test_remove_user(self):
        r = self.mygrpc.remove_user(uid=1,org_id=1,operator_uid=1)
        print(r)

    def test_save_user_auth(self):
        r = self.mygrpc.save_user_auth(org_id=1,uid=1,role_id=1,loginUid=1)
        print(r)

    def test_search(self):
        r = self.mygrpc.search(org_id=1,key=1,**from_=1)
        print(r)

    def test_set_user_forbid_status(self):
        r = self.mygrpc.set_user_forbid_status(org_id=1,uid=1,is_forbid=1)
        print(r)

    def test_transfer_anchor(self):
        r = self.mygrpc.transfer_anchor(org_id=1,anchor_uid=1)
        print(r)

    def test_unbind(self):
        r = self.mygrpc.unbind(uid=1)
        print(r)

    def test_wechat_bind(self):
        r = self.mygrpc.wechat_bind(uid=1,org_id=1,openid=1)
        print(r)

    def test_wechat_unbind(self):
        r = self.mygrpc.wechat_unbind(uid=1,org_id=1)
        print(r)


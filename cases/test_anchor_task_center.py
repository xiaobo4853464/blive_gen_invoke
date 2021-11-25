"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.anchor_task_center import Anchor_task_center


class TestAnchor_task_center(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Anchor_task_center()

    def test_anchor_in_member_id(self):
        r = self.mygrpc.anchor_in_member_id(uid=1,member_id=1)
        print(r)

    def test_anchor_in_member_id_list(self):
        r = self.mygrpc.anchor_in_member_id_list(member_id_list=1,uid=1,timestamp=1)
        print(r)

    def test_anchor_is_new_people(self):
        r = self.mygrpc.anchor_is_new_people(uid=1)
        print(r)

    def test_anchor_new_task_is_valid(self):
        r = self.mygrpc.anchor_new_task_is_valid(uid=1,member_ids=1)
        print(r)

    def test_anchor_task_info(self):
        r = self.mygrpc.anchor_task_info(uid=1)
        print(r)

    def test_copy_anchor_group(self):
        r = self.mygrpc.copy_anchor_group()
        print(r)

    def test_copy_anchor_member(self):
        r = self.mygrpc.copy_anchor_member()
        print(r)

    def test_copy_anchor_task(self):
        r = self.mygrpc.copy_anchor_task(task_id=1,task_group_id=1)
        print(r)

    def test_create_and_edit_task_group(self):
        r = self.mygrpc.create_and_edit_task_group(title=1,task_group_cycle=1,area_ids=1,creator=1)
        print(r)

    def test_del_anchor_member(self):
        r = self.mygrpc.del_anchor_member()
        print(r)

    def test_del_anchor_task(self):
        r = self.mygrpc.del_anchor_task(task_id=1)
        print(r)

    def test_del_people_task_cfg(self):
        r = self.mygrpc.del_people_task_cfg(people_task_id=1)
        print(r)

    def test_get_anchor_group(self):
        r = self.mygrpc.get_anchor_group()
        print(r)

    def test_get_anchor_group_list(self):
        r = self.mygrpc.get_anchor_group_list()
        print(r)

    def test_get_anchor_member(self):
        r = self.mygrpc.get_anchor_member()
        print(r)

    def test_get_anchor_member_list(self):
        r = self.mygrpc.get_anchor_member_list()
        print(r)

    def test_get_anchor_task_by_people_id(self):
        r = self.mygrpc.get_anchor_task_by_people_id(people_ids=1)
        print(r)

    def test_get_anchor_task_detail(self):
        r = self.mygrpc.get_anchor_task_detail(task_id=1)
        print(r)

    def test_get_current_anchor_task(self):
        r = self.mygrpc.get_current_anchor_task(uid=1)
        print(r)

    def test_get_member_id_by_uid_and_time(self):
        r = self.mygrpc.get_member_id_by_uid_and_time(uid=1)
        print(r)

    def test_get_member_id_by_uid_and_time_for_task(self):
        r = self.mygrpc.get_member_id_by_uid_and_time_for_task(uid=1)
        print(r)

    def test_get_people_task_cfg_detail(self):
        r = self.mygrpc.get_people_task_cfg_detail()
        print(r)

    def test_get_people_task_cfg_list(self):
        r = self.mygrpc.get_people_task_cfg_list()
        print(r)

    def test_get_percentage_task_target_num(self):
        r = self.mygrpc.get_percentage_task_target_num(uid=1,task_id=1,sub_task_id=1,level=1)
        print(r)

    def test_get_task_group_child_task(self):
        r = self.mygrpc.get_task_group_child_task(task_group_id=1)
        print(r)

    def test_get_task_group_detail(self):
        r = self.mygrpc.get_task_group_detail(task_group_id=1)
        print(r)

    def test_get_task_group_info_by_people_flush_period(self):
        r = self.mygrpc.get_task_group_info_by_people_flush_period(flush_period=1)
        print(r)

    def test_get_task_group_list(self):
        r = self.mygrpc.get_task_group_list()
        print(r)

    def test_online_and_offline_people_task_cfg(self):
        r = self.mygrpc.online_and_offline_people_task_cfg(people_task_id=1)
        print(r)

    def test_online_or_offline_task(self):
        r = self.mygrpc.online_or_offline_task(task_id=1,task_group_id=1)
        print(r)

    def test_online_or_offline_task_group(self):
        r = self.mygrpc.online_or_offline_task_group(task_group_id=1)
        print(r)

    def test_receive_reward(self):
        r = self.mygrpc.receive_reward(uid=1)
        print(r)

    def test_receive_reward_record(self):
        r = self.mygrpc.receive_reward_record(uid=1)
        print(r)

    def test_set_anchor_group(self):
        r = self.mygrpc.set_anchor_group()
        print(r)

    def test_sync_new_member(self):
        r = self.mygrpc.sync_new_member(uid=1)
        print(r)

    def test_update_user_protected_period(self):
        r = self.mygrpc.update_user_protected_period(uid=1)
        print(r)

    def test_watch_video_tutorial(self):
        r = self.mygrpc.watch_video_tutorial(uid=1,task_id=1,sub_task_id=1)
        print(r)


"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.activity_task import Activity_task


class TestActivity_task(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Activity_task()

    def test_check_get_gift_package_condition(self):
        r = self.mygrpc.check_get_gift_package_condition(package_id=1, uid=1)
        print(r)

    def test_get_all_gift_package_list(self):
        r = self.mygrpc.get_all_gift_package_list(firm_name=1)
        print(r)

    def test_get_open_platform_task_reward(self):
        r = self.mygrpc.get_open_platform_task_reward(task_id=1, level=1)
        print(r)

    def test_get_task_info_by_act_id(self):
        r = self.mygrpc.get_task_info_by_act_id(act_id=1)
        print(r)

    def test_receive_task_reward(self):
        r = self.mygrpc.receive_task_reward(reward_source=1, uid=1)
        print(r)


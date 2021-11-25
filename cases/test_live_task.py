"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.live_task import Live_task


class TestLive_task(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Live_task()

    def test_get_finalist_task(self):
        r = self.mygrpc.get_finalist_task()
        print(r)

    def test_get_finalist_task_aid_rank(self):
        r = self.mygrpc.get_finalist_task_aid_rank()
        print(r)

    def test_get_finalist_task_pendant(self):
        r = self.mygrpc.get_finalist_task_pendant()
        print(r)

    def test_get_finalist_task_rank(self):
        r = self.mygrpc.get_finalist_task_rank()
        print(r)

    def test_get_task(self):
        r = self.mygrpc.get_task()
        print(r)

    def test_get_task_pendant(self):
        r = self.mygrpc.get_task_pendant()
        print(r)


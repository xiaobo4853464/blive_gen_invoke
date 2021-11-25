"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.push_live import Push_live


class TestPush_live(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Push_live()

    def test_set_room_filter(self):
        r = self.mygrpc.set_room_filter(room_id=1, start_time=1, end_time=1, source=1, source_id=1)
        print(r)


"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.xheartbeat import Xheartbeat


class TestXheartbeat(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Xheartbeat()

    def test_batch_get_user_watch_time(self):
        r = self.mygrpc.batch_get_user_watch_time(uid=1)
        print(r)

    def test_get_base_task_conf_list(self):
        r = self.mygrpc.get_base_task_conf_list(activity_id=1,channel_id=1)
        print(r)

    def test_get_user_total_watch_time(self):
        r = self.mygrpc.get_user_total_watch_time(uid=1,room_id=1,start_ts=1,end_ts=1)
        print(r)

    def test_get_user_watch_time(self):
        r = self.mygrpc.get_user_watch_time(uid=1)
        print(r)

    def test_get_watch_task_conf_list(self):
        r = self.mygrpc.get_watch_task_conf_list()
        print(r)

    def test_heart_beat(self):
        r = self.mygrpc.heart_beat(platform=1,buvid=1,room_id=1,parent_id=1,area_id=1,timestamp=1,secret_key=1,sign=1,watch_time=1,client_ts=1)
        print(r)

    def test_mobile_exit(self):
        r = self.mygrpc.mobile_exit(platform=1,buvid=1,room_id=1,parent_id=1,area_id=1,timestamp=1,secret_key=1,sign=1,watch_time=1,client_ts=1)
        print(r)

    def test_update_base_task_conf_status_off(self):
        r = self.mygrpc.update_base_task_conf_status_off(activity_id=1,channel_id=1)
        print(r)


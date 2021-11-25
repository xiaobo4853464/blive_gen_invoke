"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.xlive_data import Xlive_data


class TestXlive_data(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Xlive_data()

    def test_all_live_time_mile_stone(self):
        r = self.mygrpc.all_live_time_mile_stone()
        print(r)

    def test_get_anchor_list(self):
        r = self.mygrpc.get_anchor_list(page_number=1,page_size=1,parent_area_id=1,area_id=1)
        print(r)

    def test_get_anchor_tag_list(self):
        r = self.mygrpc.get_anchor_tag_list(parent_area_id=1,area_id=1,uid=1)
        print(r)

    def test_get_broadcast_count_by_room_id(self):
        r = self.mygrpc.get_broadcast_count_by_room_id()
        print(r)

    def test_get_dau(self):
        r = self.mygrpc.get_dau(room_id=1,date=1)
        print(r)

    def test_get_first_record_by_live_id(self):
        r = self.mygrpc.get_first_record_by_live_id(uid=1,live_id=1)
        print(r)

    def test_get_history(self):
        r = self.mygrpc.get_history(live_ids=1)
        print(r)

    def test_get_last_live_info(self):
        r = self.mygrpc.get_last_live_info()
        print(r)

    def test_get_live_details(self):
        r = self.mygrpc.get_live_details(start_time=1,end_time=1)
        print(r)

    def test_get_live_info_by_date(self):
        r = self.mygrpc.get_live_info_by_date(room_id=1,start_date=1,end_date=1)
        print(r)

    def test_get_live_info_by_live_key(self):
        r = self.mygrpc.get_live_info_by_live_key(room_id=1,live_key=1)
        print(r)

    def test_get_live_key_by_time(self):
        r = self.mygrpc.get_live_key_by_time(room_id=1,start_time=1,end_time=1)
        print(r)

    def test_get_next_untag_anchor(self):
        r = self.mygrpc.get_next_untag_anchor(parent_area_id=1,area_id=1)
        print(r)

    def test_get_population_by_streamer_event(self):
        r = self.mygrpc.get_population_by_streamer_event()
        print(r)

    def test_get_real_time_live_info(self):
        r = self.mygrpc.get_real_time_live_info()
        print(r)

    def test_get_real_time_live_info_by_area_ids(self):
        r = self.mygrpc.get_real_time_live_info_by_area_ids(start_time=1,end_time=1)
        print(r)

    def test_get_real_time_live_info_except_area_ids(self):
        r = self.mygrpc.get_real_time_live_info_except_area_ids(start_time=1,end_time=1)
        print(r)

    def test_get_record_list(self):
        r = self.mygrpc.get_record_list(start_date=1,end_date=1)
        print(r)

    def test_get_record_list_new(self):
        r = self.mygrpc.get_record_list_new(start_date=1,end_date=1)
        print(r)

    def test_get_record_list_page(self):
        r = self.mygrpc.get_record_list_page(start_date=1,end_date=1)
        print(r)

    def test_get_room_ef_days(self):
        r = self.mygrpc.get_room_ef_days(room_ids=1)
        print(r)

    def test_get_sub_by_live_id(self):
        r = self.mygrpc.get_sub_by_live_id(live_id=1,uid=1)
        print(r)

    def test_get_total_live_time(self):
        r = self.mygrpc.get_total_live_time()
        print(r)

    def test_get_valid_live_info(self):
        r = self.mygrpc.get_valid_live_info()
        print(r)

    def test_live_key_by_time_id(self):
        r = self.mygrpc.live_key_by_time_id()
        print(r)

    def test_lock_anchor_tag_edit(self):
        r = self.mygrpc.lock_anchor_tag_edit(uid=1,parent_area_id=1,area_id=1,last_operate_ts=1)
        print(r)

    def test_lock_hold_heart_beat(self):
        r = self.mygrpc.lock_hold_heart_beat(uid=1,parent_area_id=1,area_id=1,last_operate_ts=1)
        print(r)

    def test_register_live_time_mile_stone(self):
        r = self.mygrpc.register_live_time_mile_stone(source_identify=1,start_at=1,end_at=1,notify_live_time_before_finish=1,task_type=1,mile_stone_value=1)
        print(r)

    def test_unlock_anchor_tag_edit(self):
        r = self.mygrpc.unlock_anchor_tag_edit(uid=1,parent_area_id=1,area_id=1)
        print(r)

    def test_update_live_time_mile_stone(self):
        r = self.mygrpc.update_live_time_mile_stone(mile_stone_id=1,source_identify=1,update_fields=1)
        print(r)


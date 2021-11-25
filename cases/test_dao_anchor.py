"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.dao_anchor import Dao_anchor


class TestDao_anchor(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Dao_anchor()

    def test_add_pendant_to_room(self):
        r = self.mygrpc.add_pendant_to_room(room_id=1,pendant_id=1,expire_at=1)
        print(r)

    def test_anchor_incre(self):
        r = self.mygrpc.anchor_incre(req_id=1,fields=1,uid=1)
        print(r)

    def test_anchor_update(self):
        r = self.mygrpc.anchor_update(fields=1,uid=1)
        print(r)

    def test_delete_tag_by_i_d(self):
        r = self.mygrpc.delete_tag_by_i_d(room_id=1,tag_id=1,tag_sub_id=1)
        print(r)

    def test_fetch_areas(self):
        r = self.mygrpc.fetch_areas()
        print(r)

    def test_fetch_room_by_i_ds(self):
        r = self.mygrpc.fetch_room_by_i_ds()
        print(r)

    def test_flush_cache_by_id(self):
        r = self.mygrpc.flush_cache_by_id(room_id=1,table_name=1)
        print(r)

    def test_get_all_pendant_list(self):
        r = self.mygrpc.get_all_pendant_list(room_ids=1)
        print(r)

    def test_get_popularity_by_room_ids(self):
        r = self.mygrpc.get_popularity_by_room_ids()
        print(r)

    def test_get_tag_list_by_room_id(self):
        r = self.mygrpc.get_tag_list_by_room_id()
        print(r)

    def test_get_tag_room_list(self):
        r = self.mygrpc.get_tag_room_list(tag_id=1,tag_sub_id=1,page=1,page_size=1)
        print(r)

    def test_incr_popularity(self):
        r = self.mygrpc.incr_popularity()
        print(r)

    def test_pendant_add_to_room(self):
        r = self.mygrpc.pendant_add_to_room(type=1,name=1,priority=1,room_id=1,expire_at=1)
        print(r)

    def test_pendant_create(self):
        r = self.mygrpc.pendant_create(type=1,name=1,priority=1)
        print(r)

    def test_pendant_query(self):
        r = self.mygrpc.pendant_query()
        print(r)

    def test_pendant_update(self):
        r = self.mygrpc.pendant_update(id=1)
        print(r)

    def test_query_area_info(self):
        r = self.mygrpc.query_area_info()
        print(r)

    def test_room_create(self):
        r = self.mygrpc.room_create(uid=1)
        print(r)

    def test_room_extend_incre(self):
        r = self.mygrpc.room_extend_incre(req_id=1,fields=1,room_id=1)
        print(r)

    def test_room_extend_update(self):
        r = self.mygrpc.room_extend_update(fields=1,room_id=1)
        print(r)

    def test_room_online_info_by_area(self):
        r = self.mygrpc.room_online_info_by_area()
        print(r)

    def test_room_online_list_by_area(self):
        r = self.mygrpc.room_online_list_by_area()
        print(r)

    def test_room_online_list_from_d_b(self):
        r = self.mygrpc.room_online_list_from_d_b()
        print(r)

    def test_room_tag_create(self):
        r = self.mygrpc.room_tag_create(room_id=1,tag_id=1)
        print(r)

    def test_room_update(self):
        r = self.mygrpc.room_update(fields=1,room_id=1)
        print(r)


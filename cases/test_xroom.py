"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.xroom import Xroom


class TestXroom(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Xroom()

    def test_room_id_and_short_id_info(self):
        r = self.mygrpc.room_id_and_short_id_info(roomid=1)
        print(r)

    def test_short_id_add(self):
        r = self.mygrpc.short_id_add(short_id=1)
        print(r)

    def test_short_id_del(self):
        r = self.mygrpc.short_id_del(short_id=1)
        print(r)

    def test_short_id_info(self):
        r = self.mygrpc.short_id_info(short_id=1)
        print(r)

    def test_short_id_list(self):
        r = self.mygrpc.short_id_list()
        print(r)

    def test_short_id_list_export(self):
        r = self.mygrpc.short_id_list_export()
        print(r)

    def test_short_room_add(self):
        r = self.mygrpc.short_room_add(short_id=1,roomid=1,valid_type=1)
        print(r)

    def test_short_room_back(self):
        r = self.mygrpc.short_room_back(short_id=1,end_reason=1)
        print(r)

    def test_short_room_list(self):
        r = self.mygrpc.short_room_list()
        print(r)

    def test_short_room_list_export(self):
        r = self.mygrpc.short_room_list_export()
        print(r)


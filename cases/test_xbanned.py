"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.xbanned import Xbanned


class TestXbanned(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Xbanned()

    def test_add_black(self):
        r = self.mygrpc.add_black(uid=1,tuid=1)
        print(r)

    def test_add_shield_keyword(self):
        r = self.mygrpc.add_shield_keyword(keyword=1)
        print(r)

    def test_add_silent_user(self):
        r = self.mygrpc.add_silent_user(tuid=1,room_id=1,hour=1)
        print(r)

    def test_admin_del(self):
        r = self.mygrpc.admin_del(uid=1,type=1)
        print(r)

    def test_admin_list(self):
        r = self.mygrpc.admin_list(uid=1,type=1,page=1,size=1)
        print(r)

    def test_del_black(self):
        r = self.mygrpc.del_black(uid=1,tuid=1)
        print(r)

    def test_del_shield_keyword(self):
        r = self.mygrpc.del_shield_keyword(keyword=1)
        print(r)

    def test_del_silent_user(self):
        r = self.mygrpc.del_silent_user(tuid=1,room_id=1)
        print(r)

    def test_filter(self):
        r = self.mygrpc.filter(area=1,message=1,mid=1,uip=1)
        print(r)

    def test_get_admin_shield_rule(self):
        r = self.mygrpc.get_admin_shield_rule()
        print(r)

    def test_get_black_list(self):
        r = self.mygrpc.get_black_list(uid=1)
        print(r)

    def test_get_block_list_simple(self):
        r = self.mygrpc.get_block_list_simple(room_id=1,pn=1,ps=1)
        print(r)

    def test_get_danmu_shield(self):
        r = self.mygrpc.get_danmu_shield(uid=1)
        print(r)

    def test_get_keyword_list(self):
        r = self.mygrpc.get_keyword_list()
        print(r)

    def test_get_manage_list(self):
        r = self.mygrpc.get_manage_list(pn=1,ps=1)
        print(r)

    def test_get_room_silent(self):
        r = self.mygrpc.get_room_silent(room_id=1)
        print(r)

    def test_get_shield_info(self):
        r = self.mygrpc.get_shield_info(uid=1)
        print(r)

    def test_get_shield_user(self):
        r = self.mygrpc.get_shield_user(uid=1)
        print(r)

    def test_get_silent_user_list(self):
        r = self.mygrpc.get_silent_user_list(room_id=1,pn=1,ps=1)
        print(r)

    def test_get_site_block_status(self):
        r = self.mygrpc.get_site_block_status(uid=1)
        print(r)

    def test_hit(self):
        r = self.mygrpc.hit(area=1,msg=1)
        print(r)

    def test_is_black_user(self):
        r = self.mygrpc.is_black_user(uid=1,tuid=1)
        print(r)

    def test_is_block_user(self):
        r = self.mygrpc.is_block_user(uid=1,roomid=1)
        print(r)

    def test_is_shield_user(self):
        r = self.mygrpc.is_shield_user(uid=1,target_uid=1)
        print(r)

    def test_is_site_block_user(self):
        r = self.mygrpc.is_site_block_user(uid=1)
        print(r)

    def test_multi_add_block(self):
        r = self.mygrpc.multi_add_block(days=1)
        print(r)

    def test_room_live_off(self):
        r = self.mygrpc.room_live_off(room_id=1)
        print(r)

    def test_room_silent(self):
        r = self.mygrpc.room_silent(room_id=1,type=1,uid=1)
        print(r)

    def test_room_silent_off(self):
        r = self.mygrpc.room_silent_off(room_id=1)
        print(r)

    def test_shield_content(self):
        r = self.mygrpc.shield_content(uid=1,content=1)
        print(r)

    def test_un_block(self):
        r = self.mygrpc.un_block(uid=1)
        print(r)

    def test_verify(self):
        r = self.mygrpc.verify(uid=1,biz_code=1)
        print(r)


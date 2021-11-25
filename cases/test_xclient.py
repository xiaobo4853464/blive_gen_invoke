"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.xclient import Xclient


class TestXclient(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Xclient()

    def test_accept_invitation(self):
        r = self.mygrpc.accept_invitation()
        print(r)

    def test_add(self):
        r = self.mygrpc.add(title=1,type=1,device=1,startTime=1,endTime=1,imageUrl=1)
        print(r)

    def test_banner_judgment(self):
        r = self.mygrpc.banner_judgment(username=1,id=1,**pass_=1)
        print(r)

    def test_download_build_conn_list(self):
        r = self.mygrpc.download_build_conn_list()
        print(r)

    def test_edit(self):
        r = self.mygrpc.edit(id=1)
        print(r)

    def test_filter_tab_by_room(self):
        r = self.mygrpc.filter_tab_by_room(room_id=1,filter_tab=1,start_time=1,end_time=1,source=1,source_id=1)
        print(r)

    def test_get_activity(self):
        r = self.mygrpc.get_activity(**from_=1)
        print(r)

    def test_get_all_tabs(self):
        r = self.mygrpc.get_all_tabs(roomid=1)
        print(r)

    def test_get_banner(self):
        r = self.mygrpc.get_banner(location=1,platform=1)
        print(r)

    def test_get_build_conn_list(self):
        r = self.mygrpc.get_build_conn_list()
        print(r)

    def test_get_info(self):
        r = self.mygrpc.get_info(platform=1)
        print(r)

    def test_get_judge_info(self):
        r = self.mygrpc.get_judge_info()
        print(r)

    def test_get_judgment_list(self):
        r = self.mygrpc.get_judgment_list()
        print(r)

    def test_get_list(self):
        r = self.mygrpc.get_list(type=1)
        print(r)

    def test_get_platform_list(self):
        r = self.mygrpc.get_platform_list()
        print(r)

    def test_list(self):
        r = self.mygrpc.list()
        print(r)

    def test_mobile_tab(self):
        r = self.mygrpc.mobile_tab()
        print(r)

    def test_off(self):
        r = self.mygrpc.off(roomid=1)
        print(r)

    def test_offline(self):
        r = self.mygrpc.offline(id=1)
        print(r)

    def test_sort(self):
        r = self.mygrpc.sort(roomid=1)
        print(r)

    def test_un_judge_banner_count(self):
        r = self.mygrpc.un_judge_banner_count()
        print(r)

    def test_web_tab(self):
        r = self.mygrpc.web_tab()
        print(r)


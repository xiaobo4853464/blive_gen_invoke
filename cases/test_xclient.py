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

    def test_download_build_conn_list(self):
        r = self.mygrpc.download_build_conn_list()
        print(r)

    def test_get_build_conn_list(self):
        r = self.mygrpc.get_build_conn_list()
        print(r)


"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.resource import Resource


class TestResource(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Resource()

    def test_send_email(self):
        r = self.mygrpc.send_email(to_address=1, head=1, content=1)
        print(r)


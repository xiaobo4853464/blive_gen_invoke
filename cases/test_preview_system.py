"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.preview_system import Preview_system


class TestPreview_system(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Preview_system()

    def test_get_list(self):
        r = self.mygrpc.get_list(id=1, size=1)
        print(r)


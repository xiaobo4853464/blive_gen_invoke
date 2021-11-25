"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.matrix import Matrix


class TestMatrix(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Matrix()

    def test_eval(self):
        r = self.mygrpc.eval()
        print(r)


"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.xlive_data import Xlive_data


class TestXlive_data(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Xlive_data()

    def test_get_population_by_streamer_event(self):
        r = self.mygrpc.get_population_by_streamer_event()
        print(r)


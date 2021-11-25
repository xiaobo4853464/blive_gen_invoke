"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.xactivity import Xactivity


class TestXactivity(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Xactivity()

    def test_get_bls2020_area_pendant(self):
        r = self.mygrpc.get_bls2020_area_pendant(room_id=1)
        print(r)

    def test_get_bls2020_finalist_pendant(self):
        r = self.mygrpc.get_bls2020_finalist_pendant(room_id=1, act_id=1)
        print(r)

    def test_get_bls2020_parent_area_pendant(self):
        r = self.mygrpc.get_bls2020_parent_area_pendant(room_id=1)
        print(r)

    def test_get_bls2020_personal_pendant(self):
        r = self.mygrpc.get_bls2020_personal_pendant(room_id=1)
        print(r)

    def test_get_bls2020_ready_pendant(self):
        r = self.mygrpc.get_bls2020_ready_pendant(room_id=1)
        print(r)

    def test_get_bls2020_spec_area_pendant(self):
        r = self.mygrpc.get_bls2020_spec_area_pendant(room_id=1)
        print(r)

    def test_get_bls2020_ultimate_pendant(self):
        r = self.mygrpc.get_bls2020_ultimate_pendant(room_id=1)
        print(r)

    def test_get_lanturn2021_pendant(self):
        r = self.mygrpc.get_lanturn2021_pendant(act_id=1, room_id=1, ruid=1)
        print(r)

    def test_get_march_blind_gift2021_pendant(self):
        r = self.mygrpc.get_march_blind_gift2021_pendant(act_id=1, room_id=1, ruid=1)
        print(r)

    def test_get_multiple_widget_banner(self):
        r = self.mygrpc.get_multiple_widget_banner(room_id=1, ruid=1)
        print(r)

    def test_get_sep_rank_pendant(self):
        r = self.mygrpc.get_sep_rank_pendant(room_id=1)
        print(r)

    def test_get_widget_banner(self):
        r = self.mygrpc.get_widget_banner(act_id=1, room_id=1, ruid=1)
        print(r)

    def test_get_winter_vacation2021_pendant(self):
        r = self.mygrpc.get_winter_vacation2021_pendant(room_id=1)
        print(r)


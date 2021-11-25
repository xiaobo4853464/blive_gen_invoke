"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.quiz_lottery import Quiz_lottery


class TestQuiz_lottery(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Quiz_lottery()

    def test_award_add(self):
        r = self.mygrpc.award_add(jackpot_id=1, award_type=1, award_name=1, pic=1, change=1, forwho=1)
        print(r)

    def test_award_biz_i_d(self):
        r = self.mygrpc.award_biz_i_d()
        print(r)

    def test_award_del(self):
        r = self.mygrpc.award_del()
        print(r)

    def test_copy_jackpot(self):
        r = self.mygrpc.copy_jackpot()
        print(r)

    def test_ensure_button(self):
        r = self.mygrpc.ensure_button()
        print(r)

    def test_fack_join(self):
        r = self.mygrpc.fack_join()
        print(r)

    def test_jackpot_add(self):
        r = self.mygrpc.jackpot_add()
        print(r)

    def test_jackpot_detail(self):
        r = self.mygrpc.jackpot_detail()
        print(r)

    def test_jackpot_list(self):
        r = self.mygrpc.jackpot_list()
        print(r)

    def test_start(self):
        r = self.mygrpc.start()
        print(r)


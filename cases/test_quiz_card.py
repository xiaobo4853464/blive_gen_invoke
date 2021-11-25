"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.quiz_card import Quiz_card


class TestQuiz_card(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Quiz_card()

    def test_add_card_by_subscribe(self):
        r = self.mygrpc.add_card_by_subscribe(uid=1, tid=1)
        print(r)

    def test_create_card(self):
        r = self.mygrpc.create_card(uid=1, code=1)
        print(r)

    def test_current_blance(self):
        r = self.mygrpc.current_blance(uid=1)
        print(r)

    def test_get_code(self):
        r = self.mygrpc.get_code(uid=1)
        print(r)

    def test_set_card_num(self):
        r = self.mygrpc.set_card_num(uids=1, num=1)
        print(r)

    def test_use_card(self):
        r = self.mygrpc.use_card(uid=1)
        print(r)


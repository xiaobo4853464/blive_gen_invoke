"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.quiz_admin import Quiz_admin


class TestQuiz_admin(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Quiz_admin()

    def test_create_question(self):
        r = self.mygrpc.create_question(content=1, option_a=1, option_b=1)
        print(r)

    def test_del_question(self):
        r = self.mygrpc.del_question(id=1)
        print(r)

    def test_edit_question(self):
        r = self.mygrpc.edit_question(id=1, content=1, option_a=1, option_b=1)
        print(r)

    def test_get_question_info(self):
        r = self.mygrpc.get_question_info(ids=1)
        print(r)

    def test_get_question_list(self):
        r = self.mygrpc.get_question_list()
        print(r)

    def test_import_questions(self):
        r = self.mygrpc.import_questions(file=1)
        print(r)


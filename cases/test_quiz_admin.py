"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.quiz_admin import Quiz_admin


class TestQuiz_admin(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Quiz_admin()

    def test_create_push(self):
        r = self.mygrpc.create_push()
        print(r)

    def test_create_question(self):
        r = self.mygrpc.create_question(content=1,option_a=1,option_b=1)
        print(r)

    def test_create_session(self):
        r = self.mygrpc.create_session(title=1,bonus=1,jackpot_id=1,status=1,qids=1)
        print(r)

    def test_create_session_card(self):
        r = self.mygrpc.create_session_card(title=1,start_time=1,award=1,on_time=1,off_time=1,event=1)
        print(r)

    def test_del_question(self):
        r = self.mygrpc.del_question(id=1)
        print(r)

    def test_del_session(self):
        r = self.mygrpc.del_session(id=1)
        print(r)

    def test_edit_push(self):
        r = self.mygrpc.edit_push()
        print(r)

    def test_edit_question(self):
        r = self.mygrpc.edit_question(id=1,content=1,option_a=1,option_b=1)
        print(r)

    def test_edit_session(self):
        r = self.mygrpc.edit_session(id=1,title=1,bonus=1,jackpot_id=1,status=1,qids=1)
        print(r)

    def test_edit_session_card(self):
        r = self.mygrpc.edit_session_card(id=1,title=1,start_time=1,award=1,on_time=1,off_time=1)
        print(r)

    def test_get_push_info(self):
        r = self.mygrpc.get_push_info(session_id=1)
        print(r)

    def test_get_push_list(self):
        r = self.mygrpc.get_push_list()
        print(r)

    def test_get_push_question_result(self):
        r = self.mygrpc.get_push_question_result(session_id=1,qid=1,number=1)
        print(r)

    def test_get_push_result(self):
        r = self.mygrpc.get_push_result(session_id=1)
        print(r)

    def test_get_question_info(self):
        r = self.mygrpc.get_question_info(ids=1)
        print(r)

    def test_get_question_list(self):
        r = self.mygrpc.get_question_list()
        print(r)

    def test_get_session_card_info(self):
        r = self.mygrpc.get_session_card_info(id=1)
        print(r)

    def test_get_session_card_list(self):
        r = self.mygrpc.get_session_card_list()
        print(r)

    def test_get_session_info(self):
        r = self.mygrpc.get_session_info(id=1)
        print(r)

    def test_get_session_list(self):
        r = self.mygrpc.get_session_list()
        print(r)

    def test_import_questions(self):
        r = self.mygrpc.import_questions(file=1)
        print(r)

    def test_on_off_session_card(self):
        r = self.mygrpc.on_off_session_card(id=1,type=1)
        print(r)

    def test_push_answer(self):
        r = self.mygrpc.push_answer(session_id=1,qid=1,number=1)
        print(r)

    def test_push_question(self):
        r = self.mygrpc.push_question(session_id=1,qid=1,number=1)
        print(r)

    def test_push_result(self):
        r = self.mygrpc.push_result(session_id=1)
        print(r)


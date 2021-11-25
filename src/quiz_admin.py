"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""
from tiny import grpc_call


class Quiz_admin(object):

    def __init__(self, service_name):
        self.service_name = service_name

    @grpc_call(path="/live.quizadmin.question/GetQuestionList")
    def get_question_list(self, level=None, keyword=None, page=None, limit=None):
        """### 题库列表"""

    @grpc_call(path="/live.quizadmin.question/CreateQuestion")
    def create_question(self, content, option_a, option_b, type=None, level=None, option_c=None, option_d=None, answer=None):
        """### 添加题目"""

    @grpc_call(path="/live.quizadmin.question/EditQuestion")
    def edit_question(self, id, content, option_a, option_b, type=None, level=None, option_c=None, option_d=None, answer=None):
        """### 编辑题目"""

    @grpc_call(path="/live.quizadmin.question/DelQuestion")
    def del_question(self, id):
        """### 删除题目"""

    @grpc_call(path="/live.quizadmin.question/ImportQuestions")
    def import_questions(self, file):
        """### 导入题目"""

    @grpc_call(path="/live.quizadmin.question/GetQuestionInfo")
    def get_question_info(self, ids):
        """### 获取题目详情"""


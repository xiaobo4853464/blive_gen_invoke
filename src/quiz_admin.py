from tiny import grpc_call

class Quiz_admin(object):
    def __init__(self,service_name):
        self.service_name=service_name
    
    @grpc_call(path="/live.quizadmin.card/GetSessionCardList")
    def get_session_card_list(self, page=None, limit=None):
        """### 获取卡片列表"""

    @grpc_call(path="/live.quizadmin.card/CreateSessionCard")
    def create_session_card(self, title, start_time, award, on_time, off_time, event):
        """### 创建场次卡片"""

    @grpc_call(path="/live.quizadmin.card/EditSessionCard")
    def edit_session_card(self, id, title, start_time, award, on_time, off_time):
        """### 编辑场次卡片"""

    @grpc_call(path="/live.quizadmin.card/GetSessionCardInfo")
    def get_session_card_info(self, id):
        """### 获取卡片详情"""

    @grpc_call(path="/live.quizadmin.card/OnOffSessionCard")
    def on_off_session_card(self, id, type):
        """###上下线场次卡片"""

    @grpc_call(path="/live.quizadmin.session/CreateSession")
    def create_session(self, title, bonus, jackpot_id, status, qids):
        """### 新建场次"""

    @grpc_call(path="/live.quizadmin.session/EditSession")
    def edit_session(self, id, title, bonus, jackpot_id, status, qids):
        """### 编辑场次"""

    @grpc_call(path="/live.quizadmin.session/GetSessionList")
    def get_session_list(self, page=None, limit=None):
        """### 场次列表"""

    @grpc_call(path="/live.quizadmin.session/DelSession")
    def del_session(self, id):
        """### 删除场次"""

    @grpc_call(path="/live.quizadmin.session/GetSessionInfo")
    def get_session_info(self, id):
        """### 获取场次详情"""

    @grpc_call(path="/live.quizadmin.push/GetPushList")
    def get_push_list(self, page=None, limit=None):
        """### 获取推送列表"""

    @grpc_call(path="/live.quizadmin.push/CreatePush")
    def create_push(self, session_id=None):
        """### 新建推送"""

    @grpc_call(path="/live.quizadmin.push/EditPush")
    def edit_push(self, id=None, session_id=None):
        """### 编辑推送"""

    @grpc_call(path="/live.quizadmin.push/GetPushInfo")
    def get_push_info(self, session_id):
        """### 推送详情"""

    @grpc_call(path="/live.quizadmin.push/PushQuestion")
    def push_question(self, session_id, qid, number):
        """### 推送题目"""

    @grpc_call(path="/live.quizadmin.push/PushAnswer")
    def push_answer(self, session_id, qid, number):
        """### 推送答案"""

    @grpc_call(path="/live.quizadmin.push/PushResult")
    def push_result(self, session_id):
        """### 推送结果"""

    @grpc_call(path="/live.quizadmin.push/GetPushQuestionResult")
    def get_push_question_result(self, session_id, qid, number):
        """### 获取存活人数和复活卡使用数"""

    @grpc_call(path="/live.quizadmin.push/GetPushResult")
    def get_push_result(self, session_id):
        """### 获取最终存活人数、人均分成"""

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

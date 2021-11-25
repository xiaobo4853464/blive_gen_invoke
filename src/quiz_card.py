"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""
from tiny import grpc_call


class Quiz_card(object):

    def __init__(self, service_name):
        self.service_name = service_name

    @grpc_call(path="/live.quizcard.Card/CreateCard")
    def create_card(self, uid, code, buvid=None):
        """### 填邀请码获取复活卡"""

    @grpc_call(path="/live.quizcard.Card/GetCode")
    def get_code(self, uid):
        """### 获取uid的邀请码及库存"""

    @grpc_call(path="/live.quizcard.Card/UseCard")
    def use_card(self, uid, session_id=None, question_id=None):
        """### 扣复活卡"""

    @grpc_call(path="/live.quizcard.Card/CurrentBlance")
    def current_blance(self, uid):
        """### 获取uid当前的余额，包支付的接口"""

    @grpc_call(path="/live.quizcard.Card/SetCardNum")
    def set_card_num(self, uids, num):
        """### 设置邀请码数量 调试用"""

    @grpc_call(path="/live.quizcard.Card/AddCardBySubscribe")
    def add_card_by_subscribe(self, uid, tid, buvid=None):
        """###  获取uid当前的邀请码数量"""


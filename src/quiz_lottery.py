"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""
from tiny import grpc_call


class Quiz_lottery(object):

    def __init__(self, service_name):
        self.service_name = service_name

    @grpc_call(path="/live.quizlottery.Lottery/Start")
    def start(self, quizid=None, jackpot_id=None, roomid=None):
        """### 开始抽奖"""

    @grpc_call(path="/live.quizlottery.Lottery/AwardBizID")
    def award_biz_i_d(self, biz_id=None, uid=None):
        """### 现金发放查询是否有记录"""

    @grpc_call(path="/live.quizlottery.Lottery/JackpotList")
    def jackpot_list(self, page=None, page_size=None, for_quiz=None):
        """### 奖池列表"""

    @grpc_call(path="/live.quizlottery.Lottery/JackpotDetail")
    def jackpot_detail(self, jackpot_ids=None):
        """### 根据id 查询奖池"""

    @grpc_call(path="/live.quizlottery.Lottery/JackpotAdd")
    def jackpot_add(self, name=None, id=None):
        """### 新增奖池"""

    @grpc_call(path="/live.quizlottery.Lottery/AwardAdd")
    def award_add(self, jackpot_id, award_type, award_name, pic, change, forwho, award_id=None, vaild_day=None, limit=None, price=None, token=None, award_item_id=None):
        """### 新增奖励"""

    @grpc_call(path="/live.quizlottery.Lottery/AwardDel")
    def award_del(self, award_id=None):
        """### 删除奖励"""

    @grpc_call(path="/live.quizlottery.Lottery/EnsureButton")
    def ensure_button(self, jackpot_id=None, ensure_or_not=None):
        """### 确认，取消确认，确认后奖励不可修改，"""

    @grpc_call(path="/live.quizlottery.Lottery/CopyJackpot")
    def copy_jackpot(self, jackpot_id=None):
        """### 复制"""

    @grpc_call(path="/live.quizlottery.Lottery/FackJoin")
    def fack_join(self, quizid=None, roomid=None):
        """### 无标题"""


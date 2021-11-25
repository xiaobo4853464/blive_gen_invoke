"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""
from tiny import grpc_call


class Xactivity(object):

    def __init__(self, service_name):
        self.service_name = service_name

    @grpc_call(path="/live.xactivity.rank_pendant/getSepRankPendant")
    def get_sep_rank_pendant(self, room_id):
        """### 无标题"""

    @grpc_call(path="/live.xactivity.rank_pendant/getBls2020ReadyPendant")
    def get_bls2020_ready_pendant(self, room_id):
        """### bls2020预备赛挂件"""

    @grpc_call(path="/live.xactivity.rank_pendant/getBls2020ParentAreaPendant")
    def get_bls2020_parent_area_pendant(self, room_id):
        """### bls2020大分区赛挂件"""

    @grpc_call(path="/live.xactivity.rank_pendant/getBls2020AreaPendant")
    def get_bls2020_area_pendant(self, room_id, ruid=None):
        """### bls2020小分区挂件"""

    @grpc_call(path="/live.xactivity.rank_pendant/getBls2020SpecAreaPendant")
    def get_bls2020_spec_area_pendant(self, room_id, ruid=None):
        """### bls2020专项赛挂件"""

    @grpc_call(path="/live.xactivity.rank_pendant/getBls2020PersonalPendant")
    def get_bls2020_personal_pendant(self, room_id, ruid=None):
        """### bls2020单项赛挂件"""

    @grpc_call(path="/live.xactivity.rank_pendant/getBls2020FinalistPendant")
    def get_bls2020_finalist_pendant(self, room_id, act_id, ruid=None):
        """### bls2020全站赛挂件"""

    @grpc_call(path="/live.xactivity.rank_pendant/getBls2020UltimatePendant")
    def get_bls2020_ultimate_pendant(self, room_id, ruid=None):
        """### bls2020全站赛挂件"""

    @grpc_call(path="/live.xactivity.rank_pendant/getWidgetBanner")
    def get_widget_banner(self, act_id, room_id, ruid, source=None, uid=None):
        """### 获取活动挂件信息接口  TODO:以后统一走这个接口 返回挂件信息"""

    @grpc_call(path="/live.xactivity.rank_pendant/getMultipleWidgetBanner")
    def get_multiple_widget_banner(self, room_id, ruid, act_ids=None, source=None, uid=None):
        """### 批量获取挂件接口"""

    @grpc_call(path="/live.xactivity.rank_pendant/getWinterVacation2021Pendant")
    def get_winter_vacation2021_pendant(self, room_id, ruid=None):
        """### 2021寒假活动挂件"""

    @grpc_call(path="/live.xactivity.rank_pendant/getLanturn2021Pendant")
    def get_lanturn2021_pendant(self, act_id, room_id, ruid, source=None, uid=None):
        """### 元宵活动"""

    @grpc_call(path="/live.xactivity.rank_pendant/getMarchBlindGift2021Pendant")
    def get_march_blind_gift2021_pendant(self, act_id, room_id, ruid, source=None, uid=None):
        """### 三月盲盒活动"""


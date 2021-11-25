"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""
from tiny import grpc_call


class Pay_play(object):

    def __init__(self, service_name):
        self.service_name = service_name

    @grpc_call(path="/live.payplay.v1.PayLive/preBuy")
    def pre_buy(self, uid, goods_id, goods_num):
        """###付费直播预检"""

    @grpc_call(path="/live.payplay.v1.PayLive/sucBuy")
    def suc_buy(self, uid=None, goods_id=None, platform=None, order_id=None, goods_num=None, total_price=None):
        """###付费直播预检"""

    @grpc_call(path="/live.payplay.v1.PayLive/getMyTickets")
    def get_my_tickets(self, uid):
        """###获取我的票务列表"""

    @grpc_call(path="/live.payplay.v1.PayLive/getTicketDetail")
    def get_ticket_detail(self, uid, ticketing_id):
        """###获取门票详情"""

    @grpc_call(path="/live.payplay.v1.PayLive/shareTicket")
    def share_ticket(self, uid=None, ticket_number=None):
        """###分享接口"""

    @grpc_call(path="/live.payplay.v1.PayLive/getShareTicket")
    def get_share_ticket(self, uid=None, share_code=None):
        """###获取分享信息接口"""

    @grpc_call(path="/live.payplay.v1.PayLive/takeTicket")
    def take_ticket(self, uid=None, share_code=None):
        """###领取接口"""

    @grpc_call(path="/live.payplay.v1.PayLive/getTicketsStatus")
    def get_tickets_status(self, uid=None, ticket_number=None):
        """###获取门票状态"""

    @grpc_call(path="/live.payplay.v1.PayLive/buyInfo")
    def buy_info(self, ticketing_id=None):
        """### 支付组件票务详情"""

    @grpc_call(path="/live.payplay.v1.PayLive/sendTicket")
    def send_ticket(self, uids, goods_id, apply_name, reason, msg_id, send_message=None):
        """###赠票（奖励、后台）"""

    @grpc_call(path="/live.payplay.v1.PayLive/liveValidate")
    def live_validate(self, uid=None, room_id=None, ip=None):
        """###付费直播间鉴权"""


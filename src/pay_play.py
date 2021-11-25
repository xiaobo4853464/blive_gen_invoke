from tiny import grpc_call

class Pay_play(object):
    def __init__(self,service_name):
        self.service_name=service_name
    
    @grpc_call(path="/live.payplay.v1.payLiveAdmin/AddGoods")
    def add_goods(self, platform=None, title=None, back_title=None, type=None, price=None, start_time=None, end_time=None, ip_limit=None, is_limit_total=None, limit_total_num=None, is_need=None, award_list=None, show_image=None, show_start_time=None, show_end_time=None):
        """###*"""

    @grpc_call(path="/live.payplay.v1.payLiveAdmin/UpdateGoods")
    def update_goods(self, id=None, platform=None, title=None, back_title=None, type=None, price=None, start_time=None, end_time=None, ip_limit=None, is_limit_total=None, limit_total_num=None, is_need=None, award_list=None, show_image=None, show_start_time=None, show_end_time=None):
        """###*"""

    @grpc_call(path="/live.payplay.v1.payLiveAdmin/GetGoodsList")
    def get_goods_list(self, id=None, platform=None, back_title=None, type=None, ip_limit=None, page_num=None, page_size=None):
        """###*"""

    @grpc_call(path="/live.payplay.v1.payLiveAdmin/CloseBuy")
    def close_buy(self, id=None):
        """###*"""

    @grpc_call(path="/live.payplay.v1.payLiveAdmin/OpenBuy")
    def open_buy(self, id=None):
        """###*"""

    @grpc_call(path="/live.payplay.v1.payLiveAdmin/ApplyGiveTicket")
    def apply_give_ticket(self, goods_id=None, uid=None, apply_name=None, reason=None):
        """###*"""

    @grpc_call(path="/live.payplay.v1.payLiveAdmin/AddLive")
    def add_live(self, room_id, title, start_time, end_time, live_pic, ad_pic, goods_link, goods_id, buy_goods_id, platform=None, status=None, live_end_time=None, ip_limit=None):
        """###* 生成付费直播信息"""

    @grpc_call(path="/live.payplay.v1.payLiveAdmin/UpdateLive")
    def update_live(self, live_id=None, platform=None, room_id=None, title=None, status=None, start_time=None, end_time=None, live_end_time=None, live_pic=None, ad_pic=None, goods_link=None, goods_id=None, buy_goods_id=None, ip_limit=None):
        """###* 更新付费直播信息"""

    @grpc_call(path="/live.payplay.v1.payLiveAdmin/GetLiveList")
    def get_live_list(self, room_id=None, title=None, ip_limit=None, page_num=None, page_size=None, source=None):
        """###* 获取付费直播列表"""

    @grpc_call(path="/live.payplay.v1.payLiveAdmin/CloseAuth")
    def close_auth(self, live_id=None):
        """###* 关闭鉴权"""

    @grpc_call(path="/live.payplay.v1.payLiveAdmin/OpenAuth")
    def open_auth(self, live_id=None):
        """###* 开启鉴权"""

    @grpc_call(path="/live.payplay.v1.payLiveAdmin/GetAllGoodsSimpleInfo")
    def get_all_goods_simple_info(self, title=None):
        """###* 获取所有票务简单信息(活动奖励后台)"""

    @grpc_call(path="/live.payplay.v1.SuperChat/enable")
    def enable(self, room_id, ruid, parent_area_id=None, area_id=None):
        """### 获取房间是否开启留言"""

    @grpc_call(path="/live.payplay.v1.SuperChat/getMessageList")
    def get_message_list(self, room_id, ruid=None, needIsRanked=None):
        """### 房间留言列表"""

    @grpc_call(path="/live.payplay.v1.SuperChat/ownMessageList")
    def own_message_list(self, room_id, uid, ruid=None):
        """### 登陆用户留言列表"""

    @grpc_call(path="/live.payplay.v1.SuperChat/config")
    def config(self, room_id, ruid, uid, parent_area_id=None, area_id=None):
        """### 获取下发文案配置 和档位配置"""

    @grpc_call(path="/live.payplay.v1.SuperChat/isEnable")
    def is_enable(self, room_id, parent_area_id, area_id):
        """### 房间是否开通付费留言功能 （不带列表，只返回功能开通状态）"""

    @grpc_call(path="/live.payplay.v1.Lpl/queryOrder")
    def query_order(self, uid=None, order_id=None):
        """### 对账"""

    @grpc_call(path="/live.payplay.v1.Lpl/support")
    def support(self, platform=None, build=None, mobi_app=None, uid=None, room_id=None, match_id=None, round=None, team_id=None, player_id=None, cmt_id=None, buy_num=None, live_statistics=None, statistics=None, ip=None):
        """### 付费支持"""

    @grpc_call(path="/live.payplay.v1.Lpl/matchInfo")
    def match_info(self, room_id=None, match_id=None, round=None):
        """### 比赛信息"""

    @grpc_call(path="/live.payplay.v1.PayLiveClass/createPayLiveRoom")
    def create_pay_live_room(self, epid, face, title, room_id, start_time, end_time, link_url, ip_limit=None):
        """###创建一个付费直播间"""

    @grpc_call(path="/live.payplay.v1.PayLiveClass/updatePayLiveRoom")
    def update_pay_live_room(self, pay_live_id, epid, face, title, room_id, start_time, end_time, link_url, ip_limit=None):
        """###更新一个付费直播间"""

    @grpc_call(path="/live.payplay.v1.PayLiveClass/updatePayLiveStatus")
    def update_pay_live_status(self, pay_live_id, status=None):
        """### 更新付费直播状态"""

    @grpc_call(path="/live.payplay.v1.PayLiveClass/checkPayLiveRoom")
    def check_pay_live_room(self, room_id, start_time, end_time):
        """### 判断是否是付费直播间"""

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

from tiny import grpc_call

class Xlottery(object):
    def __init__(self,service_name):
        self.service_name=service_name
    
    @grpc_call(path="/live.xlottery.v1.SmallTV/Start")
    def start(self, uid=None, roomid=None, gift_id=None, num=None, tid=None, style_id=None, area_id=None, not_send_notice=None):
        """### 开启小电视抽奖"""

    @grpc_call(path="/live.xlottery.v1.SmallTV/Join")
    def join(self, roomid, raffleId, type, uid=None):
        """### 加入小电视抽奖"""

    @grpc_call(path="/live.xlottery.v1.SmallTV/Notice")
    def notice(self, raffleId, type, uid=None):
        """### 获取中奖结果"""

    @grpc_call(path="/live.xlottery.v1.SmallTV/GetAward")
    def get_award(self, roomid, raffleId, type, uid=None, platform=None):
        """### v4版的notice"""

    @grpc_call(path="/live.xlottery.v1.SmallTV/Check")
    def check(self, roomid, uid=None):
        """### 检查是否加入了小电视抽奖 v4版"""

    @grpc_call(path="/live.xlottery.v1.SmallTV/Check3")
    def check3(self, roomid, uid=None):
        """### 检查是否加入了小电视抽奖 v3版"""

    @grpc_call(path="/live.xlottery.v1.SmallTV/DBConf")
    def d_b_conf(self, method=None, awardID=None, giftID=None, table=None, content=None):
        """### 修改小电视配置"""

    @grpc_call(path="/live.xlottery.v1.SmallTV/JoinTV")
    def join_t_v(self, roomid, id, type, uid=None):
        """###2019.7.24"""

    @grpc_call(path="/live.xlottery.v1.SmallTV/CheckTV")
    def check_t_v(self, roomid, uid=None):
        """### 新check"""

    @grpc_call(path="/live.xlottery.v1.Lottery/DanmuStart")
    def danmu_start(self, roomid=None, ruid=None, uid=None):
        """### **************弹幕抽奖**************"""

    @grpc_call(path="/live.xlottery.v1.Lottery/DanmuJoin")
    def danmu_join(self, id, uid=None, source=None, session_id=None, launch_id=None, jumpfrom=None, jumpfrom_extend=None, simple_id=None, screen_status=None, live_status=None, av_id=None, flow_extend=None, bussiness_extend=None, data_extend=None):
        """### 参与弹幕抽奖"""

    @grpc_call(path="/live.xlottery.v1.Lottery/DanmuCheck")
    def danmu_check(self, roomid, uid=None):
        """### 进入房间页检查有无弹幕抽奖"""

    @grpc_call(path="/live.xlottery.v1.Lottery/DanmuAdd")
    def danmu_add(self, roomid, duration, award_name, award_num, award_image, name=None, danmu=None, join_type=None, require_type=None, require_value=None, gift_id=None, gift_name=None, price=None, creater=None):
        """### 弹幕抽奖后台"""

    @grpc_call(path="/live.xlottery.v1.Lottery/DanmuUpdate")
    def danmu_update(self, status, id, roomid):
        """### 下线接口"""

    @grpc_call(path="/live.xlottery.v1.Lottery/DanmuList")
    def danmu_list(self, page):
        """###  弹幕抽奖配置列表页 """

    @grpc_call(path="/live.xlottery.v1.Lottery/DanmuWinUsers")
    def danmu_win_users(self, id):
        """###  弹幕中奖用户列表"""

    @grpc_call(path="/live.xlottery.v1.Lottery/DanmuGiftListByRoomID")
    def danmu_gift_list_by_room_i_d(self, roomid):
        """### 根据房间页查询 礼物面板列表"""

    @grpc_call(path="/live.xlottery.v1.lottery/get_list")
    def get_list(self, page, page_size):
        """### 获取配置列表"""

    @grpc_call(path="/live.xlottery.v1.lottery/get_plan")
    def get_plan(self, id):
        """### 获取计划详情"""

    @grpc_call(path="/live.xlottery.v1.lottery/add_award")
    def add_award(self, id=None, pool_id=None, award_type=None, award_id=None, award_id_type=None, award_expire=None, award_expire_type=None, award_num=None, chance=None, asset_icon=None, day_limit=None, week_limit=None, round_limit=None):
        """### 添加奖品"""

    @grpc_call(path="/live.xlottery.v1.lottery/update_plan_status")
    def update_plan_status(self, id=None, status=None):
        """### 下线计划"""

    @grpc_call(path="/live.xlottery.v1.lottery/update_award_status")
    def update_award_status(self, id=None, status=None):
        """### 删除奖励"""

    @grpc_call(path="/live.xlottery.v1.gift_draw/drawPrize")
    def draw_prize(self, uid, gift_id, anchor_id, room_id, third_id, continuous_num, lottery_time, platform, lottrty_id, build=None, parent_area_id=None, area_id=None, mobi_app=None, gift_source=None):
        """### 道具抽实物奖励"""

    @grpc_call(path="/live.xlottery.v1.gift_draw/getLotteryRes")
    def get_lottery_res(self, draw_id, uid):
        """### 获取抽奖结果"""

    @grpc_call(path="/live.xlottery.v1.gift_draw/getAwardPoolInfo")
    def get_award_pool_info(self, room_id, act_id):
        """### 新的获取奖池信息"""

    @grpc_call(path="/live.xlottery.v1.SilverBox/GetCurrentTask")
    def get_current_task(self, uid=None, platform=None):
        """### 银瓜子宝箱"""

    @grpc_call(path="/live.xlottery.v1.RedPocket/RedPocketCreate")
    def red_pocket_create(self, ruid=None, amount=None, order_id=None, biz_extra=None):
        """### 创建官方红包"""

    @grpc_call(path="/live.xlottery.v1.RedPocket/RedPocketUpdate")
    def red_pocket_update(self, id, entry_type, delay_receive_time, sponsor_uid=None, appointment_time=None, focus_users=None):
        """### 更新官方红包信息"""

    @grpc_call(path="/live.xlottery.v1.RedPocket/RedPocketUpdateStatus")
    def red_pocket_update_status(self, id, status):
        """### 更新红包状态"""

    @grpc_call(path="/live.xlottery.v1.RedPocket/RedPocketGetList")
    def red_pocket_get_list(self, page, page_size, ruid=None, sponsor_uid=None, status=None):
        """### 获取官方红包列表"""

    @grpc_call(path="/live.xlottery.v1.RedPocket/RedPocketPreCheck")
    def red_pocket_pre_check(self, uid, amount, biz_extra):
        """### 官方红包商品预检(用于订单系统)"""

    @grpc_call(path="/live.xlottery.v1.RedPocket/RedPocketTrigger")
    def red_pocket_trigger(self, id):
        """### 立即触发红包抽奖"""

    @grpc_call(path="/live.xlottery.v1.RedPocket/RedPocketCheck")
    def red_pocket_check(self, roomId=None, uid=None):
        """### 获取抽奖信息 方法为get"""

    @grpc_call(path="/live.xlottery.v1.RedPocket/RedPocketGetResult")
    def red_pocket_get_result(self, id=None, uid=None, serverHash=None):
        """### 获取中奖情况 方法为get"""

    @grpc_call(path="/live.xlottery.v1.RedPocket/RedPocketGetAwardList")
    def red_pocket_get_award_list(self, id=None):
        """### 获取中奖列表 方法为get"""

    @grpc_call(path="/live.xlottery.v1.Capsule/get_detail")
    def get_detail(self, uid=None, **from_):
        """### 无标题"""

    @grpc_call(path="/live.xlottery.v1.Capsule/open_capsule")
    def open_capsule(self, uid=None, type=None, count=None, platform=None):
        """### 无标题"""

    @grpc_call(path="/live.xlottery.v1.Capsule/get_coin_list")
    def get_coin_list(self, page, page_size):
        """###获取抽奖券列表"""

    @grpc_call(path="/live.xlottery.v1.Capsule/get_coin_detail")
    def get_coin_detail(self, id=None):
        """### 无标题"""

    @grpc_call(path="/live.xlottery.v1.Capsule/update_coin_config")
    def update_coin_config(self, title, change_num, start_time, end_time, gift_type, id=None, status=None, gift_config=None, area_ids=None, all_room=None, weight=None, auto_turn=None, room_ids=None):
        """### 无标题"""

    @grpc_call(path="/live.xlottery.v1.Capsule/update_coin_status")
    def update_coin_status(self, id, status=None):
        """### 无标题"""

    @grpc_call(path="/live.xlottery.v1.Capsule/delete_coin")
    def delete_coin(self, id):
        """### 无标题"""

    @grpc_call(path="/live.xlottery.v1.Capsule/get_pool_list")
    def get_pool_list(self, page, page_size, type=None, pool_id=None, title=None):
        """###获取奖池列表"""

    @grpc_call(path="/live.xlottery.v1.Capsule/update_pool")
    def update_pool(self, title, start_time, end_time, rule, id=None, type=None, coin_id=None, open_num_1=None, product_limit_1=None, is_limit_1=None, open_num_2=None, product_limit_2=None, is_limit_2=None, open_num_3=None, product_limit_3=None, is_limit_3=None, operate_user_name=None, is_single_pool=None):
        """###更新奖池"""

    @grpc_call(path="/live.xlottery.v1.Capsule/delete_pool")
    def delete_pool(self, id):
        """###删除奖池"""

    @grpc_call(path="/live.xlottery.v1.Capsule/update_pool_status")
    def update_pool_status(self, id, status=None):
        """###更新奖池是否执行状态"""

    @grpc_call(path="/live.xlottery.v1.Capsule/get_pool_detail")
    def get_pool_detail(self, pool_id, uid=None):
        """### 无标题"""

    @grpc_call(path="/live.xlottery.v1.Capsule/get_pool_prize")
    def get_pool_prize(self, pool_id):
        """###获取某个奖池的奖励列表"""

    @grpc_call(path="/live.xlottery.v1.Capsule/get_prize_type")
    def get_prize_type(self, type=None):
        """###获取所有的奖励类型"""

    @grpc_call(path="/live.xlottery.v1.Capsule/update_pool_prize")
    def update_pool_prize(self, type, id=None, pool_id=None, num=None, object_id=None, expire=None, web_url=None, mobile_url=None, description=None, jump_url=None, pro_type=None, chance=None, loop=None, limit=None, weight=None, white_uids=None, limit_type=None, single_limit_num=None, all_limit_num=None, operate_user_name=None, is_single_pool=None):
        """###更新或创建奖池的奖励列表"""

    @grpc_call(path="/live.xlottery.v1.Capsule/delete_pool_prize")
    def delete_pool_prize(self, id):
        """###删除奖池的奖励列表"""

    @grpc_call(path="/live.xlottery.v1.Capsule/get_capsule_info")
    def get_capsule_info(self, uid=None, type=None, **from_):
        """### 无标题"""

    @grpc_call(path="/live.xlottery.v1.Capsule/get_capsule_info_by_id")
    def get_capsule_info_by_id(self, uid=None, id=None, **from_):
        """### 无标题"""

    @grpc_call(path="/live.xlottery.v1.Capsule/open_capsule_by_type")
    def open_capsule_by_type(self, uid=None, type=None, count=None, platform=None, ip=None):
        """### 无标题"""

    @grpc_call(path="/live.xlottery.v1.Capsule/open_capsule_by_id")
    def open_capsule_by_id(self, uid=None, id=None, count=None, platform=None):
        """### 无标题"""

    @grpc_call(path="/live.xlottery.v1.Capsule/open_capsule_by_pool")
    def open_capsule_by_pool(self, pool_id=None, round_id=None, uids=None, is_send_award=None, bottom_pool_id=None):
        """### 无标题"""

    @grpc_call(path="/live.xlottery.v1.Capsule/get_coupon_list")
    def get_coupon_list(self, uid=None):
        """### 无标题"""

    @grpc_call(path="/live.xlottery.v1.Capsule/get_product_list")
    def get_product_list(self, page, page_size):
        """### 无标题"""

    @grpc_call(path="/live.xlottery.v1.Capsule/update_product")
    def update_product(self, id=None, name=None):
        """### 无标题"""

    @grpc_call(path="/live.xlottery.v1.Capsule/update_product_status")
    def update_product_status(self, id=None, status=None):
        """### 无标题"""

    @grpc_call(path="/live.xlottery.v1.Capsule/get_prize_list_by_type")
    def get_prize_list_by_type(self, prize_type=None, object_id=None):
        """###获取某个奖励类型下的所有奖励，如获取实物奖励类型的所有奖励"""

    @grpc_call(path="/live.xlottery.v1.Capsule/get_prize_by_ids")
    def get_prize_by_ids(self, ids):
        """### 无标题"""

    @grpc_call(path="/live.xlottery.v1.Capsule/get_pool_status")
    def get_pool_status(self, ids=None):
        """### 无标题"""

    @grpc_call(path="/live.xlottery.v1.Capsule/reduce_user_capsule")
    def reduce_user_capsule(self, uid, coin_id, count, platform):
        """### 无标题"""

    @grpc_call(path="/live.xlottery.v1.Capsule/get_user_coin_num")
    def get_user_coin_num(self, uid, coin_id):
        """### 无标题"""

    @grpc_call(path="/live.xlottery.v1.Capsule/get_pool_prize_by_pool")
    def get_pool_prize_by_pool(self, pool_id, bottom_pool_id=None):
        """### 无标题"""

    @grpc_call(path="/live.xlottery.v1.Capsule/open_capsule_by_id_with_multi_pool")
    def open_capsule_by_id_with_multi_pool(self, uid=None, coin_id=None, pool_id=None, count=None, each_num=None, **from_):
        """### 无标题"""

    @grpc_call(path="/live.xlottery.v1.Capsule/get_coin_gift")
    def get_coin_gift(self, coin_id=None, room_id=None):
        """###获取扭蛋要送什么礼物，获取礼物列表的接口"""

    @grpc_call(path="/live.xlottery.v1.Capsule/get_user_award")
    def get_user_award(self, uid=None, lottery_date=None, page=None, page_size=None):
        """###给运营产品客服看的用户抽扭蛋获得的奖励"""

    @grpc_call(path="/live.xlottery.v1.Capsule/get_user_award_list")
    def get_user_award_list(self, uid, page=None, page_size=None):
        """###获取用户最近的50条奖励"""

    @grpc_call(path="/live.xlottery.v1.Capsule/SendAwardByCapsuleId")
    def send_award_by_capsule_id(self, uid, capsule_id, award_type, award_num):
        """### 发送特定奖池奖品"""

    @grpc_call(path="/live.xlottery.v1.Capsule/GetUserAwardLogByPoolId")
    def get_user_award_log_by_pool_id(self, uid=None, pool_ids=None, next_id=None, page_size=None, month=None):
        """### 获取用户中奖记录"""

    @grpc_call(path="/live.xlottery.v1.Capsule/SendAwardCdk")
    def send_award_cdk(self, uid, ex_id, award_num, web_img=None, mobile_img=None, source=None, source_id=None, activity_owner=None):
        """###直接发放cdk"""

    @grpc_call(path="/live.xlottery.v1.Capsule/SendCdk")
    def send_cdk(self, object_id=None, uid=None, stream_id=None, source=None, num=None):
        """### 发放cdk"""

    @grpc_call(path="/live.xlottery.v1.gift_lottery/get_list")
    def get_list(self, page, page_size):
        """###后台"""

    @grpc_call(path="/live.xlottery.v1.gift_lottery/get_plan")
    def get_plan(self, id):
        """### 获取计划详情"""

    @grpc_call(path="/live.xlottery.v1.gift_lottery/add_award")
    def add_award(self, id=None, pool_id=None, award_type=None, award_id=None, award_expire=None, award_expire_type=None, award_num=None, chance=None, asset_icon=None, day_limit=None, week_limit=None, round_limit=None, award_name=None):
        """### 添加奖品"""

    @grpc_call(path="/live.xlottery.v1.gift_lottery/update_plan_status")
    def update_plan_status(self, id=None, status=None):
        """### 下线计划"""

    @grpc_call(path="/live.xlottery.v1.gift_lottery/update_award_status")
    def update_award_status(self, id=None, status=None):
        """### 删除奖励"""

    @grpc_call(path="/live.xlottery.v1.gift_lottery/getAward")
    def get_award(self, roomid, raffleId, type, uid=None, platform=None):
        """### 无标题"""

    @grpc_call(path="/live.xlottery.v1.gift_lottery/check")
    def check(self, roomid, uid=None):
        """###web端"""

    @grpc_call(path="/live.xlottery.v1.gift_lottery/join")
    def join(self, roomid, id, type, uid=None):
        """### 无标题"""

    @grpc_call(path="/live.xlottery.v1.gift_lottery/checkTV")
    def check_t_v(self, roomid, uid=None):
        """###app端"""

    @grpc_call(path="/live.xlottery.v1.gift_lottery/GetFleetLottery")
    def get_fleet_lottery(self, uid):
        """### 无标题"""

    @grpc_call(path="/live.xlottery.v1.Exchange_code/get_list")
    def get_list(self, page, page_size, ex_code_name=None, id=None, up_status=None):
        """###列表页面"""

    @grpc_call(path="/live.xlottery.v1.Exchange_code/get_one_record")
    def get_one_record(self, id=None):
        """###获取一条记录"""

    @grpc_call(path="/live.xlottery.v1.Exchange_code/update_info")
    def update_info(self, ex_code_name, ac_name, ac_link_web, ac_link_mobile, id=None, start_time=None, end_time=None, forever=None, remark=None, file_key=None):
        """###更新"""

    @grpc_call(path="/live.xlottery.v1.Exchange_code/update_status")
    def update_status(self, id, up_status=None):
        """###更新上下线状态"""

    @grpc_call(path="/live.xlottery.v1.Exchange_code/info_list")
    def info_list(self, page, page_size, ex_code_id, uid=None):
        """###查看详情列表"""

    @grpc_call(path="/live.xlottery.v1.Exchange_code/export_excel")
    def export_excel(self, ex_code_id, type, uid=None):
        """###导出excel"""

    @grpc_call(path="/live.xlottery.v1.Exchange_code/GetExchangeCodeInfo")
    def get_exchange_code_info(self, ex_ids):
        """###获取兑换码总量和库存"""

    @grpc_call(path="/live.xlottery.v1.Anchor/Gifts")
    def gifts(self, roomid, uid=None):
        """### 房间可用礼物列表"""

    @grpc_call(path="/live.xlottery.v1.Anchor/Add")
    def add(self, award_name, award_num, duration, danmu=None, join_type=None, require_type=None, require_value=None, gift_id=None, gift_name=None, gift_price=None, gift_num=None, roomid=None, uid=None, quiz_roomid=None, other_follow_roomid=None):
        """### 主播添加抽奖"""

    @grpc_call(path="/live.xlottery.v1.Anchor/Start")
    def start(self, id, uid=None):
        """### 主播开启抽奖"""

    @grpc_call(path="/live.xlottery.v1.Anchor/Recall")
    def recall(self, id, uid=None):
        """### 撤回抽奖"""

    @grpc_call(path="/live.xlottery.v1.Anchor/Stop")
    def stop(self, id, uid=None):
        """### 手动结束抽奖"""

    @grpc_call(path="/live.xlottery.v1.Anchor/SetEnd")
    def set_end(self, id, uid=None):
        """### 主播抽奖被驳回,通知已经知道"""

    @grpc_call(path="/live.xlottery.v1.Anchor/Info")
    def info(self, roomid, id=None, uid=None, need_winner=None):
        """### 主播是否有添加抽奖入口:1. 正在抽奖的信息, 前端轮训,必须传id 2. 进房间页面的时候,不需传id 3.抽奖结束时候端上h5页面关闭，广播无法传给h5的时候查询中奖用户，id需要，need_winner需要传true"""

    @grpc_call(path="/live.xlottery.v1.Anchor/Record")
    def record(self, page, uid=None):
        """### 主播抽奖记录"""

    @grpc_call(path="/live.xlottery.v1.Anchor/HasRecord")
    def has_record(self, uid=None):
        """### 有没有发起过抽奖"""

    @grpc_call(path="/live.xlottery.v1.Anchor/DanmuName")
    def danmu_name(self, uid=None):
        """### 历史词"""

    @grpc_call(path="/live.xlottery.v1.Anchor/Done")
    def done(self, id, uid=None):
        """### 处理完抽奖"""

    @grpc_call(path="/live.xlottery.v1.Anchor/BeOld")
    def be_old(self, uid=None):
        """### 主播端取消new的icon"""

    @grpc_call(path="/live.xlottery.v1.Anchor/Check")
    def check(self, roomid, uid=None):
        """### 房间页面有没有正在进行的抽奖"""

    @grpc_call(path="/live.xlottery.v1.Anchor/AwardRecord")
    def award_record(self, page, uid=None):
        """### 参与主播抽奖获奖记录"""

    @grpc_call(path="/live.xlottery.v1.Anchor/GiveAddressInfo")
    def give_address_info(self, id, address, uid=None, recipient=None, phone=None):
        """### 填写收货地址"""

    @grpc_call(path="/live.xlottery.v1.Anchor/RandTime")
    def rand_time(self, id):
        """### 校验时间"""

    @grpc_call(path="/live.xlottery.v1.Anchor/GetSpecialSkin")
    def get_special_skin(self, roomId):
        """### 获取是否有特殊皮肤"""

    @grpc_call(path="/live.xlottery.v1.Anchor/GetCheckLotteryList")
    def get_check_lottery_list(self, status, page, page_size, start_time=None, end_time=None, anchor_uid=None, lottery_id=None):
        """###获取待审核抽奖列表（待审核，已通过，已驳回）"""

    @grpc_call(path="/live.xlottery.v1.Anchor/GetLotteryResultList")
    def get_lottery_result_list(self, page, page_size, lottery_id=None, anchor_uid=None, start_time=None, end_time=None, award_name=None, uid=None):
        """###主播抽奖结果"""

    @grpc_call(path="/live.xlottery.v1.Anchor/GetLotteryUserList")
    def get_lottery_user_list(self, lottery_id):
        """###获取某条抽奖的中奖名单"""

    @grpc_call(path="/live.xlottery.v1.Anchor/GetWhiteList")
    def get_white_list(self, page, page_size, anchor_uid=None, start_time=None, end_time=None):
        """###主播白名单"""

    @grpc_call(path="/live.xlottery.v1.Anchor/DeleteWhiteAnchor")
    def delete_white_anchor(self, anchor_uid):
        """###删除白名单用户"""

    @grpc_call(path="/live.xlottery.v1.Anchor/SuperUID")
    def super_u_i_d(self, uids, method=None):
        """### 更新超级白名单（无需人工审核）"""

    @grpc_call(path="/live.xlottery.v1.Anchor/GetSkinList")
    def get_skin_list(self, page, page_size):
        """###换皮后台"""

    @grpc_call(path="/live.xlottery.v1.Anchor/UpdateSkinStatus")
    def update_skin_status(self, id, status=None):
        """###白名单状态修改"""

    @grpc_call(path="/live.xlottery.v1.Anchor/UpdateSkin")
    def update_skin(self, title, roomIds, startTime, endTime, id=None, titleColor=None, timeColor=None, awardColor=None, commonColor=None, unfollowedButton=None, followedButton=None, joinedButton=None, winButton=None, notWinButton=None, closeButton=None, endBulletFrame=None, joinBackground=None, joinedBackground=None, topPic=None, loadingAnimation=None, startBulletFrame=None, topFrameAnimation=None, emptyPic=None, ruleColor=None, awardPic=None, startBulletWiderFrame=None, startBulletHigherFrame=None):
        """###新增或update皮肤配置"""

    @grpc_call(path="/live.xlottery.v1.Pk/Join")
    def join(self, id, uid=None):
        """### 无标题"""

    @grpc_call(path="/live.xlottery.v1.Pk/Join2")
    def join2(self, id, uid=None):
        """### 无标题"""

    @grpc_call(path="/live.xlottery.v1.Pk/JoinPK")
    def join_p_k(self, id, uid=None):
        """### 新版即时抽奖"""

    @grpc_call(path="/live.xlottery.v1.Pk/Check")
    def check(self, roomid, uid=None):
        """### 无标题"""

    @grpc_call(path="/live.xlottery.v1.Storm/Start")
    def start(self, uid=None, ruid=None, roomid=None, useShield=None, num=None, beatid=None, skipExternalCheck=None):
        """### 开启节奏风暴"""

    @grpc_call(path="/live.xlottery.v1.Storm/CanStart")
    def can_start(self, uid=None, ruid=None, roomid=None, useShield=None, num=None, beatid=None, skipExternalCheck=None):
        """###节奏风暴是否能开启"""

    @grpc_call(path="/live.xlottery.v1.Storm/Join")
    def join(self, id=None, roomid=None, color=None, mid=None, platform=None, captcha_token=None, captcha_phrase=None, buvid=None):
        """###加入节奏风暴"""

    @grpc_call(path="/live.xlottery.v1.Storm/Check")
    def check(self, roomid, uid=None):
        """###检查是否加入节奏风暴 """

    @grpc_call(path="/live.xlottery.v1.Box/GetStatus")
    def get_status(self, roomid=None, uid=None, platform=None, aid=None):
        """### 活动宝箱"""

    @grpc_call(path="/live.xlottery.v1.Box/Draw")
    def draw(self, aid=None, number=None, uid=None, buvid=None):
        """### 参与抽奖"""

    @grpc_call(path="/live.xlottery.v1.Box/WinnerGroupInfo")
    def winner_group_info(self, aid=None, number=None, uid=None):
        """### getWinnerGroupInfo"""

    @grpc_call(path="/live.xlottery.v1.Box/GetRoomActivityByRoomid")
    def get_room_activity_by_roomid(self, roomid=None):
        """### 获取抽奖 web端接口"""

    @grpc_call(path="/live.xlottery.v1.Box/GetUserInfoList")
    def get_user_info_list(self, roomid=None, uids=None):
        """### 获取中奖用户信息"""

    @grpc_call(path="/live.xlottery.v1.Guard/Start")
    def start(self, uid=None, ruid=None, roomid=None, privilege=None, playflowID=None, sub_level=None, msg_id=None):
        """### 开启抽奖"""

    @grpc_call(path="/live.xlottery.v1.Guard/Join")
    def join(self, roomid, id, type, uid=None):
        """### 加入抽奖"""

    @grpc_call(path="/live.xlottery.v1.Guard/Check")
    def check(self, roomid, uid=None, isGetUser=None, isGetPayFlow=None):
        """### 房间页是否有抽奖"""

    @grpc_call(path="/live.xlottery.v1.Guard/JoinGuard")
    def join_guard(self, roomid, id, type, uid=None):
        """### 新版即时抽奖"""

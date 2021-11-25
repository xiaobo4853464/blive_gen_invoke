from tiny import grpc_call

class Xactivity(object):
    def __init__(self,service_name):
        self.service_name=service_name
    
    @grpc_call(path="/live.xactivity.v1.specApi/ActivityVideoPKIncr")
    def activity_video_p_k_incr(self, uid=None, ruid=None, room_id=None, parent_area_id=None, area_id=None, goods_type=None, goods_id=None, gift_id=None, coin_type=None, goods_num=None, pay_coin=None, total_coin=None, pk_score=None, pk_id=None, season_id=None, timestamp=None, msg_id=None, extra_json=None):
        """### pk值加分"""

    @grpc_call(path="/live.xactivity.v1.specApi/aprilBonus21PKLog")
    def april_bonus21_p_k_log(self, uid=None, ruid=None, timestamp=None):
        """### 赏金赛pk记录"""

    @grpc_call(path="/live.xactivity.v1.specApi/aprilBonus21Tab")
    def april_bonus21_tab(self, uid=None, room_id=None, rank_type=None):
        """### 获取榜单Tab"""

    @grpc_call(path="/live.xactivity.v1.specApi/aprilBonusRankDelete")
    def april_bonus_rank_delete(self, stage=None, round=None, type=None, uid=None, other=None):
        """### 本轮赏金榜 删除"""

    @grpc_call(path="/live.xactivity.v1.specApi/aprilBonusWithdraw")
    def april_bonus_withdraw(self, uid=None):
        """### 提现"""

    @grpc_call(path="/live.xactivity.v1.specApi/maySweetToken")
    def may_sweet_token(self, uid=None):
        """### 甜蜜季 碎片接口"""

    @grpc_call(path="/live.xactivity.v1.specApi/JSOpenStarToken")
    def j_s_open_star_token(self, uid=None, ruid=None, is_pay=None, ip=None):
        """### 用户开启星令"""

    @grpc_call(path="/live.xactivity.v1.specApi/JSGetUserStarToken")
    def j_s_get_user_star_token(self, uids=None, ruid=None):
        """### 批量获取用户星令开启状态"""

    @grpc_call(path="/live.xactivity.v1.specApi/JSReceiveAwards")
    def j_s_receive_awards(self, level=None, receive_type=None, uid=None, ruid=None):
        """### 星令领取奖励"""

    @grpc_call(path="/live.xactivity.v1.specApi/JSAwardsList")
    def j_s_awards_list(self, uid=None, ruid=None):
        """### 星令奖励列表"""

    @grpc_call(path="/live.xactivity.v1.specApi/JSLottery")
    def j_s_lottery(self, pool_id=None, num=None, uid=None, risk=None):
        """### 七月星令抽奖"""

    @grpc_call(path="/live.xactivity.v1.specApi/JSShareAct")
    def j_s_share_act(self, uid=None, ruid=None):
        """### 分享动态加经验，只有第一次分享才能获得经验"""

    @grpc_call(path="/live.xactivity.v1.specApi/julyStarTxStatus")
    def july_star_tx_status(self, uid=None):
        """### 7月嘉年华获取兑换状态(含权用"""

    @grpc_call(path="/live.xactivity.v1.specApi/julyCarnivalScoreLog")
    def july_carnival_score_log(self, uid=None, page=None, page_size=None):
        """### 七月预热 积分记录"""

    @grpc_call(path="/live.xactivity.v1.specApi/julyStarTokenScoreLog")
    def july_star_token_score_log(self, uid=None, page=None, page_size=None):
        """### 七月第二阶段 积分记录"""

    @grpc_call(path="/live.xactivity.v1.specApi/JulyRankTask")
    def july_rank_task(self, act_id=None, uid=None):
        """### 7月嘉年华 任务进度"""

    @grpc_call(path="/live.xactivity.v1.specApi/JulyRankTaskUpgrade")
    def july_rank_task_upgrade(self, uid=None, level=None, act_id=None, platform=None, mobi_app=None, build=None, device=None, **from_):
        """###  7月嘉年华 任务升级"""

    @grpc_call(path="/live.xactivity.v1.specApi/JulyRankLuckDog")
    def july_rank_luck_dog(self, act_id=None):
        """### 7月嘉年华 第三阶段欧皇信息接口"""

    @grpc_call(path="/live.xactivity.v1.specApi/JulyRankBatteryReward")
    def july_rank_battery_reward(self, act_id=None):
        """###  7月嘉年华 第三阶段福利大放送接口"""

    @grpc_call(path="/live.xactivity.v1.specApi/JulyRankParentAreaSign")
    def july_rank_parent_area_sign(self, uid=None):
        """### 7月嘉年华 第三阶段 大分区赛新人报名导入"""

    @grpc_call(path="/live.xactivity.v1.specApi/JulyRankAreaSign")
    def july_rank_area_sign(self, uid=None):
        """### 7月嘉年华 第三阶段 小分区赛60强报名导入"""

    @grpc_call(path="/live.xactivity.v1.specApi/AGOpenFreeGuard")
    def a_g_open_free_guard(self, uid=None, ruid=None, is_pay=None, ip=None):
        """### 《《《《《《《《《《《《《《《《8月大航海》》》》》》》》》》》》》》》》》》》》》》》"""

    @grpc_call(path="/live.xactivity.v1.specApi/AGLottery")
    def a_g_lottery(self, pool_id=None, num=None, uid=None, risk=None):
        """### 8月 星令抽奖"""

    @grpc_call(path="/live.xactivity.v1.specApi/AGBoxLottery")
    def a_g_box_lottery(self, pool_id=None, ruid=None, uid=None, risk=None):
        """### 8月 宝箱抽奖"""

    @grpc_call(path="/live.xactivity.v1.specApi/AGAwardsList")
    def a_g_awards_list(self, uid=None, ruid=None):
        """### 8月 星令奖励列表"""

    @grpc_call(path="/live.xactivity.v1.specApi/AGReceiveAwards")
    def a_g_receive_awards(self, level=None, receive_type=None, uid=None, ruid=None):
        """### 8月 星令领取奖励"""

    @grpc_call(path="/live.xactivity.v1.specApi/AGShareAct")
    def a_g_share_act(self, uid=None, ruid=None):
        """### 8月 分享动态加经验，只有第一次分享才能获得经验"""

    @grpc_call(path="/live.xactivity.v1.specApi/AGGetUserStarToken")
    def a_g_get_user_star_token(self, uids=None, ruid=None):
        """### 8月 批量获取用户星令开启状态"""

    @grpc_call(path="/live.xactivity.v1.specApi/AGLotteryLuckyGuysLog")
    def a_g_lottery_lucky_guys_log(self, uid=None):
        """### 8月 抽奖"吸吸欧气"列表(写db会回源"""

    @grpc_call(path="/live.xactivity.v1.specApi/SepActTaskUpgrade")
    def sep_act_task_upgrade(self, uid=None, level=None):
        """### 《9月超星学园》 9月用户任务升级"""

    @grpc_call(path="/live.xactivity.v1.specApi/SepActUserTaskInfo")
    def sep_act_user_task_info(self, uid=None):
        """### 9月用户任务信息"""

    @grpc_call(path="/live.xactivity.v1.specApi/SepActPoolInfo")
    def sep_act_pool_info(self, uid=None):
        """### 9月奖池信息"""

    @grpc_call(path="/live.xactivity.v1.specApi/SepActUseCard")
    def sep_act_use_card(self, uid=None, card_type=None):
        """### 9月用户使用技能卡"""

    @grpc_call(path="/live.xactivity.v1.specApi/SepMABagLottery")
    def sep_m_a_bag_lottery(self, id, uid, act_id, platform=None, mobi_app=None, build=None, device=None, **from_):
        """### 9月中秋领取福袋"""

    @grpc_call(path="/live.xactivity.v1.specApi/ActDataCardValidState")
    def act_data_card_valid_state(self, uid):
        """### 活动资料卡皮肤有效状态查询"""

    @grpc_call(path="/live.xactivity.v1.specApi/SGOpenFreeGuard")
    def s_g_open_free_guard(self, uid=None, ruid=None, is_pay=None, ip=None):
        """### 《《《《《《《《《《《《《《《《9月大航海》》》》》》》》》》》》》》》》》》》》》》》"""

    @grpc_call(path="/live.xactivity.v1.specApi/SGLottery")
    def s_g_lottery(self, pool_id=None, num=None, uid=None, risk=None):
        """### 9月 星令抽奖"""

    @grpc_call(path="/live.xactivity.v1.specApi/SGAwardsList")
    def s_g_awards_list(self, uid=None, ruid=None):
        """### 9月 星令奖励列表"""

    @grpc_call(path="/live.xactivity.v1.specApi/sGReceiveAwards")
    def s_g_receive_awards(self, level=None, receive_type=None, uid=None, ruid=None):
        """### 9月 星令领取奖励"""

    @grpc_call(path="/live.xactivity.v1.specApi/SGShareAct")
    def s_g_share_act(self, uid=None, ruid=None):
        """### 9月 分享动态加经验，只有第一次分享才能获得经验"""

    @grpc_call(path="/live.xactivity.v1.specApi/SGGetUserStarToken")
    def s_g_get_user_star_token(self, uids=None, ruid=None):
        """### 9月 批量获取用户星令开启状态"""

    @grpc_call(path="/live.xactivity.v1.specApi/SGLotteryLuckyGuysLog")
    def s_g_lottery_lucky_guys_log(self, uid=None):
        """### 9月 抽奖"吸吸欧气"列表(写db会回源"""

    @grpc_call(path="/live.xactivity.v1.specApi/SGTaskInfos")
    def s_g_task_infos(self, ruid=None):
        """### 9月 任务接口"""

    @grpc_call(path="/live.xactivity.v1.specApi/TokenInfos")
    def token_infos(self, uid=None, ruid=None):
        """### 星令通用"""

    @grpc_call(path="/live.xactivity.v1.specApi/Sep21TopicTaskInfo")
    def sep21_topic_task_info(self, uid=None, task_type=None):
        """### 9月话题活动 - 任务信息接口"""

    @grpc_call(path="/live.xactivity.v1.specApi/Sep21TopicReceiveAward")
    def sep21_topic_receive_award(self, uid=None, task_type=None):
        """### 9月话题活动 - 领取任务奖励接口"""

    @grpc_call(path="/live.xactivity.v1.specApi/Sep21TopicPreApply")
    def sep21_topic_pre_apply(self, uid=None, task_type=None):
        """### 9月话题活动 - 预报名接口"""

    @grpc_call(path="/live.xactivity.v1.specApi/OctNationalGiftWall")
    def oct_national_gift_wall(self, uid=None):
        """### 国庆活动 礼物墙"""

    @grpc_call(path="/live.xactivity.v1.specApi/OctNationalAchievementReceive")
    def oct_national_achievement_receive(self, uid=None, achivement_id=None):
        """### 国庆活动 成就领取"""

    @grpc_call(path="/live.xactivity.v1.specApi/Oct21RedLeafPoolInfo")
    def oct21_red_leaf_pool_info(self, pool_id):
        """### 10月红叶赏奖池信息接口"""

    @grpc_call(path="/live.xactivity.v1.specApi/Oct21RedLeafPoolList")
    def oct21_red_leaf_pool_list(self, start_pool_id):
        """### 10月红叶赏奖池列表接口"""

    @grpc_call(path="/live.xactivity.v1.specApi/Oct21RedLeafNewGuide")
    def oct21_red_leaf_new_guide(self, uid=None):
        """### 10月红叶赏记录新手引导"""

    @grpc_call(path="/live.xactivity.v1.specApi/Oct21RedLeafDrawBag")
    def oct21_red_leaf_draw_bag(self, uid, pool_id, pool_version, draw_num, ruid, bag_id=None, type=None, is_confirm_pay_toast=None, ip=None):
        """### 10月红叶赏抽取福袋接口"""

    @grpc_call(path="/live.xactivity.v1.specApi/NovDriftingBottleThrow")
    def nov_drifting_bottle_throw(self, uid=None, ruid=None, drifting_content=None, platform=None):
        """### >>>>>>>>>>>双十一漂流瓶<<<<<<<<<<<<<<"""

    @grpc_call(path="/live.xactivity.v1.specApi/NovDriftingBottleOpen")
    def nov_drifting_bottle_open(self, uid=None, ruid=None, bottle_id=None, type=None):
        """### 捞瓶子"""

    @grpc_call(path="/live.xactivity.v1.specApi/NovDriftingBottlePool")
    def nov_drifting_bottle_pool(self, ruid=None):
        """### 池塘"""

    @grpc_call(path="/live.xactivity.v1.specApi/BLS2021PreStarWish")
    def b_l_s2021_pre_star_wish(self, uid=None, wish_id=None, star_num=None):
        """### bls2021 星点许愿"""

    @grpc_call(path="/live.xactivity.v1.specApi/BLS2021PreStarWishLog")
    def b_l_s2021_pre_star_wish_log(self, uid=None, page=None):
        """### bls2021 星点许愿获取记录"""

    @grpc_call(path="/live.xactivity.v1.specApi/Bls21AreaReceiveRewards")
    def bls21_area_receive_rewards(self, uid=None, reward_id=None):
        """### BLS小分区赛 领取礼物墙奖励"""

    @grpc_call(path="/live.xactivity.v1.specApi/Bls21BigPlayerData")
    def bls21_big_player_data(self, uid=None):
        """### BLS大玩家 数据接口"""

    @grpc_call(path="/live.xactivity.v1.specApi/NovAnchorActScoreLog")
    def nov_anchor_act_score_log(self, uid=None, page=None, page_size=None):
        """### 11月全平台主播活动 积分记录"""

    @grpc_call(path="/live.xactivity.v1.specApi/SnowEnjoyPoolInfo")
    def snow_enjoy_pool_info(self, pool_id, pool_type):
        """### 冰雪赏奖池信息接口"""

    @grpc_call(path="/live.xactivity.v1.specApi/SnowEnjoyPoolList")
    def snow_enjoy_pool_list(self, start_pool_id, pool_type):
        """### 冰雪赏奖池列表接口"""

    @grpc_call(path="/live.xactivity.v1.specApi/SnowEnjoyNewGuide")
    def snow_enjoy_new_guide(self, uid=None):
        """###冰雪赏记录新手引导"""

    @grpc_call(path="/live.xactivity.v1.specApi/SnowEnjoyDrawBag")
    def snow_enjoy_draw_bag(self, uid, pool_id, pool_version, draw_num, ruid, pool_type, bag_id=None, type=None, is_confirm_pay_toast=None, ip=None):
        """### 冰雪赏抽取福袋接口"""

    @grpc_call(path="/live.xactivity.v1.specApi/BLS21ParentAreaPKList")
    def b_l_s21_parent_area_p_k_list(self, team_id=None):
        """### 大分区赛pk list"""

    @grpc_call(path="/live.xactivity.v1.specApi/BlsBigAreaForceSwitch")
    def bls_big_area_force_switch(self, act_id=None, uid=None, team_id=None, sign_id=None, rank_id=None):
        """### BLS大分区赛 临时使用,强制切换赛道"""

    @grpc_call(path="/live.xactivity.v1.specApi/BLS2021VSRankWheelData")
    def b_l_s2021_v_s_rank_wheel_data(self, team_id=None, ruid=None, wheel_id=None):
        """### BLS虚拟专项赛排位车轮赛数据"""

    @grpc_call(path="/live.xactivity.v1.specApi/BlsLifeSubArea")
    def bls_life_sub_area(self, uid=None, areas=None):
        """### BLS生活预约分区"""

    @grpc_call(path="/live.xactivity.v1.specApi/BlsLifeSubList")
    def bls_life_sub_list(self, uid=None):
        """### BLS生活 预约结果"""

    @grpc_call(path="/live.xactivity.v1.spring/halfInit")
    def half_init(self, room_id=None, uid=None):
        """### 半屏初始化接口"""

    @grpc_call(path="/live.xactivity.v1.spring/fullInit")
    def full_init(self, uid=None):
        """### 全屏初始化接口"""

    @grpc_call(path="/live.xactivity.v1.spring/getSignUpTeam")
    def get_sign_up_team(self, act_id=None, ruid=None, extra_data=None):
        """### 获取报名赛道接口"""

    @grpc_call(path="/live.xactivity.v1.spring/signUp")
    def sign_up(self, act_id=None, team_id=None, ruid=None):
        """### 报名接口"""

    @grpc_call(path="/live.xactivity.v1.spring/fireworksInit")
    def fireworks_init(self, room_id=None, ruid=None, uid=None):
        """### 烟花活动 半屏初始化接口"""

    @grpc_call(path="/live.xactivity.v1.spring/skybox2021Draw")
    def skybox2021_draw(self, room_id, pool_id, uid):
        """### 抽卡"""

    @grpc_call(path="/live.xactivity.v1.spring/skybox2021DrawTen")
    def skybox2021_draw_ten(self, room_id, pool_id, uid):
        """### 十连"""

    @grpc_call(path="/live.xactivity.v1.generalRankFrontend/ActivityIndex")
    def activity_index(self, sub_act_ids=None):
        """### 活动榜单初始化接口 提供所有活动榜单所需参数，当前房间主播榜单信息"""

    @grpc_call(path="/live.xactivity.v1.generalRankFrontend/ActivityIndexV2")
    def activity_index_v2(self, act_id=None):
        """### 活动榜单初始化接口V2 提供所有活动榜单所需参数，当前房间主播榜单信息"""

    @grpc_call(path="/live.xactivity.v1.generalRankFrontend/ActivityIndexV3")
    def activity_index_v3(self, act_id=None):
        """### 不解tab json"""

    @grpc_call(path="/live.xactivity.v1.generalRankFrontend/ActivityIndexV4")
    def activity_index_v4(self, act_id=None, uid=None):
        """### 不解tab json + 预演配置 (需要登陆态"""

    @grpc_call(path="/live.xactivity.v1.generalRankFrontend/ActivitySignUp")
    def activity_sign_up(self, act_id, ruid, other=None, team_id=None, extra_data=None):
        """### 报名"""

    @grpc_call(path="/live.xactivity.v1.generalRankFrontend/ActivityHalfInit")
    def activity_half_init(self, act_id, room_id, uid=None, ruid=None):
        """### 半屏初始化"""

    @grpc_call(path="/live.xactivity.v1.generalRankFrontend/ActivityFullInit")
    def activity_full_init(self, act_id, uid=None):
        """### 全屏初始化"""

    @grpc_call(path="/live.xactivity.v1.generalRankFrontend/ActSignUpData")
    def act_sign_up_data(self, act_id, uid, eliminate_status=None, sign_up_status_json=None, sign_up_status=None):
        """### 活动通用报名数据"""

    @grpc_call(path="/live.xactivity.v1.generalRankFrontend/ActResultData")
    def act_result_data(self, act_id, uid):
        """### 活动通用结果页数据"""

    @grpc_call(path="/live.xactivity.v1.AprilPlayWith/AnchorSetGameInfo")
    def anchor_set_game_info(self, act_id=None, ruid=None, config_json=None, price=None):
        """### 主播设置游戏信息(新增 or 更新)【登录态】"""

    @grpc_call(path="/live.xactivity.v1.AprilPlayWith/AnchorSetEnable")
    def anchor_set_enable(self, act_id=None, ruid=None, is_enable=None):
        """### 主播开启|暂停陪玩【登录态】"""

    @grpc_call(path="/live.xactivity.v1.AprilPlayWith/GetRoomQueue")
    def get_room_queue(self, act_id=None, ruid=None, offset=None, page_size=None, uid=None):
        """### 获取房间排队队列"""

    @grpc_call(path="/live.xactivity.v1.AprilPlayWith/AnchorSetComplete")
    def anchor_set_complete(self, act_id=None, ruid=None, queue_id=None):
        """### 主播完成陪玩【登录态】"""

    @grpc_call(path="/live.xactivity.v1.AprilPlayWith/UserSetGameInfo")
    def user_set_game_info(self, act_id=None, team_id=None, uid=None, config_json=None):
        """### 用户设置游戏信息【登录态】"""

    @grpc_call(path="/live.xactivity.v1.AprilPlayWith/UserInQueue")
    def user_in_queue(self, act_id=None, room_id=None, uid=None):
        """### 用户排队上车【登录态】"""

    @grpc_call(path="/live.xactivity.v1.AprilPlayWith/PlayWithRank")
    def play_with_rank(self, page, team_id=None, rank_id=None, page_size=None):
        """### 陪玩活动总榜|分区榜|推荐主播"""

    @grpc_call(path="/live.xactivity.v1.common/BehaviorSendGift")
    def behavior_send_gift(self, uid=None, room_id=None, ruid=None, parent_area_id=None, area_id=None, goods_id=None, gift_id=None, coin_type=None, goods_price=None, goods_num=None, total_coin=None, pay_coin=None, timestamp=None, eventId=None, eventName=None, eventVersion=None, transmit_data=None, liveId=None, origin_gift_id=None):
        """### 行为系统 送礼行为"""

    @grpc_call(path="/live.xactivity.v1.common/BehaviorChangePlayStatus")
    def behavior_change_play_status(self, uid=None, room_id=None, live_id=None, live_key=None, time=None, status=None, origin_msg=None, transmit_data=None):
        """### 行为系统 开关播行为"""

    @grpc_call(path="/live.xactivity.v1.VideoPkS2/videoPkS2PKLog")
    def video_pk_s2_p_k_log(self, uid=None, ruid=None, timestamp=None):
        """### 赏金赛pk记录"""

    @grpc_call(path="/live.xactivity.v1.VideoPkS2/videoPkS2RankParams")
    def video_pk_s2_rank_params(self, uid=None, room_id=None):
        """### 获取本轮战况榜,应援榜"""

    @grpc_call(path="/live.xactivity.v1.VideoPkS2/videoPkS2Withdraw")
    def video_pk_s2_withdraw(self, uid=None):
        """### 提现"""

    @grpc_call(path="/live.xactivity.v1.VideoPkS2/videoPkS2Join")
    def video_pk_s2_join(self, uid=None, pk_join_token=None):
        """### 加入PK"""

    @grpc_call(path="/live.xactivity.v1.generalTrading/GetActScore")
    def get_act_score(self, act_id, uid):
        """### 获取活动数值 (登陆态)"""

    @grpc_call(path="/live.xactivity.v1.generalTrading/GoodsExchange")
    def goods_exchange(self, id, act_id, uid, extra_data=None):
        """### 兑换"""

    @grpc_call(path="/live.xactivity.v1.generalTrading/GoodsExchangeList")
    def goods_exchange_list(self, act_id, uid=None):
        """### 兑换列表"""

    @grpc_call(path="/live.xactivity.v1.Summer2021/Summer2021GetScore")
    def summer2021_get_score(self, uid=None):
        """### 获取兑换数值"""

    @grpc_call(path="/live.xactivity.v1.Summer2021/Summer2021GetSignUpTeam")
    def summer2021_get_sign_up_team(self, uid=None):
        """### 获取主播当前可以报名的队伍"""

    @grpc_call(path="/live.xactivity.v1.bind/GetAccountBindInfo")
    def get_account_bind_info(self, uid=None, type=None):
        """### 查询openid"""

    @grpc_call(path="/live.xactivity.v1.bind/AddAccountBindInfo")
    def add_account_bind_info(self, openid=None, nickname=None, avatar=None, ip=None, bind_type=None, uid=None):
        """### 增加绑定"""

    @grpc_call(path="/live.xactivity.v1.bind/GetBindInfosByOpenid")
    def get_bind_infos_by_openid(self, openid=None, type=None):
        """### openid查询b站ID 反查"""

    @grpc_call(path="/live.xactivity.v1.bind/UnBindByUid")
    def un_bind_by_uid(self, uid=None, type=None):
        """### 解绑"""

    @grpc_call(path="/live.xactivity.v1.Genshin202107/GenshinThumbsUp")
    def genshin_thumbs_up(self, uid=None):
        """### 无标题"""

    @grpc_call(path="/live.xactivity.v1.Genshin202107/GenshinGetThumbsUpStatus")
    def genshin_get_thumbs_up_status(self, uid=None):
        """### 无标题"""

    @grpc_call(path="/live.xactivity.v1.Genshin202107/GenshinSpecialTaskReceiveReward")
    def genshin_special_task_receive_reward(self, uid=None, jackpotId=None):
        """### 无标题"""

    @grpc_call(path="/live.xactivity.v1.march_blind_gift/marchBlindGiftGetTeam")
    def march_blind_gift_get_team(self, ruid):
        """### 获取赛道接口"""

    @grpc_call(path="/live.xactivity.v1.march_blind_gift/marchBlindGiftApply")
    def march_blind_gift_apply(self, ruid, team):
        """### 报名接口"""

    @grpc_call(path="/live.xactivity.v1.march_blind_gift/marchBlindGiftStatus")
    def march_blind_gift_status(self, ruid):
        """### 报名状态"""

    @grpc_call(path="/live.xactivity.v1.march_blind_gift/marchBlindGiftMasterInfo")
    def march_blind_gift_master_info(self, ruid, room_id):
        """### 主播信息"""

    @grpc_call(path="/live.xactivity.rank/getRankTab")
    def get_rank_tab(self, id=None):
        """### 主播队伍阶段总榜"""

    @grpc_call(path="/live.xactivity.rank/getAreaTeamByRoomId")
    def get_area_team_by_room_id(self, act_id, room_id, period, area_id, parent_area_id):
        """### 根据roomid获分区队伍or报名队伍"""

    @grpc_call(path="/live.xactivity.rank/getPromotionStatus")
    def get_promotion_status(self, act_id):
        """### 获取晋级状态"""

    @grpc_call(path="/live.xactivity.rank/getMasterPromotionStatus")
    def get_master_promotion_status(self, act_id, uid, timestamp=None):
        """### 获取主播是否在榜"""

    @grpc_call(path="/live.xactivity.rank/msgWallGetUserRank")
    def msg_wall_get_user_rank(self, room_id, act_id):
        """###福气墙活动用户榜单接口"""

    @grpc_call(path="/live.xactivity.activity_content/getContentList")
    def get_content_list(self, page, page_size=None, act_id=None):
        """###获取文案配置列表"""

    @grpc_call(path="/live.xactivity.activity_content/getContentInfo")
    def get_content_info(self, id):
        """###活动文案配置详情"""

    @grpc_call(path="/live.xactivity.activity_content/getContentInfos")
    def get_content_infos(self, act_id, group_name=None):
        """###获取文案配置"""

    @grpc_call(path="/live.xactivity.award_data/getActUserAwardNum")
    def get_act_user_award_num(self, award_type=None, act_id=None, uid=None, timestamp=None):
        """### 获取用户奖励数据"""

    @grpc_call(path="/live.xactivity.award_data/getBls2020Buff")
    def get_bls2020_buff(self, uid=None):
        """### 无标题"""

    @grpc_call(path="/live.xactivity.lanturn2021/lanturn21MasterInfo")
    def lanturn21_master_info(self, room_id, period):
        """### 主播信息"""

    @grpc_call(path="/live.xactivity.lanturn2021/lanturn21Apply")
    def lanturn21_apply(self, ruid, extra_int=None):
        """### 报名"""

    @grpc_call(path="/live.xactivity.lanturn2021/lanturn21ApplyStatus")
    def lanturn21_apply_status(self, ruid):
        """### 报名状态"""

    @grpc_call(path="/live.xactivity.lanturn2021/lanturn21ApplySwitch")
    def lanturn21_apply_switch(self, ruid):
        """### 切换赛道"""

    @grpc_call(path="/live.xactivity.lanturn2021/lanturn21LuckyUserRank")
    def lanturn21_lucky_user_rank(self, room_id):
        """### 欧皇榜"""

    @grpc_call(path="/live.xactivity.lanturn2021/lanturn21PromotedMasters")
    def lanturn21_promoted_masters(self, team):
        """### 获取已晋级的主播"""

    @grpc_call(path="/live.xactivity.matchroom/matchRoomStatus")
    def match_room_status(self, room_id=None, area_parent_id=None, area_id=None, mobi_app=None):
        """### 无标题"""

    @grpc_call(path="/live.xactivity.matchroom/matchRoomInfo")
    def match_room_info(self, room_id=None, uid=None):
        """### 无标题"""

    @grpc_call(path="/live.xactivity.award_backend/getAwardConfig")
    def get_award_config(self, act_id=None):
        """### 获取奖励基础配置"""

    @grpc_call(path="/live.xactivity.award_backend/getAwardList")
    def get_award_list(self, act_id=None):
        """### 获取奖励列表"""

    @grpc_call(path="/live.xactivity.august/augustPendant")
    def august_pendant(self, room_id):
        """### 无标题"""

    @grpc_call(path="/live.xactivity.august/augustPendantPk")
    def august_pendant_pk(self, room_id):
        """### 无标题"""

    @grpc_call(path="/live.xactivity.august/augustPendantRank")
    def august_pendant_rank(self, room_id):
        """### 无标题"""

    @grpc_call(path="/live.xactivity.august/augustMasterInfo")
    def august_master_info(self, room_id):
        """### 无标题"""

    @grpc_call(path="/live.xactivity.august/augustUserRank")
    def august_user_rank(self, room_id, page, uid=None):
        """### 无标题"""

    @grpc_call(path="/live.xactivity.s10/follow")
    def follow(self, uid=None, ruid=None, index=None, day=None):
        """### 无标题"""

    @grpc_call(path="/live.xactivity.s10/index")
    def index(self, uid=None):
        """### 无标题"""

    @grpc_call(path="/live.xactivity.s10/watchTaskIndex")
    def watch_task_index(self, uid=None):
        """###二路流直播间观看时长查询接口"""

    @grpc_call(path="/live.xactivity.s10/watchTask")
    def watch_task(self, uid=None, duration=None, aid=None, date=None):
        """###二路流直播间观看时长任务"""

    @grpc_call(path="/live.xactivity.s10/follow2")
    def follow2(self, uid=None, ruid=None):
        """###二路有关注任务"""

    @grpc_call(path="/live.xactivity.s10/follow2Task")
    def follow2_task(self, uid=None, ruid=None):
        """###消费队列"""

    @grpc_call(path="/live.xactivity.treasureBoxExchange/BoxInfo")
    def box_info(self, uid=None):
        """### 宝箱信息"""

    @grpc_call(path="/live.xactivity.treasureBoxExchange/OpenBox")
    def open_box(self, uid, boxId):
        """### 开启宝箱"""

    @grpc_call(path="/live.xactivity.treasureBoxExchange/UserBoxStatus")
    def user_box_status(self, uid):
        """### 用户宝箱状态"""

    @grpc_call(path="/live.xactivity.spring_festival2021/springFestival2021PeriodOneApply")
    def spring_festival2021_period_one_apply(self, ruid, timestamp=None, extra_int=None):
        """### 春节1阶段报名"""

    @grpc_call(path="/live.xactivity.spring_festival2021/springFestival2021PeriodThreeApply")
    def spring_festival2021_period_three_apply(self, ruid, timestamp=None, extra_int=None):
        """### 春节3阶段报名"""

    @grpc_call(path="/live.xactivity.spring_festival2021/springFestival2021PeriodOneApplyStatus")
    def spring_festival2021_period_one_apply_status(self, ruid, timestamp=None, extra_int=None):
        """### 春节1阶段报名状态"""

    @grpc_call(path="/live.xactivity.spring_festival2021/springFestival2021MasterInfo")
    def spring_festival2021_master_info(self, room_id, ruid=None):
        """### 春节主播信息（第三阶段使用"""

    @grpc_call(path="/live.xactivity.july/indexJuly")
    def index_july(self, act_id=None, uid=None):
        """### 无标题"""

    @grpc_call(path="/live.xactivity.july/roomIndexJuly")
    def room_index_july(self, act_id, room_id):
        """### 无标题"""

    @grpc_call(path="/live.xactivity.july/julyPendant")
    def july_pendant(self, room_id):
        """### 无标题"""

    @grpc_call(path="/live.xactivity.activity_backend/getActivityList")
    def get_activity_list(self, page=None, page_size=None):
        """### 获取活动列表"""

    @grpc_call(path="/live.xactivity.activity_backend/getActivityInfo")
    def get_activity_info(self, id=None):
        """### 获取活动详情"""

    @grpc_call(path="/live.xactivity.award/getActivityAwardList")
    def get_activity_award_list(self, award_type=None):
        """### 获取奖励基础配置"""

    @grpc_call(path="/live.xactivity.award/addUserAward")
    def add_user_award(self, award_type=None, award_id=None, award_num=None, award_expire_time=None, source=None, msg_id=None, extra_data=None, uids=None):
        """### 添加奖励"""

    @grpc_call(path="/live.xactivity.winterVacation/winterVacation21MasterInfo")
    def winter_vacation21_master_info(self, room_id, period):
        """### 寒假活动主播信息"""

    @grpc_call(path="/live.xactivity.winterVacation/winterVacation21Apply")
    def winter_vacation21_apply(self, ruid, send_timestamp=None):
        """### 寒假活动一阶段报名"""

    @grpc_call(path="/live.xactivity.winterVacation/winterVacation21ApplyStatus")
    def winter_vacation21_apply_status(self, ruid):
        """### 寒假活动一阶段报名状态"""

    @grpc_call(path="/live.xactivity.winterVacation/winterVacation21ApplySwitch")
    def winter_vacation21_apply_switch(self, ruid):
        """### 寒假活动 切换赛道"""

    @grpc_call(path="/live.xactivity.winterVacation/winterVacation21PromotedMasters")
    def winter_vacation21_promoted_masters(self, team):
        """### 获取已晋级的主播"""

    @grpc_call(path="/live.xactivity.activity/index")
    def index(self, act_id=None, uid=None):
        """### 无标题"""

    @grpc_call(path="/live.xactivity.activity/indexJune")
    def index_june(self, act_id=None, uid=None):
        """### 无标题"""

    @grpc_call(path="/live.xactivity.activity/rankTopNJune")
    def rank_top_n_june(self, top=None):
        """### 无标题"""

    @grpc_call(path="/live.xactivity.activity/exchangeKanban")
    def exchange_kanban(self, act_id=None, id=None, uid=None):
        """### 无标题"""

    @grpc_call(path="/live.xactivity.activity/getUserKanban")
    def get_user_kanban(self, act_id=None, uid=None):
        """### 无标题"""

    @grpc_call(path="/live.xactivity.activity/getUserApplyDataByType")
    def get_user_apply_data_by_type(self, act_id=None, uid=None, apply_type=None):
        """### 无标题"""

    @grpc_call(path="/live.xactivity.activity/teamBattleInfo")
    def team_battle_info(self, act_id, period, data_key, room_id=None):
        """### team对抗信息"""

    @grpc_call(path="/live.xactivity.activity/battleList")
    def battle_list(self, day=None):
        """### 对抗分组列表"""

    @grpc_call(path="/live.xactivity.activity/updateUserApply")
    def update_user_apply(self, act_id=None, apply_type=None, uids=None, apply_end_time=None, team_id=None):
        """### 更新报名信息"""

    @grpc_call(path="/live.xactivity.activity/getActPeriodTeamConfig")
    def get_act_period_team_config(self, act_id=None):
        """### 获取队伍信息"""

    @grpc_call(path="/live.xactivity.activity/getTeamByRoom")
    def get_team_by_room(self, act_id, period, room_id):
        """### 根据房间号查找team"""

    @grpc_call(path="/live.xactivity.activity/getCurActTime")
    def get_cur_act_time(self, act_id=None):
        """### 无标题"""

    @grpc_call(path="/live.xactivity.activity/QueryFansMedalRedis")
    def query_fans_medal_redis(self, medal_type=None, ruid=None, task_id=None):
        """### 获取分子勋章、亲密度加速缓存"""

    @grpc_call(path="/live.xactivity.activity/SendGoldCoinGift")
    def send_gold_coin_gift(self, uid, order_id):
        """### 626 - 购买大会员抽取价值500金瓜子道具"""

    @grpc_call(path="/live.xactivity.activity/SendFreeGift")
    def send_free_gift(self, uid, order_id):
        """### 626 - 老爷领取直播礼物(免费道具)"""

    @grpc_call(path="/live.xactivity.bls2020/bls2020MasterInfo")
    def bls2020_master_info(self, act_id=None, room_id=None):
        """### 无标题"""

    @grpc_call(path="/live.xactivity.bls2020/getBuffInfo")
    def get_buff_info(self, uid=None, act_id=None):
        """### 无标题"""

    @grpc_call(path="/live.xactivity.bls2020/getBls2020pareaMasterInfo")
    def get_bls2020parea_master_info(self, act_id=None, room_id=None):
        """### 半屏主播"""

    @grpc_call(path="/live.xactivity.bls2020/getPareaMasterBattleList")
    def get_parea_master_battle_list(self, act_id=None, period=None, team=None):
        """### 半屏对战表信息"""

    @grpc_call(path="/live.xactivity.bls2020/getPareaMasterBattleInfo")
    def get_parea_master_battle_info(self, act_id=None, room_id=None):
        """### 半屏主播对战信息"""

    @grpc_call(path="/live.xactivity.bls2020/bls2020AreaMasterInfo")
    def bls2020_area_master_info(self, act_id, room_id, ruid=None):
        """###bls 小分区赛 主播info"""

    @grpc_call(path="/live.xactivity.bls2020/bls2020AreaSpcMasterInfo")
    def bls2020_area_spc_master_info(self, act_id, room_id, ruid=None):
        """###bls 专项赛 主播info"""

    @grpc_call(path="/live.xactivity.bls2020/bls2020PersonalMasterInfo")
    def bls2020_personal_master_info(self, room_id, apply_complete, ruid=None):
        """###bls 单项赛 主播info"""

    @grpc_call(path="/live.xactivity.bls2020/bls2020AreaApplyChange")
    def bls2020_area_apply_change(self, team_id, uid=None):
        """###bls 分区赛 赛道切换"""

    @grpc_call(path="/live.xactivity.bls2020/bls2020AreaChangeStatus")
    def bls2020_area_change_status(self, uid=None):
        """###bls 分区赛 状态获取"""

    @grpc_call(path="/live.xactivity.bls2020/bls2020SpecGetActId")
    def bls2020_spec_get_act_id(self, room_id=None, act_id=None):
        """### bls 分区赛/专项赛使用，根据roomid及时间获取当前进行中的活动id"""

    @grpc_call(path="/live.xactivity.bls2020/bls2020SpecRankTopText")
    def bls2020_spec_rank_top_text(self, act_id=None, team_id=None):
        """### bls 专项赛 榜单 top text"""

    @grpc_call(path="/live.xactivity.bls2020/bls2020PersonalApply")
    def bls2020_personal_apply(self, apply_teams=None, ruid=None):
        """### bls 单项赛报名"""

    @grpc_call(path="/live.xactivity.bls2020/bls2020PersonalApplyIndex")
    def bls2020_personal_apply_index(self, ruid=None, room_id=None):
        """### bls 单项赛报名index"""

    @grpc_call(path="/live.xactivity.bls2020/bls2020MVPRank")
    def bls2020_m_v_p_rank(self, page=None):
        """### bls 单项赛 当红人气王"""

    @grpc_call(path="/live.xactivity.bls2020/bls2020SemifinalInfo")
    def bls2020_semifinal_info(self, act_id=None, room_id=None):
        """### bls 半决赛 主播信息接口"""

    @grpc_call(path="/live.xactivity.bls2020/bls2020SemifinalPendant")
    def bls2020_semifinal_pendant(self, uid=None, room_id=None):
        """### bls 半决赛 挂件接口 (仅供测试使用:实际是通过 /xlive/activity-interface/v1/widgetBanner/GetWidgetBannerList 获取)"""

    @grpc_call(path="/live.xactivity.bls2020/bls2020SemifinalMasterRank")
    def bls2020_semifinal_master_rank(self, act_id, name, page, period=None, team=None, day=None):
        """### bls 半决赛 主播榜"""

    @grpc_call(path="/live.xactivity.bls2020/bls2020SemifinalAidRank")
    def bls2020_semifinal_aid_rank(self, page, ruid=None, room_id=None):
        """### bls 半决赛 应援榜"""

    @grpc_call(path="/live.xactivity.bls2020/bls2020GuildRankIndex")
    def bls2020_guild_rank_index(self, act_id=None, uid=None):
        """### bls 公会赛index"""

    @grpc_call(path="/live.xactivity.bls2020/bls2020GuildRankList")
    def bls2020_guild_rank_list(self, act_id=None, period=None, team=None, date=None, page=None, page_size=None, uid=None):
        """### bls 公会赛榜单"""

    @grpc_call(path="/live.xactivity.bls2020/guildBuffInfo")
    def guild_buff_info(self, act_id=None):
        """### bls公会赛Buff"""

    @grpc_call(path="/live.xactivity.bls2020/getBls2020FinalMasterInfo")
    def get_bls2020_final_master_info(self, act_id=None, room_id=None):
        """### bls全站赛主播信息"""

    @grpc_call(path="/live.xactivity.bls2020/getBls2020UltimateMasterInfo")
    def get_bls2020_ultimate_master_info(self, act_id=None, room_id=None):
        """### bls赛全站总决赛主播信息"""

    @grpc_call(path="/live.xactivity.bls2020/getBls2020UltimateMasterAidRank")
    def get_bls2020_ultimate_master_aid_rank(self, act_id, room_id):
        """### bls赛全站总决赛用户贡献榜单"""

    @grpc_call(path="/live.xactivity.rank_backend/getRankConfig")
    def get_rank_config(self, act_id=None):
        """### 榜单基础配置"""

    @grpc_call(path="/live.xactivity.rank_backend/getRankInfo")
    def get_rank_info(self, act_id=None):
        """### 获取榜单信息"""

    @grpc_call(path="/live.xactivity.rank_backend/getRankTabConfig")
    def get_rank_tab_config(self, act_id=None):
        """### 获取榜单tab配置"""

    @grpc_call(path="/live.xactivity.rank_backend/getRankTabList")
    def get_rank_tab_list(self, act_id=None):
        """### 榜单tab明细"""

    @grpc_call(path="/live.xactivity.rank_backend/getRankTabInfo")
    def get_rank_tab_info(self, act_id=None, id=None):
        """### 榜单tab明细"""

    @grpc_call(path="/live.xactivity.rank_backend/getRankDataList")
    def get_rank_data_list(self, act_id=None, rank_id=None, rank_name=None, params=None, page=None):
        """### 榜单基础配置"""

    @grpc_call(path="/live.xactivity.treasureDebrisCompound/CompoundGiftList")
    def compound_gift_list(self, uid=None):
        """### 合成礼物列表"""

    @grpc_call(path="/live.xactivity.treasureDebrisCompound/DoCompoundGift")
    def do_compound_gift(self, uid, giftId):
        """### 合成礼物"""

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

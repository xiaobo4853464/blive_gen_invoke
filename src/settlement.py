from tiny import grpc_call

class Settlement(object):
    def __init__(self,service_name):
        self.service_name=service_name
    
    @grpc_call(path="/live.settlement.v1.GiftSettlement/rateList")
    def rate_list(self, type=None, target_id=None, start_date=None, end_date=None, page=None, page_size=None):
        """###道具转化比例配置列表"""

    @grpc_call(path="/live.settlement.v1.GiftSettlement/addRateConfig")
    def add_rate_config(self, type=None, target_id=None, rate=None, start_date=None, end_date=None, operator=None):
        """###新增配置"""

    @grpc_call(path="/live.settlement.v1.GiftSettlement/updateRateConfig")
    def update_rate_config(self, id=None, type=None, target_id=None, rate=None, start_date=None, end_date=None, operator=None):
        """###更新配置"""

    @grpc_call(path="/live.settlement.v1.GiftSettlement/delRateConfig")
    def del_rate_config(self, id=None):
        """###删除配置"""

    @grpc_call(path="/live.settlement.v1.GiftSettlement/getRateListByType")
    def get_rate_list_by_type(self, type=None):
        """###全量测试用户列表"""

    @grpc_call(path="/live.settlement.v1.GiftSettlement/modifySettlementType")
    def modify_settlement_type(self, uid=None, special_gift=None, normal_gift=None, award_punishment=None, salary=None, month_settlement=None, source=None, user_type=None):
        """###更改结算方式"""

    @grpc_call(path="/live.settlement.v1.GiftSettlement/giftStreamAccountType")
    def gift_stream_account_type(self, tids=None, timestamp=None):
        """###获取礼物流水各资金池花费金额"""

    @grpc_call(path="/live.settlement.v1.GiftSettlement/getHamsterByDay")
    def get_hamster_by_day(self, uid=None, timestamp=None):
        """###获取主播一天的金仓鼠总数"""

    @grpc_call(path="/live.settlement.v1.GiftSettlement/getCoinByTids")
    def get_coin_by_tids(self, tids=None, timestamp=None):
        """### 无标题"""

    @grpc_call(path="/live.settlement.v1.Settlement/salary")
    def salary(self, transaction_id, code, uid, salary, timestamp):
        """###工资接口"""

    @grpc_call(path="/live.settlement.v1.Settlement/query")
    def query(self, transaction_id, timestamp):
        """###结算信息查询"""

    @grpc_call(path="/live.settlement.v1.Settlement/revenueDetail")
    def revenue_detail(self, ruid, date):
        """###主播某天收益详情"""

    @grpc_call(path="/live.settlement.v1.Settlement/preDeduct")
    def pre_deduct(self, transaction_id, uid, hamster, deduct_type, reason):
        """###金仓鼠退款自动审批"""

    @grpc_call(path="/live.settlement.v1.Settlement/getByUidMonth")
    def get_by_uid_month(self, month=None, uid=None):
        """###获取月结记录"""

    @grpc_call(path="/live.settlement.v1.Settlement/getHamsterChangeByThirdId")
    def get_hamster_change_by_third_id(self, timestamp=None, third_id=None):
        """###获取金仓鼠变更记录"""

    @grpc_call(path="/live.settlement.v1.Settlement/getWithdrawApply")
    def get_withdraw_apply(self, uid=None, apply_date=None):
        """###获取快捷账户提现记录"""

    @grpc_call(path="/live.settlement.v1.Settlement/getCoinStream")
    def get_coin_stream(self, start_time=None, end_time=None, page_size=None, last_id=None, uid=None):
        """###分页查询coin表数据"""

    @grpc_call(path="/live.settlement.v1.Settlement/getStreamerTotalProfits")
    def get_streamer_total_profits(self, uids, time_start, time_end):
        """###查询多位主播一段时间内的总收益"""

    @grpc_call(path="/live.settlement.v1.Settlement/modifySettleTypeForMonth")
    def modify_settle_type_for_month(self, uid=None, old_account=None, new_account=None, month=None, intercept_status=None, remark=None):
        """###修改结算类型（出错用）"""

    @grpc_call(path="/live.settlement.v1.Settlement/modifySettlementType")
    def modify_settlement_type(self, uid=None, account_type=None, ios_delay=None, source=None):
        """### 修改账户入账账户"""

    @grpc_call(path="/live.settlement.v1.Settlement/gethamsterNoOp")
    def gethamster_no_op(self, uid=None, start_time=None, end_time=None):
        """### 查询去除运营奖惩的金参数总数(下游保证不跨月"""

    @grpc_call(path="/live.settlement.v1.Settlement/getSettlementType")
    def get_settlement_type(self, uid=None):
        """### 获取账户入账账户"""

    @grpc_call(path="/live.settlement.intercept/getRuleById")
    def get_rule_by_id(self, rule_id=None):
        """### 根据拦截规则ID获取拦截规则现状中的规则详情"""

    @grpc_call(path="/live.settlement.intercept/getRule")
    def get_rule(self, rule_id=None, uid=None, room_id=None, anchor_name=None, intercept_sdate=None, intercept_edate=None, state=None, apply_stime=None, apply_etime=None, applicant=None, page=None, page_size=None, is_export=None):
        """### 获取拦截规则现状列表"""

    @grpc_call(path="/live.settlement.intercept/getApply")
    def get_apply(self, uid=None, room_id=None, anchor_name=None, intercept_sdate=None, intercept_edate=None, apply_type=None, state=None, apply_stime=None, apply_etime=None, applicant=None, page=None, page_size=None, rule_id=None, is_export=None):
        """### 获取拦截规则申请记录"""

    @grpc_call(path="/live.settlement.intercept/getAnchorInfo")
    def get_anchor_info(self, uid=None):
        """### 获取主播信息"""

    @grpc_call(path="/live.settlement.intercept/addApply")
    def add_apply(self, uid=None, intercept_sdate=None, intercept_edate=None, apply_remark=None, applicant=None):
        """### 申请添加拦截规则"""

    @grpc_call(path="/live.settlement.intercept/checkBAddApply")
    def check_b_add_apply(self, content=None):
        """### 检查批量添加拦截规则的数据合法性"""

    @grpc_call(path="/live.settlement.intercept/batchAddApply")
    def batch_add_apply(self, content=None, applicant=None):
        """### 申请批量添加拦截规则"""

    @grpc_call(path="/live.settlement.intercept/modifyApply")
    def modify_apply(self, rule_id=None, intercept_sdate=None, intercept_edate=None, apply_remark=None, applicant=None):
        """### 申请更改拦截规则"""

    @grpc_call(path="/live.settlement.intercept/checkBModifyApply")
    def check_b_modify_apply(self, content=None):
        """### 检查批量添加拦截规则的数据合法性"""

    @grpc_call(path="/live.settlement.intercept/batchModifyApply")
    def batch_modify_apply(self, content=None, applicant=None):
        """### 申请批量修改拦截规则，唯一标识为 uid,intercept_sdate,intercept_edate"""

    @grpc_call(path="/live.settlement.intercept/deleteRule")
    def delete_rule(self, rule_id=None, apply_remark=None, applicant=None):
        """### 申请批量删除拦截规则"""

    @grpc_call(path="/live.settlement.intercept/revoke")
    def revoke(self, apply_id=None, applicant=None):
        """### 撤回拦截规则变更申请"""

    @grpc_call(path="/live.settlement.intercept/examine")
    def examine(self, apply_id=None, examine_type=None, applicant=None):
        """### 审批拦截规则变更申请"""

    @grpc_call(path="/live.settlement.intercept/getWithdrawApplyRecord")
    def get_withdraw_apply_record(self, uid=None, room_id=None, anchor_name=None, min_amount=None, max_amount=None, apply_sdate=None, apply_edate=None, received_sdate=None, received_edate=None, state=None, delay_day=None, page=None, page_size=None, is_export=None):
        """### 规则生效现状"""

    @grpc_call(path="/live.settlement.intercept/getMoneyLimitList")
    def get_money_limit_list(self, record_type=None, order_by=None, page=None, page_size=None):
        """### 获取金额限制规则记录"""

    @grpc_call(path="/live.settlement.intercept/modifyMoneyLimit")
    def modify_money_limit(self, amount_max=None, amount_min=None, apply_remark=None, applicant=None):
        """### 更该金额限制规则"""

    @grpc_call(path="/live.settlement.intercept/revokeMoneyLimit")
    def revoke_money_limit(self, id=None, applicant=None):
        """### 撤回金额限制规则更改申请"""

    @grpc_call(path="/live.settlement.intercept/examineMoneyLimit")
    def examine_money_limit(self, id=None, examine_type=None, applicant=None):
        """### 审核更改金额限制规则申请"""

    @grpc_call(path="/live.settlement.intercept/getDelayList")
    def get_delay_list(self, record_type=None, order_by=None, page=None, page_size=None):
        """### 获取到账时间规则记录"""

    @grpc_call(path="/live.settlement.intercept/modifyDelay")
    def modify_delay(self, delay_day=None, apply_remark=None, applicant=None):
        """### 更改到账时间规则"""

    @grpc_call(path="/live.settlement.intercept/revokeDelay")
    def revoke_delay(self, id=None, applicant=None):
        """### 撤回到账时间规则更改申请"""

    @grpc_call(path="/live.settlement.intercept/examineDelay")
    def examine_delay(self, id=None, examine_type=None, applicant=None):
        """### 审核到账时间规则更改申请"""

    @grpc_call(path="/live.settlement.intercept/getBigWithdrawList")
    def get_big_withdraw_list(self, uid=None, page=None, page_size=None):
        """### 获取列表"""

    @grpc_call(path="/live.settlement.intercept/saveBigWithdraw")
    def save_big_withdraw(self, id=None, uid=None, state=None, remark=None):
        """### 保存白名单修改"""

    @grpc_call(path="/live.settlement.v1.settle.AnchorSettlement/list")
    def list(self, date=None, uid=None, order_by=None, page=None, size=None):
        """### 审核环节弃用"""

    @grpc_call(path="/live.settlement.v1.settle.AnchorSettlement/passAll")
    def pass_all(self, date=None, applicant=None):
        """### 审核环节弃用"""

    @grpc_call(path="/live.settlement.v1.settle.AnchorSettlement/pass")
    def pass_(self, id=None, applicant=None):
        """### 审核环节弃用"""

    @grpc_call(path="/live.settlement.v1.settle.AnchorSettlement/reject")
    def reject(self, id=None, applicant=None):
        """### 审核环节弃用"""

    @grpc_call(path="/live.settlement.v1.AnchorHamster/applyWithdraw")
    def apply_withdraw(self, uid=None, amount=None, amount_min=None, amount_max=None, amount_cardinality=None, delay_day=None):
        """###申请提现"""

    @grpc_call(path="/live.settlement.v1.AnchorHamster/applyWithdrawNew")
    def apply_withdraw_new(self, uid=None, amount=None, amount_min=None, amount_max=None, amount_cardinality=None, delay_day=None, return_url=None):
        """###申请提现（现金）"""

    @grpc_call(path="/live.settlement.v1.AnchorHamster/cancelWithdraw")
    def cancel_withdraw(self, uid=None, stream_id=None):
        """###取消提现"""

    @grpc_call(path="/live.settlement.v1.AnchorHamster/getRunningWithdraw")
    def get_running_withdraw(self, uid=None):
        """###获取已经预下单但未超时的提现单"""

    @grpc_call(path="/live.settlement.v1.AnchorHamster/getWithdrawStatus")
    def get_withdraw_status(self, uid=None, stream_id=None):
        """### 获取提现单状态"""

    @grpc_call(path="/live.settlement.v1.AnchorHamster/getWithdrawConfig")
    def get_withdraw_config(self, uid=None):
        """###获取提现配置"""

    @grpc_call(path="/live.settlement.v1.AnchorHamster/getHamsterChangeRecord")
    def get_hamster_change_record(self, uid=None, year=None, month=None, page=None, page_size=None, reason=None, order=None, start_month=None, end_month=None, ac_type=None):
        """###获取用户账单"""

    @grpc_call(path="/live.settlement.v1.AnchorHamster/getAnchorIncome")
    def get_anchor_income(self, uid=None, date=None):
        """###获取主播收益数据"""

    @grpc_call(path="/live.settlement.v1.AnchorHamster/getAnchorInGrey")
    def get_anchor_in_grey(self, uid=None):
        """###获取是否在灰度名单中"""

    @grpc_call(path="/live.settlement.v1.AnchorHamster/addWithdrawMonthly")
    def add_withdraw_monthly(self, uid=None, amount=None, delay_day=None):
        """###每月自动快捷转贝壳"""

    @grpc_call(path="/live.settlement.v1.AnchorHamster/getHamsterChangeRecords")
    def get_hamster_change_records(self, uid=None, anchor_name=None, room_id=None, category_reason=None, max_hamster=None, min_hamster=None, start_time=None, end_time=None, is_export=None, page_num=None, page_size=None):
        """###查询快账户变更表(后台用)"""

    @grpc_call(path="/live.settlement.v1.AnchorHamster/withdrawNotify")
    def withdraw_notify(self, msg_id, msg_content):
        """###支付中心提现通知接口"""

    @grpc_call(path="/live.settlement.v1.AnchorHamster/withdrawStatusManage")
    def withdraw_status_manage(self, raw_data, next_status):
        """###提现单状态扭转,统计管理提现单状态"""

    @grpc_call(path="/live.settlement.v1.AnchorHamster/withdrawRefund")
    def withdraw_refund(self, refund_stream_id, stream_id, wallet_id, uid, amount):
        """### 提现单退款"""

    @grpc_call(path="/live.settlement.v1.intercept.anchorIntercept/add")
    def add(self, uid=None, remark=None, applicant=None):
        """### 添加主播拦截"""

    @grpc_call(path="/live.settlement.v1.intercept.anchorIntercept/del")
    def del_(self, id=None, applicant=None):
        """### 删除主播拦截"""

    @grpc_call(path="/live.settlement.v1.intercept.anchorIntercept/modifyRemark")
    def modify_remark(self, id=None, remark=None, applicant=None):
        """### 修改备注"""

    @grpc_call(path="/live.settlement.v1.intercept.anchorIntercept/list")
    def list(self, uid=None, page=None, size=None):
        """### 拦截列表"""

    @grpc_call(path="/live.settlement.v1.intercept.anchorIntercept/logList")
    def log_list(self, page=None, size=None, uid=None):
        """### 拦截日志列表"""

    @grpc_call(path="/live.settlement.v1.intercept.anchorIntercept/interceptHistory")
    def intercept_history(self, date=None):
        """### 拦截下载历史记录"""

    @grpc_call(path="/live.settlement.v1.intercept.anchorIntercept/addInterceptHistory")
    def add_intercept_history(self, uid=None, anchor_name=None, room_id=None, settle_type=None, hamster=None, timestamp=None, remark=None):
        """### 添加拦截拦截记录(公会用)"""

    @grpc_call(path="/live.settlement.v1.intercept.anchorIntercept/onAddAuthGuild")
    def on_add_auth_guild(self, uid=None):
        """### 当加入官方公会"""

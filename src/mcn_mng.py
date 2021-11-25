from tiny import grpc_call

class Mcn_mng(object):
    def __init__(self,service_name):
        self.service_name=service_name
    
    @grpc_call(path="/live.mcnmng.v1.operationLog/GetOperationLogList")
    def get_operation_log_list(self, page, page_size, org_type=None, org_val=None, search_type=None, search=None, operation_types=None, year=None, start_date=None, end_date=None, operate_page=None, src_type=None):
        """### 获取公会操作日志列表"""

    @grpc_call(path="/live.mcnmng.v1.operationLog/ExportOperationLogList")
    def export_operation_log_list(self, org_type=None, org_val=None, search_type=None, search=None, operation_types=None, year=None, start_date=None, end_date=None, operate_page=None, src_type=None, operator=None, export_id=None):
        """### 导出操作日志列表"""

    @grpc_call(path="/live.mcnmng.v1.operationLog/AddOperationLog")
    def add_operation_log(self, org_id=None, operator_uid=None, operator_name=None, platform=None, operation_page=None, first_level=None, second_level=None, content=None):
        """### 添加操作日志"""

    @grpc_call(path="/live.mcnmng.v1.operationLog/GetLogTypeFilter")
    def get_log_type_filter(self, src_type=None):
        """### 获取操作日志类型筛选器"""

    @grpc_call(path="/live.mcnmng.v1.oa/StartFlow")
    def start_flow(self, flow_type, ids, operator):
        """### 发起OA流程"""

    @grpc_call(path="/live.mcnmng.v1.oa/GetEmailPreview")
    def get_email_preview(self, flow_type, ids, operator):
        """### 获取结算审批邮件预览"""

    @grpc_call(path="/live.mcnmng.v1.oa/GetSalaryAuditList")
    def get_salary_audit_list(self, type, search=None, status=None, month=None, branch=None, operator=None, page=None, page_size=None):
        """### 获取审批详情列表"""

    @grpc_call(path="/live.mcnmng.v1.oa/GetOperatorInfo")
    def get_operator_info(self, flow_type, flow_ids):
        """### 获取审批人信息"""

    @grpc_call(path="/live.mcnmng.v1.oa/GetRelationInfo")
    def get_relation_info(self, flow_type, flow_ids=None, oa_ids=None, payment_ids=None):
        """### 查询审批关联信息"""

    @grpc_call(path="/live.mcnmng.v1.anchorMng/CommitApply")
    def commit_apply(self, anchor_uid, code, org_id, operator_uid):
        """### CommitApply 主播提交申请"""

    @grpc_call(path="/live.mcnmng.v1.anchorMng/CheckApplyJoin")
    def check_apply_join(self, uid):
        """### CheckApplyJoin 入会资格判断"""

    @grpc_call(path="/live.mcnmng.v1.anchorMng/CheckAnchorRenew")
    def check_anchor_renew(self, uid):
        """### 查询主播是否符合续约条件"""

    @grpc_call(path="/live.mcnmng.v1.anchorMng/CommitQuitGuild")
    def commit_quit_guild(self, uid):
        """### 提交主播退会申请"""

    @grpc_call(path="/live.mcnmng.v1.anchorMng/GuildFireAnchor")
    def guild_fire_anchor(self, uid, org_id, reason=None, operator_uid=None):
        """### 公会解约主播"""

    @grpc_call(path="/live.mcnmng.v1.anchorMng/GetGuildFireAnchorInfo")
    def get_guild_fire_anchor_info(self, uid, apply_id):
        """### 主播获取解约信息"""

    @grpc_call(path="/live.mcnmng.v1.anchorMng/IsGuildAnchor")
    def is_guild_anchor(self, uid):
        """### 判断主播是否为公会主播"""

    @grpc_call(path="/live.mcnmng.v1.Export/ExportAnchorList")
    def export_anchor_list(self, time_range=None, start_date=None, end_date=None, area=None, uid=None, staff_uid=None, uname=None, export_id=None, gid=None, operator_uid=None, search_type=None, search=None):
        """###导出主播列表"""

    @grpc_call(path="/live.mcnmng.v1.Export/ExportGuildAnchor")
    def export_guild_anchor(self, status=None, staff_uid=None, mid=None, export_id=None, g_id=None, operator_uid=None, search_type=None, search=None, anchor_type=None):
        """###导出公会主播"""

    @grpc_call(path="/live.mcnmng.v1.Export/ExportLiveRecord")
    def export_live_record(self, time_range=None, start_date=None, end_date=None, uid=None, export_id=None, g_id=None, operator_uid=None):
        """###导出直播记录"""

    @grpc_call(path="/live.mcnmng.v1.Banner/GetBannerList")
    def get_banner_list(self, sort_name=None, sort_type=None, page=None, page_size=None):
        """### B端banner列表"""

    @grpc_call(path="/live.mcnmng.v1.Banner/AddBanner")
    def add_banner(self, link, jump_link, start_time, end_time, title=None, sort=None):
        """### 增加banner"""

    @grpc_call(path="/live.mcnmng.v1.Banner/UpdateBanner")
    def update_banner(self, link, jump_link, start_time, end_time, id=None, title=None, sort=None):
        """### 修改banner"""

    @grpc_call(path="/live.mcnmng.v1.Banner/OffLineBanner")
    def off_line_banner(self, id=None):
        """### 下线banner"""

    @grpc_call(path="/live.mcnmng.v1.Banner/DeleteBanner")
    def delete_banner(self, id=None):
        """### 删除banner"""

    @grpc_call(path="/live.mcnmng.v1.Guild/GetGuildInfo")
    def get_guild_info(self, guild_id=None):
        """### 查询公会信息"""

    @grpc_call(path="/live.mcnmng.v1.Guild/GetGuildSignInfo")
    def get_guild_sign_info(self, guild_id=None):
        """###查询公会签约信息"""

    @grpc_call(path="/live.mcnmng.v1.Guild/IsMaster")
    def is_master(self, uid=None):
        """### 查询公会信息"""

    @grpc_call(path="/live.mcnmng.v1.Guild/GetGuildSignAreas")
    def get_guild_sign_areas(self, guild_id=None):
        """### 查询公会签约分区"""

    @grpc_call(path="/live.mcnmng.v1.Guild/GetGuildByUids")
    def get_guild_by_uids(self, uids):
        """### 批量查询公会主播归属关系(不超过50个)"""

    @grpc_call(path="/live.mcnmng.v1.Guild/GetAnchorsByGuild")
    def get_anchors_by_guild(self, guild_id):
        """###查询指定公会内的所有主播"""

    @grpc_call(path="/live.mcnmng.v1.Guild/GetGuildList")
    def get_guild_list(self, page, page_size, search_key=None, uid=None):
        """###查询公会列表"""

    @grpc_call(path="/live.mcnmng.v1.Guild/GenGuildQrCode")
    def gen_guild_qr_code(self, org_id, cooperation_duration, anchor_type, operator_uid, staff_uid, share_ratio=None, remark=None, expired_at=None, code_type=None):
        """### 生成公会二维码"""

    @grpc_call(path="/live.mcnmng.v1.Guild/GetGuildQrCode")
    def get_guild_qr_code(self, code):
        """### 获取公会二维码"""

    @grpc_call(path="/live.mcnmng.v1.Guild/GetGuildQuestionStatus")
    def get_guild_question_status(self, uid=None, batch_id=None):
        """### 获取公会答题状态"""

    @grpc_call(path="/live.mcnmng.v1.Guild/SubmitGuildQuestion")
    def submit_guild_question(self, batch_id, uid=None):
        """### 提交公会答题"""

    @grpc_call(path="/live.mcnmng.v1.Guild/SaveAnswerInfo")
    def save_answer_info(self, batch_id, question_id, options, choice_id, uid=None):
        """### 保存公会答题信息"""

    @grpc_call(path="/live.mcnmng.v1.Guild/GetAnswerAnalysisList")
    def get_answer_analysis_list(self, batch_id, uid=None, status=None):
        """### 获取公会答题结果解析列表"""

    @grpc_call(path="/live.mcnmng.v1.Guild/GetExpiredAnchorList")
    def get_expired_anchor_list(self, search_guild=None, search_uid=None, page=None, page_size=None):
        """### 清退主播列表"""

    @grpc_call(path="/live.mcnmng.v1.Guild/GetExpiredAnchorDetail")
    def get_expired_anchor_detail(self, g_id=None, uid=None, room_id=None, stuff_uid=None, anchor_type=None, anchor_status=None, confirm_status=None, execute_satus=None, sort=None, page=None, page_size=None, search_type=None, search=None):
        """### 清退主播详情"""

    @grpc_call(path="/live.mcnmng.v1.Guild/FireAnchor")
    def fire_anchor(self, uids=None, g_id=None, operator=None):
        """### 清退主播(支持批量)"""

    @grpc_call(path="/live.mcnmng.v1.Guild/ConfirmFireAnchor")
    def confirm_fire_anchor(self, apply_id, uid):
        """### 公会确认清退主播(支持批量)"""

    @grpc_call(path="/live.mcnmng.v1.Guild/AddAnchorRenewRecord")
    def add_anchor_renew_record(self, uid, org_id, apply_type, share_ratio=None, start_time=None, end_time=None, qrcode=None, auto_renewal=None, cooperation_duration=None, operator_uid=None):
        """### 添加主播续约申请"""

    @grpc_call(path="/live.mcnmng.v1.Guild/GetAnchorRenewRecord")
    def get_anchor_renew_record(self, apply_id, uid):
        """### 获取主播续约申请"""

    @grpc_call(path="/live.mcnmng.v1.Guild/CancelAnchorAutoRenew")
    def cancel_anchor_auto_renew(self, uid, org_id):
        """### 取消主播自动续约"""

    @grpc_call(path="/live.mcnmng.v1.Guild/GetGuildRenewList")
    def get_guild_renew_list(self, org_id, handle_status=None, staff_uid=None, anchor_name=None, anchor_uid=None, page=None, page_size=None, sort_type=None, sort=None, search_type=None, search=None):
        """### 获取公会续约信息列表"""

    @grpc_call(path="/live.mcnmng.v1.Guild/GetAnchorGuildInfo")
    def get_anchor_guild_info(self, uid):
        """### 获取主播"我的公会"信息"""

    @grpc_call(path="/live.mcnmng.v1.Guild/GetGuildNotice")
    def get_guild_notice(self, uid):
        """### 获取公会主播红点提示"""

    @grpc_call(path="/live.mcnmng.v1.Anchor/GetAnchorList")
    def get_anchor_list(self, g_id, page, page_size, uid=None, room_id=None, staff_uid=None, status=None, sort_type=None, sort=None, search_type=None, search=None, anchor_type=None):
        """### 查询我的主播概况"""

    @grpc_call(path="/live.mcnmng.v1.Anchor/JudgeNinetyFiveAnchor")
    def judge_ninety_five_anchor(self, uids=None):
        """### 查询95分主播"""

    @grpc_call(path="/live.mcnmng.v1.Anchor/SearchGuildAnchorUname")
    def search_guild_anchor_uname(self, org_id, word=None):
        """### 搜索公会主播昵称"""

    @grpc_call(path="/live.mcnmng.v1.Anchor/GetAnchorInfo")
    def get_anchor_info(self, uids):
        """### 查询主播身份"""

    @grpc_call(path="/live.mcnmng.v1.workflow/GetAuditList")
    def get_audit_list(self, start_time=None, end_time=None, search=None, approval=None, audit_type=None, audit_status=None, page=None, page_size=None):
        """### GetAuditList 获取审批列表"""

    @grpc_call(path="/live.mcnmng.v1.workflow/GetBasicInfoAudit")
    def get_basic_info_audit(self, apply_id):
        """### GetBasicInfoAudit 获取公会基础资料申请详情"""

    @grpc_call(path="/live.mcnmng.v1.workflow/GetRecruitAudit")
    def get_recruit_audit(self, apply_id):
        """### GetRecruitAudit 获取公会招募信息申请详情"""

    @grpc_call(path="/live.mcnmng.v1.workflow/Approve")
    def approve(self, apply_id, approval=None, approval_type=None, check_uid=None):
        """### Approve 审批通过(支持批量)"""

    @grpc_call(path="/live.mcnmng.v1.workflow/Reject")
    def reject(self, apply_id, approval=None, approval_type=None, reason=None, check_uid=None):
        """### Reject 审批拒绝(支持批量)"""

    @grpc_call(path="/live.mcnmng.v1.workflow/GetChangeLog")
    def get_change_log(self, id_type, id_value, business_type, page=None, page_size=None):
        """### GetChangeLog 获取变更历史"""

    @grpc_call(path="/live.mcnmng.v1.workflow/GetGuildInfoDetail")
    def get_guild_info_detail(self, guild_id):
        """### GetGuildInfoDetail 后台查看公会资料"""

    @grpc_call(path="/live.mcnmng.v1.workflow/GetAnchorJoinApplyList")
    def get_anchor_join_apply_list(self, org_id, search_type=None, search=None, status=None, page=None, page_size=None):
        """### GetAnchorJoinApplyList 获取主播入会申请列表"""

    @grpc_call(path="/live.mcnmng.v1.workflow/GetAnchorApplyLog")
    def get_anchor_apply_log(self, search_guild=None, search_uid=None, page=None, page_size=None):
        """### GetAnchorApplyLog 获取后台入退会记录"""

    @grpc_call(path="/live.mcnmng.v1.workflow/GetAnchorActiveEvents")
    def get_anchor_active_events(self, uid):
        """### GetAnchorActiveEvents 获取主播进行中的流程"""

    @grpc_call(path="/live.mcnmng.v1.workflow/GetAnchorQuitApplyList")
    def get_anchor_quit_apply_list(self, org_id, type, handle_status=None, staff_uid=None, anchor_name=None, anchor_uid=None, page=None, page_size=None, sort_type=None, sort=None, search_type=None, search=None):
        """### GetAnchorQuitApplyList 获取退会审批列表"""

    @grpc_call(path="/live.mcnmng.v1.Message/GetMessage")
    def get_message(self, token):
        """###查看消息"""

    @grpc_call(path="/live.mcnmng.v1.Message/SaveMessage")
    def save_message(self, title=None, uid=None, guild_id=None, openid=None, token=None, context=None, operate_time=None):
        """###保存消息"""

    @grpc_call(path="/live.mcnmng.v1.Message/GetBuildConList")
    def get_build_con_list(self, uid=None, username=None, start_time=None, end_time=None, page=None, page_size=None):
        """###获取主播建联列表"""

    @grpc_call(path="/live.mcnmng.v1.Message/DeleteBuildConList")
    def delete_build_con_list(self, id):
        """###列表删除"""

    @grpc_call(path="/live.mcnmng.v1.Message/DownloadBuildConnList")
    def download_build_conn_list(self, uid=None, username=None, start_time=None, end_time=None):
        """### 下载建联数据"""

    @grpc_call(path="/live.mcnmng.v1.Message/CheckUpFile")
    def check_up_file(self, url):
        """###模版下载(废弃)"""

    @grpc_call(path="/live.mcnmng.v1.Message/ConfirmBuildCon")
    def confirm_build_con(self, url):
        """###文件提交"""

    @grpc_call(path="/live.mcnmng.v1.Message/AcceptInvitation")
    def accept_invitation(self, contact_id, uid):
        """### 主播接收邀请函"""

    @grpc_call(path="/live.mcnmng.v1.Message/GetContactInfo")
    def get_contact_info(self, uid):
        """### 获取建联分区的运营QQ号"""

    @grpc_call(path="/live.mcnmng.v1.Message/SendSms")
    def send_sms(self, mid=None, mobile=None, country=None, tcode=None, tparam=None):
        """### 发送短信消息"""

    @grpc_call(path="/live.mcnmng.v1.monitor/LivingRoomList")
    def living_room_list(self, search_type=None, search=None, staff_uid=None, area=None, org_id=None, uid=None, order_by=None, order_type=None):
        """### LivingRoomList 获取在播房间列表"""

    @grpc_call(path="/live.mcnmng.v1.monitor/LivingRoomTop")
    def living_room_top(self, uid, operate_type, staff_uid=None):
        """### LivingRoomTop 置顶/取消置顶直播间"""

    @grpc_call(path="/live.mcnmng.v1.Data/GetMyAnchorDataInfo")
    def get_my_anchor_data_info(self, uid=None, gid=None, start_date=None, end_date=None):
        """### 查询我的主播概况"""

    @grpc_call(path="/live.mcnmng.v1.Data/GetMyAnchorList")
    def get_my_anchor_list(self, page, page_size, uid=None, gid=None, area_id=None, start_date=None, end_date=None, staff_uid=None, search_type=None, search=None, roomid=None, order_by=None, order_type=None):
        """### 我的主播列表"""

    @grpc_call(path="/live.mcnmng.v1.Data/GetPersonData")
    def get_person_data(self, guild_id=None, uid=None):
        """### 查看单个主播基础数据"""

    @grpc_call(path="/live.mcnmng.v1.Data/GetCoreData")
    def get_core_data(self, time_range, start_date=None, end_date=None, guild_id=None):
        """### 工作台查询核心数据"""

    @grpc_call(path="/live.mcnmng.v1.Data/GetIncomeRank")
    def get_income_rank(self, guild_id=None, start_date=None, end_date=None):
        """### 查询公会收益榜单"""

    @grpc_call(path="/live.mcnmng.v1.Data/GetIncomeChart")
    def get_income_chart(self, guild_id=None, start_date=None, end_date=None):
        """### 查询公会7日收益趋势"""

    @grpc_call(path="/live.mcnmng.v1.Data/GetCoinChart")
    def get_coin_chart(self, guild_id=None, start_date=None, end_date=None):
        """### 查询公会7日流水趋势"""

    @grpc_call(path="/live.mcnmng.v1.Data/GetOpenAnchorChart")
    def get_open_anchor_chart(self, guild_id=None, start_date=None, end_date=None):
        """### 查询公会7日开播趋势"""

    @grpc_call(path="/live.mcnmng.v1.Data/GetGuildCommonData")
    def get_guild_common_data(self, guild_id=None, start_date=None, end_date=None):
        """### 查询公会公共数据"""

    @grpc_call(path="/live.mcnmng.v1.Data/GetPersonalChart")
    def get_personal_chart(self, uid, data_type, guild_id=None, start_date=None, end_date=None):
        """### 查询单个主播聚合和趋势数据"""

    @grpc_call(path="/live.mcnmng.v1.Data/GetPersonalRec")
    def get_personal_rec(self, uid, guild_id, start_date=None, end_date=None):
        """### 查询单个主播直播记录"""

    @grpc_call(path="/live.mcnmng.v1.information/GetBasicInfo")
    def get_basic_info(self, guild_id):
        """### GetBasicInfo 获取公会基础资料"""

    @grpc_call(path="/live.mcnmng.v1.information/UpdateBasicInfo")
    def update_basic_info(self, guild_id, uid=None, guild_logo=None, area_ids=None, guild_intro=None):
        """### UpdateBasicInfo 更新公会基础资料"""

    @grpc_call(path="/live.mcnmng.v1.information/GetRecruitInfo")
    def get_recruit_info(self, guild_id):
        """### GetRecruitInfo 获取公会招募信息"""

    @grpc_call(path="/live.mcnmng.v1.information/UpdateRecruitInfo")
    def update_recruit_info(self, guild_id, uid=None, requirements=None, welfare=None):
        """### UpdateRecruitInfo 更新公会招募信息"""

    @grpc_call(path="/live.mcnmng.v1.Notice/DelNotice")
    def del_notice(self, notice_id, uid=None):
        """###删除公告"""

    @grpc_call(path="/live.mcnmng.v1.Notice/DetailNotice")
    def detail_notice(self, notice_id, uid=None):
        """###查看公告"""

    @grpc_call(path="/live.mcnmng.v1.Notice/ImportantNotice")
    def important_notice(self, notice_id, operate_type):
        """###是否重要"""

    @grpc_call(path="/live.mcnmng.v1.Notice/OperateNotice")
    def operate_notice(self, notice_id, operate_type):
        """###上线、下线"""

    @grpc_call(path="/live.mcnmng.v1.Notice/ListNotices")
    def list_notices(self, category=None, status=None, important=None, title=None, notice_id=None, start_time=None, end_time=None, page=None, page_size=None, order_by=None, uid=None):
        """###公告列表"""

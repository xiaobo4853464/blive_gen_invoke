from tiny import grpc_call

class Mozi(object):
    def __init__(self,service_name):
        self.service_name=service_name
    
    @grpc_call(path="/live.mozi.rankBattle/GetBattleConfigList")
    def get_battle_config_list(self, name=None, page_index=None, page_size=None):
        """### 获取对抗配置列表"""

    @grpc_call(path="/live.mozi.rankBattle/GetBattleConfigInfo")
    def get_battle_config_info(self, id):
        """### 获取对抗配置详情"""

    @grpc_call(path="/live.mozi.rankBattle/GetRoundList")
    def get_round_list(self, config_id, page_index=None, page_size=None):
        """### 获取场次配置列表"""

    @grpc_call(path="/live.mozi.rankBattle/RoundExport")
    def round_export(self, config_id):
        """### 场次导出"""

    @grpc_call(path="/live.mozi.rankBattle/RoundImport")
    def round_import(self, config_id, csv_content):
        """### 场次导入"""

    @grpc_call(path="/live.mozi.rankBattle/SaveBattleConfig")
    def save_battle_config(self, start_time, num, score_type, id=None, act_name=None, act_props=None, end_time=None, act_status=None, filter_area_conf=None, auto_update_conf=None, score_gold_switch=None, score_gold_conf=None, score_super_chat_switch=None, score_super_chat_conf=None, score_guard_switch=None, score_guard_conf=None, score_free_gift_switch=None, score_free_gift_conf=None, operator=None):
        """### 保存对抗配置"""

    @grpc_call(path="/live.mozi.rankBattle/UpdateBattleConfigStatus")
    def update_battle_config_status(self, id, act_status=None):
        """### 保存对抗配置上下线"""

    @grpc_call(path="/live.mozi.rankBattle/UpdateRound")
    def update_round(self, id=None, start_time=None, end_time=None, uid1=None, uid2=None):
        """### 保存对抗场次配置上下线(目前只能修改无法新增）"""

    @grpc_call(path="/live.mozi.rankBattle/GetBattleRoundConfigFrontend")
    def get_battle_round_config_frontend(self, config_id):
        """### 模版组件前端接口"""

    @grpc_call(path="/live.mozi.rankBattle/GetBattleRoundInfoFrontend")
    def get_battle_round_info_frontend(self, config_id, session, page_size=None):
        """### 模版组件前端接口"""

    @grpc_call(path="/live.mozi.signUpBackend/GetActSignUpList")
    def get_act_sign_up_list(self, act_name=None, conf_status=None, page_index=None, page_size=None, sign_type=None):
        """### 查询活动报名列表"""

    @grpc_call(path="/live.mozi.signUpBackend/UpdateActConfStatus")
    def update_act_conf_status(self, id=None, conf_status=None):
        """### 更新活动上下线状态"""

    @grpc_call(path="/live.mozi.signUpBackend/UpdateActSignUp")
    def update_act_sign_up(self, id=None, act_name=None, start_time=None, end_time=None, operator=None, black_id=None, white_id=None, not_simultaneous_ids=None, review_state=None, sign_type=None, notice_id=None, show_track_info=None, show_change_track=None):
        """### 更新保存活动报名信息(id为0表示新增，否则为修改)"""

    @grpc_call(path="/live.mozi.signUpBackend/GetActSignUpById")
    def get_act_sign_up_by_id(self, id=None):
        """### 获取活动报名信息"""

    @grpc_call(path="/live.mozi.signUpBackend/GetActSignUpMsgById")
    def get_act_sign_up_msg_by_id(self, id=None):
        """### 获取活动报名详细信息(报名id，报名名称，状态，总人数)"""

    @grpc_call(path="/live.mozi.signUpBackend/GetAnchorSignUpMsgByUid")
    def get_anchor_sign_up_msg_by_uid(self, id=None, uid=None):
        """### 根据uid，查询主播参与的所有赛道信息"""

    @grpc_call(path="/live.mozi.signUpBackend/UpdateSignUpTeamByUid")
    def update_sign_up_team_by_uid(self, id=None, uid=None, team_id=None):
        """### 根据uid，修改参加活动报名的赛道"""

    @grpc_call(path="/live.mozi.signUpBackend/ExportActSignUpUserList")
    def export_act_sign_up_user_list(self, id=None):
        """### 导出报名(文件为活动报名的用户表)"""

    @grpc_call(path="/live.mozi.signUpBackend/QueryJobStatus")
    def query_job_status(self, job_key=None):
        """### 查询导出处理结果"""

    @grpc_call(path="/live.mozi.signUpBackend/ActSignUpListBatchToSql")
    def act_sign_up_list_batch_to_sql(self, ids=None):
        """### 批量导出活动报名列表数据sql"""

    @grpc_call(path="/live.mozi.signup/SignUp")
    def sign_up(self, uid=None, sign_id=None, sign_type=None, start_time=None, end_time=None, other_message=None, team_id=None):
        """### 用户报名"""

    @grpc_call(path="/live.mozi.signup/BatchUserSignUp")
    def batch_user_sign_up(self, uids=None, sign_id=None, sign_type=None, start_time=None, end_time=None, team_id=None, other_message=None):
        """### 批量用户报名至同一赛道"""

    @grpc_call(path="/live.mozi.signup/BatchUpdateUserSignUp")
    def batch_update_user_sign_up(self, uids=None, sign_id=None, sign_type=None, start_time=None, end_time=None, team_id=None, other_message=None):
        """### 批量用户修改报名信息"""

    @grpc_call(path="/live.mozi.signup/GetUserSignStatus")
    def get_user_sign_status(self, uid=None, sign_id=None):
        """### 获取用户报名信息"""

    @grpc_call(path="/live.mozi.signup/GetUserSignStatusBatchSignIds")
    def get_user_sign_status_batch_sign_ids(self, uid=None, sign_ids=None):
        """### 批量获取用户报名信息，最多支持10个(多个sign id查询)"""

    @grpc_call(path="/live.mozi.signup/UpdateUserSignUpInfo")
    def update_user_sign_up_info(self, uid=None, sign_id=None, update_type=None, other_message=None, start_time=None, end_time=None, team_id=None, sign_state=None):
        """### 修改报名信息"""

    @grpc_call(path="/live.mozi.signup/GetAllUserSignUp")
    def get_all_user_sign_up(self, sign_id=None, table_num=None, page=None, page_size=None):
        """### 获取某个报名Id的所有报名用户,(直接查DB。使用该接口时请慎重)"""

    @grpc_call(path="/live.mozi.signup/DiffSetSignUp")
    def diff_set_sign_up(self, source_sign_id=None, filter_sign_id=None, target_sign_id=None, other_message=None, start_time=None, end_time=None, team_id=None):
        """### 差集报名 将A中排除掉B的人报到C 不支持互斥逻辑"""

    @grpc_call(path="/live.mozi.signup/BatchGetUserSignUp")
    def batch_get_user_sign_up(self, sign_id=None, uids=None):
        """### 批量获取某个报名ID下指定用户的报名信息 (先查缓存，查不到查db，最多限制20条)"""

    @grpc_call(path="/live.mozi.signup/BatchUserReSpawnSignUp")
    def batch_user_re_spawn_sign_up(self, origin_sign_id=None, target_sign_id=None, fix_score_rank_list=None, start_time=None, end_time=None, offset=None, fix_score_start=None, fix_score_end=None, filter_list=None):
        """### 用户报名到复活榜"""

    @grpc_call(path="/live.mozi.signup/GetAllUserById")
    def get_all_user_by_id(self, sign_id=None, sign_state=None, offset=None, limit=None, uid=None):
        """###=======模版活动使用的接口，就像诺兰的电影，请不要试图理解它，要去感受它======="""

    @grpc_call(path="/live.mozi.signup/GetAllUserByUids")
    def get_all_user_by_uids(self, sign_ids=None, uids=None):
        """### 模板活动后台专用，直接查db！！！union all查询某些Uid 下的报名数据（模板活动后台之外的业务禁！止！使！用！！！！）"""

    @grpc_call(path="/live.mozi.signup/GetAllUserCountById")
    def get_all_user_count_by_id(self, sign_id=None, sign_state=None, offset=None, limit=None, uid=None):
        """### 模板活动后台专用，直接查db！！！union all查询某个sign up id 下的报名数量（模板活动后台之外的业务禁！止！使！用！！！！）"""

    @grpc_call(path="/live.mozi.signup/DeleteUserSignUpInfo")
    def delete_user_sign_up_info(self, sign_id=None, uid=None):
        """### 模板活动后台专用，删除报名数据（模板活动后台之外的业务禁！止！使！用！！！！）"""

    @grpc_call(path="/live.mozi.signup/UpdateActTimeConf")
    def update_act_time_conf(self, id=None, start_time=None, end_time=None):
        """### 模板活动后台专用 更新活动报名时间配置"""

    @grpc_call(path="/live.mozi.signup/BatchImportTemplateUserSignUp")
    def batch_import_template_user_sign_up(self, act_id=None, other_message=None, team_id=None, start_time=None, end_time=None, uids=None):
        """### 模版后台导入"""

    @grpc_call(path="/live.mozi.actCenterBackend/GetActList")
    def get_act_list(self, act_name=None, page_index=None, page_size=None):
        """### 获取活动列表"""

    @grpc_call(path="/live.mozi.actCenterBackend/GetSubList")
    def get_sub_list(self, act_id=None):
        """### 通过活动ID获取子活动"""

    @grpc_call(path="/live.mozi.actCenterBackend/GetActDetail")
    def get_act_detail(self, id=None):
        """### 获取活动配置详情"""

    @grpc_call(path="/live.mozi.actCenterBackend/UpdateSubActStatus")
    def update_sub_act_status(self, sub_act_id=None, conf_status=None):
        """### 修改子活动上下线配置"""

    @grpc_call(path="/live.mozi.actCenterBackend/GetEffectActList")
    def get_effect_act_list(self, timestamp=None):
        """### 获取某段时间内的有效配置 (目前和产品确认,拉取的配置应该为3个月前 至 未生效的所有活动)"""

    @grpc_call(path="/live.mozi.actCenterBackend/GetActListBatchToSql")
    def get_act_list_batch_to_sql(self, ids=None):
        """### 批量导出活动中心数据sql"""

    @grpc_call(path="/live.mozi.actCenterBackend/GetActSortList")
    def get_act_sort_list(self, page_index=None, page_size=None):
        """### 获取活动排序列表"""

    @grpc_call(path="/live.mozi.actCenterBackend/UpdateActWeight")
    def update_act_weight(self, act_id=None, weight_id=None):
        """### 更新活动权重"""

    @grpc_call(path="/live.mozi.actCenterBackend/UpdateActStatus")
    def update_act_status(self, act_id=None, act_status=None):
        """### 更新活动上下线配置"""

    @grpc_call(path="/live.mozi.actCenterBackend/GetOperationActList")
    def get_operation_act_list(self, act_id=None, act_name=None, operator=None, page_index=None, page_size=None):
        """### 获取运营活动列表"""

    @grpc_call(path="/live.mozi.actCenterBackend/GetOperationActDetail")
    def get_operation_act_detail(self, id=None):
        """### 获取运营活动配置详情"""

    @grpc_call(path="/live.mozi.autoSignUpBackend/getAutoSignUpConfigList")
    def get_auto_sign_up_config_list(self, config_name=None, page=None, page_size=None):
        """### 获取活动列表"""

    @grpc_call(path="/live.mozi.autoSignUpBackend/getAutoSignUpConfigById")
    def get_auto_sign_up_config_by_id(self, id=None):
        """###根据配置id获取配置"""

    @grpc_call(path="/live.mozi.autoSignUpBackend/updateAutoSignUpConfigStatus")
    def update_auto_sign_up_config_status(self, id=None, exec_status=None):
        """###配置上下线"""

    @grpc_call(path="/live.mozi.autoSignUpBackend/getAutoSignUpConfigLogList")
    def get_auto_sign_up_config_log_list(self, config_id=None):
        """###获取配置id日志列表"""

    @grpc_call(path="/live.mozi.autoSignUpBackend/batchExportSql")
    def batch_export_sql(self, ids=None):
        """### 批量导出服务端sql"""

    @grpc_call(path="/live.mozi.actCenter/GetActCenterEnterList")
    def get_act_center_enter_list(self, uid=None):
        """### 活动中心入口列表接口"""

    @grpc_call(path="/live.mozi.actCenter/GetActCenterList")
    def get_act_center_list(self, uid, tab_id, page_index, page_size):
        """### 活动列表接口"""

    @grpc_call(path="/live.mozi.actCenter/GetActCenterDetail")
    def get_act_center_detail(self, act_id):
        """### 活动详情接口"""

    @grpc_call(path="/live.mozi.actCenter/GetActSignUpInfo")
    def get_act_sign_up_info(self, uid, act_id):
        """### 报名信息查询接口"""

    @grpc_call(path="/live.mozi.actCenter/GetActResultDetail")
    def get_act_result_detail(self, uid, act_id):
        """### 活动结果页查询接口"""

    @grpc_call(path="/live.mozi.actCenter/GetTopicActJoinList")
    def get_topic_act_join_list(self, uid, act_id, page_index, page_size):
        """### 话题活动参与记录接口"""

    @grpc_call(path="/live.mozi.actCenter/GetActInfoByTopicIds")
    def get_act_info_by_topic_ids(self, topic_id=None):
        """### 根据话题查询活动信息"""

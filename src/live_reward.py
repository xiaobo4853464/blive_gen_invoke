from tiny import grpc_call

class Live_reward(object):
    def __init__(self,service_name):
        self.service_name=service_name
    
    @grpc_call(path="/live.reward.lotteryOrder/GetOrderList")
    def get_order_list(self, uid=None, offset_id=None, act_id=None):
        """### 获取订单列表"""

    @grpc_call(path="/live.reward.lotteryOrder/SaveAwardList")
    def save_award_list(self, award_data, uid):
        """### 保存用户选择申请奖品数据"""

    @grpc_call(path="/live.reward.lotteryOrder/GetOrderDetail")
    def get_order_detail(self, key=None, uid=None):
        """### 获取订单确认页数据"""

    @grpc_call(path="/live.reward.lotteryOrder/GetOrderById")
    def get_order_by_id(self, id, uid):
        """### 通过id获取订单数据"""

    @grpc_call(path="/live.reward.lotteryOrder/CreateOrder")
    def create_order(self, key, platform, receiver_name, phone, province, city, addr_detail, ip, uid, area=None, build=None, mobile_app=None):
        """### 下单"""

    @grpc_call(path="/live.reward.lotteryOrder/SetAddr")
    def set_addr(self, order_id=None, receiver_name=None, phone=None, province=None, city=None, area=None, addr_detail=None, uid=None):
        """### 修改发货地址"""

    @grpc_call(path="/live.reward.lotteryOrder/GetOrder")
    def get_order(self, order_id):
        """### 查询订单状态"""

    @grpc_call(path="/live.reward.lotteryOrder/GetOrderListForMlive")
    def get_order_list_for_mlive(self, act_id=None, status=None, apply_start=None, apply_end=None, page=None, series_id=None, search_type=None, search_value=None):
        """### 【---------------后台接口---------------】"""

    @grpc_call(path="/live.reward.lotteryOrder/ExportOrder")
    def export_order(self, act_id=None, status=None, apply_start=None, apply_end=None, series_id=None, search_type=None, search_value=None):
        """### 导出订单"""

    @grpc_call(path="/live.reward.lotteryOrder/ImportOrder")
    def import_order(self, file_url=None):
        """### 导入物流单号"""

    @grpc_call(path="/live.reward.lotteryOrder/QueryJobStatus")
    def query_job_status(self, job_key=None):
        """### 查询导入和导出处理结果"""

    @grpc_call(path="/live.reward.lotteryOrder/OrderDetail")
    def order_detail(self, id):
        """### 后台查询订单详情接口"""

    @grpc_call(path="/live.reward.lotteryOrder/SaveOrder")
    def save_order(self, id, receiver_name=None, phone=None, province=None, city=None, area=None, addr_detail=None, remark=None):
        """### 编辑订单接口"""

    @grpc_call(path="/live.reward.lotteryOrder/SaveOrderAward")
    def save_order_award(self, order_award_pkid, dispatch_number=None):
        """### 编辑订单奖品接口"""

    @grpc_call(path="/live.reward.physicalAward/exchangeAward")
    def exchange_award(self, award_id=None, uid=None, platform=None, mobi_app=None, build=None):
        """### 碎片兑换奖品 code不为0表示失败"""

    @grpc_call(path="/live.reward.physicalAward/initData")
    def init_data(self, act_id=None):
        """### 初始数据接口"""

    @grpc_call(path="/live.reward.physicalAward/exchangeAwardList")
    def exchange_award_list(self, act_id, award_type=None, show_level=None, page=None, size=None):
        """### 【碎片炼金厂】活动有效期内可兑换奖品列表"""

    @grpc_call(path="/live.reward.physicalAward/lotteryLog")
    def lottery_log(self, target_id=None, target_type=None, act_id=None):
        """### 【欧皇榜】抽奖中奖记录(前50条记录，先查当前月，数据量不够再查上个月)"""

    @grpc_call(path="/live.reward.physicalAward/myAwardLog")
    def my_award_log(self, uid=None, year_month=None, offset=None, act_id=None):
        """### 用户获奖记录(3个月内的流水，支持分页查)"""

    @grpc_call(path="/live.reward.physicalAward/myAwardList")
    def my_award_list(self, uid=None, act_id=None):
        """### 我的奖品列表"""

    @grpc_call(path="/live.reward.physicalAward/GetScoreId")
    def get_score_id(self, act_id=None):
        """### 通过活动id 获取活动信息"""

    @grpc_call(path="/live.reward.physicalAward/addSubStock")
    def add_sub_stock(self, lottery_id=None, unique_id=None, act_id=None, award_id=None, add_type=None, num=None):
        """### 幂等加减奖品库存"""

    @grpc_call(path="/live.reward.jsonConfig/getJsonContent")
    def get_json_content(self, id=None):
        """### 获取文案内容"""

    @grpc_call(path="/live.reward.rewardConfig/rewardData")
    def reward_data(self, reward_id=None):
        """### 前端奖励数据接口"""

    @grpc_call(path="/live.reward.rewardConfig/sendReward")
    def send_reward(self, source=None, msg_id=None, package_id=None, uids=None, msg_time=None, extra_data=None, is_apply=None, business_type=None, business_id=None):
        """### 发送打包奖励"""

    @grpc_call(path="/live.reward.rewardConfig/applyReward")
    def apply_reward(self, source=None, msg_ids=None, uid=None):
        """### 发奖流水查询"""

    @grpc_call(path="/live.reward.rewardConfig/applyRewardLog")
    def apply_reward_log(self, source=None, msg_ids=None, uid=None):
        """### 申领记录查询"""

    @grpc_call(path="/live.reward.rewardConfig/rewardConf")
    def reward_conf(self, reward_id=None):
        """### 获取奖励配置数据"""

    @grpc_call(path="/live.reward.rewardConfig/rewardPackageConf")
    def reward_package_conf(self, package_ids=None):
        """### 获取奖励打包配置数据 【仅支持6个月内的奖励配置查询，一次最多支持支持查10条packageId】"""

    @grpc_call(path="/live.reward.docConfig/getDocContent")
    def get_doc_content(self, id=None):
        """### 获取文案内容"""

    @grpc_call(path="/live.reward.docConfig/DocConfigBatchToSql")
    def doc_config_batch_to_sql(self, ids=None):
        """###批量导出文案配置数据sql"""

    @grpc_call(path="/live.reward.physicalAwardAdmin/import")
    def import_(self, csv_content=None, act_id=None, pool_id=None, series_id=None):
        """### 导入csv数据"""

    @grpc_call(path="/live.reward.physicalAwardAdmin/list")
    def list(self, act_id, pool_id, page, size):
        """### 奖品列表"""

    @grpc_call(path="/live.reward.physicalAwardAdmin/delete")
    def delete(self, id=None):
        """### 删除奖品"""

    @grpc_call(path="/live.reward.physicalAwardAdmin/actList")
    def act_list(self, act_name=None, page=None, page_size=None):
        """### 获取活动列表"""

    @grpc_call(path="/live.reward.rewardConfigAdmin/configList")
    def config_list(self, act_name=None, start_date=None, end_date=None, page=None, size=None):
        """### 活动奖励配置列表"""

    @grpc_call(path="/live.reward.rewardConfigAdmin/configSave")
    def config_save(self, id=None, act_name=None, reward_desc=None, reward_type=None, operator=None):
        """### 保存活动奖励"""

    @grpc_call(path="/live.reward.rewardConfigAdmin/configDetail")
    def config_detail(self, reward_id=None, operator=None):
        """### 活动奖励详情"""

    @grpc_call(path="/live.reward.rewardConfigAdmin/checkImportAwardItems")
    def check_import_award_items(self, reward_id=None, csv_content=None, operator=None):
        """### 检测导入配置"""

    @grpc_call(path="/live.reward.rewardConfigAdmin/importAwardItems")
    def import_award_items(self, reward_id=None, csv_content=None, operator=None):
        """### 导入奖励配置"""

    @grpc_call(path="/live.reward.rewardConfigAdmin/configCopy")
    def config_copy(self, reward_id=None, operator=None):
        """### 复制活动奖励 & 奖品列表"""

    @grpc_call(path="/live.reward.rewardConfigAdmin/rewardItemList")
    def reward_item_list(self, reward_id=None, operator=None):
        """### 活动奖励奖品配置项列表"""

    @grpc_call(path="/live.reward.rewardConfigAdmin/deleteAward")
    def delete_award(self, ids=None, operator=None):
        """### 删除奖品配置，支持批量"""

    @grpc_call(path="/live.reward.rewardConfigAdmin/exportSql")
    def export_sql(self, reward_id=None, operator=None):
        """### 导出服务端配置"""

    @grpc_call(path="/live.reward.rewardConfigAdmin/batchExportSql")
    def batch_export_sql(self, ids=None):
        """### 批量导出服务端sql"""

    @grpc_call(path="/live.reward.rewardConfigAdmin/getRewardConfigList")
    def get_reward_config_list(self, reward_id=None):
        """### 上游后台读取活动奖励列表"""

    @grpc_call(path="/live.reward.actScoreAdmin/actScoreList")
    def act_score_list(self, act_score_id=None, act_score_name=None, page=None, size=None):
        """### json列表"""

    @grpc_call(path="/live.reward.actScoreAdmin/actScoreDetail")
    def act_score_detail(self, id=None):
        """### 详情"""

    @grpc_call(path="/live.reward.actScoreAdmin/actScoreSave")
    def act_score_save(self, id=None, act_score_name=None, act_score_desc=None, operator=None):
        """### 保存配置"""

    @grpc_call(path="/live.reward.docConfigAdmin/docList")
    def doc_list(self, act_name=None, page=None, size=None):
        """### 文案列表"""

    @grpc_call(path="/live.reward.docConfigAdmin/docDetail")
    def doc_detail(self, id=None):
        """### 详情"""

    @grpc_call(path="/live.reward.docConfigAdmin/docSave")
    def doc_save(self, id=None, act_name=None, doc_desc=None, is_enable=None, content=None, operator=None):
        """### 保存文案配置"""

    @grpc_call(path="/live.reward.docConfigAdmin/docSwitchStatus")
    def doc_switch_status(self, id=None, is_enable=None, operator=None):
        """### 上下线"""

    @grpc_call(path="/live.reward.realAwardAdmin/productList")
    def product_list(self, page=None, size=None, product_name=None):
        """### 实物奖品仓库列表 （奖品视图）"""

    @grpc_call(path="/live.reward.realAwardAdmin/productListItem")
    def product_list_item(self, product_id=None, page=None, size=None):
        """### 实物奖品仓库列表明细 （奖品视图）"""

    @grpc_call(path="/live.reward.realAwardAdmin/orderList")
    def order_list(self, page=None, size=None, department_id=None, create_account=None):
        """### 实物奖品仓库列表 （单据视图）"""

    @grpc_call(path="/live.reward.realAwardAdmin/orderListItem")
    def order_list_item(self, page=None, size=None, order_id=None):
        """### 实物奖品仓库列表明细 （单据视图）"""

    @grpc_call(path="/live.reward.realAwardAdmin/refund")
    def refund(self, sub_order_id=None, count=None, apply_account=None):
        """### 退还实物奖品"""

    @grpc_call(path="/live.reward.realAwardAdmin/realAwardProjectAdd")
    def real_award_project_add(self, project_name=None, create_user=None):
        """### 新建项目"""

    @grpc_call(path="/live.reward.realAwardAdmin/realAwardProjectList")
    def real_award_project_list(self, creater_name=None, project_name=None, page=None, size=None):
        """### 项目列表"""

    @grpc_call(path="/live.reward.realAwardAdmin/realAwardProjectChange")
    def real_award_project_change(self, id=None, status=None):
        """### 项目上下线"""

    @grpc_call(path="/live.reward.realAwardAdmin/realAwardProjectPropertyList")
    def real_award_project_property_list(self, project_id=None):
        """### 项目明细数据"""

    @grpc_call(path="/live.reward.realAwardAdmin/realAwardProjectPropertyDelete")
    def real_award_project_property_delete(self, id=None):
        """### 项目明细删除"""

    @grpc_call(path="/live.reward.realAwardAdmin/realAwardProjectPropertySave")
    def real_award_project_property_save(self, id=None, name=None, desc=None, control_type=None, limit_conf=None, remark=None, project_id=None):
        """### 项目明细保存"""

    @grpc_call(path="/live.reward.realAwardAdmin/realAwardItemList")
    def real_award_item_list(self, project_id=None, page=None, size=None, create_account=None):
        """### 项目奖品列表"""

    @grpc_call(path="/live.reward.realAwardAdmin/realAwardItemSave")
    def real_award_item_save(self, id=None, project_award_name=None, project_id=None, source_id=None, product_id=None, apply_count=None, extra_json=None, apply_account=None):
        """### 项目奖品新增or更新"""

    @grpc_call(path="/live.reward.realAwardAdmin/realAwardItemDelete")
    def real_award_item_delete(self, id=None, apply_account=None):
        """### 项目奖品删除"""

    @grpc_call(path="/live.reward.realAwardAdmin/realAwardItemDownload")
    def real_award_item_download(self, project_id=None):
        """### 下载项目奖品csv"""

    @grpc_call(path="/live.reward.realAwardAdmin/realAwardProductList")
    def real_award_product_list(self, project_name=None, pre_order_id=None, award_name=None, invoice_no=None, uid=None, page=None, size=None):
        """### 真实奖品列表"""

    @grpc_call(path="/live.reward.realAwardAdmin/realAwardProductLogList")
    def real_award_product_log_list(self, award_id=None, page=None, size=None):
        """### 真实奖品日志列表"""

    @grpc_call(path="/live.reward.realAwardAdmin/realAwardGetProAwardInfo")
    def real_award_get_pro_award_info(self, project_id=None, product_id=None, apply_account=None):
        """### 获取新增项目奖品数据"""

    @grpc_call(path="/live.reward.jsonConfigAdmin/jsonList")
    def json_list(self, act_name=None, page=None, size=None):
        """### json列表"""

    @grpc_call(path="/live.reward.jsonConfigAdmin/jsonDetail")
    def json_detail(self, id=None):
        """### 详情"""

    @grpc_call(path="/live.reward.jsonConfigAdmin/jsonSave")
    def json_save(self, id=None, act_name=None, doc_desc=None, is_enable=None, content=None, operator=None):
        """### 保存配置"""

    @grpc_call(path="/live.reward.jsonConfigAdmin/jsonSwitchStatus")
    def json_switch_status(self, id=None, is_enable=None, operator=None):
        """### 上下线"""

    @grpc_call(path="/live.reward.jsonConfigAdmin/JsonConfigBatchToSql")
    def json_config_batch_to_sql(self, ids=None):
        """### 批量导出文案json配置数据sql"""

    @grpc_call(path="/live.reward.userItemBackend/GetAllItemList")
    def get_all_item_list(self, page=None, page_size=None, item_name=None):
        """###活动数值管理列表接口"""

    @grpc_call(path="/live.reward.userItem/UpdateUserItem")
    def update_user_item(self, item_id, num, uid, tid, source, expire=None, target_uid=None, target_parent_area_id=None, target_area_id=None, target_other=None, platform=None, mobi_app=None, build=None, device=None, context_type=None, context_id=None, extra_data=None, update_time=None):
        """### 修改物品数量"""

    @grpc_call(path="/live.reward.userItem/GetUserItem")
    def get_user_item(self, item_id, uid, target_uid=None, target_parent_area_id=None, target_area_id=None, target_other=None):
        """### get物品数量"""

    @grpc_call(path="/live.reward.userItem/GetLogForUser")
    def get_log_for_user(self, item_id=None, uid=None, start_time=None, end_time=None, page=None, page_size=None, target_uid=None, target_parent_area_id=None, target_area_id=None, target_other=None, target_otupdate_typeher=None):
        """### 获取日志(用户态，给用户自己看的)"""

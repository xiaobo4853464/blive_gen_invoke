from tiny import grpc_call

class Data_one_piece_task(object):
    def __init__(self,service_name):
        self.service_name=service_name
    
    @grpc_call(path="/live.dataonepiecetask.Label/AddFeature")
    def add_feature(self, feature_id=None, entity_type=None, feature_name=None, feature_desc=None, spark_sql=None, is_roll_refresh=None, valid_date=None, redis_prefix=None, manager=None, front_conf=None, update_desc=None, bind_filter_id=None, data_source=None, guide_status=None):
        """### AddFeature 新增一个自定义标签"""

    @grpc_call(path="/live.dataonepiecetask.Label/UpdateFeature")
    def update_feature(self, feature_id=None, entity_type=None, feature_name=None, feature_desc=None, spark_sql=None, is_roll_refresh=None, valid_date=None, redis_prefix=None, manager=None, front_conf=None, update_desc=None, bind_filter_id=None, data_source=None, guide_status=None):
        """### UpdateFeature 变更一个自定义标签"""

    @grpc_call(path="/live.dataonepiecetask.Label/SelectFeature")
    def select_feature(self, feature_id=None):
        """### SelectFeature 查询一个自定义标签"""

    @grpc_call(path="/live.dataonepiecetask.Label/SearchFeature")
    def search_feature(self, page=None, pagesize=None):
        """### SearchFeature 筛选自定义标签列表"""

    @grpc_call(path="/live.dataonepiecetask.Label/DeleteFeature")
    def delete_feature(self, feature_id=None):
        """### DeleteFeature 删除一个自定义标签（软删）"""

    @grpc_call(path="/live.dataonepiecetask.Label/ToolRunBskJob")
    def tool_run_bsk_job(self, project_id=None, self_dependence=None, start_date=None, end_date=None, execute_period=None):
        """### ToolRunBskJob 工具方法：执行一个 Berserker 任务"""

    @grpc_call(path="/live.dataonepiecetask.Label/ToolSearchBskJob")
    def tool_search_bsk_job(self, project_id=None):
        """### ToolSearchBskJob 工具方法：查询一个 Berserker 任务状态"""

    @grpc_call(path="/live.dataonepiecetask.Label/SelectFeatureJobList")
    def select_feature_job_list(self, feature_id=None, entity_type=None, feature_name=None):
        """### SelectFeatureJobList 查询任务列表"""

    @grpc_call(path="/live.dataonepiecetask.Label/FuzzyForJobName")
    def fuzzy_for_job_name(self, feature_name_prefix=None):
        """### FuzzyForJobName 根据任务名称模糊查询任务名称列表"""

    @grpc_call(path="/live.dataonepiecetask.Label/FeaDataSampling")
    def fea_data_sampling(self, feature_id=None, has_filter=None):
        """### FeaDataSampling 反查数据抽样"""

    @grpc_call(path="/live.dataonepiecetask.Label/AddFeatureAsUser")
    def add_feature_as_user(self, feature_id=None, entity_type=None, feature_name=None, feature_desc=None, spark_sql=None, is_roll_refresh=None, valid_date=None, redis_prefix=None, manager=None, front_conf=None, update_desc=None, bind_filter_id=None, data_source=None, guide_status=None):
        """### AddFeatureAsUser 反查界面化新增关联条件接口，新增一个 berserker 任务"""

    @grpc_call(path="/live.dataonepiecetask.Label/UpdateFeatureAsUser")
    def update_feature_as_user(self, feature_id=None, entity_type=None, feature_name=None, feature_desc=None, spark_sql=None, is_roll_refresh=None, valid_date=None, redis_prefix=None, manager=None, front_conf=None, update_desc=None, bind_filter_id=None, data_source=None, guide_status=None):
        """### UpdateFeatureAsUser 反查界面化修改关联条件接口，修改一个 berserker 任务"""

    @grpc_call(path="/live.dataonepiecetask.Label/FindGroupInfo")
    def find_group_info(self, fea_cate_group_id=None, entity_type=None):
        """### FindGroupInfo 反查界面化详情页，条件关联分组查询"""

    @grpc_call(path="/live.dataonepiecetask.Label/FindGroupList")
    def find_group_list(self, fea_cate_group_id=None):
        """### FindGroupList 反查界面化详情页，分组查询"""

    @grpc_call(path="/live.dataonepiecetask.Label/SearchFeaInfo")
    def search_fea_info(self, fea_id=None, fea_name=None, fea_cn_name=None, data_entity_type=None, is_online=None, fea_cate_group_id=None):
        """### SearchFeaInfo 反查特征列表信息查询"""

    @grpc_call(path="/live.dataonepiecetask.Label/FuzzyForFeaId")
    def fuzzy_for_fea_id(self, fea_id_prefix=None):
        """### FuzzyForFeaId 通过反查特征 id 模糊查询 特征列表id"""

    @grpc_call(path="/live.dataonepiecetask.Label/FuzzyForFeaName")
    def fuzzy_for_fea_name(self, fea_name_prefix=None):
        """### FuzzyForFeaName 通过反查名称模糊查询相关符合条件 名称list"""

    @grpc_call(path="/live.dataonepiecetask.Label/FuzzyForFeaCnName")
    def fuzzy_for_fea_cn_name(self, fea_cn_name_prefix=None):
        """###FuzzyForFeaCnName 通过反查中文名称模糊查询相关符合条件 中文名称list"""

    @grpc_call(path="/live.dataonepiecetask.Label/TestDiagnosisCallback")
    def test_diagnosis_callback(self, featureId=None, paramNum=None, label=None, date=None):
        """### 无标题"""

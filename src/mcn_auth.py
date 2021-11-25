from tiny import grpc_call

class Mcn_auth(object):
    def __init__(self,service_name):
        self.service_name=service_name
    
    @grpc_call(path="/live.mcnauth.Auth/GetAuthUserInfo")
    def get_auth_user_info(self, org_id, superior_uid, inferior_uid):
        """### 获取用户基本信息"""

    @grpc_call(path="/live.mcnauth.Auth/GetUserAuthList")
    def get_user_auth_list(self, org_id, uid):
        """### 获取登陆用户的权限列表"""

    @grpc_call(path="/live.mcnauth.Auth/GetSubUserAuthList")
    def get_sub_user_auth_list(self, org_id, superior_uid, inferior_uid, selected_role_id=None):
        """### 获取下属对应的权限列表"""

    @grpc_call(path="/live.mcnauth.Auth/GetRoleAuthList")
    def get_role_auth_list(self, org_id, selected_role_id):
        """### 获取角色对应的权限列表"""

    @grpc_call(path="/live.mcnauth.Auth/GetSubStructure")
    def get_sub_structure(self, org_id, uid):
        """### 获取下属的组织架构"""

    @grpc_call(path="/live.mcnauth.Auth/GetSubStructureUserList")
    def get_sub_structure_user_list(self, org_id, uid, selected_role_id=None, page=None, page_size=None):
        """### 分页获取下属列表"""

    @grpc_call(path="/live.mcnauth.Auth/GetUserList")
    def get_user_list(self, org_id, page=None, page_size=None, is_bind_wechat=None):
        """### 分页的全量用户列表"""

    @grpc_call(path="/live.mcnauth.Auth/AddOrg")
    def add_org(self, org_id, org_name, creator_uid, creator_uname=None, editor_name=None):
        """### 添加组织"""

    @grpc_call(path="/live.mcnauth.Auth/AddUser")
    def add_user(self, org_id, uid, uname, parent_uid, role_id, operator_uid):
        """### 添加成员"""

    @grpc_call(path="/live.mcnauth.Auth/MultiAddUser")
    def multi_add_user(self, org_id, file_url, uid, operator_uid):
        """### 批量添加成员"""

    @grpc_call(path="/live.mcnauth.Auth/MoveUser")
    def move_user(self, uid, parent_uid, org_id, operator_uid):
        """### 转移成员"""

    @grpc_call(path="/live.mcnauth.Auth/MigrateStaffToOther")
    def migrate_staff_to_other(self, org_id, uid, final_uid, operator=None):
        """### 迁移用户的下级成员到其他成员下"""

    @grpc_call(path="/live.mcnauth.Auth/MigrateAnchorToOther")
    def migrate_anchor_to_other(self, org_id, final_uid, uid, operator=None):
        """### 迁移管理的主播"""

    @grpc_call(path="/live.mcnauth.Auth/RemoveUser")
    def remove_user(self, uid, org_id, operator_uid):
        """### 删除成员"""

    @grpc_call(path="/live.mcnauth.Auth/TransferAnchor")
    def transfer_anchor(self, org_id, anchor_uid, staff_uid=None):
        """### 主播转会(仅限内部调用)"""

    @grpc_call(path="/live.mcnauth.Auth/RemoveAnchor")
    def remove_anchor(self, anchor_uid):
        """### 删除主播(仅限内部调用)"""

    @grpc_call(path="/live.mcnauth.Auth/MultiUpdateAnchor")
    def multi_update_anchor(self, org_id, staff_uid, anchor_uid_list, operator_uid):
        """### 批量修改主播的经纪人(当前仅限内部调用)"""

    @grpc_call(path="/live.mcnauth.Auth/AddSuperAdmin")
    def add_super_admin(self, org_id, uid, uname=None, editor_name=None, token=None):
        """### 添加超级管理员(仅限内部调用)"""

    @grpc_call(path="/live.mcnauth.Auth/RemoveSuperAdmin")
    def remove_super_admin(self, org_id, uid):
        """### 删除超级管理员(仅限内部调用)"""

    @grpc_call(path="/live.mcnauth.Auth/GetRoleList")
    def get_role_list(self, org_id):
        """### 获取角色列表"""

    @grpc_call(path="/live.mcnauth.Auth/SaveUserAuth")
    def save_user_auth(self, org_id, uid, role_id, loginUid, auth_ids=None):
        """### 保存用户权限"""

    @grpc_call(path="/live.mcnauth.Auth/GetAuthMngList")
    def get_auth_mng_list(self, org_id, operator_uid=None):
        """### 获取权限管理列表"""

    @grpc_call(path="/live.mcnauth.Auth/GetUserListByRoleId")
    def get_user_list_by_role_id(self, org_id, role_id, page=None, page_size=None):
        """### 获取组织内某一角色的人员列表"""

    @grpc_call(path="/live.mcnauth.Auth/GetUserDetailInTransfer")
    def get_user_detail_in_transfer(self, org_id, uid):
        """### 转移成员页面查看详情"""

    @grpc_call(path="/live.mcnauth.Auth/Login")
    def login(self, uid):
        """### 登录接口"""

    @grpc_call(path="/live.mcnauth.Auth/Search")
    def search(self, org_id, key, **from_):
        """### 通用搜索"""

    @grpc_call(path="/live.mcnauth.Auth/HasPermission")
    def has_permission(self, org_id, uid, route):
        """### 路由鉴权"""

    @grpc_call(path="/live.mcnauth.Auth/GetAnchorList")
    def get_anchor_list(self, org_id, superior_uid, inferior_uid=None, anchor_uid=None, page=None, page_size=None):
        """### 获取管理的主播列表"""

    @grpc_call(path="/live.mcnauth.Auth/WechatBind")
    def wechat_bind(self, uid, org_id, openid, wechat_name=None):
        """### 微信的绑定/解绑不在auth中处理，是别的服务处理好之后通知过来的"""

    @grpc_call(path="/live.mcnauth.Auth/WechatUnbind")
    def wechat_unbind(self, uid, org_id):
        """###解绑"""

    @grpc_call(path="/live.mcnauth.Auth/GetBrokerRoleByUids")
    def get_broker_role_by_uids(self, uids=None, org_id=None):
        """###批量获取紧急人基本信息"""

    @grpc_call(path="/live.mcnauth.Auth/GetUserListByPermission")
    def get_user_list_by_permission(self, permission):
        """###获取有某个权限的所有人员"""

    @grpc_call(path="/live.mcnauth.Auth/GetMcnAuthByTypeAndSortId")
    def get_mcn_auth_by_type_and_sort_id(self, auth_type, sort_id):
        """###根据authType和sortId获取mcn_auth"""

    @grpc_call(path="/live.mcnauth.Auth/GetGuildUserList")
    def get_guild_user_list(self, page, page_size, org_id, uid=None, role_id=None):
        """### 查询公会成员列表"""

    @grpc_call(path="/live.mcnauth.Auth/SetUserForbidStatus")
    def set_user_forbid_status(self, org_id, uid, is_forbid, editor_name=None):
        """### 封禁/解封成员"""

    @grpc_call(path="/live.mcnauth.Auth/GetGuildSuperAdmins")
    def get_guild_super_admins(self, org_id):
        """### 获取公会超管（当前仅限内部调用）"""

    @grpc_call(path="/live.mcnauth.Auth/ModifyGuildSuperAdmin")
    def modify_guild_super_admin(self, org_id, old_uid, new_uid, editor_name):
        """### 修改超管"""

    @grpc_call(path="/live.mcnauth.Auth/RemoveGuildUser")
    def remove_guild_user(self, org_id, uid, transfer_uid, editor_name):
        """### 删除公会成员"""

    @grpc_call(path="/live.mcnauth.Auth/GetOrgIdsByUid")
    def get_org_ids_by_uid(self, uid):
        """### 根据uid获取用户所有的组织id（当前仅限内部调用）"""

    @grpc_call(path="/live.mcnauth.Auth/GetSubUserAndAnchorCount")
    def get_sub_user_and_anchor_count(self, org_id, uid):
        """### 获取用户的下级成员及主播数量"""

    @grpc_call(path="/live.mcnauth.Auth/GetAnchorStaffInfo")
    def get_anchor_staff_info(self, uids):
        """### 获取主播经纪人信息"""

    @grpc_call(path="/live.mcnauth.Auth/GetAllValidStaff")
    def get_all_valid_staff(self, start_time=None, end_time=None):
        """### 获取所有有效的公会管理人员"""

    @grpc_call(path="/live.mcnauth.Wechat/Bind")
    def bind(self, openid, wechat_name=None):
        """###绑定"""

    @grpc_call(path="/live.mcnauth.Wechat/Unbind")
    def unbind(self, uid):
        """###解绑"""

from tiny import grpc_call

class Xrewardcenter(object):
    def __init__(self,service_name):
        self.service_name=service_name
    
    @grpc_call(path="/live.xrewardcenter.v1.AnchorReward/myReward")
    def my_reward(self, uid, page=None):
        """### (主播侧)-我的主播奖励(登录态)"""

    @grpc_call(path="/live.xrewardcenter.v1.AnchorReward/useRecord")
    def use_record(self, uid, page=None):
        """###* (主播侧)-奖励使用记录(登录态)"""

    @grpc_call(path="/live.xrewardcenter.v1.AnchorReward/useReward")
    def use_reward(self, id, uid, use_plat):
        """###* (主播侧)-使用奖励(登录态)"""

    @grpc_call(path="/live.xrewardcenter.v1.AnchorReward/isViewed")
    def is_viewed(self, uid):
        """###* (主播侧)-奖励和任务红点(登录态)"""

    @grpc_call(path="/live.xrewardcenter.v1.AnchorReward/addReward")
    def add_reward(self, reward_id, roomid, source, uid, order_id, lifespan=None, num=None):
        """### (主播侧)-添加主播奖励(内部接口)"""

    @grpc_call(path="/live.xrewardcenter.v1.Reward/RewardSendStatus")
    def reward_send_status(self, uids=None, date=None, msg_id=None):
        """### 查询奖励发送状态"""

    @grpc_call(path="/live.xrewardcenter.v1.Reward/ReissueReward")
    def reissue_reward(self, uid=None, msg_id=None, date=None):
        """### 补发奖励"""

    @grpc_call(path="/live.xrewardcenter.v1.Reward/GrantBagReward")
    def grant_bag_reward(self, uids=None, targetId=None, bagID=None):
        """###  GrantBagReward  内部测试打包奖励接口"""

    @grpc_call(path="/live.xrewardcenter.v0.RewardPool/Set")
    def set(self, name, reward_config, id=None, creator=None):
        """### 设置奖池"""

    @grpc_call(path="/live.xrewardcenter.v0.RewardPool/Get")
    def get(self, id):
        """### 读取奖池"""

    @grpc_call(path="/live.xrewardcenter.v0.RewardPool/List")
    def list(self, page=None, page_size=None):
        """### 奖池列表"""

    @grpc_call(path="/live.xrewardcenter.v0.RewardPool/GetPools")
    def get_pools(self, page=None, page_size=None):
        """### 分页获取已经配置的奖池信息"""

    @grpc_call(path="/live.xrewardcenter.v2.AnchorReward/RewardList")
    def reward_list(self, type, reward_type, user_id, page=None, pagesize=None):
        """### 奖励列表 (主播侧)"""

    @grpc_call(path="/live.xrewardcenter.v2.AnchorReward/UseReward")
    def use_reward(self, record_id, type, user_id, platform=None):
        """### 佩戴新奖励(主播侧)"""

    @grpc_call(path="/live.xrewardcenter.v2.AnchorReward/HasExpire")
    def has_expire(self, user_id, type=None):
        """### 截止今天上次查看是否有奖励过期(主播侧)"""

    @grpc_call(path="/live.xrewardcenter.v2.AnchorReward/RoomHeadBox")
    def room_head_box(self, room_ids=None, user_ids=None):
        """### 获取房间当前 头像框 目前只支持小批量获取"""

    @grpc_call(path="/live.xrewardcenter.v2.AnchorReward/RoomSkin")
    def room_skin(self, room_id=None):
        """### 获取房间当前 皮肤ID, 为room-service定制"""

    @grpc_call(path="/live.xrewardcenter.v2.AnchorReward/CancelReward")
    def cancel_reward(self, source_id=None, reward_type=None, reward_id=None, user_ids=None):
        """### 撤销当前奖励"""

    @grpc_call(path="/live.xrewardcenter.v2.Skin/Current")
    def current(self, room_id=None, skin_platform=None, skin_version=None, area_v2_parent_id=None, area_v2_id=None, device=None, build=None, mobi_app=None):
        """### 获取当前房间的皮肤"""

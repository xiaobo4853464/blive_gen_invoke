"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""
from tiny import grpc_call


class Gift(object):

    def __init__(self, service_name):
        self.service_name = service_name

    @grpc_call(path="/live.xgift.v1.Bag/BagList")
    def bag_list(self, roomid=None, uid=None, platform=None, build=None, mobi_app=None):
        """### 包裹列表"""

    @grpc_call(path="/live.xgift.v1.Bag/BagReduce")
    def bag_reduce(self, uid=None, gift_num=None, bag_id=None, gift_id=None, platform=None, biz_id=None):
        """### 提供送礼接口扣减道具"""

    @grpc_call(path="/live.xgift.v1.Bag/BagDeleteTask")
    def bag_delete_task(self, table=None, limit=None):
        """### 移除过期道具"""

    @grpc_call(path="/live.xgift.v1.Bag/BagInfoAdmin")
    def bag_info_admin(self, uid=None, next_offset=None, prev_offset=None, page_size=None, export=None):
        """### 用户包裹资产"""

    @grpc_call(path="/live.xgift.v1.Bag/ClearBagDot")
    def clear_bag_dot(self, uid):
        """### 清理包裹红点"""

    @grpc_call(path="/live.xgift.v1.Bag/GetBagDot")
    def get_bag_dot(self, uid):
        """### 获取包裹红点"""

    @grpc_call(path="/live.xgift.v1.Bag/GetBagListByUid")
    def get_bag_list_by_uid(self, uid, status=None):
        """### 用户包裹列表 后台用 （包括 金瓜子包裹、免费包裹）"""

    @grpc_call(path="/live.xgift.v1.Bag/SilverPackageStream")
    def silver_package_stream(self, uid=None, gift_id=None, bag_id=None, source=None, begin_time=None, end_time=None, page=None, page_size=None):
        """### 用户银瓜子包裹查询"""


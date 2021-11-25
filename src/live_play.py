"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""
from tiny import grpc_call


class Live_play(object):

    def __init__(self, service_name):
        self.service_name = service_name

    @grpc_call(path="/live.liveplay.MessageWall/GetMsgList")
    def get_msg_list(self, page, page_size, act_id, start_time, end_time, ruid=None):
        """###获取消息列表"""

    @grpc_call(path="/live.liveplay.MessageWall/UpOrDownMsg")
    def up_or_down_msg(self, id=None, status=None):
        """###更新上下线状态"""

    @grpc_call(path="/live.liveplay.MessageWall/BatchPublishMsg")
    def batch_publish_msg(self, act_id, start_time, end_time, force_pub=None):
        """###批量发布留言"""

    @grpc_call(path="/live.liveplay.MessageWall/SendMessage")
    def send_message(self, ruid=None, uid=None, message=None, coin=None, act_id=None, room_id=None):
        """### 发送留言"""

    @grpc_call(path="/live.liveplay.MessageWall/GetMessage")
    def get_message(self, act_id=None):
        """### 获取留言"""

    @grpc_call(path="/live.liveplay.MessageWall/GetScore")
    def get_score(self, uid=None, ruid=None, act_id=None):
        """### 获取福气值个数"""

    @grpc_call(path="/live.liveplay.MessageWall/GetMessagesByCondition")
    def get_messages_by_condition(self, act_id, ruid, uid, start_time, end_time):
        """### 指定条件查主播所有的留言"""


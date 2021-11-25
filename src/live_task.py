"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""
from tiny import grpc_call


class Live_task(object):

    def __init__(self, service_name):
        self.service_name = service_name

    @grpc_call(path="/live.livetask.Bls2020/GetTask")
    def get_task(self, uid=None, room_id=None):
        """### 获取用户任务"""

    @grpc_call(path="/live.livetask.Bls2020/GetTaskPendant")
    def get_task_pendant(self, uid=None, room_id=None):
        """### 主播助力任务挂件"""

    @grpc_call(path="/live.livetask.Bls2020/GetFinalistTask")
    def get_finalist_task(self, uid=None, room_id=None):
        """### 获取入围赛任务进度"""

    @grpc_call(path="/live.livetask.Bls2020/GetFinalistTaskPendant")
    def get_finalist_task_pendant(self, uid=None, room_id=None):
        """### 入围赛挂件"""

    @grpc_call(path="/live.livetask.Bls2020/GetFinalistTaskRank")
    def get_finalist_task_rank(self, team_id=None, page=None):
        """### 入围赛榜单 (只展示当天)"""

    @grpc_call(path="/live.livetask.Bls2020/GetFinalistTaskAidRank")
    def get_finalist_task_aid_rank(self, ruid=None, room_id=None):
        """### 入围赛应援榜"""


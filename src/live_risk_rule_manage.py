"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""
from tiny import grpc_call


class Live_risk_rule_manage(object):

    def __init__(self, service_name):
        self.service_name = service_name

    @grpc_call(path="/rule/list")
    def list(self, ty=None, sid=None, stat=None):
        """### 无标题"""

    @grpc_call(path="/rule/add")
    def add(self, ty=None, sid=None, name=None, des=None, sal=None, content=None, user=None):
        """### 无标题"""

    @grpc_call(path="/rule/update")
    def update(self, id=None, des=None, sal=None, content=None, user=None):
        """### 无标题"""

    @grpc_call(path="/rule/start")
    def start(self, id=None, user=None, stat=None):
        """### 无标题"""

    @grpc_call(path="/rule/index")
    def index(self, id):
        """### 无标题"""

    @grpc_call(path="/scene/add")
    def add(self, ty=None, sname=None, queue=None, api=None, exe_model=None):
        """### 无标题"""

    @grpc_call(path="/get/scence")
    def scence(self, ty=None):
        """### 无标题"""

    @grpc_call(path="/change/model")
    def model(self, sid=None, sname=None, exe_model=None):
        """### 无标题"""


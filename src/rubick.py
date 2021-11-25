"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""
from tiny import grpc_call


class Rubick(object):

    def __init__(self, service_name):
        self.service_name = service_name

    @grpc_call(path="/api/strategy/delete")
    def delete(self, id=None):
        """### 删除接口"""

    @grpc_call(path="/api/strategy/list")
    def list(self, pageNo=None, pageSize=None, sortField=None, sortOrder=None, id=None, status=None, recall=None, feature=None, filter=None, model=None, rerank=None, muser=None, comment=None):
        """### 列表接口"""

    @grpc_call(path="/api/strategy/save")
    def save(self, id=None, comment=None, status=None, recall=None, feature=None, filter=None, model=None, rerank=None, isAdd=None):
        """### 新增或更新接口"""

    @grpc_call(path="/api/strategy/test")
    def test(self, id=None, comment=None, status=None, recall=None, feature=None, filter=None, model=None, rerank=None, isAdd=None):
        """### 验证接口"""

    @grpc_call(path="/api/strategy/multi")
    def multi(self, action=None, ids=None):
        """### 批量接口: 删除/上线/下线"""


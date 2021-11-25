"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""
from tiny import grpc_call


class Matrix(object):

    def __init__(self, service_name):
        self.service_name = service_name

    @grpc_call(path="/live.matrix.brain/Eval")
    def eval(self, user_id=None, expr=None):
        """### Eval"""


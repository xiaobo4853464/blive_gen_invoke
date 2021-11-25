from tiny import grpc_call

class Matrix(object):
    def __init__(self,service_name):
        self.service_name=service_name
    
    @grpc_call(path="/live.matrix.wechat/SendMessage")
    def send_message(self, message=None, real_name=None, type=None):
        """### Send Message To Business WeChat"""

    @grpc_call(path="/live.matrix.brain/Eval")
    def eval(self, user_id=None, expr=None):
        """### Eval"""

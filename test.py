from tiny import grpc_call


class A():
    def __init__(self, service_name):
        self.service_name = service_name

    @grpc_call(path="/hello")
    def hello(self):
        pass


A('xb').hello()

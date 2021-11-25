from tiny import grpc_call

class Live_risk_metrics(object):
    def __init__(self,service_name):
        self.service_name=service_name
    
    @grpc_call(path="/live.riskmetrics.v1.MetricService/GetCount")
    def get_count(self, ruleName=None, useCache=None, metricName=None, seconds=None, field=None):
        """### 无标题"""

    @grpc_call(path="/live.riskmetrics.v1.MetricService/IsIn")
    def is_in(self, ruleName=None, useCache=None, metricName=None, field=None):
        """### 无标题"""

    @grpc_call(path="/live.riskmetrics.v1.MetricService/GetNumber")
    def get_number(self, ruleName=None, useCache=None, metricName=None, field=None):
        """### 无标题"""

    @grpc_call(path="/live.riskmetrics.v1.MetricService/GetString")
    def get_string(self, ruleName=None, useCache=None, metricName=None, field=None):
        """### 无标题"""

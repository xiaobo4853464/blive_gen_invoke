from tiny import grpc_call

class Push_live(object):
    def __init__(self,service_name):
        self.service_name=service_name
    
    @grpc_call(path="/live.pushlive.v1.Filter/SetRoomFilter")
    def set_room_filter(self, room_id, start_time, end_time, source, source_id):
        """###批量房间屏蔽tab"""

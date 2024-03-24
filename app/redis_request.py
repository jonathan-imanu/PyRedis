from app.redis_encoder import RedisEncoder
from app.redis_parser import RedisParser

class RedisRequest:
    def __init__(self, request) -> None:
        self.data = RedisParser.parse_value(request)
        self.command = self.data[0].lower()
        
    def response(self)-> bytes:
        if self.command == "ping":
            return RedisEncoder.encode_simple_string("PONG")
        elif self.command == "echo":
            return RedisEncoder.encode_bulk_string(self.data[1])
    
    
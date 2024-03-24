from app.redis_encoder import RedisEncoder
from app.redis_parser import RedisParser

class RedisRequest:
    def __init__(self, request_bytes: bytes):
        self.data = RedisParser().parse(request_bytes)
        self.command = self.data[0].lower()
        
    def response(self, server) -> bytes:
        """Returns a response for the request in bytes depending on the command

        Returns:
            bytes: A response for the request
        """
        if self.command == "ping":
            return RedisEncoder.encode_simple_string("PONG")
        elif self.command == "echo":
            return RedisEncoder.encode_bulk_string(self.data[1])
        
        elif self.command == "set":
            # server.db[self.data[1]] = self.data[2]
            # return RedisEncoder.encode_simple_string("OK")
            var = self.data[1]
            val = self.data[2]
            expiry = None
            
            if len(self.data) > 4 and self.data[4].lower() == "px":
                expiry = self.data[4]
            return server.database.set(var, val, expiry)
            
        elif self.command == "get":
            # data = server.db[self.data[1]]
            # if not data: 
            #     return RedisEncoder.encode_bulk_string("-1") 
            # return RedisEncoder.encode_simple_string(data)
            return server.database.get(self.data[1])
    
    
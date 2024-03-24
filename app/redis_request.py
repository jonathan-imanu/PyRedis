from app.redis_encoder import RedisEncoder
from app.redis_parser import RedisParser

class RedisRequest:
    def __init__(self, request_bytes: bytes):
        self.data = RedisParser().parse(request_bytes)
        self.command = self.data[0].lower()
        
    def response(self, db) -> bytes:
        """Returns a response for the request in bytes depending on the command

        Returns:
            bytes: A response for the request
        """
        if self.command == "ping":
            return RedisEncoder.encode_simple_string("PONG")
        elif self.command == "echo":
            return RedisEncoder.encode_bulk_string(self.data[1])
        elif self.command == "set":
            db[self.data[1]] = self.data[2]
            return RedisEncoder.encode_simple_string("OK")
        elif self.command == "get":
            return db[self.data[1]]

    def __str__(self):
        return str(self.data)
    
    
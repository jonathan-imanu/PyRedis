from app.redis_encoder import RedisEncoder
from app.redis_parser import RedisParser
from app.constants import Commands, Arguments

class RedisRequest:
    def __init__(self, request_bytes: bytes):
        self.data = RedisParser().parse(request_bytes)
        self.command = self.data[0].upper()
        
    def response(self, server) -> bytes:
        """Returns a response for the request in bytes depending on the command

        Returns:
            bytes: A response for the request
        """
        match self.command:
            case Commands.PING:
                return RedisEncoder.encode_simple_string("PONG")
            case Commands.ECHO:
                return RedisEncoder.encode_bulk_string(self.data[1])
            case Commands.SET:
                var = self.data[1]
                val = self.data[2]
                expiry = None
                if len(self.data) > 4 and self.data[3].upper() == Arguments.PX:
                    expiry = self.data[4]
                return server.database.set(var, val, expiry)
            case Commands.GET:
                return server.database.get(self.data[1])
            case Commands.INFO:
                print(RedisEncoder.encode_bulk_string(server.role))
                return RedisEncoder.encode_bulk_string(server.role)
    
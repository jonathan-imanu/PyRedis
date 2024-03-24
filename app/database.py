from time import time
from collections import namedtuple
from typing import Optional
from app.redis_encoder import RedisEncoder

# ITEM = namedtuple("value", "expiry")

NULL_BULK_STRING = b'$-1\r\n'

class Database():
    def __init__(self):
       self.database: dict[str, tuple] = {}
    
    def ms_time() -> int:
        """Returns the current time in milliseconds."""
        return int(time() * 1000)
    
    # def set(self, variable: str, value: str, expiry: Optional[int] = None) -> str:
    def set(self, variable, value, expiry=None):
        if expiry is None:
            self.database[variable] = (value, expiry)
        else:
            expiry += Database.ms_time()
            self.database[variable] = (value, expiry)
        return RedisEncoder.encode_simple_string("OK")
     
    def get(self, variable: str) -> str:
        if variable not in self.database:
            print(NULL_BULK_STRING)
            return NULL_BULK_STRING
 
        item = self.database[variable]
        
        if item[1] and item[1] <= Database.ms_time():
            del self.database[variable]
            print(NULL_BULK_STRING)
            return NULL_BULK_STRING
        
        return RedisEncoder.encode_bulk_string(item[0])
    
    





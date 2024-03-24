from time import time
from collections import namedtuple
from typing import Optional
from app.redis_encoder import RedisEncoder

ITEM = namedtuple("value", "expiry")

class Database():
    def __init__(self):
       self.database: dict[str, ITEM] = {}
    
    def ms_time() -> int:
        """Returns the current time in milliseconds."""
        return int(time() * 1000)
    
    # def set(self, variable: str, value: str, expiry: Optional[int] = None) -> str:
    def set(self, variable, value, expiry=None):
        if expiry is None:
            self.database[variable] = ITEM(value, expiry)
        else:
            expiry = expiry + self.ms_time()
            self.database[variable] = ITEM(value, expiry)
        return RedisEncoder.encode_simple_string("OK")
     
    def get(self, variable: str) -> str:
        if variable not in self.database:
            return RedisEncoder.encode_bulk_string("-1")
 
        item = self.database[variable]
        
        if item.expiry and item.expiry <= self.ms_time():
            del self.database[variable]
            return RedisEncoder.encode_bulk_string("-1")
        
        return RedisEncoder.encode_bulk_string(item)
    
    





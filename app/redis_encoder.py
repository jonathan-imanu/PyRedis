CRLF = b'\r\n'

class RedisEncoder:
    @staticmethod
    def encode_simple_string(string) -> bytes:
        return b"+" + string.encode() + CRLF
    @staticmethod
    def encode_simple_errors():
        pass
    @staticmethod
    def encode_integers(error):
        pass
    @staticmethod
    def encode_bulk_string(string):
        return b"$" +  str(len(string)).encode() + CRLF + string.encode() + CRLF
    @staticmethod
    def encode_arrays(array):
        pass
        
        
        
    
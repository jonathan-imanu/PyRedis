CRLF = b'\r\n'

class RedisEncoder:
    @staticmethod
    def encode_simple_string(string) -> bytes:
        return b"+" + string.encode() + CRLF
    @staticmethod
    def encode_simple_errors():
        raise NotImplementedError
        pass
    @staticmethod
    def encode_integers(error):
        raise NotImplementedError
        pass
    @staticmethod
    def encode_bulk_string(string):
        return b"$" +  str(len(string)).encode() + CRLF + string.encode() + CRLF
    @staticmethod
    def encode_arrays(array):
        raise NotImplementedError
        pass
        
        
        
    
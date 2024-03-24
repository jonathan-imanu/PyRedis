class RedisEncoder:
    @staticmethod
    def encode_simple_string(string) -> bytes:
        return b"+" + string.encode() + b"\r\n"
    def encode_simple_errors():
        pass
    def encode_integers(error):
        pass
    def encode_bulk_string(string):
        return b"$" + string.encode() + b"\r\n"
    def encode_arrays(array):
        pass
        
        
        
    
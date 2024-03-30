CRLF = b'\r\n'

class RedisEncoder:
    @staticmethod
    def encode_simple_string(string) -> bytes:
        return b"+" + string.encode() + CRLF
    @staticmethod
    def encode_simple_errors(error) -> bytes:
        return b"-" + error.encode() + CRLF
    @staticmethod
    def encode_integers(error):
        raise NotImplementedError
    @staticmethod
    def encode_bulk_string(string):
        return b"$" +  str(len(string)).encode() + CRLF + string.encode() + CRLF
    @staticmethod
    def encode_arrays(array):
        encoded_array = b"*"
        encoded_array += str(len(array)).encode()
        encoded_array += CRLF
        for element in array:
            encoded_array += RedisEncoder.encode_bulk_string(element)
            encoded_array += CRLF
        return encoded_array
        
        
        
        
    
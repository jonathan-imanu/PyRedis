from typing import Any, List

class RedisParser:
    """
    Class to parse the redis input
    """
    def __init__(self):
        self.string: bytes = b""
        self.len: int = 0
        self.index: int = 0
        self.value = None
    def inc(self) -> None:
        self.index += 1
    def curr(self) -> bytes:
        """
        Get the current byte
        :return: The current byte
        """
        return self.string[self.index : self.index + 1]
    def get(self, i) -> bytes:
        """
        Get the byte value at ith position
        :param i: The position
        :return: The byte value
        """
        return self.string[i : i + 1]
    def substring(self, i, j) -> bytes:
        """
        Get the bytes from i(included) to j(excluded)
        :param i: Start position
        :param j: End position
        :return: The byte values
        """
        return self.string[i:j]
    def parse(self, b: bytes) -> Any:
        """
        Parse the bytes to interpretable values
        :param b: the bytes to parse
        :return: The parsed input
        """
        self.string = b
        self.len = len(self.string)
        self.index = 0
        return self.parse_value()
    def parse_value(self) -> Any:
        """
        Parse the bytes to interpretable values
        :return: the parsed value
        """
        if self.current_byte() == b"+":
            return self.parse_simple_str()
        elif self.current_byte() == b"-":
            return self.parse_simple_errors()
        elif self.current_byte() == b":":
            return self.parse_integers()
        elif self.current_byte() == b"*":
            return self.parse_array()
        elif self.current_byte() == b"$":
            return self.parse_bulk_string()
        else:
            raise NotImplementedError
    def parse_array(self) -> List:
        """
        Parse the bytes to interpretable array
        :return: array
        """
        arr = []
        self.parse_single(b"*")
        array_length = self.parse_digits()
        self.parse_endline()
        for i in range(array_length):
            arr.append(self.parse_value())
        return arr
    def parse_bulk_string(self) -> str:
        """
        Parse the bytes to interpretable string
        :return: string
        """
        self.parse_single(b"$")
        string_length = self.parse_digits()
        self.parse_endline()
        string = self.substring(self.index, self.index + string_length)
        self.index += string_length
        self.parse_endline()
        return string.decode()
    def parse_digits(self) -> int:
        """
        Parse the digits as long as it is valid
        :return: the integer representation of the parsed digits
        """
        i = self.index
        while self.curr().isdigit():
            self.inc()
        return int(self.substring(i, self.index))
    def parse_single(self, b: bytes):
        """
        Parse the current byte if it is equal to input
        :param b: The input
        """
        if self.curr() == b:
            self.inc()
    def parse_endline(self):
        """
        Parse the end line of redis
        """
        if self.substring(self.index, self.index + 2) == b"\r\n":
            self.index += 2 
   

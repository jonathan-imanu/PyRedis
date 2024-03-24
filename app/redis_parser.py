from typing import Any, List

class RedisParser:
    def __init__(self):
        self.string: bytes = b""
        self.len: int = 0
        self.index: int = 0
        self.value = None
    
    def increment(self) -> None:
        self.index += 1
    
    def current_byte(self) -> bytes:
        return self.string[self.index: self.index + 1]
    
    def get(self, i) -> bytes:
        """ Get the byte value at position i

        Args:
            i (int): The position 

        Returns:
            bytes: The byte value
        """
        return self.string[i : i + 1]
    
    def substring(self, i, j) -> bytes:
        """Get the byte values starting at postion i 
        and stopping before postion j

        Args:
            i (int): Position 1
            j (int): Position 2

        Returns:
            bytes: The byte values
        """
        return self.string[i: j]
    
    def parse_digits(self) -> int:
        """
        Parse the digits as long as it is valid
        :return: the integer representation of the parsed digits
        """
        idx = self.index
        while self.current_byte().isdigit():
            self.increment()
        return self.substring(idx, self.index)
        
    def parse_single(self, b: bytes) -> None:
        """
        Parse the current byte if it is equal to input
        :param b: The input
        """
        if self.current_byte == b:
            self.increment()
            
    def parse_endline(self):
        """
        Parse the end line of redis
        """
        if(self.substring(self.index, self.index + 2) == b"\r\n"):
            self.index += 2
    
    def parse_simple_str(self) -> str:
        """Parse the bytes to an interpretable string

        Returns:
            str: The interpretable string
        """
        self.parse_single(b"+")
        length = self.parse_digits()
        self.parse_endline()
        string = self.substring(self.index, self.index + length)
        self.index += length
        self.parse_endline()
        return string.decode()
    
    def parse_simple_errors(self) -> Any:
        """Parse the bytes to interpretable error

        Returns:
            Any: IDK YET TBH
        """
        raise NotImplementedError
    
    def parse_integers(self) -> int:
        """Parse the bytes to an interpretable integer

        Returns:
            int: The interpretable integer
        """
        raise NotImplementedError
    
    def parse_array(self) -> List:
        """Parse the bytes to an interpretable array

        Returns:
            List: The interpretable array
        """
        list = []
        self.parse_single(b"*")
        length = self.parse_digits()
        self.parse_endline()
        for i in range(length):
            list.append(self.parse_value())
        return list     
        
    def parse_bulk_string(self) -> str:
        """Parse the bytes to a bulk string

        Returns:
            str: The interpretable string
        """
        self.parse_single(b"$")
        length = self.parse_digits()
        self.parse_endline()
        string = self.substring(self.index, self.index + length)
        self.index += length
        self.parse_endline()
        return string.decode()
    
    def parse_value(self, b: bytes) -> Any:
        """Parse the value to something comprehensible

        Raises:
            NotImplementedError: When the RESP data type is not in RESP 2

        Returns:
            Any: Dependent on the first byte
        """
        self.string = b
        self.len = len(self.string)
        self.index = 0
        
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
    
   

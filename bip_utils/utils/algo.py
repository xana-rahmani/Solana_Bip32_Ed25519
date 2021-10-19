from typing import Union


class AlgoUtils:
    """ Class container for algorithm utility functions. """

    @staticmethod
    def Encode(data: Union[bytes, str],
               encoding: str = "utf-8") -> bytes:
        """ Encode to bytes.

        Args:
            data (str or bytes): Data
            encoding (str)     : Encoding type

        Returns:
            bytes: String encoded to bytes

        Raises:
            TypeError: If the data is neither string nor bytes
        """
        if isinstance(data, str):
            return data.encode(encoding)
        elif isinstance(data, bytes):
            return data
        raise TypeError("Invalid data type")

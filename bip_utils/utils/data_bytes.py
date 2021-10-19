from bip_utils.utils.conversion import ConvUtils


class DataBytes:
    """ Bytes class. It allows to get bytes in different formats. """

    def __init__(self,
                 key_bytes: bytes) -> None:
        """ Construct class.

        Args:
            key_bytes (bytes): Key bytes
        """
        self.m_key_bytes = key_bytes

    def ToBytes(self) -> bytes:
        """ Get key bytes.

        Returns:
            bytes: Key bytes
        """
        return self.m_key_bytes

    def ToHex(self) -> str:
        """ Get key bytes in hex format.

        Returns:
            str: Key bytes in hex format
        """
        return ConvUtils.BytesToHexString(self.m_key_bytes)

    def ToInt(self,
              endianness: str = "big") -> int:
        """ Get key bytes as an integer.

        Args:
            endianness (str, optional): Endianness

        Returns:
            int: Key bytes as an integer
        """
        return ConvUtils.BytesToInteger(self.m_key_bytes, endianness)

    def __bytes__(self) -> bytes:
        """ Get key bytes.

        Returns:
            bytes: Key bytes
        """
        return self.ToBytes()

    def __str__(self) -> str:
        """ Get key bytes as string.

        Returns:
            str: Key bytes as string
        """
        return self.ToHex()

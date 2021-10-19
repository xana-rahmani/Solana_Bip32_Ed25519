import hashlib
import hmac
from typing import Union
from bip_utils.utils.algo import AlgoUtils


class CryptoUtils:
    """ Class container for crypto utility functions. """

    @staticmethod
    def Sha256(data: Union[bytes, str]) -> bytes:
        """ Compute the SHA256 of the specified bytes.

        Args:
            data (str or bytes): Data

        Returns:
            bytes: Computed SHA256
        """
        return hashlib.sha256(AlgoUtils.Encode(data)).digest()

    @staticmethod
    def HmacSha512(key: Union[bytes, str],
                   data: Union[bytes, str]) -> bytes:
        """ Compute the HMAC-SHA512 of the specified bytes with the specified key.

        Args:
            key (str or bytes) : Key
            data (str or bytes): Data

        Returns:
            bytes: Computed HMAC-SHA512
        """
        return hmac.new(AlgoUtils.Encode(key), AlgoUtils.Encode(data), hashlib.sha512).digest()

    @staticmethod
    def Hash160(data: Union[bytes, str]) -> bytes:
        """ Compute the Bitcoin Hash-160 of the specified bytes.

        Args:
            data (str or bytes): Data

        Returns:
            bytes: Computed Hash-160
        """
        return hashlib.new("ripemd160", CryptoUtils.Sha256(data)).digest()

    @staticmethod
    def Pbkdf2HmacSha512(password: Union[bytes, str],
                         salt: Union[bytes, str],
                         itr_num: int) -> bytes:
        """ Compute the PBKDF2 HMAC-SHA512 of the specified password, using the specified keys and iteration number.

        Args:
            password (str or bytes): Password
            salt (str or bytes)    : Salt
            itr_num (int)          : Iteration number

        Returns:
            bytes: Computed PBKDF2 HMAC-SHA512
        """
        return hashlib.pbkdf2_hmac("sha512", AlgoUtils.Encode(password), AlgoUtils.Encode(salt), itr_num)

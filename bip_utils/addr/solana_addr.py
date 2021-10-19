from typing import Union
from bip_utils.addr.utils import AddrUtils
from bip_utils.base58 import Base58Encoder
from bip_utils.ecc import IPublicKey


class SolAddr:
    """ Solana address class. It allows the Solana address generation. """

    @staticmethod
    def EncodeKey(pub_key: Union[bytes, IPublicKey]) -> str:
        """ Get address in Solana format.

        Args:
            pub_key (bytes or IPublicKey): Public key bytes or object

        Returns:
            str: Address string

        Raises:
            ValueError: If the public key is not valid
            TypeError: If the public key is not ed25519
        """
        pub_key_obj = AddrUtils.ValidateAndGetEd25519Key(pub_key)

        return Base58Encoder.Encode(pub_key_obj.RawCompressed().ToBytes()[1:])

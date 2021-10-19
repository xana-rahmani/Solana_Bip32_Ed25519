from typing import Type, Union
from bip_utils.ecc import (IPublicKey, Ed25519PublicKey)
from bip_utils.ecc.ed25519 import Ed25519


class AddrUtils:
    """ Class container for address utility functions. """

    @staticmethod
    def ValidateAndGetEd25519Key(pub_key: Union[bytes, IPublicKey]) -> IPublicKey:
        """ Validate and get a ed25519 public key.

        Args:
            pub_key (bytes or IPublicKey object): Public key bytes or object

        Returns:
            IPublicKey object: IPublicKey object

        Raises:
            TypeError: If the public key is not ed25519
            ValueError: If the public key is not valid
        """
        return AddrUtils.__ValidateAndGetGenericKey(pub_key, Ed25519PublicKey)

    @staticmethod
    def __ValidateAndGetGenericKey(pub_key: Union[bytes, IPublicKey],
                                   pub_key_cls: Type[IPublicKey]) -> IPublicKey:
        """ Validate and get a generic public key.

        Args:
            pub_key (bytes or IPublicKey object): Public key bytes or object
            pub_key_cls (IPublicKey): Public key class type

        Returns:
            IPublicKey object: IPublicKey object

        Raises:
            TypeError: If the public key is not of the correct class type
            ValueError: If the public key is not valid
        """
        if isinstance(pub_key, bytes):
            pub_key = pub_key_cls.FromBytes(pub_key)
        elif not isinstance(pub_key, pub_key_cls):
            raise TypeError("A %s public key is required" % Ed25519.Name())

        return pub_key

from typing import Union
from bip_utils.bip32.bip32_base import Bip32Base
from bip_utils.bip32.bip32_key_data import Bip32KeyIndex
from bip_utils.conf import Bip44Solana
from bip_utils.ecc import EllipticCurveTypes, IPrivateKey


class Bip32Ed25519SlipConst:
    """ Class container for BIP32 ed25519 constants. """

    # Elliptic curve type
    CURVE_TYPE: EllipticCurveTypes = EllipticCurveTypes.ED25519

    # HMAC key for generating master key
    MASTER_KEY_HMAC_KEY: bytes = b"ed25519 seed"

    # Solana Key Net Version
    SolanaKeyNetVersion = Bip44Solana.KeyNetVersions()


class SolanaBip32Ed25519Slip(Bip32Base):
    """ BIP32 ed25519 class. It allows master key generation and children keys derivation using ed25519 curve.
    Derivation based on SLIP-0010.
    """

    #
    # Class methods for construction
    #

    @classmethod
    def FromSeed(cls, seed_bytes: bytes) -> Bip32Base:
        """ Create a Bip32 object from the specified seed (e.g. BIP39 seed).

        Args:
            seed_bytes (bytes)                           : Seed bytes

        Returns:
            Bip32Base object: Bip32Base object

        Raises:
            ValueError: If the seed is too short
            Bip32KeyError: If the seed is not suitable for master key generation
        """
        return cls._FromSeed(seed_bytes,
                             Bip32Ed25519SlipConst.MASTER_KEY_HMAC_KEY,
                             Bip32Ed25519SlipConst.SolanaKeyNetVersion,
                             Bip32Ed25519SlipConst.CURVE_TYPE)

    @classmethod
    def FromSeedAndPath(cls, seed_bytes: bytes, path: str) -> Bip32Base:
        """ Create a Bip32 object from the specified seed (e.g. BIP39 seed) and path.

        Args:
            seed_bytes (bytes)                           : Seed bytes
            path (str)                                   : Path

        Returns:
            Bip32Base object: Bip32Base object

        Raises:
            ValueError: If the seed length is too short
            Bip32KeyError: If the seed is not suitable for master key generation
        """
        return cls._FromSeedAndPath(seed_bytes,
                                    Bip32Ed25519SlipConst.MASTER_KEY_HMAC_KEY,
                                    path,
                                    Bip32Ed25519SlipConst.SolanaKeyNetVersion,
                                    Bip32Ed25519SlipConst.CURVE_TYPE)

    @classmethod
    def FromExtendedKey(cls, key_str: str) -> Bip32Base:
        """ Create a Bip32 object from the specified extended key.

        Args:
            key_str (str)                                : Extended key string

        Returns:
            Bip32Base object: Bip32Base object

        Raises:
            Bip32KeyError: If the key is not valid
        """
        return cls._FromExtendedKey(key_str,
                                    Bip32Ed25519SlipConst.SolanaKeyNetVersion,
                                    Bip32Ed25519SlipConst.CURVE_TYPE)

    @classmethod
    def FromPrivateKey(cls, priv_key: Union[bytes, IPrivateKey]) -> Bip32Base:
        """ Create a Bip32 object from the specified private key.
        The key will be considered a master key with the chain code set to zero,
        since there is no way to recover the key derivation data.

        Args:
            priv_key (bytes or IPrivateKey)              : Private key

        Returns:
            Bip32Base object: Bip32Base object

        Raises:
            Bip32KeyError: If the key is not valid
        """
        return cls._FromPrivateKey(priv_key,
                                   Bip32Ed25519SlipConst.SolanaKeyNetVersion,
                                   Bip32Ed25519SlipConst.CURVE_TYPE)

    @staticmethod
    def IsPublicDerivationSupported() -> bool:
        """ Get if public derivation is supported.

        Returns:
            bool: True if supported, false otherwise.
        """
        return False

    @staticmethod
    def IsPrivateUnhardenedDerivationSupported() -> bool:
        """ Get if private derivation with not-hardened indexes is supported.

        Returns:
            bool: True if supported, false otherwise.
        """
        return False

    #
    # Protected methods
    #

    @classmethod
    def _CkdPrivEd25519Slip(cls,
                            bip32_obj: Bip32Base,
                            index: Bip32KeyIndex) -> Bip32Base:
        """ Create a child key of the specified index using private derivation.
        It shall be implemented by children classes depending on the elliptic curve.

        Args:
            bip32_obj (Bip32Base object): Bip32Base object
            index (Bip32KeyIndex object): Key index

        Returns:
            Bip32Base object: Bip32Base object

        Raises:
            Bip32KeyError: If the index results in an invalid key
        """

        # Data for HMAC
        data = b"\x00" + bip32_obj.m_priv_key.Raw().ToBytes() + bytes(index)

        # Compute HMAC halves
        i_l, i_r = bip32_obj._HmacHalves(data)

        # Construct and return a new Bip32 object
        return cls(priv_key=i_l,
                   pub_key=None,
                   chain_code=i_r,
                   curve_type=bip32_obj.CurveType(),
                   depth=bip32_obj.Depth().Increase(),
                   index=index,
                   fprint=bip32_obj.m_pub_key.FingerPrint(),
                   key_net_ver=bip32_obj.KeyNetVersions())

    def _CkdPriv(self,
                 index: Bip32KeyIndex) -> Bip32Base:
        """ Create a child key of the specified index using private derivation.
        It shall be implemented by children classes depending on the elliptic curve.

        Args:
            index (Bip32KeyIndex object): Key index

        Returns:
            Bip32Base object: Bip32Base object

        Raises:
            Bip32KeyError: If the index results in an invalid key
        """
        return self._CkdPrivEd25519Slip(self, index)

    def _CkdPub(self, index: Bip32KeyIndex) -> Bip32Base:
        """ Create a child key of the specified index using public derivation.
        It shall be implemented by children classes depending on the elliptic curve.

        Args:
            index (Bip32KeyIndex object): Key index

        Returns:
            Bip32Base object: Bip32Base object

        Raises:
            Bip32KeyError: If the index results in an invalid key
        """

        # Not supported by Ed25519 SLIP-0010
        pass

from enum import Enum, auto, unique


@unique
class AddrTypes(Enum):
    """ Enumerative for address types. """

    SOL = auto()


@unique
class Bip32Types(Enum):
    """ Enumerative for BIP32 types. """

    ED25519_SLIP = auto()

from enum import Enum, auto, unique


@unique
class EllipticCurveTypes(Enum):
    """ Enumerative for elliptic curve types. """

    ED25519 = auto(),

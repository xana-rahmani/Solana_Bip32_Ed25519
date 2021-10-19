from bip_utils.utils import ConvUtils


class CoinNames:
    """ Helper class for representing coin names. """

    def __init__(self,
                 name: str,
                 abbr: str) -> None:
        """ Construct class.

        Args:
            name (str): Name
            abbr (str): Abbreviation
        """
        self.m_name = name
        self.m_abbr = abbr

    def Name(self) -> str:
        """ Get name.

        Returns :
            str: Name
        """
        return self.m_name

    def Abbreviation(self) -> str:
        """ Get abbreviation.

        Returns:
            str: Abbreviation
        """
        return self.m_abbr


class KeyNetVersions:
    """ Helper class for representing key net versions. """

    # Length
    LENGTH: int = 4

    def __init__(self,
                 pub_net_ver: bytes,
                 priv_net_ver: bytes) -> None:
        """ Construct class.

        Args:
            pub_net_ver (bytes) : Public net version
            priv_net_ver (bytes): Private net version
        """
        self.m_pub_net_ver = ConvUtils.HexStringToBytes(pub_net_ver)
        self.m_priv_net_ver = ConvUtils.HexStringToBytes(priv_net_ver)

    @staticmethod
    def Length() -> int:
        """ Get the key net version length.

        Returns:
            int: Key net version length
        """
        return KeyNetVersions.LENGTH

    def Public(self) -> bytes:
        """ Get public net version.

        Returns:
            bytes: Public net version
        """
        return self.m_pub_net_ver

    def Private(self) -> bytes:
        """ Get private net version.

        Returns:
            bytes: Private net version
        """
        return self.m_priv_net_ver

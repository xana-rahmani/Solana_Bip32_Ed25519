# BIP-0039 reference: https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki


from bip_utils.utils import ConvUtils, CryptoUtils


class Bip39SeedGeneratorConst:
    """ Class container for BIP39 seed generator constants. """

    # Salt modifier for seed generation
    SEED_SALT_MOD: str = "mnemonic"

    # PBKDF2 round for seed generation
    SEED_PBKDF2_ROUNDS: int = 2048

    # Seed length in bytes
    SEED_BYTE_LEN: int = 64


class Bip39SeedGenerator:
    """ BIP39 seed generator class. It generates the seed from a mnemonic in according to BIP39. """

    @staticmethod
    def Generate(mnemonic: str, passphrase: str = "") -> bytes:
        """ Generate the seed using the specified passphrase.

        Args:
            passphrase (str, optional): Passphrase, empty if not specified

        Returns:
            bytes: Generated seed
            :param mnemonic:
            :param passphrase:
        """

        # Get salt
        salt = ConvUtils.NormalizeNfkd(Bip39SeedGeneratorConst.SEED_SALT_MOD + passphrase)

        # Compute key
        key = CryptoUtils.Pbkdf2HmacSha512(mnemonic, salt, Bip39SeedGeneratorConst.SEED_PBKDF2_ROUNDS)

        del mnemonic, passphrase
        return key

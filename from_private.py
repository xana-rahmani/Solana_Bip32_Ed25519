import binascii
from bip_utils import SolanaBip32Ed25519Slip
from bip_utils.addr.solana_addr import SolAddr

priv_key = input('Enter Private Key: ')
priv_key_bytes = binascii.unhexlify(str.encode(priv_key))

bip32 = SolanaBip32Ed25519Slip.FromPrivateKey(priv_key=priv_key_bytes)
privateKey = bip32.PrivateKey().Raw()
publicKey = bip32.PublicKey().RawCompressed()
print("\tPrivateKey:", privateKey.ToHex())
print("\tPublicKey: ", publicKey.ToHex())
print("\tSecret: ", privateKey.ToHex() + publicKey.ToHex()[2:])
print("\tAddress:   ", SolAddr.EncodeKey(publicKey.ToBytes()))
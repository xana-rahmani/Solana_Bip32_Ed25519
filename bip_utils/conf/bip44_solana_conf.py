from bip_utils.conf.bip_solana_conf_enum import AddrTypes, Bip32Types
from bip_utils.conf.bip_solana_conf_helper import CoinNames, KeyNetVersions
from bip_utils.conf.bip_solana_conf import BipCoinConf

# Configuration for Solana
Bip44Solana: BipCoinConf = BipCoinConf(
    coin_name=CoinNames("Solana", "SOL"),
    is_testnet=False,
    def_path="0'",
    key_net_ver=KeyNetVersions(b"0488b21e", b"0488ade4"),
    wif_net_ver=None,
    bip32_type=Bip32Types.ED25519_SLIP,
    addr_conf={},
    addr_type=AddrTypes.SOL)

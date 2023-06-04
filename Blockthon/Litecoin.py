from .Utils import Wallet_, LTC, Ltc_Balance, Mnemonic_To_Bytes, Bytes_To_PrivateKey


def PrivateKey_To_LTC(privatekey: str, format='P2PKH'):
    """
    convert hex private key (string) to 4 type address for litecoin
    :param privatekey: Private Key Hex.
    :type privatekey: string.
    :param format: Address Type Format - 'P2PKH'  / 'P2WPKH' / 'P2SH' / 'P2WSH' .
    :type format: string

    :returns: string address.

    >>> from Blockthon.Litecoin import PrivateKey_To_LTC
    >>> import os
    >>> key = os.urandom(32).hex()
    >>> p2pkh = PrivateKey_To_LTC(key, 'P2PKH')
    >>> p2sh = PrivateKey_To_LTC(key, 'P2SH')
    >>> p2wpkh = PrivateKey_To_LTC(key, 'P2WPKH')
    >>> p2wsh = PrivateKey_To_LTC(key, 'P2WSH')
    """
    ltc: Wallet_ = Wallet_(LTC)
    ltc.from_private_key(privatekey)
    if format == 'P2PKH':
        return ltc.p2pkh_address()
    elif format == 'P2SH':
        return ltc.p2sh_address()
    elif format == 'P2WSH':
        return ltc.p2wsh_address()
    elif format == 'P2WPKH':
        return ltc.p2wpkh_address()
    else:
        return ltc.p2pkh_address()


def Mnemonic_To_LTC(mnemonicwords):
    seed = Mnemonic_To_Bytes(mnemonicwords)
    key = Bytes_To_PrivateKey(seed)
    ltc: Wallet_ = Wallet_(LTC)
    ltc.from_private_key(key)
    return ltc.p2pkh_address()


def Balance_LTC(addr): return Ltc_Balance(addr)

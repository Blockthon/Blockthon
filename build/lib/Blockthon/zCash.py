from .Utils import Wallet_, ZEC, Zec_Balance, Mnemonic_To_Bytes, Bytes_To_PrivateKey


def PrivateKey_To_ZEC(privatekey: str, format='P2PKH'):
    """
    convert hex private key (string) to 1 type address for zcash
    :param privatekey: Private Key Hex.
    :return: address.

    >>> from Blockthon.zCash import PrivateKey_To_ZEC
    >>> import os
    >>> key = os.urandom(32).hex()
    >>> address = PrivateKey_To_ZEC(key)
    """
    zec: Wallet_ = Wallet_(ZEC)
    zec.from_private_key(privatekey)
    return zec.p2pkh_address()


def Mnemonic_To_ZEC(mnemonicwords):
    seed = Mnemonic_To_Bytes(mnemonicwords)
    key = Bytes_To_PrivateKey(seed)
    zec: Wallet_ = Wallet_(ZEC)
    zec.from_private_key(key)
    return zec.p2pkh_address()


def Balance_ZEC(addr): return Zec_Balance(addr)
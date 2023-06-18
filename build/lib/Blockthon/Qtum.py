from .Utils import Wallet_, QTUM, Qtum_Balance, Mnemonic_To_Bytes, Bytes_To_PrivateKey


def PrivateKey_To_QTUM(privatekey: str):
    """
    convert hex private key (string) to 1 type address for qtum
    :param privatekey: Private Key Hex.
    :type privatekey: string.

    :returns: string address.

    >>> from Blockthon.Qtum import PrivateKey_To_QTUM
    >>> import os
    >>> key = os.urandom(32).hex()
    >>> p2pkh = PrivateKey_To_QTUM(key)
    """
    qtum: Wallet_ = Wallet_(QTUM)
    qtum.from_private_key(privatekey)
    return qtum.p2pkh_address()


def Mnemonic_To_QTUM(mnemonicwords):
    seed = Mnemonic_To_Bytes(mnemonicwords)
    key = Bytes_To_PrivateKey(seed)
    qtum: Wallet_ = Wallet_(QTUM)
    qtum.from_private_key(key)
    return qtum.p2pkh_address()


def Balance_QTUM(addr): return Qtum_Balance(addr)
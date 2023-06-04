from .Utils import Wallet_, RVN, Rvn_Balance, Mnemonic_To_Bytes, Bytes_To_PrivateKey


def PrivateKey_To_RVN(privatekey: str):
    """
    convert hex private key (string) to 1 type address for rvn
    :param privatekey: Private Key Hex.
    :type privatekey: string.

    :returns: string address.

    >>> from Blockthon.Ravencoin import PrivateKey_To_RVN
    >>> import os
    >>> key = os.urandom(32).hex()
    >>> p2pkh = PrivateKey_To_RVN(key)
    """
    rvn: Wallet_ = Wallet_(RVN)
    rvn.from_private_key(privatekey)
    return rvn.p2pkh_address()


def Mnemonic_To_RVN(mnemonicwords):
    seed = Mnemonic_To_Bytes(mnemonicwords)
    key = Bytes_To_PrivateKey(seed)
    rvn: Wallet_ = Wallet_(RVN)
    rvn.from_private_key(key)
    return rvn.p2pkh_address()


def Balance_RVN(addr): return Rvn_Balance(addr)
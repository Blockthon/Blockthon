from .Utils import Wallet_, DGB, Dgb_Balance, Mnemonic_To_Bytes, Bytes_To_PrivateKey


def PrivateKey_To_DGB(privatekey: str, format='P2PKH'):
    """
    convert hex private key (string) to 1 type address for digibyte
    :param privatekey: Private Key Hex.
    :type privatekey: string.
    :param format: Address Type Format - 'P2PKH' .
    :type format: string

    :returns: string address.

    >>> from Blockthon.DigiByte import PrivateKey_To_DGB
    >>> import os
    >>> key = os.urandom(32).hex()
    >>> p2pkh = PrivateKey_To_DGB(key, 'P2PKH')
    """
    dgb: Wallet_ = Wallet_(DGB)
    dgb.from_private_key(privatekey)
    if format == 'P2PKH':
        return dgb.p2pkh_address()
    else:
        return dgb.p2pkh_address()


def Mnemonic_To_DGB(mnemonicwords):
    seed = Mnemonic_To_Bytes(mnemonicwords)
    key = Bytes_To_PrivateKey(seed)
    dgb: Wallet_ = Wallet_(DGB)
    dgb.from_private_key(key)
    return dgb.p2pkh_address()


def Balance_DGB(addr): return Dgb_Balance(addr)
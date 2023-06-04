from .Utils import Wallet_, BTG, Btg_Balance, Mnemonic_To_Bytes, Bytes_To_PrivateKey


def PrivateKey_To_BTG(privatekey: str, format='P2PKH'):
    """
    convert hex private key (string) to 2 type address for bitcoin gold
    :param privatekey: Private Key Hex.
    :type privatekey: string.
    :param format: Address Type Format - 'P2PKH'  / 'P2SH' .
    :type format: string

    :returns: string address.

    >>> from Blockthon.BitcoinGold import PrivateKey_To_BTG
    >>> import os
    >>> key = os.urandom(32).hex()
    >>> p2pkh = PrivateKey_To_BTG(key, 'P2PKH')
    >>> p2sh = PrivateKey_To_BTG(key, 'P2SH')
    """
    btg: Wallet_ = Wallet_(BTG)
    btg.from_private_key(privatekey)
    if format == 'P2PKH':
        return btg.p2pkh_address()
    elif format == 'P2SH':
        return btg.p2sh_address()
    else:
        return btg.p2pkh_address()


def Mnemonic_To_BTG(mnemonicwords):
    seed = Mnemonic_To_Bytes(mnemonicwords)
    key = Bytes_To_PrivateKey(seed)
    btg: Wallet_ = Wallet_(BTG)
    btg.from_private_key(key)
    return btg.p2pkh_address()


def Balance_BTG(addr): return Btg_Balance(addr)
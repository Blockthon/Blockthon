from .Utils import Wallet_, DASH, Dash_Balance, Mnemonic_To_Bytes, Bytes_To_PrivateKey


def PrivateKey_To_DASH(privatekey: str, format='P2PKH'):
    """
    convert hex private key (string) to 1 type address for dash
    :param privatekey: Private Key Hex.
    :type privatekey: string.
    :param format: Address Type Format - 'P2PKH' .
    :type format: string

    :returns: string address.

    >>> from Blockthon.Dash import PrivateKey_To_DASH
    >>> import os
    >>> key = os.urandom(32).hex()
    >>> p2pkh = PrivateKey_To_DASH(key, 'P2PKH')
    """
    dash: Wallet_ = Wallet_(DASH)
    dash.from_private_key(privatekey)
    if format == 'P2PKH':
        return dash.p2pkh_address()
    else:
        return dash.p2pkh_address()


def Mnemonic_To_DASH(mnemonicwords):
    seed = Mnemonic_To_Bytes(mnemonicwords)
    key = Bytes_To_PrivateKey(seed)
    dash: Wallet_ = Wallet_(DASH)
    dash.from_private_key(key)
    return dash.p2pkh_address()


def Balance_DASH(addr): return Dash_Balance(addr)
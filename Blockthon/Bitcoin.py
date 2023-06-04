from .Utils import (
    PrivateKey_To_Addr,
    PrivateKey_To_Mnemonics,
    PrivateKey_From_Passphrase as Word_To_Hex,
    PrivateKey_From_Dec,
    Btc_Balance,
    BTC,
    Wallet_,

)


def PrivateKey_To_CompressAddr(privatekey): return PrivateKey_To_Addr(privatekey, True)


def PrivateKey_To_UnCompressAddr(privatekey): return PrivateKey_To_Addr(privatekey, False)


def PrivateKey_To_Address(privatekey, Type='P2PKH'):
    """
    >>> from Blockthon.Bitcoin import PrivateKey_To_Addr
    >>> import os
    >>> # Generate Random Private Key Hex
    >>> key = os.urandom(32).hex()
    >>> # Convert Private Key HEX To Compress Address
    >>> compress_Address = PrivateKey_To_Addr(key, 'compress')
    >>> # Convert Private Key HEX To Un Compress Address
    >>> uncompress_Address = PrivateKey_To_Addr(key, 'uncompress')
    >>> # Convert Private Key HEX To P2PKH Address Type
    >>> p2pkh_Address = PrivateKey_To_Addr(key, 'P2PKH')
    >>> # Convert Private Key HEX To P2SH Address Type
    >>> p2sh_Address = PrivateKey_To_Addr(key, 'P2SH')
    >>> # Convert Private Key HEX To P2WPKH Address Type
    >>> p2wpkh_Address = PrivateKey_To_Addr(key, 'P2WPKH')
    >>> # Convert Private Key HEX To P2WSH Address Type
    >>> p2wsh_Address = PrivateKey_To_Addr(key, 'P2WSH')
    >>> # Convert Private Key HEX To P2WPKH in P2SH Address Type
    >>> p2wpkhinp2sh_Address = PrivateKey_To_Addr(key, 'P2WPKHinP2SH')
    >>> # Convert Private Key HEX To P2WSH in P2SH Address Type
    >>> p2wshinp2sh_Address = PrivateKey_To_Addr(key, 'P2WSHinP2SH')

    :param privatekey: string
    :param Type: ('compress' / 'uncompress' / 'P2PKH' / 'P2SH' / 'P2WSH' / 'P2WPKH' / 'P2WSHinP2SH' / 'P2WPKHinP2SH' )
    :return: address (string)

    """
    btc: Wallet_ = Wallet_(BTC)
    btc.from_private_key(privatekey)
    if Type == 'compress':
        return PrivateKey_To_CompressAddr(privatekey)
    elif Type == 'uncompress':
        return PrivateKey_To_UnCompressAddr(privatekey)
    elif Type == 'P2PKH':
        return btc.p2pkh_address()
    elif Type == 'P2SH':
        return btc.p2sh_address()
    elif Type == 'P2WPKH':
        return btc.p2wpkh_address()
    elif Type == 'P2WSH':
        return btc.p2wsh_address()
    elif Type == 'P2WPKHinP2SH':
        return btc.p2wpkh_in_p2sh_address()
    elif Type == 'P2WSHinP2SH':
        return btc.p2wsh_in_p2sh_address()
    else:
        return btc.p2pkh_address()


# Convert Number (Dec) [integer|int] To Private Key HEX return privatekey (string)[HEX]
def PrivateKey_From_Number(number): return PrivateKey_From_Dec(number)


# Convert Private Key HEX To Mnemonic Word's and return mnemonic string
def PrivateKey_To_Mnemonic(privatekey): return PrivateKey_To_Mnemonics(privatekey)


# convert Private Key HEX To Word Character and Return word string
def PrivateKey_From_Passphrase(passphrase): return Word_To_Hex(passphrase)


# Send Request For Per Address Balance and Return Value Balance [string]
def Balance_BTC(address): return Btc_Balance(address)

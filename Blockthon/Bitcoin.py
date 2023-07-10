from .Utils import HexToBTC
from .lib import Hexlify, MnemonicToBytes, DecToBytes


def Address_From_PrivateKey(privatekey: str, Type: str) -> str:
    """
    Convert Private Key (Hex) To All Type's Bitcoin Address.

    >>> # Example Address With a Type's: 'P2PKH'/'P2SH'/'P2WPKH'/'P2WSH'/'P2WPKHinP2SH'/ 'P2WSHinP2SH'
    >>> P2PKH = Address_From_PrivateKey(privatekey, Type='P2PKH')
    >>> P2SH = Address_From_PrivateKey(privatekey, Type='P2SH')
    >>> P2WPKH = Address_From_PrivateKey(privatekey, Type='P2WPKH')
    >>> P2WSH = Address_From_PrivateKey(privatekey, Type='P2WSH')
    >>> P2WPKH_Segwit = Address_From_PrivateKey(privatekey, Type='P2WPKHinP2SH')
    >>> P2WSH_Segwit = Address_From_PrivateKey(privatekey, Type='P2WSHinP2SH')

    :return: BitcoinAddress_string.
    """
    if Type == 'P2PKH':
        return HexToBTC(privatekey, 'P2PKH')
    elif Type == 'P2SH':
        return HexToBTC(privatekey, 'P2SH')
    elif Type == 'P2WSH':
        return HexToBTC(privatekey, 'P2WSH')
    elif Type == 'P2WPKH':
        return HexToBTC(privatekey, 'P2WPKH')
    elif Type == 'P2WPKHinP2SH':
        return HexToBTC(privatekey, 'P2WPKHinP2SH')
    elif Type == 'P2WSHinP2SH':
        return HexToBTC(privatekey, 'P2WSHinP2SH')
    else:
        return HexToBTC(privatekey, 'P2PKH')


def Address_From_Bytes(byte: bytes) -> str: return Address_From_PrivateKey(Hexlify(byte))


def Address_From_Mnemonic(mnemonics: str) -> str: return Address_From_Bytes(MnemonicToBytes(mnemonics))


def Address_From_Dec(dec: int) -> str: return Address_From_Bytes(DecToBytes(dec))


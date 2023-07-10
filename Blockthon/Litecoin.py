from .Utils import HexToLTC
from .lib import Hexlify, MnemonicToBytes, DecToBytes


def Address_From_PrivateKey(privatekey: str, Type: str) -> str:
    """
    Convert Private Key (Hex) To All Type's Litecoin Address.

    >>> # Example Address With Type's: 'P2PKH'/'P2SH'/'P2WPKH'/'P2WSH'
    >>> P2PKH_Litecoin = Address_From_PrivateKey(privatekey, Type='P2PKH')
    >>> P2SH_Litecoin = Address_From_PrivateKey(privatekey, Type='P2SH')
    >>> P2WPKH_Litecoin = Address_From_PrivateKey(privatekey, Type='P2WPKH')
    >>> P2WSH_Litecoin = Address_From_PrivateKey(privatekey, Type='P2WSH')

    :return: LitecoinAddress_string.
    """
    if Type == 'P2PKH':
        return HexToLTC(privatekey, 'P2PKH')
    elif Type == 'P2SH':
        return HexToLTC(privatekey, 'P2SH')
    elif Type == 'P2WSH':
        return HexToLTC(privatekey, 'P2WSH')
    elif Type == 'P2WPKH':
        return HexToLTC(privatekey, 'P2WPKH')
    else:
        return HexToLTC(privatekey, 'P2PKH')


def Address_From_Bytes(byte: bytes) -> str: return Address_From_PrivateKey(Hexlify(byte))


def Address_From_Mnemonic(mnemonics: str) -> str: return Address_From_Bytes(MnemonicToBytes(mnemonics))


def Address_From_Dec(dec: int) -> str: return Address_From_Bytes(DecToBytes(dec))


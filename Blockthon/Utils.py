from hdwallet import HDWallet as HD
from hdwallet.symbols import (BTC, ETH, DOGE, DASH, TRX, LTC,
                              BTG, DGB, RVN, QTUM, ZEC)


def HexToBTG(hexed: str) -> str:
    hd: HD = HD(symbol=BTG)
    hd.from_private_key(private_key=hexed)
    return hd.p2pkh_address()


def HexToETH(hexed: str) -> str:
    hd: HD = HD(symbol=ETH)
    hd.from_private_key(private_key=hexed)
    return hd.p2pkh_address()


def HexToTRX(hexed: str) -> str:
    hd: HD = HD(symbol=TRX)
    hd.from_private_key(private_key=hexed)
    return hd.p2pkh_address()


def HexToDOGE(hexed: str) -> str:
    hd: HD = HD(symbol=DOGE)
    hd.from_private_key(private_key=hexed)
    return hd.p2pkh_address()


def HexToDASH(hexed: str) -> str:
    hd: HD = HD(symbol=DASH)
    hd.from_private_key(private_key=hexed)
    return hd.p2pkh_address()


def HexToDGB(hexed: str) -> str:
    hd: HD = HD(symbol=DGB)
    hd.from_private_key(private_key=hexed)
    return hd.p2pkh_address()


def HexToRVN(hexed: str) -> str:
    hd: HD = HD(symbol=RVN)
    hd.from_private_key(private_key=hexed)
    return hd.p2pkh_address()


def HexToQTUM(hexed: str) -> str:
    hd: HD = HD(symbol=QTUM)
    hd.from_private_key(private_key=hexed)
    return hd.p2pkh_address()


def HexToZEC(hexed: str) -> str:
    hd: HD = HD(symbol=ZEC)
    hd.from_private_key(private_key=hexed)
    return hd.p2pkh_address()


def HexToLTC(hexed: str, Type: str) -> str:
    """
        convert hex string to all address litecoin types with any format

        >>> p2pkh_address = HexToLTC(hexed, 'P2PKH')
        >>> p2sh_address = HexToLTC(hexed, 'P2SH')
        >>> p2wpkh_address = HexToLTC(hexed, 'P2WPKH')
        >>> p2wsh_address = HexToLTC(hexed, 'P2WSH')

        :param hexed:
        :param Type:
        :return: address.
        """
    hd: HD = HD(symbol=LTC)
    hd.from_private_key(hexed)
    if Type == 'P2PKH' or Type == 'p2pkh':
        return hd.p2pkh_address()
    elif Type == 'P2SH' or Type == 'p2sh':
        return hd.p2sh_address()
    elif Type == 'P2WPKH' or Type == 'p2wpkh':
        return hd.p2wpkh_address()
    elif Type == 'P2WSH' or Type == 'p2wsh':
        return hd.p2wsh_address()
    else:
        return hd.p2pkh_address()


def HexToBTC(hexed: str, Type: str) -> str:
    """
    convert hex string to all address bitcoin types with any format

    >>> p2pkh_address = HexToBTC(hexed, 'P2PKH')
    >>> p2sh_address = HexToBTC(hexed, 'P2SH')
    >>> p2wpkh_address = HexToBTC(hexed, 'P2WPKH')
    >>> p2wsh_address = HexToBTC(hexed, 'P2WSH')

    :param hexed:
    :param Type:
    :return: address.
    """
    hd: HD = HD(symbol=BTC)
    hd.from_private_key(hexed)
    if Type == 'P2PKH' or Type == 'p2pkh':
        return hd.p2pkh_address()
    elif Type == 'P2SH' or Type == 'p2sh':
        return hd.p2sh_address()
    elif Type == 'P2WPKH' or Type == 'p2wpkh':
        return hd.p2wpkh_address()
    elif Type == 'P2WSH' or Type == 'p2wsh':
        return hd.p2wsh_address()
    elif Type == 'P2WSHinP2SH' or Type == 'p2wshinp2sh':
        return hd.p2wsh_in_p2sh_address()
    elif Type == 'P2WPKHinP2SH' or Type == 'p2wpkhinp2sh':
        return hd.p2wpkh_in_p2sh_address()
    else:
        return hd.p2pkh_address()
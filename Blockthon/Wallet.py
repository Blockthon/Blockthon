# Blockthon/Wallet.py
# Programmer and Owner: Mmdrza.Com
# More Detail's: https://blockthon.github.io/Blockthon
# Email: PyMmdrza@Gmail.Com
# -----------------------------------------
from .lib import (
    Hexlify, unHexlify, PVK, SH256, DecToBytes,
    DecToHex, HexToBin, HexToMne, BytesToHex, AddrToH160,
    BytesToPub, BytesToAddr, BytesToWif, BytesToMnemonic,
    BytesToDec, BytsToRIPEMD160, getBytes, getBin, getMnemonic,
    MnemonicToBytes, MnemToRoot, WifAddr, WifToBytes, BinToHex)
from .Utils import HexToBTC


# *-------------------------------------------------------------------* #

def getPrivateKey() -> str:
    """ Generated Random Private Key HEX Without Repeat. """
    return PVK()


# *-------------------------------------------------------------------* #

def getMnemonics(size: int = 12) -> str:
    """ Generate Random Mnemonic Without Repeat, with Any Size 12, 18, 24. """
    return getMnemonic(size)


# *-------------------------------------------------------------------* #

def getSeed() -> bytes:
    """ Generated Random Bytes (seed) Without repeat. """
    return getBytes()


# *-------------------------------------------------------------------* #

def getBinary(size: int = 256) -> str:
    """ Generated Random Binary Without repeat and return Number's To String """
    return getBin(size)


# *-------------------------------------------------------------------* #

def PrivateKey_To_Binary(privatekey: str) -> bin:
    """ Convert Private key Hex To Binary [return: bin] """
    return HexToBin(privatekey)


# *-------------------------------------------------------------------* #

def PrivateKey_To_Bytes(privatekey: str) -> bytes:
    """ Convert Private Key (Hex) To Seed (Bytes) Return Bytes. """
    return unHexlify(privatekey)


# *-------------------------------------------------------------------* #

def PrivateKey_To_Dec(privatekey: str) -> int:
    """ Convert Private Key (Hex) To Decimal Number [Return: int] """
    return int(privatekey, 16)


# *-------------------------------------------------------------------* #

def PrivateKey_To_INT(privatekey: str) -> int:
    """ Convert Private Key (Hex) To Decimal Number [Return: int] """
    return int(privatekey, 16)


# *-------------------------------------------------------------------* #

def PrivateKey_To_Mnemonic(privatekey: str, size: int) -> str:
    """ Convert Private Key (Hex) To Mnemonic [Return: str] """
    if size == 12 or size == 18 or size == 24:
        return HexToMne(privatekey, size)
    else:
        return f"To create a mnemonic, you need to enter the size (number) of words"


# *-------------------------------------------------------------------* #

def PrivateKey_To_RIPEMD160(privatekey: str) -> str:
    """ Convert Private Key (Hex) To RIPEMD160 [Return: Hex String]"""
    seed = unHexlify(privatekey)
    return Bytes_To_RIPEMD160(seed)


# *-------------------------------------------------------------------* #

def PrivateKey_To_Address(privatekey: str, compress: bool = False) -> str:
    """ Convert Private Key (HEX) To Compress and UnCompress Address. """
    seed = unHexlify(privatekey)
    if compress:
        return BytesToAddr(seed, compress=True)
    else:
        return BytesToAddr(seed, compress=False)


# *-------------------------------------------------------------------* #

def PrivateKey_To_Compress_Addr(privatekey: str) -> str:
    """ Convert Private Key (HEX) To Compressed Bitcoin Address """
    return PrivateKey_To_Address(privatekey, compress=True)


# *-------------------------------------------------------------------* #

def PrivateKey_To_UnCompress_Addr(privatekey: str) -> str:
    """ Convert Private Key (HEX) To UnCompressed Bitcoin Address """
    return PrivateKey_To_Address(privatekey, compress=False)


# *-------------------------------------------------------------------* #

def PrivateKey_To_PublicKey(privatekey: str, compress: bool = False) -> str:
    """ Convert Private Key To PublicKey """
    seed = unHexlify(privatekey)
    if compress:
        return BytesToPub(seed, compress=True)
    else:
        return BytesToPub(seed, compress=False)


# *-------------------------------------------------------------------* #

def PrivateKey_P2PKH_Addr(privatekey: str) -> str:
    """ Convert Private Key HEX To `P2PKH` Bitcoin Address."""
    return HexToBTC(privatekey, Type='P2PKH')


# *-------------------------------------------------------------------* #

def PrivateKey_P2SH_Addr(privatekey: str) -> str:
    """ Convert Private Key HEX To `P2SH` Bitcoin Address. """
    return HexToBTC(privatekey, Type='P2SH')


# *-------------------------------------------------------------------* #

def PrivateKey_P2WPKH_Addr(privatekey: str) -> str:
    """ Convert Private Key HEX To `P2WPKH` Bitcoin Address. """
    return HexToBTC(privatekey, Type='P2WPKH')


# *-------------------------------------------------------------------* #

def PrivateKey_P2WSH_Addr(privatekey: str) -> str:
    """ Convert Private Key HEX To `P2WSH` Bitcoin Address."""
    return HexToBTC(privatekey, Type='P2WSH')


# *-------------------------------------------------------------------* #

def PrivateKey_P2WPKH_Segwit(privatekey: str) -> str:
    """ Convert Private Key HEX To `P2WPKH in Segwit` Bitcoin Address."""
    return HexToBTC(privatekey, Type='P2WPKHinP2SH')


# *-------------------------------------------------------------------* #

def PrivateKey_P2WSH_Segwit(privatekey: str) -> str:
    """ Convert Private Key HEX To `P2WSH in Segwit` Bitcoin Address. """
    return HexToBTC(privatekey, Type='P2WSHinP2SH')


# *-------------------------------------------------------------------* #

def Address_To_RIPEMD160(address_string: str) -> str:
    """ Convert String Address To RIPEMD160 (HASH160) """
    return AddrToH160(address_string)


# *-------------------------------------------------------------------* #

def Bytes_To_PrivateKey(byte: bytes) -> str:
    """ Convert Bytes To Hex (Private Key). """
    return Hexlify(byte)


# *-------------------------------------------------------------------* #

def Bytes_To_Address(byte: bytes, compress: bool = False) -> str:
    """ Convert Bytes To Compress and UnCompress Address, For compress Address on param after bytes enter `compress=True` and for uncompress Address `compress=False` or without compress."""
    if compress:
        return BytesToAddr(byte, compress=True)
    else:
        return BytesToAddr(byte, compress=False)


# *-------------------------------------------------------------------* #
def Bytes_To_RIPEMD160(byte: bytes) -> str:
    """ Convert Bytes (seed) To RIPEMD160 and Return: string """
    return Hexlify(BytsToRIPEMD160(byte))


# *-------------------------------------------------------------------* #

def Bytes_To_Mnemonic(byte: bytes, size: int = 12) -> str:
    """ Convert Bytes To Mnemonic with Size Mnemonic, [size=12, 18, 24]. """
    return BytesToMnemonic(byte, size)


# *-------------------------------------------------------------------* #

def Bytes_To_Dec(byte: bytes) -> int:
    """ Convert Bytes To Number Decimal and Return:[integer]. """
    return BytesToDec(byte)


# *-------------------------------------------------------------------* #

def Bytes_To_Wif(byte: bytes, compress: bool = False) -> str:
    """ Convert Bytes To WIF Compress and UnCompress Wif [byte, compress=False/True] """
    if compress:
        return BytesToWif(byte, compress=True)
    else:
        return BytesToWif(byte, compress=False)


# *-------------------------------------------------------------------* #

def Bytes_To_PublicKey(byte: bytes, compress: bool = False) -> str:
    """ Convert Bytes To Compress PublicKey and UnCompress PublicKey. """
    if compress:
        return BytesToPub(byte, compress=True)
    else:
        return BytesToPub(byte, compress=False)


# *-------------------------------------------------------------------* #

def Wif_To_PublicKey(wif: str, compress: bool = False) -> str:
    """ Convert Wif To Public Key Compress and UnCompress. """
    bytesWif = WifToBytes(wif)
    if compress:
        return BytesToPub(bytesWif, compress=True)
    else:
        return BytesToPub(bytesWif, compress=False)


# *-------------------------------------------------------------------* #

def Wif_To_Bytes(wif):
    """ Convert WIF To Bytes (seed) """
    return WifToBytes(wif)


# *-------------------------------------------------------------------* #
def Wif_To_RIPEMD160(wif: str) -> str:
    """ Convert WIF To RIPEMD160 """
    wif_byte = WifToBytes(wif)
    return Bytes_To_RIPEMD160(wif_byte)


# *-------------------------------------------------------------------* #

def Wif_To_PrivateKey(wif: str) -> str:
    """ Convert WIF To Private Key (Hex), """
    return BytesToHex(WifToBytes(wif))


# *-------------------------------------------------------------------* #

def Wif_To_Mnemonic(wif: str, size=12) -> str:
    """ Convert WIF To Mnemonic Word's with size: 12, 18, 24 [default: 12] """
    byte_w = WifToBytes(wif)
    return BytesToMnemonic(byte_w[:-1], size)


# *-------------------------------------------------------------------* #

def Wif_To_Address(wif: str) -> str:
    """ Convert Wif To Address - WIF Compress To Compress Address and UnCompress Wif To Address UnCompress """
    return WifAddr(wif)


# *-------------------------------------------------------------------* #

def Mnemonic_To_RootKey(mnemonics: str) -> str:
    """ Convert Mnemonic String Word's TO Root Key (XPRV) """
    return MnemToRoot(mnemonics)


# *-------------------------------------------------------------------* #

def Mnemonic_To_Bytes(mnemonics: str) -> bytes:
    """ Convert Mnemonic To Bytes (seed) """
    return MnemonicToBytes(mnemonics)


# *-------------------------------------------------------------------* #

def Mnemonic_To_Wif(mnemonics: str, compress: bool = False) -> str:
    """ Convert Mnemonic Word's To WIF Compress or UnCompress [compress=False/True] """
    seed = MnemonicToBytes(mnemonics)
    if compress:
        return BytesToWif(seed, compress=True)
    else:
        return BytesToWif(seed, compress=False)


# *-------------------------------------------------------------------* #

def Mnemonic_To_PrivateKey(mnemonics: str) -> str:
    """ Convert Mnemonic To Private Key (Hex) """
    seed = MnemonicToBytes(mnemonics)
    return Hexlify(seed)


# *-------------------------------------------------------------------* #

def Mnemonic_To_PublicKey(mnemonics: str, compress: bool = False) -> str:
    """ Convert Mnemonic To Public Key. """
    mneBytes = MnemonicToBytes(mnemonics)
    if compress:
        return BytesToPub(mneBytes, compress=True)
    else:
        return BytesToAddr(mneBytes, compress=False)


# *-------------------------------------------------------------------* #

def Mnemonic_To_Address(mnemonics: str, compress: bool = False) -> str:
    """ Convert Mnemonic To Compress Address And UnCompress Address (compress=False/True) """
    seedByte = MnemonicToBytes(mnemonics)
    if compress:
        return BytesToAddr(seedByte, compress=True)
    else:
        return BytesToAddr(seedByte, compress=False)


# *-------------------------------------------------------------------* #

def Mnemonic_To_RIPEMD160(mnemonics: str) -> str:
    """ Convert Mnemonic To RIPEMD160 """
    mneByte = MnemonicToBytes(mnemonics)
    return Bytes_To_RIPEMD160(mneByte)


# *-------------------------------------------------------------------* #

def Binary_To_PrivateKey(bin_string: str) -> str:
    """ Convert Binary String To Private Key (hex) [return: string] """
    return BinToHex(bin_string)


# *-------------------------------------------------------------------* #

def Dec_To_PrivateKey(dec: int) -> str:
    """ Convert Decimal Number To Hex (Private Key) """
    return DecToHex(dec)


# *-------------------------------------------------------------------* #

def Dec_To_Bytes(dec: int) -> bytes:
    """ Convert Decimal Number To Bytes """
    return DecToBytes(dec)


# *-------------------------------------------------------------------* #

def Passphrase_To_PrivateKey(passphrase: str) -> str:
    """ Convert Passphrase To HEX Private Key. """
    return SH256(passphrase.encode('utf-8')).hexdigest()


# *-------------------------------------------------------------------* #

def Passphrase_To_Bytes(passphrase: str) -> bytes:
    """ Convert Passphrase To Bytes Seed """
    return unHexlify(Passphrase_To_PrivateKey(passphrase))


# *-------------------------------------------------------------------* #

def Passphrase_To_Wif(passphrase: str) -> str:
    """ Convert Passphrase To Wif """
    return BytesToWif(Passphrase_To_Bytes(passphrase))


# *-------------------------------------------------------------------* #

def Passphrase_To_Address(passphrase: str, compress: bool = False) -> str:
    """ Convert Passphrase To Compress Or UnCompress Address (compress=False/True) """
    byte = Passphrase_To_Bytes(passphrase)
    if compress:
        return BytesToAddr(byte, compress=True)
    else:
        return BytesToAddr(byte, compress=False)


# *-------------------------------------------------------------------* #

def Passphrase_To_Dec(passphrase: str) -> int:
    """ Convert Passphrase To Decimal Number [Return: integer number] """
    byte = Passphrase_To_Bytes(passphrase)
    return Bytes_To_Dec(byte)

# *-------------------------------------------------------------------* #

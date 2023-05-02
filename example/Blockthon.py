# //////////////////////////////////////////////////
# // Github : github.com/Pymmdrza                 //
# // official Page : https://github.com/Blockthon //
# //////////////////////////////////////////////////

import codecs
from os import urandom
from bit import Key
from bit.format import bytes_to_wif
from binascii import hexlify
from mnemonic import Mnemonic
from codecs import decode as Decode
import requests, json


def PrivateKey():
    return urandom(32).hex()


def PrivateKey_To_Dec(private_key):
    """ Convert Hex to Integer Return int [dec] """
    return int(private_key, 16)


# Convert Private Key (HEX) To Bytes
def PrivateKey_To_Bytes(private_key):
    """ Convert Hex to Bytes and Return binary [byte] """
    return Decode(private_key, 'hex')


# Convert Bytes (SEED) To Mnemonic
def Bytes_To_Mnemonic(Byte_String):
    """ Convert Bytes to Mnemonic Word with 256 bit Size and Return str [mnemonic] """
    return Mnemonic('english').to_mnemonic(Byte_String)


# Convert Bytes (Seed) To HEX (Private Key)
def Bytes_To_PrivateKey(Byte_String):
    """ convert bytes to hex for private key and return str [private_key] """
    return hexlify(Byte_String).decode('utf-8')


# Convert Private Key (HEX) To Mnemonic
def PrivateKey_To_Mnemonic(private_key):
    """Convert HEX To Bytes , after converting , convert to Mnemonic (WORD)
    PrivateKey: str --> Byte: Binary --> Mnemonic(Word): str"""
    Byte_String: str = PrivateKey_To_Bytes(private_key)
    return Mnemonic('english').to_mnemonic(Byte_String)


# Convert Byte To WIF Compressed and Un Compressed
def Bytes_To_WIF(Bytes_, compressed=False):
    """ convert bytes to wif and after compressed and uncompressed address """
    if compressed:
        wif = bytes_to_wif(Bytes_, compressed=True)
    else:
        wif = bytes_to_wif(Bytes_)
    return wif


# compressed and un compressed address from private key hex
def Addr_From_PrivateKey(private_key, compress=False):
    """ convert hex private key to compressed address and un compressed : return [str] """
    seed = codecs.decode(private_key, 'hex')
    if compress:
        _wc = bytes_to_wif(seed, compressed=True)
        bits = Key(_wc)
        return bits.address
    else:
        _wu = bytes_to_wif(seed, compressed=False)
        bitu = Key(_wu)
        return bitu.address


# Check Value Address Balance
def Balance(address):
    """check balance of value per address and return : str [balance]"""
    req = requests.get(f"https://bitcoin.atomicwallet.io/api/v2/address/{address}").json()
    return dict(req)['balance']

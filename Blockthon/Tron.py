from .Utils import Wallet_, TRX, Trx_Balance, Mnemonic_To_Bytes, Bytes_To_PrivateKey

def PrivateKey_To_TRX(privatekey):
    trx: Wallet_ = Wallet_(TRX)
    trx.from_private_key(privatekey)
    return trx.p2pkh_address()

def Mnemonic_To_TRX(mnemonicwords):
    seed = Mnemonic_To_Bytes(mnemonicwords)
    key = Bytes_To_PrivateKey(seed)
    trx: Wallet_ = Wallet_(TRX)
    trx.from_private_key(key)
    return trx.p2pkh_address()

def Balance_TRX(addr): return Trx_Balance(addr)

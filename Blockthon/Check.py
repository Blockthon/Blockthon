import requests, json


def Btc_Balance(address: str) -> str:
    req = requests.get(f"https://bitcoin.atomicwallet.io/api/v2/address/{address}").json()
    return dict(req)['balance']


# --------------------------------------------------------------------------------
# Check Value Ethereum Address Balance Return [str]
def Eth_Balance(address: str) -> str:
    req = requests.get(f"https://ethereum.atomicwallet.io/api/v2/address/{address}").json()
    return dict(req)['balance']


# --------------------------------------------------------------------------------
# Check Value Litecoin Address Balance Return [str]
def Ltc_Balance(address: str) -> str:
    """ Check Value Litecoin Address Balance Return [str] """
    req = requests.get(f"https://litecoin.atomicwallet.io/api/v2/address/{address}").json()
    return dict(req)['balance']


# --------------------------------------------------------------------------------
# Check Value TRON Address Balance Return [str]
def Trx_Balance(address: str) -> str:
    """ Check Value TRON Address Balance Return [str] """
    req = requests.get(f"https://apilist.tronscanapi.com/api/accountv2?address={address}&source=true").json()
    return dict(req)['balance']


# --------------------------------------------------------------------------------
# Check Value Dogecoin Address Balance Return [str]
def Doge_Balance(address: str) -> str:
    """ Check Value Dogecoin Address Balance Return [str] """
    req = requests.get(f"https://dogecoin.atomicwallet.io/api/v2/address/{address}").json()
    return dict(req)['balance']


# --------------------------------------------------------------------------------
# Check Value Bitcoin Gold Address Balance Return [str]
def Btg_Balance(address: str) -> str:
    """ Check Value Bitcoin Gold Address Balance Return [str] """
    req = requests.get(f"https://bgold.atomicwallet.io/api/v1/address/{address}").json()
    return dict(req)['balance']


# --------------------------------------------------------------------------------
# Check Value DigiByte Address Balance Return [str]
def Dgb_Balance(address: str) -> str:
    """ Check Value DigiByte Address Balance Return [str] """
    req = requests.get(f"https://digibyte.atomicwallet.io/api/v1/address/{address}").json()
    return dict(req)['balance']


# --------------------------------------------------------------------------------
# Check Value Ravencoin Address Balance Return [str]
def Rvn_Balance(address: str) -> str:
    """ Check Value Ravencoin Address Balance Return [str] """
    req = requests.get(f"https://ravencoin.atomicwallet.io/api/v1/address/{address}").json()
    return dict(req)['balance']


# --------------------------------------------------------------------------------
# Check Value Qtum Address Balance Return [str]
def Qtum_Balance(address: str) -> str:
    """ Check Value Qtum Address Balance Return [str] """
    req = requests.get(f"https://qtum.atomicwallet.io/api/v1/address/{address}").json()
    return dict(req)['balance']


# --------------------------------------------------------------------------------
# Check Value ZCASH Address Balance Return [str]
def Zec_Balance(address: str) -> str:
    """ Check Value ZCASH Address Balance Return [str] """
    req = requests.get(f"https://zcash.atomicwallet.io/api/v1/address/{address}").json()
    return dict(req)['balance']


# --------------------------------------------------------------------------------
# Check Value Dash Address Balance: return [str]
def Dash_Balance(address: str) -> str:
    """ # Check Value Dash Address Balance: return [str] """
    req = requests.get(f"https://dash.atomicwallet.io/api/v1/address/{address}").json()
    return dict(req)['balance']

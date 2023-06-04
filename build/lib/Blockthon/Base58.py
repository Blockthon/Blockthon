from hashlib import new, sha256 as _sha256

BASE58_ALPHABET = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
BASE58_ALPHABET_LIST = list(BASE58_ALPHABET)
BASE58_ALPHABET_INDEX = {char: index for index, char in enumerate(BASE58_ALPHABET)}


def sha256(bytestr):
    return _sha256(bytestr).digest()


def double_sha256(bytestr):
    return _sha256(_sha256(bytestr).digest()).digest()


def double_sha256_checksum(bytestr):
    return double_sha256(bytestr)[:4]


def ripemd160_sha256(bytestr):
    return new('ripemd160', sha256(bytestr)).digest()


hash160 = ripemd160_sha256


def b58_encode(v):
    p, acc = 1, 0
    for c in reversed(v):
        acc += p * c
        p = p << 8

    string = ""
    while acc:
        acc, idx = divmod(acc, 58)
        string = BASE58_ALPHABET[idx] + string

    # Pad for leading zeroes
    for c in v:
        if c == 0:
            string = BASE58_ALPHABET[0] + string
        else:
            break

    return string


def b58check_encode(version, payload):
    data = version + payload
    check = _sha256(_sha256(data).digest()).digest()[:4]
    return b58_encode(data + check)


def b58_decode(v):
    if not isinstance(v, str):
        v = v.decode('ascii')

    decimal = 0
    for char in v:
        decimal = decimal * 58 + BASE58_ALPHABET.index(char)
    return decimal.to_bytes((decimal.bit_length() + 7) // 8, 'big')


def b58check_decode(v):
    v_bytes = b58_decode(v)
    actual_checksum = _sha256(_sha256(v_bytes[:-4]).digest()).digest()
    expected_checksum = v_bytes[-4:]
    if actual_checksum[:4] != expected_checksum:
        raise ValueError("Invalid checksum")
    return v_bytes[:-4]


def Base58_(hashaddr_):
    a_ = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
    b58_ = ''
    _lz = len(hashaddr_) - len(hashaddr_.lstrip('0'))
    _addrNum = int(hashaddr_, 16)
    while _addrNum > 0:
        dg_ = _addrNum % 58
        cdg_ = a_[dg_]
        b58_ = cdg_ + b58_
        _addrNum //= 58
    on_ = _lz // 2
    for one in range(on_):
        b58_ = '1' + b58_
    return b58_
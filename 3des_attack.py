from sage.crypto.block_cipher.des import DES
from math import ceil, log

msg = 'hello'

def encrypt(k: str) -> str:
    return k + msg

def decrypt(k: str) -> str:
    return k + msg

def keys() -> 'list[str]':
    quantity = pow(2, 56)
    res = []
    n = ceil(log(quantity, 10))
    for k in range(1, quantity + 1):
        diff = n - ceil(log(k, 10))
        res.append('0' * diff + str(k) + '0')
    return res

alpha = list(map(encrypt, keys()))
beta = list(map(decrypt, keys()))

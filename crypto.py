#!/usr/bin python3

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
 
key = bytes(range(16))

# message blocks
m0 = b"\x00" * 16
m1 = b"\x01" * 16

# initialization vectors
iv  = b"\x0a" * 16
iv0 = iv
iv1 = iv ^ (b'\x00' * 15 + b'\x01')

# cbc on each block independently = ecb
cbc0 = Cipher(algorithm=algorithms.AES(key), mode=modes.CBC(iv))
cbc_block0 = cbc0.encryptor().update(m0)
cbc_block1 = cbc0.encryptor().update(m1)
cbc_ecb = (cbc_block0 + cbc_block1).hex()

# cbc on multiple blocks
cbc1 = Cipher(algorithm=algorithms.AES(key), mode=modes.CBC(iv))
cbc = cbc1.encryptor().update(m0 + m1).hex()

# cbc on chained individual blocks = cbc on multiple blocks
_cbc0 = Cipher(algorithm=algorithms.AES(key), mode=modes.CBC(iv)).encryptor().update(m0)
_cbc1 = Cipher(algorithm=algorithms.AES(key), mode=modes.CBC(_cbc0)).encryptor().update(m1)
_cbc = (_cbc0 + _cbc1).hex()

assert(cbc == _cbc)

# ctr on each block = ecb
ctr0 = Cipher(algorithm=algorithms.AES(key), mode=modes.CTR(iv))
ctr_block0 = ctr0.encryptor().update(m0)
ctr_block1 = ctr0.encryptor().update(m1)
ctr_ecb = (ctr_block0 + ctr_block1).hex()

# ctr on multiple blocks
ctr1 = Cipher(algorithm=algorithms.AES(key), mode=modes.CTR(iv))
ctr = ctr1.encryptor().update(m0 + m1).hex()

_ctr0 = Cipher(algorithm=algorithms.AES(key), mode=modes.CTR(iv)).encryptor().update(m0)
_ctr1 = Cipher(algorithm=algorithms.AES(key), mode=modes.CTR(_ctr0)).encryptor().update(m1)
_ctr = (_ctr0 + _ctr1).hex()

if cbc_ecb == ctr_ecb:
  print('ECB success!')

print('cbc0: ' + cbc_ecb)
print('ctr0: ' + ctr_ecb)
print('cbc1: ' + cbc)
print('ctr1: ' + ctr)

if cbc == _cbc:
  print('CBC success!')
elif ctr == ctr_ecb:
  print('CTR success!')
else:
  sig = ''
  n = len(cbc) // 32
  # iterate over each 32 byte block of ciphertext
  for i in range(n):
    if cbc[:32] != cbc_ecb[:32]:
      sig += '^' * 32
    else:
      sig += '.' * 32
    cbc = cbc[32:]
    cbc_ecb = cbc_ecb[32:]
  print('diff ', sig)

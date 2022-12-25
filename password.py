#!/usr/bin python3

from getpass import getpass
from hashlib import pbkdf2_hmac
from secrets import token_bytes

# always salt your hash
salt = token_bytes(32)

def hash(bs: bytes):
    return pbkdf2_hmac('sha256', bs, salt, 100_000)

# set a confirmed password within 5 attempts
attempts = 5
while attempts >= 0:
    p = hash(bytes(getpass('Password: '), encoding='utf8'))
    q = hash(bytes(getpass('Confirm: '), encoding='utf8'))
    if p != q:
        if attempts == 1:
            print('Password mismatch. Try again. You have %s remaining attempt.' % attempts)
        elif attempts > 0:
            print('Password mismatch. Try again. You have %s remaining attempts.' % attempts)
        else:
            print('Sorry for your luck. Bye bye!')
        attempts -= 1
    else:
        print('Your password salt: ' + salt.hex())
        print('Your password hash: ' + p.hex())
        break

def guess(attempt: str) -> bool:
    g = hash(bytes(attempt, encoding='utf8'))
    return g == p

#!/usr/bin python3

import sys
import getpass
import hashlib
import secrets

# always salt your hash
salt = secrets.token_bytes(32)

def hash(bs: bytes):
    return hashlib.pbkdf2_hmac('sha256', bs, salt, 100_000)

# set a confirmed password within 5 attempts
attempts = 5
while attempts >= 0:
    p = hash(bytes(getpass.getpass('Password: '), encoding='utf8'))
    q = hash(bytes(getpass.getpass('Confirm: '), encoding='utf8'))
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
    try:
        g = hash(bytes(attempt, encoding='utf8'))
        return g == p
    except:
        print("Goodbye!")
        sys.exit(1)

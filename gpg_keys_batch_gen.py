#!/usr/bin python

import timeit
from os import system, environ, listdir
from secrets import token_hex
from pathlib import Path

# set/unset env var

def set_gpg(value: str):
    '''
    Set GNUPGHOME env var to `value`
    '''
    environ['GNUPGHOME'] = value
    print(f'GNUPGHOME set to {value}')

def unset_gpg():
    '''
    Unset GNUPGHOME env var
    '''
    environ.pop('GNUPGHOME', None)
    print('GNUPGHOME unset')

# generate keys

key_types = {'RSA', 'ELG', 'DSA', 'ECDH', 'ECDSA', 'EDDSA'}

def create_file(fpath: Path):
    if not fpath.exists():
        if not fpath.parent.exists():
            system(f'mkdir {fpath.parent}')
        system(f'touch {fpath}')

def key_gen_file(key_type: str, subkey_type: str, key_len: int, num: int):
    fpath = Path.cwd() / key_type / f'{subkey_type}_{key_len}_{num}'
    create_file(fpath)
    pwd = token_hex(32)
    contents = f'''Key-Type: {key_type}
Key-Length: {key_len}
Subkey-Type: {subkey_type}
Subkey-Length: {key_len}
Name-Real: {key_type}_{subkey_type}
Name-Comment: {num}
Name-Email: {key_type}_{subkey_type}_{key_len}_{num}@foo.bar
Expire-Date: 0
Passphrase: {pwd}
%commit
'''
    with fpath.open("w") as f:
        f.write(contents)
        f.close()

def key_gen(fpath: Path):
    system(f'gpg --batch --generate-key {fpath}')

def is_relevant_dir(fname: str) -> bool:
    fpath = Path.cwd() / fname
    return fname in key_types and fpath.is_dir()

key_gen_file('RSA', 'ELG-E', 1024, 0)
key_gen_file('RSA', 'ELG-E', 1024, 1)

for n in range(2):
    path = Path.cwd()
    key_dirs = list(filter(is_relevant_dir, listdir(path)))
    for dir in key_dirs:
        path = path / dir
        key_files = listdir(path)
        for key_file in key_files:
            key_gen(path / key_file)

# def key_gen(algo: str, num: int) -> str:
#     system(f'gpg --batch --default-new-key-algo "{algo}" --quick-generate-key "{algo}_key{num}" > {algo}/key{num}')

# RSA keys: 1024-4096 bits

# --verify

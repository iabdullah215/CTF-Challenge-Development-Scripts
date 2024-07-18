#!/usr/bin/env python3

from Crypto.Util.number import getPrime, bytes_to_long

with open('flag.txt', 'rb') as f:
    flag = f.read()

p = getPrime(1024)
q = getPrime(1024)

n1 = p * q
n2 = getPrime(1024) * q

moduli = [n1, n2]

e = 65537
c = bytes_to_long(flag)

for n in moduli:
    c = pow(c, e, n)

print("Encrypted message:", c)

with open('public-key.txt', 'w') as f:
    f.write(f'n1: {n1}\n')
    f.write(f'n2: {n2}\n')
    f.write(f'e: {e}\n')
    f.write(f'c: {c}\n')

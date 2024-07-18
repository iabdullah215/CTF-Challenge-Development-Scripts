from gmpy2 import *

def decrypt(c, p, q, e):
     ph = (p-1)*(q-1)
     d = invert(e, ph)
     return pow(c, d, p*q)

params = {}
with open("public-key.txt") as f:
    for line in f:
        line = line.rstrip()
        name, value = line.split(":")
        params[name] = mpz(int(value))

# Since we only have two moduli, we find the common prime between n1 and n2
q = gcd(params["n1"], params["n2"])
p = params["n1"] // q
r = params["n2"] // q

assert(p * q == params["n1"])
assert(r * q == params["n2"])

# Decrypt the message step by step
a1 = decrypt(params["c"], r, q, params["e"])
a2 = decrypt(a1, p, q, params["e"])

print(bytes.fromhex(format(a2, 'x')).decode("ascii"))

from gmpy2 import mpz
from gmpy2 import t_mod, invert, powmod, add, mul, is_prime
import textwrap

p_string = 'value-of-p'
g_string = 'value-of-g'
h_string = 'value-of-h'


def pretty_print(x):
    x = textwrap.wrap(x, width=32)
    for i in x:
        print(" ",i)
    print()


def build_table(h, g, p, B):
    table, z = {}, h
    g_inverse = invert(g, p)
    table[h] = 0
    for x1 in range(1, B):
        z = t_mod(mul(z, g_inverse), p)
        table[z] = x1
    return table


def lookup(table, g, p, B):
    gB, z = powmod(g, B, p), 1
    for x0 in range(B):
        if z in table:
            x1 = table[z]
            return x0, x1
        z = t_mod(mul(z, gB), p)
    return None, None


def find_x(h, g, p, B):
    table = build_table(h, g, p, B)
    x0, x1 = lookup(table, g, p, B)
    Bx0 = mul(x0, B)
    x = add(Bx0, x1)
    return x


def run(p_string, g_string, h_string):

    p = mpz(p_string)
    g = mpz(g_string)
    h = mpz(h_string)
    B = mpz(2) ** mpz(20)

    assert is_prime(p)
    assert g < p
    assert h < p

    x = find_x(h, g, p, B)

    assert h == powmod(g, x, p)
    return x


if __name__=="__main__":

    print("finding Flag...")

    x = run(p_string, g_string, h_string)

    print("Flag = ", x)

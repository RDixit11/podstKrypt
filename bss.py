import random
import math

def check_prime(n):
    if n == 1:
        return False

    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        else:
            i=i+1

    return True

def get_prime():
    while True:
        x = random.randint(10000, 100000)
        if check_prime(x) == True and x % 4 == 3:
            return x

def bss_alg(bit):
    p = get_prime()
    q = get_prime()

    N = p*q

    x = random.randint(2, N-1)
    while math.gcd(x, N) != 1:
        x = random.randint(2, N-1)

    seed = (x**2) % N
    x0 = seed

    for i in range(0, bit):
        x0 = (x0**2) % N

    return p, q, N, x0%2

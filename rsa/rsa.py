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
        x = random.randint(1000, 9999)
        if check_prime(x) == True:
            return x

def generate_keys():
    p = get_prime()
    q = get_prime()
    print(p,q)

    n = p*q
    
    phi = (p-1)*(q-1)
    print(phi)
    e = random.randint(1000,9999)
    while math.gcd(phi, e) != 1:
        e = random.randint(1000,9999)

    print(e)

    d = pow(e, -1, phi)

    print(d)
    return n,e,d



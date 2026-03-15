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

    n = p*q
    
    phi = (p-1)*(q-1)
    e = random.randint(1000,9999)
    while math.gcd(phi, e) != 1:
        e = random.randint(1000,9999)

    d = pow(e, -1, phi)

    return n,e,d

def cipher_mess(mess, n, e, d):
    mess_int = [int(letter,16) for letter in mess]
    
    encrypt_mess=[]

    for letter in mess_int:
        c = pow(letter, e, n)
        encrypt_mess.append(c)
    print(encrypt_mess)
    return encrypt_mess

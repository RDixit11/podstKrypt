import random
import math

def check_prime(n):
    if n == 1:
        return false
    
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        else:
            i=i+1

    return True

def get_prime(l, h):
    while True:
        x = random.randint(l,h)
        if check_prime(x) == True:
            return x


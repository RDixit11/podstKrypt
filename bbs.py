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

def bbs_alg(bit):
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

    return x0%2

def sbt(file):
    f = open(file, "r")
    ones = 0
    for line in f:
        ones = ones + line.count("1")

    if ones > 9725 and ones < 10275:
        print(f"Single bit test passed: {ones}")
    else:
        print(f"Single bit test not passed: {ones}")

def st(file):
    f = open(file, "r")
    line = f.read().splitlines()
    s = "".join(line)
    

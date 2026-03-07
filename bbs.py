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
        res = f"Single bit test passed: {ones}"
    else:
        res = f"Single bit test not passed: {ones}" 
    return res

def st(file):
    with open(file) as f:
        s = "".join(f.read().splitlines())

    count = {i:0 for i in range(1,7)}

    length = 0

    for b in s:
        if b == '1':
            length += 1
        else:
            if length > 0:
                count[min(length,6)] += 1
                length = 0

    if length > 0:
        count[min(length,6)] += 1

    res = []

    ranges = {
        1:(2315,2685),
        2:(1114,1386),
        3:(527,723),
        4:(240,384),
        5:(103,209),
        6:(103,209)
    }

    for i in range(1,7):
        low, high = ranges[i]
        if low < count[i] < high:
            res.append(f"Test passed for series length {i}")
        else:
            res.append(f"Test FAILED for series length {i}")

    return res

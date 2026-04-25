import random

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

def get_prime(l, h):
    while True:
        x = random.randint(l,h)
        if check_prime(x) == True:
            return x

def secret_split(secret, n, t): # n - liczba udzialow; t - liczba udzialow potrzebna do odtworzenia
    p = get_prime(secret+1,10000)
    while p < n:
        p = get_prime(secret+1, 10000)

    a_list = [secret]
    for i in range(t-1):
        a = random.randint(0, p-1)
        a_list.append(a)

    shares = []
    
    for x in range(1, n+1):
        y=0
        for power, a in enumerate(a_list):
            y = (y + a * pow(x, power, p)) % p
    
        shares.append((x, y))

    return shares, p

def secret_recon(shares, t, p):
    secret = 0

    for i in range(t):
        x_i, y_i = shares[i]

        val = 1

        for j in range(t):
            if i == j:
                continue

            x_j, _ = shares[j]

            num = (-x_j) % p
            den = (x_i - x_j) % p

            inv_den = pow(den, -1, p)

            val = (val * num * inv_den) % p

        secret = (secret + y_i * val) % p

    return secret

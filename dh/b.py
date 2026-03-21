import dh
import random

with open("comm.txt", "r") as f:
    n_g = f.readline().split()

n = int(n_g[0])
g = int(n_g[1])

print(n, g)

y = random.randint(100000, 999999)

Y = pow(g, y, n)

print(Y)

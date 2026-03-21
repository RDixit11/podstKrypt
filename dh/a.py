import random
import dh
from sympy import primitive_root

n = dh.get_prime()

g = primitive_root(n)

with open("comm.txt", "w") as f:
    f.write(f"{str(n)} {str(g)}\n")

x = random.randint(100000, 999999)

X = pow(g,x,n)

print(X)

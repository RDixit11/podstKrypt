import sys
from tss import *

if len(sys.argv) < 2:
    print("TODO")
    print("python3 main.py <secret> <n> <k>")
else:
    secret = int(sys.argv[1])
    n = int(sys.argv[2])
    k = int(sys.argv[3])
    print(f"ORIGINAL SECRET: {secret}")
    s_list = secret_split(secret,n,k)
    print(f"SHARES LIST: {s_list}")
    recon = secret_recon(s_list, k)
    print(f"SECRET RECONSTRUCTION: {recon}")


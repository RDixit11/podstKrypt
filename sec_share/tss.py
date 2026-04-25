import random

def secret_split(secret, n, k):
    s_list=[]
    total = 0

    for i in range(n-1):
        #val = secrets.randbelow(k)
        val = random.randint(0, k-1)
        s_list.append(val)
        total = total + val
    
    last_val = (secret-total) % k
    s_list.append(last_val)
    
    return s_list

def secret_recon(s_list, k):
    s = sum(s_list) % k
    return s


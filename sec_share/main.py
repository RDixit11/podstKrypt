import sys
import tss
import sss
import matplotlib.pyplot as plt
import vss

if len(sys.argv) < 2:
    print("TODO")
    print("python3 main.py <algorithm> <secret> <n> <k>")
else:
    if sys.argv[1] == "tss":
        secret = int(sys.argv[2])
        n = int(sys.argv[3])
        k = int(sys.argv[4])
        print(f"ORIGINAL SECRET: {secret}")
        s_list = tss.secret_split(secret,n,k)
        print(f"SHARES LIST: {s_list}")
        recon = tss.secret_recon(s_list, k)
        print(f"SECRET RECONSTRUCTION: {recon}")
    
    elif sys.argv[1] == "sss":
        secret = int(sys.argv[2])
        n = int(sys.argv[3])
        t = int(sys.argv[4])
        shares, p = sss.secret_split(secret, n, t)
        print(secret)
        print(shares)
        x = [p[0] for p in shares]
        y = [p[1] for p in shares]
        
        fig, (ax1, ax2) = plt.subplots(1,2, figsize=(12,5))
        ax1.scatter(x,y)
        ax1.scatter(0, secret)
        x_t = x[:t]
        y_t = y[:t]
        ax2.scatter(x_t, y_t)

        recon = sss.secret_recon(shares, t, p)
        print(recon)
        
        ax2.scatter(0, recon)
        plt.show()
    elif sys.argv[1] == "vss":
        img = sys.argv[2]
        vss.visual_secret_share(img, "share1.png", "share2.png")

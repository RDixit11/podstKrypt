import sys
from blockCipher import *

def main():
    if len(sys.argv) != 4:
        print("Użycie python3 main.py <action> <key> <data>")
        exit(1)
    elif sys.argv[1] == "test":
        key = sys.argv[2].encode()
        data = sys.argv[3].encode()
        
        ecb_time_en, ecb_time_de, cbc_time_en, cbc_time_de, ctr_time_en, ctr_time_de = test(key, data)
        print(f"{'TYPE\\TIME:':<12} {'ECB_TIME':<10} {'CBC_TIME':<10} {'CTR_TIME':<10}")
        print(f"{'CIPHER:':<12} {ecb_time_en:<10.6f} {cbc_time_en:<10.6f} {ctr_time_en:<10.6f}")
        print(f"{'DECIPHER:':<12} {ecb_time_de:<10.6f} {cbc_time_de:<10.6f} {ctr_time_de:<10.6f}")
    
    elif sys.argv[1] == "error":
        key = sys.argv[2].encode()
        data = sys.argv[3].encode()

        error(key, data)
    elif sys.argv[1] == "cbc":
        key = sys.argv[2].encode()
        data = sys.argv[3].encode()
        
        encrypt, decrypt = cbc(key, data)

        print(f"ENCRYPTED TEXT: {encrypt}")
        print(f"DECRYPTED TEXT: {decrypt}")
if __name__ == "__main__":
    main()

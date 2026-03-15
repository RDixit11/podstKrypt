import sys
import rsa

def main():
    match sys.argv[1]:
        case "gen-keys":
            file = sys.argv[2]
            n, pub, priv = rsa.generate_keys()
            with open(file, "w") as f:
                f.write(f"{str(n)}\n")
                f.write(f"{str(pub)}\n")
                f.write(str(priv))
            print(f"public key: {n}, {pub}")
            print(f"private key: {n}, {priv}")
        case "cipher-mess":
            file = sys.stdin.readline().strip()
            mess = sys.stdin.readline().strip()
            mess = list(mess)
            mess_asc = [hex(ord(word))[2:] for word in mess]
            mess_asc_str = " ".join(mess_asc)
            print(mess_asc_str)
            
            with open(file, "r") as f:
                n = int(f.readline().strip())
                e = int(f.readline().strip())
            
            cipher_mess = rsa.cipher_mess(mess_asc, n, e)
            cipher_mess_hex = [hex(word)[2:] for word in cipher_mess]
            mess_hex_str = " ".join(cipher_mess_hex)
            print(mess_hex_str)

if __name__ == "__main__":
    main()

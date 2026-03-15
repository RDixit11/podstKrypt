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
            rsa.cipher_mess(mess_asc, 9, 5, 5)

if __name__ == "__main__":
    main()

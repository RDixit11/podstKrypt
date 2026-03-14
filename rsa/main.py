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
            file = sys.argv[2]
            mess = sys.argv[3]
            mess = list(mess)
            mess_asc = [ord(word) for word in mess]
            print(mess_asc)

if __name__ == "__main__":
    main()

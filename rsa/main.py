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
                f.write(f"{str(n)}\n")
                f.write(str(priv))
            print(pub)
            print(priv)

if __name__ == "__main__":
    main()

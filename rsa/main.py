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
        case "encrypt-mess":
            file = sys.stdin.readline().strip() # plik zawierajacy klucze
            mess = sys.stdin.readline().strip() # wiadomosc
            en_file = sys.stdin.readline().strip() # plik wyjsciowy zawierajacy zaszyfrowana wiadomosc

            mess = list(mess) 
            mess_asc = [hex(ord(word))[2:] for word in mess]
            mess_asc_str = " ".join(mess_asc)
            
            print(f"Message before encryption: {mess_asc_str}")
            
            with open(file, "r") as f:
                n = int(f.readline().strip())
                e = int(f.readline().strip())
            
            cipher_mess = rsa.encrypt_mess(mess_asc, n, e)
            cipher_mess_hex = [hex(word)[2:] for word in cipher_mess]
            mess_hex_str = " ".join(cipher_mess_hex)
            
            with open(en_file, "w") as f:
                f.write(mess_hex_str)

            print(f"Message after encryption: {mess_hex_str}")
        
        case "decrypt-mess":
            file = sys.stdin.readline().strip() # plik zawierajacy klucze
            en_file = sys.stdin.readline().strip() # plik z zaszyfrowana wiadomoscia

            with open(file, "r") as f:
                n = int(f.readline().strip())
                next(f)
                d = int(f.readline().strip())
            
            with open(en_file, "r") as f:
                en_mess = f.readline().split()
                   
            de_mess = rsa.decrypt_mess(en_mess, n, d)
            de_mess_hex = [hex(word)[2:] for word in de_mess]

            try:
                message = "".join(chr(x) for x in de_mess)
                print(f"Decrypted message: {message}")
            except ValueError:
                print(f"Unable to convert to char: {de_mess_hex}\n")

if __name__ == "__main__":
    main()

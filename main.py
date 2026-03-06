import sys
import bss

def main():
    match sys.argv[1]:
        case "bss":
            print("Blum-Blum_Shub algorithm:")
            p,q,N,res = bss.bss_alg(7)
            print(res)

if __name__ == ("__main__"):
    main()

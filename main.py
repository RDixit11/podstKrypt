import sys
import bbs

def main():
    match sys.argv[1]:
        case "bbs":
            bit = int(sys.argv[2])
            res = bbs.bbs_alg(bit)
            print(res)

if __name__ == ("__main__"):
    main()

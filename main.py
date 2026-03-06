import sys
import bbs

def main():
    match sys.argv[1]:
        case "bbs":
            bit = int(sys.argv[2])
            res = bbs.bbs_alg(bit)
            print(res)
        case "bbs-test":
            file = sys.argv[2]
            bbs.sbt(file)
        case "st":
            file = sys.argv[2]
            bbs.st(file)
if __name__ == ("__main__"):
    main()

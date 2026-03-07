import sys
import bbs

def main():
    match sys.argv[1]:
        case "bbs":
            bit = int(sys.argv[2])
            print(bbs.bbs_alg(bit))
        case "sbt":
            file = sys.argv[2]
            print(bbs.sbt(file))
        case "st":
            file = sys.argv[2]
            res = bbs.st(file)
            for i in range(len(res)):
                print(res[i])

if __name__ == ("__main__"):
    main()

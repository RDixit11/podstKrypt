import sys
import bbs

def main():
    match sys.argv[1]:
        case "bbs":
            bit = int(sys.argv[2])
            print(bbs.bbs_alg(bit))
        case "bbs-tests":
            file = sys.argv[2]
            print(bbs.sbt(file))
            
            res = bbs.st(file)
            for i in range(len(res)):
                print(res[i])
            
            print(bbs.lst(file))
            
            print(bbs.pt(file))

if __name__ == ("__main__"):
    main()

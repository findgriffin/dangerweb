from libquote import *

def build_database(qlist):
    qlist = quoteloader('quotelist.xml')
    build_database(qlist)

def makepickles(qlist, flist, find):
    qlist = quoteloader('quotelist.xml')
    ind = makeindex(qlist)
    save_quoter(qlist, ind, flist, find)

if __name__ == "__main__":
    from sys import argv
    print argv[1]
    if argv[1] == "build":
        build_database(sys.argv[2])
    elif argv[1] == "pickle":
        makepickles(argv[2], argv[3], argv[4])

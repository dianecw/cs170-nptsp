import naive_solution
import algorithm
import sanity


T = 3 # number of test cases
fout = open ("answer.out", "w")
for t in xrange(1, T+1):

    fin = open("./submission_phase1/NPSupreme" + str(t) + ".in", "r")
    N = int(fin.readline())
    d = [[] for i in range(N)]
    for i in xrange(N):
        d[i] = [int(x) for x in fin.readline().split()]
    c = fin.readline()

    # find an answer, and put into assign


    path = algorithm.find_good_construction(d, c, N)

    print ("*** TRIAL " + str(t) + " ***")
    # print("Construction")
    # print ("WEIGHT:" +  str(sanity.weight(path, d)))
    # print
    pre = sanity.weight(path,d)
    path = algorithm.improve(path, d, c)

    # print("Improvement")
    # print "VALID:" +  str(sanity.is_valid_path(path, c))
    # print "WEIGHT:" +  str(sanity.weight(path, d))
    # print
    # print
    post = sanity.weight(path, d)
    # print
    # print
    print (float(pre - post) / pre)
    print
    path = sanity.normalize(path, N)

    fout.write("%s\n" % " ".join(map(str, path)))
fout.close()

import naive_solution
import algorithm
import sanity
import supreme_mst


T = 495 # number of test cases
fold = open ("answer.out", "r")
fout = open ("answer2.out", "w")
for t in xrange(1, T+1):

    fin = open("./instances/" + str(t) + ".in", "r")
    N = int(fin.readline())
    d = [[] for i in range(N)]
    for i in xrange(N):
        d[i] = [int(x) for x in fin.readline().split()]
    c = fin.readline()

    # find an answer, and put into assign



    print ("*** TRIAL " + str(t) + " ***")

    old_sol = fold.readline().split()
    print "OLD: " + str(old_sol)
    print "SCORE: " + str(sanity.weight(old_sol,d))
    print

    # print("Construction")
    # print ("WEIGHT:" +  str(sanity.weight(path, d)))
    # print

    path = algorithm.find_good_construction(d, c, N)    
    pre = sanity.weight(path,d)
    path = algorithm.improve(path, d, c)
    post = sanity.weight(path, d)
    
    print "VALID: " +  str(sanity.is_valid_path(path, c))
    print "PATH: " + str(path)
    print "SCORE: " + str(post)
    print

    # new_edges = supreme_mst.mst_solver(d, N, 10)
    # print new_edges
    # new_path = algorithm.find_good_construction(new_edges, c, N)
    # new_path = algorithm.improve(new_path, new_edges, c)
    # new_score = sanity.weight(new_path, new_edges)

    # print "NEW PATH: " + str(new_path)
    # print "VALID: " + str(sanity.is_valid_path(new_path, c))
    # print "SCORE: " + str(new_score)
    # print

    # if new_score < post:
    #     path = new_path
    #     post = new_score

    # print
    if sanity.weight(old_sol,d) < post:
        path = old_sol
        post = sanity.weight(old_sol,d)


    fout.write("%s\n" % " ".join(map(str, path)))
fout.close()

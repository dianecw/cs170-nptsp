import algorithm
import sanity
import supreme_mst
import construction

T = 495 # number of test cases

old_solutions = []
fold = open("answer.out", "r")
for _ in range(T):
    old_solutions = old_solutions + [[int(x) for x in fold.readline().split()]]

fout = open ("answer.out", "w")


for t in range(1, T+1):

    fin = open("./instances/" + str(t) + ".in", "r")
    N = int(fin.readline())
    d = [[] for i in range(N)]
    for i in range(N):
        d[i] = [int(x) for x in fin.readline().split()]
    c = fin.readline()

    # find an answer, and put into assign

    if t%50 == 0:
        print ("*** DIVISION " + str(t) + " ***")

    old_sol = sanity.denormalize(old_solutions[t-1], N)
    old_score = sanity.weight(old_sol,d)

    if old_score == 0 or len(old_sol) < 7:
        path = old_sol

    else:

        print ("*** TRIAL " + str(t) + " ***")
        print old_score

        new_edges = supreme_mst.mst_solver(d, N)
        path = algorithm.find_good_construction(new_edges, c, N, selection_method=construction.domain_randomly_select)  
        print sanity.weight(path, new_edges)
        path = algorithm.targeted_improve(path, new_edges, c, 500)  
        print sanity.weight(path, new_edges)
        path = algorithm.improve(path, new_edges, c, 1, 100)
        print sanity.weight(path, new_edges)
        # path = algorithm.improve(path, d, c, 2, 20)
        post = sanity.weight(path, d)


        if post < old_score:
            print ("NEW: " + str(post))
            print ("OLD: " + str(old_score))
            print ("IMPROVEMENT: " + str(old_score-post))
            print ("")


        if len(old_sol) > 0 and old_score < post:
            path = old_sol
            post = sanity.weight(old_sol,d)


    path = sanity.normalize(path, N)




    fout.write("%s\n" % " ".join(map(str, path)))
fout.close()

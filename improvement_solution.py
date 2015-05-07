import naive_solution
import algorithm
import sanity
import supreme_mst

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



    print ("*** TRIAL " + str(t) + " ***")

    old_sol = sanity.denormalize(old_solutions[t-1], N)
    old_score = sanity.weight(old_sol,d)

    if old_score == 0:
        path = old_sol

    else:

        path = old_sol
        pre = sanity.weight(path,d)
        path = algorithm.improve(path, d, c, 10, 100)
        post = sanity.weight(path, d)


        print ("NEW: " + str(post))
        print ("OLD: " + str(old_score))
        print ("IMPROVEMENT: " + str(old_score-post))
        print ("")


        if len(old_sol) > 0 and sanity.weight(old_sol,d) < post:
            path = old_sol
            post = sanity.weight(old_sol,d)


    path = sanity.normalize(path, N)




    fout.write("%s\n" % " ".join(map(str, path)))
fout.close()

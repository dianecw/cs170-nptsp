import algorithm
import sanity
import supreme_mst
import greedy

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

        path = greedy.good_greedy(d, c, N)
        if path is not None and sanity.is_valid_path(path, c):
            post = sanity.weight(path, d)
            if post < old_score:
                print ("NEW: " + str(post))
                print ("OLD: " + str(old_score))
                print ("IMPROVEMENT: " + str(old_score-post))
                print ("")


            if len(old_sol) > 0 and sanity.weight(old_sol,d) < post:
                path = old_sol
                post = sanity.weight(old_sol,d)
        else:
            path = old_sol


    path = sanity.normalize(path, N)




    fout.write("%s\n" % " ".join(map(str, path)))
fout.close()

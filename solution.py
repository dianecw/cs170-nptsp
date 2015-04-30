import naive_solution
import algorithm
import sanity

def normalize(assign, N):
    new = [-1] * N
    for i in range(N):
        new[i] = assign[i] + 1

    return new



T = 4 # number of test cases
fout = open ("answer.out", "w")
for t in xrange(1, T+1):
    fin = open(str(t) + ".in", "r")
    N = int(fin.readline())
    d = [[] for i in range(N)]
    for i in xrange(N):
        d[i] = [int(x) for x in fin.readline().split()]
    c = fin.readline()

    # find an answer, and put into assign
    best = None
    best_val = float('inf')
    for i in range(10000):
        assign = algorithm.construct_path(d,c,N)
        weight = sanity.weight(assign,d) 
        if sanity.is_valid_path(assign, c) and weight < best_val:
            best_val = weight
            best = assign
    assign = best
    print("PRE - kopt")
    print assign
    print "WEIGHT:" +  str(sanity.weight(assign, d))
    for i in range(100000):
        assign = algorithm.super_kopt(d,c,assign,4)
    print("post - kopt")
    print(assign)
    print "VALID:" +  str(sanity.is_valid_path(assign, c))
    print "WEIGHT:" +  str(sanity.weight(assign, d))
    #print sanity.supreme_brute_generator(d,c,N)

    assign = normalize(assign, N)
    fout.write("%s\n" % " ".join(map(str, assign)))
fout.close()

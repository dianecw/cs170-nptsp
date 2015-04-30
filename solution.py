import naive_solution
import algorithm
import sanity

def normalize(assign, N):
    new = [-1] * N
    for i in range(N):
        new[i] = assign[i] + 1

    return new



T = 3 # number of test cases
fout = open ("answer.out", "w")
for t in xrange(1, T+1):
    fin = open(str(t) + ".in", "r")
    N = int(fin.readline())
    d = [[] for i in range(N)]
    for i in xrange(N):
        d[i] = [int(x) for x in fin.readline().split()]
    c = fin.readline()

    # find an answer, and put into assign
    
    assign = algorithm.construct_path(d,c,N)
    print assign
    print "VALID:" +  str(sanity.is_valid_path(assign, c))
    print "WEIGHT:" +  str(sanity.weight(assign, d))
    #print sanity.supreme_brute_generator(d,c,N)

    assign = normalize(assign, N)
    fout.write("%s\n" % " ".join(map(str, assign)))
fout.close()

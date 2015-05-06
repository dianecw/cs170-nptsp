import sanity

T = 495 # number of test cases

old_solutions = []
fout = open("answer2.out", "r")
for _ in range(T):
    old_solutions = old_solutions + [[int(x) for x in fout.readline().split()]]

fout = open("answer2.out", "w")

for t in range(1, T+1):
	old_sol = old_solutions[t-1]
	path = sanity.normalize(old_sol, len(old_sol))
	fout.write("%s\n" % " ".join(map(str, path)))
fout.close()
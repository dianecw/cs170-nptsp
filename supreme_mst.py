def mst_solver(edges,N, num_branches = 5 ):
    pruned = [[10000]*N for i in range(N)]
    for i in range(N):
        best = [10000]*num_branches
        best_loc = [0]*num_branches
        for j in range(N):
            for k in range(num_branches):
                if best[k] > edges[i][j]:
                    best[k] = edges[i][j]
                    best_loc[k] = j
                    break
        for k in range(num_branches):
            pruned[i][best_loc[k]] = best[k]
    return pruned


def mst_solver(edges, N, num_branches=5, fill_bias=float('inf')):
    pruned = [[fill_bias] * N for i in range(N)]
    for i in range(N):
        best = [fill_bias] * num_branches
        best_loc = [0]*num_branches
        for j in range(N):
            largest = best[0]
            largest_index = 0
            for k in range(1,num_branches):
                if largest < best[k]:
                    largest = best[k]
                    largest_index = k
                    if largest == fill_bias:
                        break
            if edges[i][j] < largest:
                best[largest_index] = edges[i][j]
                best_loc[largest_index] = j
        for k in range(num_branches):
            pruned[i][best_loc[k]] = best[k]
    for i in range(N):
        for j in range(N):
            holder1 = pruned[i][j]
            holder2 = pruned[j][i]
            if holder1 != fill_bias:
                pruned[j][i] = holder1
            if holder2 != fill_bias:
                pruned[i][j] = holder2
    closed_set = set()
    closed_set.add(0)
    stack = []
    count = 0
    for j in range(N):
        if pruned[0][j] != fill_bias and j != closed_set:
            stack.append((i, j))

    while len(stack) != 0:
        if len(closed_set) == N:
            break
        cur = stack[0]
        stack = stack[1:]
        for j in range(N):
            if pruned[cur[1]][j] != fill_bias and j not in closed_set:
                stack.append((cur[1], j))
                closed_set.add(j)
    if len(closed_set) == N:
        return pruned
    return mst_solver(edges, N, num_branches + 1, fill_bias)

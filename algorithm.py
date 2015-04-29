def get_approx_path(edges, colors, N):
	


def insertion(edges, colors, N, used_vertices, path, vertex):
    v_edges = edges[vertex]

    min_weight = v_edges[path[0]] #best is inserting at beginning
    min_position = (None,0)
    if(v_edges[path[len(path)-1]] < min_weight):
        min_weight = v_edges[path[len(path)-1]] #best is inserting at end
        min_position = (len(path)-1,None)

    for i in range(len(path) - 1):
        if i == 0: #special cases
            prev1 = colors[path[i]]
            curr = colors[vertex]
            post1 = colors[path[i+1]]
            post2 = colors[path[i+2]]
            if !(prev1 == curr and curr == post1) and !(curr == post1 and post1 == post2):
                prev_edges = edges[path[i]]
                if v_edges[path[i]] + v_edges[path[i+1]] - prev_edges[path[i+2]] < min_weight:
                    min_weight = v_edges[path[i]] + v_edges[path[i+2]] - prev_edges[path[i+2]]
                    min_position = (i,i+1)

        else if i == len(path)-2:
            prev2 = colors[path[i-1]]
            prev1 = colors[path[i]]
            curr = colors[vertex]
            post1 = colors[path[i+1]]
            if !(prev2 == prev1 and prev1 == curr) and !(prev1 == curr and curr == post1):
                prev_edges = edges[path[i]]
                if v_edges[path[i]] + v_edges[path[i+1]] - prev_edges[path[i+2]] < min_weight:
                    min_weight = v_edges[path[i]] + v_edges[path[i+2]] - prev_edges[path[i+2]]
                    min_position = (i,i+1)

        else:
            prev2 = colors[path[i-1]]
            prev1 = colors[path[i]]
            curr = colors[vertex]
            post1 = colors[path[i+1]]
            post2 = colors[path[i+2]]
            if !(prev2 == prev1 and prev1 == curr) and !(prev1 == curr and curr == post1) and !(curr == post1 and post1 == post2): # making sure we don't hit 3
                prev_edges = edges[path[i]]
                if v_edges[path[i]] + v_edges[path[i+1]] - prev_edges[path[i+2]] < min_weight:
                    min_weight = v_edges[path[i]] + v_edges[path[i+2]] - prev_edges[path[i+2]]
                    min_position = (i,i+1)
    if min_position[0] == None:
        path = [vertex] + path
    else if min_position[1] == None:
        path = path + [vertex]
    else:
        path = path[:min_position[0]+1] + [vertex] + path[min_position[1]:]
    return path




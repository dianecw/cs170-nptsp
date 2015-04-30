import random
import itertools
import sanity
import threading


def construct_path(edges, colors, N):
    used_vertices = set()
    not_used_vertices = set()
    for i in range(0, N):
        not_used_vertices.add(i)
    path = []

    # First Vertex
    vertex = randomly_select(N, not_used_vertices)
    path = [] + [vertex]
    used_vertices.add(vertex)
    not_used_vertices.remove(vertex)

    for i in range(1, N):
        newpath = "FAIL"
        while newpath == "FAIL":
            vertex = randomly_select(N, not_used_vertices)
            newpath = insertion(edges, colors, N, used_vertices, path, vertex)
        path = newpath
        used_vertices.add(vertex)
        not_used_vertices.remove(vertex)

    return path


def randomly_select(N, not_used_vertices):
    num = random.randint(0, N - 1)
    if num in not_used_vertices:
        return num
    else:
        return randomly_select(N, not_used_vertices)


def supreme_farthest_insertion(edges, non_used_verticies, used_vertices):
    best = None
    best_val = float('-inf')
    for v in non_used_verticies:
        closest_dist = float('inf')
        for v2 in used_vertices:
            cur_dist = edges[v][v2]
            if closest_dist > cur_dist:
                closest_dist = cur_dist
        if best_val < closest_dist:
            best_val = closest_dist
            best = v
    return best


def super_kopt(edges, colors, path, k):
    N = len(path)
    random_edges = sorted(random.sample(range(0, N), k - 1)) + [N]
    start = 0
    subpaths = []
    for i in range(k):
        subpaths.append(path[start:random_edges[i]])
        start = random_edges[i]
    subpaths = list(filter(lambda x :len(x) > 0, subpaths))
    permutations = itertools.permutations(subpaths)
    optimal = sanity.weight(path,edges)
    optimal_path = path 
    path = next(permutations)
    while path != None:
        path = [item for sublist in next(permutations) for item in sublist]
        weight = sanity.weight(path,edges)
        if optimal > weight and sanity.is_valid_path(path,colors, False):
            optimal = weight
            optimal_path = path
        try:
            path = next(permutations)
        except StopIteration:
            path = None
    return optimal_path


def random_kopt(edges, colors, path, k):
    N = len(path)
    random_edges = sorted(random.sample(range(0, N), k - 1)) + [N]
    start = 0
    subpaths = []
    for i in range(k):
        subpaths.append(path[start:random_edges[i]])
        start = random_edges[i]
    subpaths = list(filter(lambda x :len(x) > 0, subpaths))
    permutations = itertools.permutations(subpaths)
    path = next(permutations)
    path_list = []
    while path != None:
        path = [item for sublist in next(permutations) for item in sublist]
        weight = sanity.weight(path,edges)
        if sanity.is_valid_path(path,colors, False):
            path_list = path_list + [path]
        try:
            path = next(permutations)
        except StopIteration:
            path = None

    rand = random.randint(0,len(path_list)-1)
    return path_list[rand]


def color_valid(index, path, colors, my_color):

    after_one = (index > len(path) - 1) or (my_color != colors[path[index]])
    after_two = (index + 1 > len(path) - 1) or (
        my_color != colors[path[index + 1]])
    after = after_one or after_two

    before_one = (index - 1 < 0) or (my_color != colors[path[index - 1]])
    before_two = (index - 2 < 0) or (my_color != colors[path[index - 2]])
    before = before_one or before_two

    between = after_one or before_one

    return after and before and between


def edge_difference(index, path, edges, v_edges):
    if index == 0:
        return v_edges[path[0]]
    elif index == len(path):
        return v_edges[path[len(path) - 1]]
    else:
        return v_edges[path[index - 1]] + v_edges[path[index]] - edges[path[index - 1]][path[index]]


def insertion(edges, colors, N, used_vertices, path, vertex):
    v_edges = edges[vertex]
    my_color = colors[vertex]

    min_weight = float("inf")
    min_position = None

    for i in range(len(path) + 1):
        validity = color_valid(i, path, colors, my_color)
        weight = edge_difference(i, path, edges, v_edges)
        if validity and weight < min_weight:
            min_weight = weight
            min_position = i
    if min_position == None:
        return "FAIL"
    return path[:min_position] + [vertex] + path[min_position:]


def super_kopt_helper(edges, colors, path, i, results):
    results[i-4] = super_kopt(edges, colors, path, i)



def lin_kernigan_iteration(path, edges, colors):
    results = [None for _ in range(2)]
    threads = []
    for i in range(4,6):
        t = threading.Thread(target=super_kopt_helper, args=(edges, colors, path, i, results))
        threads.append(t)
        t.start()

    for i in range(len(threads)):
        threads[i].join()

    k_is_four = results[0]
    k_is_five = results[1]

    if sanity.weight(k_is_five, edges) < sanity.weight(k_is_four, edges):
        return k_is_five
    else:
        return k_is_four


def lin_kernigan_total(path, edges, colors, i=100000):
    for _ in range(i):
        path = lin_kernigan_iteration(path, edges, colors)
    return path


def supreme_annealing(path, edges, colors, r = 20):

    best_path = path
    best_score = sanity.weight(path, edges)
    curr_path = path

    for _ in range(r):
        curr_path = lin_kernigan_total(curr_path, edges, colors)
        score = sanity.weight(curr_path, edges)
        if score < best_score:
            best_path = curr_path
            best_score = score
        curr_path = random_kopt(edges, colors, curr_path, 4)

    return best_path










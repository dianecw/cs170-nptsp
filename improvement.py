import random
import itertools
import sanity
import threading

""" Regular k-opt, finds k random edges, breaks them, and recombines them into 
    the best permutation possible.
"""
def super_kopt(edges, colors, path, k):
    N = len(path)
    random_edges = sorted(random.sample(range(0, N), k)) + [N]
    start = 0
    subpaths = []
    for i in range(k+1):
        subpaths.append(path[start:random_edges[i]])
        start = random_edges[i]
    subpaths = list(filter(lambda x :len(x) > 0, subpaths))
    permutations = itertools.permutations(subpaths)
    optimal = sanity.weight(path,edges)
    optimal_path = path 
    path = next(permutations)
    while path != None:
        path = [item for sublist in path for item in sublist]
        weight = sanity.weight(path,edges)
        if optimal > weight and sanity.is_valid_path(path,colors, False):
            optimal = weight
            optimal_path = path
        try:
            path = next(permutations)
        except StopIteration:
            path = None
    return optimal_path

""" Purposely targest the heaviest edges in the graph to break and recombine.
"""
def targeted_k_opt(edges, colors, path, k):

    biggest_edge = None
    biggest_edge_length = -1
    for i in range(1, len(path)):
        if edges[i-1][i] > biggest_edge_length:
            biggest_edge_length = edges[i-1][i]
            biggest_edge = i
    N = len(path)
    random_edges = random.sample(range(0, N), k - 2) + [N, biggest_edge]
    random_edges = sorted(random_edges)
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
        path = [item for sublist in path for item in sublist]
        weight = sanity.weight(path,edges)
        if optimal > weight and sanity.is_valid_path(path,colors, False):
            optimal = weight
            optimal_path = path
        try:
            path = next(permutations)
        except StopIteration:
            path = None
    return optimal_path

""" For purposes of annealing.  Randomly chooses a permutation with no regard
    to how good or bad it is.
"""
def random_kopt(edges, colors, path, k):
    N = len(path)
    random_edges = sorted(random.sample(range(0, N), k)) + [N]
    start = 0
    subpaths = []
    for i in range(k+1):
        subpaths.append(path[start:random_edges[i]])
        start = random_edges[i]
    subpaths = list(filter(lambda x :len(x) > 0, subpaths))
    permutations = itertools.permutations(subpaths)
    path = next(permutations)
    path_list = []
    while path != None:
        path = [item for sublist in path for item in sublist]
        weight = sanity.weight(path,edges)
        if sanity.is_valid_path(path,colors, False):
            path_list = path_list + [path]
        try:
            path = next(permutations)
        except StopIteration:
            path = None

    if len(path_list) == 0:
        return random_kopt(edges, colors, path, k)
    else:
        rand = random.randint(0,len(path_list)-1)
        return path_list[rand]

def somewhat_random_super_kopt(edges, colors, path, k):
    N = len(path)

    max_edge, max_index = -1, -1
    for i in range(len(path) - 1):
        vertex, next = path[i], path[i+1]
        weight = edges[vertex][next]
        if weight > max_edge:
            max_edge = weight
            max_index = i

    random_edges = sorted(random.sample(range(0, N), k-1) + [i] + [N])
    start = 0
    subpaths = []
    for i in range(k+1):
        subpaths.append(path[start:random_edges[i]])
        start = random_edges[i]
    subpaths = list(filter(lambda x :len(x) > 0, subpaths))
    permutations = itertools.permutations(subpaths)
    path = next(permutations)
    path_list = []
    while path != None:
        path = [item for sublist in path for item in sublist]
        weight = sanity.weight(path,edges)
        if sanity.is_valid_path(path,colors, False):
            path_list = path_list + [path]
        try:
            path = next(permutations)
        except StopIteration:
            path = None

    if len(path_list) == 0:
        return random_kopt(edges, colors, path, k)
    else:
        rand = random.randint(0,len(path_list)-1)
        return path_list[rand]

"""Runs super_kopt and stores it into results
"""
def super_kopt_helper(edges, colors, path, i, results):
    results[i-4] = super_kopt(edges, colors, path, i)

""" LK iterations.  Threaded for performance improvement.  
"""
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

""" Runs LK i times.
"""
def lin_kernigan_total(path, edges, colors, i=1000):
    for _ in range(i):
        path = lin_kernigan_iteration(path, edges, colors)
    return path

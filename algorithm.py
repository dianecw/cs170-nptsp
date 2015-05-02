import random
import itertools
import sanity
import threading
import construction
import improvement

"""     Runs construct i times and takes the best construction.
"""
def find_good_construction(edges, colors, N, selection_method=construction.randomly_select, i=10000):
    best = None
    best_val = float('inf')
    for _ in range(i):
        path = construct(edges, colors, N)
        weight = sanity.weight(path, edges) 
        if sanity.is_valid_path(path, colors) and weight < best_val:
            best_val = weight
            best = path
    return best



"""     Constructs a path using selection_method for selecting vertices and then adds them
        to the path using the insertion method. 
"""     
def construct(edges, colors, N, selection_method=construction.randomly_select):
    used_vertices = set()
    not_used_vertices = set()
    for i in range(0, N):
        not_used_vertices.add(i)
    path = []

    # First Vertex
    vertex = construction.randomly_select(N, not_used_vertices, used_vertices, edges)
    path = [] + [vertex]
    used_vertices.add(vertex)
    not_used_vertices.remove(vertex)

    for i in range(1, N):
        newpath = "FAIL"
        while newpath == "FAIL":
            vertex = selection_method(N, not_used_vertices, used_vertices, edges)
            newpath = construction.insertion(edges, colors, N, used_vertices, path, vertex)
        path = newpath
        used_vertices.add(vertex)
        not_used_vertices.remove(vertex)

    return path



"""     Improves the path using Lyn-Kernigan in addition with a form of annealing.
        We anneal r times and k-opt i times.
"""     
def improve(path, edges, colors, r=10, i=1000):
    best_path = path
    best_score = sanity.weight(path, edges)
    curr_path = path

    for _ in range(r):
        curr_path = improvement.lin_kernigan_total(curr_path, edges, colors, i)
        score = sanity.weight(curr_path, edges)
        if score < best_score:
            best_path = curr_path
            best_score = score
        curr_path = improvement.random_kopt(edges, colors, curr_path, 4)

    return best_path




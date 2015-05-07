import random
import itertools
import sanity
import threading
import construction
import improvement

"""     Runs construct i times and takes the best construction.
"""
def find_good_construction(edges, colors, N, selection_method=construction.randomly_select, i=100):
    best = None
    best_val = float('inf')
    for _ in range(i):
        path = None
        while path == None:
            path = construct(edges, colors, N, selection_method)
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
    vertex = construction.randomly_select(N, not_used_vertices, used_vertices, edges, path)
    path = [] + [vertex]
    used_vertices.add(vertex)
    not_used_vertices.remove(vertex)

    for i in range(1, N):
        newpath = "FAIL"
        failcount = -1
        while newpath == "FAIL":
            failcount +=1
            vertex = selection_method(N, not_used_vertices, used_vertices, edges, path)
            if vertex == False:
                return None
            newpath = construction.insertion(edges, colors, N, used_vertices, path, vertex)
            if failcount == 10: 
                return None 
        path = newpath
        used_vertices.add(vertex)
        not_used_vertices.remove(vertex)

    return path



"""     Improves the path using Lyn-Kernigan in addition with a form of annealing.
        We anneal r times and k-opt i times.
"""     
def improve(path, edges, colors, r=100, i=100):
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


def targeted_improve(path, edges, colors, i=100):
    best_path = path
    best_score = sanity.weight(path, edges)
    curr_path = path

    for _ in range(i):
        curr_path = improvement.targeted_k_opt(edges, colors, path, 4)
        score = sanity.weight(curr_path, edges)
        if score < best_score:
            best_path = curr_path
            best_score = score

    return best_path




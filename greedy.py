from collections import defaultdict
import sanity
import construction
import random
import algorithm

""" Runs greedy i times and takes the best greedy path.
"""
def good_greedy(edges, colors, N, j = 100):
    best_path = None
    best_weight = float("inf")
    for i in range(N):
        path = greedy(i, edges, colors, N)
        if path == "FAIL": continue
        weight = sanity.weight(path, edges)
        if sanity.is_valid_path(path, colors) and weight < best_weight:
            best_path, best_weight = path, weight
    if best_path == None: return algorithm.find_good_construction(edges, colors, N)
    return best_path


""" Finds best greedy path from a random starting vertex.
"""
def greedy(start, edges, colors, N):
    vertex = start
    path = [vertex]
    used_vertices = set()
    used_vertices.add(vertex)
    for i in range(1,N):
        vertex = greedy_next_vertex(path, colors, edges, vertex, used_vertices, N)
        if vertex == "FAIL": return "FAIL"
        path += [vertex]
        used_vertices.add(vertex)
    return path


""" Subroutine to find the best next vertex that hasn't yet been used.
    It starts by creating a dictionary of all vertices associated with 
    their distance from the current vertex, removes all vertices that
    have already been used, and then creates a new dictionary where each
    value contains a list of all vertices with that weight.  
"""
def greedy_next_vertex(path, colors, edges, vertex, used_vertices, N):
    d = dict()
    weights = edges[vertex]
    for i in range(N):
        d[i] = weights[i]
    for e in used_vertices:
        d.pop(e) 
    new_d = defaultdict(list)
    for k,v in d.iteritems():
        new_d[v].append(k)
    final_list = []
    for k in sorted(new_d.items()):
        final_list += k[1]
    for e in final_list:
        if construction.color_valid(len(path), path, colors, colors[e]):
            return e
    return "FAIL"
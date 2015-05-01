import random
import itertools
import sanity
import threading

def randomly_select(N, not_used_vertices, used_vertices, edges):
    num = random.randint(0, N - 1)
    if num in not_used_vertices:
        return num
    else:
        return randomly_select(N, not_used_vertices, used_vertices, edges)


def supreme_farthest_insertion(N, non_used_verticies, used_vertices, edges):
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

    
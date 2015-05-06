import itertools

def is_valid_path(path, colors, print_path = True):
    c = []
    for i in range(len(path)-3):
        
        if path[i] == 101 or path[i+1] == 101 or path[i+2] == 101 or path[i+3] == 101:
            return False

        color = colors[path[i]]
        c.append(color)
        color2 = colors[path[i+1]]
        color3 = colors[path[i+2]]
        color4 = colors[path[i+3]]

        if color == color2 and color2 == color3 and color3 == color4:
            c.append(color2)
            c.append(color3)
            if print_path:
                print(c)
            return False 
    return True 


def weight(path, edges):
    total = 0
    for i in range(len(path)-1):
        total += edges[path[i]][path[i+1]]
    return total


def normalize(assign, N):
    new = [-1] * N
    for i in range(N):
        new[i] = assign[i] + 1
    return new

def denormalize(assign, N):
    new = [-1] * N
    for i in range(N):
        new[i] = assign[i] - 1
    return new


def supreme_brute_generator(edges,colors,N):
    permutations = itertools.permutations([i for i in range(N)])
    optimal = float("inf")
    optimal_path = None
    path = next(permutations)
    while path != None:
        total = 0
        for i in range(len(path)-1):
            total += edges[path[i]][path[i+1]]
        if total < optimal and is_valid_path(path,colors, False):
            optimal_path = path
            optimal = total
        try:
            path = next(permutations)
        except StopIteration:
            path = None
    return optimal, optimal_path 




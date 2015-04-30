import random

def get_approx_path(edges, colors, N):
	used_vertices = set()
	path = []

	# First Vertex
	vertex = randomly_select(N, used_vertices)
	path = [] + [vertex]
	used_vertices.add(vertex)

	for i in range(1,N):
		vertex = randomly_select(N, used_vertices)
		print vertex
		path = insertion(edges, color, N, used_vertices, path, vertex)

	return path


def randomly_select(N, used_vertices):
	num = random.randint(0,N-1)
	if num not in used_vertices:
		return num
	else:
		return randomly_select(N, used_vertices)

def supreme_farthest_insertion(edges, non_used_verticies, used_vertices):
    best = None
    best_val = float('-inf')
    for v in non_used_verticies:
        closest_dist = float('inf')
        for v2 in used_vertices:
            cur_dist = edge[v,v2]
            if closest_dist > cur_dist:
                closest_dist = cur_dist
        if best_val < closest_dist:
            best_val = closest_dist
            best = v
    return best

def spreme_brute(edges):
    path = set()
    

def supreme_kopt(k,edges,path):
    return None


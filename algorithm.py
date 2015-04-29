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

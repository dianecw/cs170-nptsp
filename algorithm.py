import random

def construct_path(edges, colors, N):
	used_vertices = set()
	not_used_vertices = set()
	for i in range(0,N):
		not_used_vertices.add(i)
	path = []

	# First Vertex
	vertex = randomly_select(N, used_vertices)
	path = [] + [vertex]
	used_vertices.add(vertex)
	not_used_vertices.remove(vertex)

	for i in range(1,N):
		vertex = randomly_select(N, used_vertices)
		path = insertion(edges, color, N, used_vertices, path, vertex)
		used_vertices.add(vertex)
		not_used_vertices.remove(vertex)

	return path


def randomly_select(N, not_used_vertices):
	num = random.randint(0,N-1)
	if num in not_used_vertices:
		return num
	else:
		return randomly_select(N, used_vertices)

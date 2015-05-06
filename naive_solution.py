def solve(edges, color, N):
	assign = [-1] * N

	assign[0] = 0
	already_used = set()
	already_used.add(0)

	for i in range(1,N):
		e = edges[assign[i-1]]
		min_edge = 101
		min_edge_vertex = 101

		for v in range(0, N):
			weight = e[v]
			if v not in already_used and weight < min_edge and v != assign[i-1]:

				if color[v] != color[assign[i-1]] or i-2 < 0 or color[v] != color[assign[i-1]]:
					min_edge = weight
					min_edge_vertex = v

		assign[i] = min_edge_vertex
		already_used.add(min_edge_vertex)

	return assign


def normalize(assign, N):
	new = [-1] * N
	for i in range(N):
		new[i] = assign[i]+1

	return new





































	return assign

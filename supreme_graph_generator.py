import random


def generate_graph(n, fileName):
	"""
	Generates an input file with name fileName.in and n vertices.
	"""
	if n % 2 != 0:
		return
	file = open(fileName + '.in', 'w+')
	file.write(str(n) + '\n')
	#file.write('hello')
	edge_matrix = [[0 for x in range(n)] for x in range(n)] 
	for i in range(n):
		edge_matrix[i][i] = 0
	for i in range(n):
		for j in range(i+1,n):
			num = random.randint(0, 100)
			edge_matrix[i][j] = num
			edge_matrix[j][i] = num

	for i in range(n):
		for j in range(n):
			file.write(str(edge_matrix[i][j]))
			if j != (n-1):
				file.write(' ')
		file.write('\n')

	#generating color values
	num_red = 0
	num_blue = 0
	for i in range(n):
		if num_red >= n/2:
			file.write('B')
			continue
		if num_blue >= n/2:
			file.write('R')
			continue
		num = random.randint(0, 1)
		if num == 0:
			file.write('R')
			num_red += 1
		else:
			file.write('B')
			num_blue += 1

for i in range(1,11):
	generate_graph(50, '50-node-' + str(i))
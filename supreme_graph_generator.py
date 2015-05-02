import random


def generate_graph(n, fileName):
	"""
	Generates an input file with name fileName.in and n vertices.
	"""
	if n % 2 != 0:
		return
	file = open('./test_cases/' + fileName + '.in', 'w+')
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

def construct_best_path(N,low = 0 ,high = 100, double_prob = .5):
    best_path = [random.randint(low,high) for _ in range(N-1)] 
    best_path_colors = [0]*N
    best_path_colors[0] = random.choice([0,1])
    best_path_colors[1] = best_path_colors[0] if random.random() < double_prob else 1- best_path_colors[0]
    num_blue = 0
    num_red = 0
    if best_path_colors[0] == 0:
        num_blue +=1
    else:
        num_red +=1
    if best_path_colors[1] == 0:
        num_blue +=1
    else:
        num_red+=1
    for i in range(2,N):
        if num_red >= N/2:
            best_path_colors[i] = 0
            num_blue +=1
            continue
        if num_blue >= N/2:
            num_red +=1
            best_path_colors[i] = 1
            continue
        rand = random.random()
        if rand < double_prob:
            if best_path_colors[i-1] != best_path_colors[i-2]:
                best_path_colors[i] = best_path_colors[i-1]
                if best_path_colors[i-1] == 0:
                    num_blue +=1
                else:
                    num_red +=1
            else:
                best_path_colors[i] = 1 - best_path_colors[i-1]
                if best_path_colors[i-1] == 1:
                    num_blue +=1
                else:
                    num_red +=1

        else:
            best_path_colors[i] = 1-best_path_colors[i-1]
            if best_path_colors[i] == 1:
                num_red +=1
            else:
                num_blue +=1
    return (best_path, best_path_colors)

def crazy_graph(N, fileName, double_prob = .5):
    best_path, best_path_colors = construct_best_path(N, 0, 50, double_prob)
    distance_lookup_table = [[0 for x in range(N)] for x in range(N)]
    distance_lookup_table[0][1] = best_path[0]
    print(sum(best_path))
    #for i in range(0,N):
     #   for j in range(i+1,N):
      #      distance_lookup_table[i][j] =  distance_lookup_table[i][j-1] + best_path[j-1]
       #     distance_lookup_table[j][i] = distance_lookup_table[i][j]

    edge_matrix = [[0 for x in range(N)] for x in range(N)]
    for i in range(N):
        for j in range(i+1,N):
            if (abs(i - j) <= 1):
                edge_matrix[i][j] = best_path[i]
            color_triple = False
            if( i-1 < 0):
                minedge = best_path[i-1]
                color_triple = best_path_colors[i-1] == best_path_colors[i]
            if (j- 1 > 0):
                minedge =max(minedge, best_path[j-1])
            if (i < N-2):
                minedge = max(minedge,best_path[i])
            if (j < N -2):
                minedge = max(minedge,best_path[j])
                color_triple = color_triple or best_path_colors[j-1] == best_path_colors[j]
           # if best_path_colors[i] == best_path_colors[j] and color_triple and minedge > 0:
           #     minedge *= (minedge - 10)//minedge
           # else:
            #    if(random.random() < .02 and minedge > 0):
            #        minedge *= (minedge - 10)//minedge
            minedge = max(0, minedge)
            edge_matrix[i][j] = random.randint(minedge,100)
            edge_matrix[j][i] = edge_matrix[i][j]

    if N % 2 != 0:
    	return
    bijection = [i for i in range(N)]
    random.shuffle(bijection)
    file = open('./test_cases2/' + fileName + '.in', 'w+')
    file.write(str(N) + '\n')
    for i in range(N):
	for j in range(N):
	    file.write(str(edge_matrix[bijection[i]][bijection[j]]))
	    if j != (N-1):
		file.write(' ')
	file.write('\n')

	#generating color values
    for i in range(N):
        if best_path_colors[bijection[i]] == 0:
	    file.write('B')
	else:
	    file.write('R')
            

        


for i in range(1,51):
        print("path" + str(i))
	crazy_graph(50, 'cray' + str(i))

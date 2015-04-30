def sanity_checker(path, colors):
    for i in range(len(path)-2):
        color = colors[i]
        color2 = colors[i+1]
        color3 = colors[i+2]
        return "FAIL" if not (color == color2 and color2 == color3)

def weight(path, edges):
    total = 0
    for i in range(len(path - 1)):
        total += edges[path[i]][path[i+1]]
    return total
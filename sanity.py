def sanity_checker(path, colors):
    c = []
    for i in range(len(path)):
        c = c + [colors[path[i]]]
    print c

    for i in range(len(path)-2):

        color = colors[path[i]]
        color2 = colors[path[i+1]]
        color3 = colors[path[i+2]]

        if color == color2 and color2 == color3:
            return "FAIL"
    return "PASS"

def weight(path, edges):
    total = 0
    for i in range(len(path)-1):
        total += edges[path[i]][path[i+1]]
    return total
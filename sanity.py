def sanity_checker(path, colors):
    for i in range(len(path)-2):
        color = colors[i]
        color2 = colors[i+1]
        color3 = colors[i+2]
        return "FAIL" if not (color == color2 and color2 == color3)
import random
import json
import os

def generuj_graf(graph,v, b):
    for i in range(1,v):
        j = 0
        while j < i:
            if random.randrange(100) < b:
                graph[i][j] = 1
                graph[j][i] = 1
            j += 1

    for i in range(v):
        deg = 0
        for j in range(v):
            if graph[i][j] > 0:
                deg += 1
        if deg % 2 != 0:
            x = random.randrange(v-i-1) + i + 1
            if graph[i][x] > 0:
                graph[i][x] = 0
                graph[x][i] = 0
            else:
                graph[i][x] = 1
                graph[x][i] = 1

def save(graph, dir, filename):
    if not os.path.exists(dir):
        os.makedirs(dir)
    with open(dir + '/' + filename, 'w') as file:
        json.dump(graph, file)

def generate():
    sizes = [i * 5 for i in range(5, 21)]
    bList = [30, 50, 70]
    for b in bList:
        for v in sizes:
            graph = [[0 for i in range(v)] for i in range(v)]
            generuj_graf(graph,v, b)
            save(graph, "./instances-{0}".format(b), "{0}.txt".format(v))

generate()


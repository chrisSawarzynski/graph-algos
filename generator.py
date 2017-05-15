import random


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

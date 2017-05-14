import graph_tools
import random


def generate_euler_graph(v=10, percent= 100):
    import math
    from graph_tools import count_edges

    graph = [[int(k != i) for k in range(v)] for i in range(v)]
    max_e = v * (v - 1) / 2
    e = math.ceil(max_e / 100 * percent)

    while count_edges(graph) != e:
        for i in range(v):
            if graph_tools.count_incidental(graph, i) % 2:
                pass

    return graph

# print(genetic_euler(1000, 70))

def create_connected_euler_graph(graph):
    import random
    import graph_tools

    added = [0]
    while len(added) != len(graph):
        k = random.randint(0, len(graph) - 1)
        while k in added:
            k = random.randint(0, len(graph) - 1)
        graph_tools.create_edge(graph, added[-1], k)
    graph.graph_tools.create_edge(graph, added[0], added[-1])




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

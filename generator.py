import graph_tools

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


def genetic_euler(v=10, percent = 100):
    import random
    import json

    e = v * (v - 1) / 2 / 100 * percent
    best = [[int(k != i) for k in range(v)] for i in range(v)]
    for i in range(10000000000000000000000000000000):
        graph = [[0 for k in range(v)] for i in range(v)]
        for i in range(1, v):
            for k in range(i):
                if random.randint(0, 1):
                    graph_tools.create_edge(graph, i, k)
                else:
                    graph_tools.delete_edge(graph, i, k)

        if graph_tools.is_euler_graph(graph) and abs(graph_tools.count_edges(graph) - e) < abs(graph_tools.count_edges(best) - e):
            best = graph
            with open("result.txt", "w") as fh:
                json.dump(best, fh)
    return best

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



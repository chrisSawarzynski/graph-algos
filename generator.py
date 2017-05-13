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


        



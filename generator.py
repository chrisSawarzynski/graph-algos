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


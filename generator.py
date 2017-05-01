def generate_euler_graph(v=10, e=100):
    graph = [[int(k != i) for k in range(v)] for i in range(v)]

    return graph


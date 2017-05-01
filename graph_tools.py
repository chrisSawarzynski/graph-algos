
def is_incidental(graph, v1, v2):
    if graph[v1][v2] == 1 and graph[v2][v1] == 1:
        return True
    return False

def create_edge(graph, v1, v2):
    graph[v1][v2] = 1
    graph[v2][v1] = 1


def delete_edge(graph, v1, v2):
    graph[v1][v2] = 0
    graph[v2][v1] = 0


def count_incidental(graph, v):
    from functools import reduce
    return reduce(lambda a, b: a+b, graph[v])

def is_euler_graph(graph):
    allEven = True
    for i in range(len(graph)):
        if count_incidental(graph,i) % 2:
            allEven = False
    return allEven
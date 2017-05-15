from functools import reduce
import graph_tools


def matrix_to_list(matrix):
    graph = [graph_tools.get_incidentals(matrix, v) for v in range(len(matrix))]
    return graph



def is_incidental(graph, v1, v2):
    return v2 in graph[v1] and v1 in graph[v2]

def create_edge(graph, v1, v2):
    if not is_incidental(graph, v1, v2):
        graph[v1].append(v2)
        graph[v2].append(v1)

def delete_edge(graph, v1, v2):
    if is_incidental(graph, v1, v2):
        graph[v1].remove(v2)
        graph[v2].remove(v1)

def count_edges(graph):
    return reduce(lambda x, y: x + len(y), graph) / 2


def count_incidental(graph, v):
    return len(graph[v])

def is_connected(graph):
    # with first element on init
    visited = [0]
    to_visit = [0]

    while to_visit:
        current = to_visit.pop()

        for i in graph[current]:
            if i not in visited:
                visited.append(i)
                to_visit.append(i)

    return len(visited) == len(graph)


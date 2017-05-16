from functools import reduce
import graph_tools
import json


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


def get_graphs():
    graphs = {}
    sizes = [i * 5 for i in range(5, 21)]
    bList = [30, 50, 70]
    for b in bList:
        graphs[b] = {}
        for v in sizes:
            with open("./instances-{0}/{1}.txt".format(b, v), 'r') as file:
                json_graph = json.load(file)
                graphs[b][v] = json_graph
    return graphs


import tools

def find_cycle(graph, v, cycle):
    for i in graph[v]:
            tools.delete_edge(graph, v, i)
            find_cycle(graph, i, cycle)
    cycle.append(v)

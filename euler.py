import graph_tools

def find_cycle(graph, v, cycle):
    for i in range(len(graph)):
        while graph[v][i]:
            graph_tools.delete_edge(graph, v, i)
            find_cycle(graph, i, cycle)
    cycle.append(v)

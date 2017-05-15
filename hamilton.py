import tools
from copy import copy

cycles = []


def find_cycle(graph, v, cycle):
    cycle.append(v)
    incidentals = filter(lambda x: x not in cycle, graph[v])

    for w in incidentals:
        if len(cycle) != len(graph):
            find_cycle(graph, w, cycle)

    if len(cycle) != len(graph) or not tools.is_incidental(graph, cycle[0], cycle[-1]):
        cycle.remove(v)


def find_all_cycles(graph, v, cycle):
    cycle.append(v)
    incidentals = filter(lambda x: x not in cycle, graph[v])

    for w in incidentals:
        find_cycle(graph, w, cycle)

    if len(cycle) != len(graph) or not tools.is_incidental(graph, cycle[0], cycle[-1]):
        cycle.remove(v)
    else:
        cycles.append(copy(cycle))
        cycle.remove(v)


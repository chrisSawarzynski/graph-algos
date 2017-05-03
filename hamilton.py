import graph_tools

def find_cycle(graph, v, cycle):
    cycle.append(v)

    incidentals = graph_tools.get_incidentals(graph, v)
    incidentals = filter(lambda x : x not in cycle, incidentals)

    for w in incidentals:
        find_cycle(graph, w, cycle)
    
    if len(cycle) != len(graph) or graph_tools.is_incidental(graph, cycle[0], cycle[-1]) == False:
        cycle.remove(v)

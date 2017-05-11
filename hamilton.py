import graph_tools
from copy import copy

cycles = []


def find_cycle(graph, v, cycle):
    cycle.append(v)
    incidentals = graph_tools.get_incidentals(graph, v)
    incidentals = filter(lambda x: x not in cycle, incidentals)

    for w in incidentals:
        find_cycle(graph, w, cycle)

    if len(cycle) != len(graph) or not graph_tools.is_incidental(graph, cycle[0], cycle[-1]):
        cycle.remove(v)
    else:
        cycles.append(copy(cycle))
        cycle.remove(v)

# 4  Hamilton(v)
# 5  {
# 6          V.Add(v);
# 7          dla każdego nieodwiedzonego sšsiada w wierzchołka v
# 8          {
# 9              Hamilton(w);
# 10          }
# 11          if V zawiera wszystkie wierzchołki grafu i istnieje krawęd z v do ródła
# 12          {
# 13              cykl znaleziony
# 14          }
# 15          else
# 16          {
# 17              V.Remove(v);
# 18          }
# 19  }

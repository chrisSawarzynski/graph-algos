import generator
import euler
import hamilton
import graph_tools
from copy import copy

original_graph = generator.generate_euler_graph(3)


if graph_tools.is_euler_graph(original_graph):
    cycle = []
    graph = copy(original_graph)
    hamilton.find_cycle(graph, 0, cycle)
    print("hamilton:")
    print(cycle)


    cycle = []
    graph = copy(original_graph)
    euler.find_cycle(graph, 0, cycle)
    print("euler:")
    print(cycle)

else:
    print("It's not euler graph")
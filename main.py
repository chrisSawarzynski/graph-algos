import generator
import euler
import hamilton
import graph_tools
from copy import copy
import time

def execution_time(function, instance):
    cycle = []
    start_time = time.time()
    function(copy(instance), 0, cycle)
    elapsed_time = time.time() - start_time
    return elapsed_time


graphs = graph_tools.get_graphs()
result = ""

functions = {
    "Hamilton cycle":hamilton.find_cycle,
    "Euler cycle":euler.find_cycle
}

for function in functions.keys():
    result += "{0}\n".format(function)
    for graph in graphs.keys():
        if graph_tools.is_euler_graph(graphs[graph][2]):
            result += "{0}\t{1}\n".format(graph, execution_time(functions[function], copy(graphs[graph][2])))
        else:
            print("It's not euler graph")
            print(graphs[graph][2])

file = open("result30.txt", "w")
file.write(result)
print(result)
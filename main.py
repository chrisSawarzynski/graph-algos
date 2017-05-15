import generator
import euler
import hamilton
import graph_tools
from copy import copy
import time
import tools

def execution_time(function, instance):
    cycle = []
    start_time = time.time()
    function(instance, 0, cycle)
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
        if graph_tools.is_euler_graph(graphs[graph][0]):
            exec_time = execution_time(functions[function], tools.matrix_to_list(graphs[graph][0]))
            result += "{0}\t{1}\n".format(graph, exec_time)
        else:
            print("It's not euler graph")

with open("result30.txt", "a") as file:
    file.write(result)

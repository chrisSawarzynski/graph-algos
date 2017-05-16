import threading
import euler
import hamilton
import graph_tools
from copy import copy
import time
import tools
import sys

threading.stack_size(67108864) # 64MB stack
sys.setrecursionlimit(2**20) # something real big


def execution_time(function, instance):
    cycle = []
    start_time = time.time()
    function(instance, 0, cycle)
    elapsed_time = time.time() - start_time
    return elapsed_time


graphs = tools.get_graphs()
result = ""

functions = {
    "Hamilton cycle":hamilton.find_cycle,
    "Hamilton cycles":hamilton.find_all_cycles,
    "Euler cycle":euler.find_cycle
}

# for function in functions.keys():
function = "Euler cycle"
result += "{0}\n".format(function)
for b in graphs.keys():
    result += "{0}\n".format(b)
    for v in graphs[b].keys():
        if graphs[b][v] and graph_tools.is_euler_graph(graphs[b][v]):
            result += "{0}\t{1}\n".format(v, execution_time(functions[function], tools.matrix_to_list(graphs[b][v])))
        else:
            result += "its not an euler graph\n"
        graph_tools.save_to_file(result)
        result = ""


import generator
import euler

graph = generator.generate_euler_graph()
cycle = []
euler.find_cycle(graph, 0, cycle)
print(cycle)

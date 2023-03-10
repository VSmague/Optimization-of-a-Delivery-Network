from graph import *


data_path = "input/"
file_name = "network.03.in"

g = Graph.graph_from_file(data_path + file_name)
print(g)

print(Graph.kruskal(g))
print(Graph.power_min_ameliore(g, 1, 4))
print(Graph.min_power2(g, 1, 4))
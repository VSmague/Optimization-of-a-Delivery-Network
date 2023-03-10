from graph import *


data_path = "input/"
file_name = "network.03.in"

g = Graph.graph_from_file(data_path + file_name)
print(g)

print(Graph.kruskal(g))
print(Graph.power_min_ameliore(g, 1, 4))
#print(Graph.min_power2(g, 1, 4))

import time
trajets=[]
temps=[]
file=open("input/routes.2.in", "r")
for k in range(10):
    edge = list(map(int, file.readline().split()))
    if len(edge)==1:
        nb_trajets=edge[0]
    else:
        node1, node2, gain = edge
        trajets.append((node1,node2))
file.close()
print(nb_trajets)
h=Graph.graph_from_file("input/network.2.in")
for src,dest in trajets:
    t_start=time.perf_counter()
    Graph.power_min_ameliore(h,src,dest)
    t_stop=time.perf_counter()
    temps.append(t_stop-t_start)
print("temps pour l'ensemble des trajets en secondes:",nb_trajets*sum(temps)/len(temps))
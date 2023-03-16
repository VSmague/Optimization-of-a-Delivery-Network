from graph import *

data_path = "input/"
file_name = "network.04.in"

g = Graph.graph_from_file(data_path + file_name)
print(g)
print(Graph.min_power2(g, 1, 4))
#g.representation(("test"))
print(Graph.kruskal(g))
print(Graph.min_power_ameliore(g, 1, 4))


def temps(f,k):
    import time
    trajets=[]
    temps=[]
    file=open("input/routes."+str(k)+".in", "r")
    for i in range(10):
        edge = list(map(int, file.readline().split()))
        if len(edge)==1:
            nb_trajets=edge[0]
        else:
            node1, node2, gain = edge
            trajets.append((node1,node2))
    file.close()
    print(nb_trajets)
    h=Graph.graph_from_file("input/network."+str(k)+".in")
    for src,dest in trajets:
        t_start=time.perf_counter()
        f(h,src,dest)
        t_stop=time.perf_counter()
        temps.append(t_stop-t_start)
        print("ok")
    print("temps pour l'ensemble des trajets de la route"+str(k)+" en secondes:",nb_trajets*sum(temps)/len(temps))
    return nb_trajets*sum(temps)/len(temps)
temps(Graph.min_power2,2)
#probleme pour routes plus grandes que 2 car dfs non recursif terminal, donc trop de profondeur de recursivité, à corriger!
#update, c'est corrigé
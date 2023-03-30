from graph import *

data_path = "input/"
file_name = "network.00.in"

g = Graph.graph_from_file(data_path + file_name)
print(g)
print(Graph.min_power2(g, 1, 4))
#g.representation(("test"))
print(Graph.kruskal(g))
print(Graph.min_power_ameliore(g, 7, 2))
print(Graph.min_power_ameliore2(g, 7, 2))


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
    x=Graph.pre_travail(h)
    for src,dest in trajets:
        t_start=time.perf_counter()
        f(x,src,dest)
        t_stop=time.perf_counter()
        temps.append(t_stop-t_start)
        print("ok")
    print("temps pour l'ensemble des trajets de la route"+str(k)+" en secondes:",nb_trajets*sum(temps)/len(temps))
    return nb_trajets*sum(temps)/len(temps)
temps(Graph.min_power_ameliore2,5)

def trucks(k):
    file=open("input/trucks."+str(k)+".in","r")
    l_trucks=[]
    nb_truck=list(map(int,file.readline().split()))[0]
    for i in range(nb_truck):
        truck=list(map(int,file.readline().split()))
        l_trucks.append(truck)
    file.close()
    return l_trucks

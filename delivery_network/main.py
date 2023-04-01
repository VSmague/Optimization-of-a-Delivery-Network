from graph import *

data_path = "input/"
file_name = "network.1.in"

#g = Graph.graph_from_file(data_path + file_name)
#g.representation(("test"))
#print(Graph.min_power_ameliore2(g, 3, 18))
#print(Graph.min_power_ameliore(Graph.pre_travail(g), 3, 18))


def temps_10(f,k):
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
    solution=[]
    h=Graph.graph_from_file("input/network."+str(k)+".in")
    for src,dest in trajets:
        t_start=time.perf_counter()
        solution.append(f(h,src,dest))
        t_stop=time.perf_counter()
        temps.append(t_stop-t_start)
    print("temps pour l'ensemble des trajets de la route"+str(k)+" en secondes:",nb_trajets*sum(temps)/len(temps))
    return solution

def temps_15(f,k):
    import time
    solution=[]
    file=open("input/routes."+str(k)+".in", "r")
    nb_trajets=list(map(int, file.readline().split()))[0]
    h=Graph.graph_from_file("input/network."+str(k)+".in")
    x=Graph.pre_travail(h)
    #fichier=open("output/routes."+str(k)+".out","a")
    t_start=time.perf_counter()
    for i in range(nb_trajets):
        src,dest,gain = list(map(int, file.readline().split()))
        path,power=f(x,src,dest)
        #fichier.write(str(power)+"\n")
        solution.append((path,power))
    t_stop=time.perf_counter()
    file.close()
    #fichier.close()
    print("temps pour l'ensemble des trajets de la route"+str(k)+" en secondes:",t_stop-t_start)
    return solution

def trucks(k):
    file=open("input/trucks."+str(k)+".in","r")
    l_trucks=[]
    nb_truck=list(map(int,file.readline().split()))[0]
    for i in range(nb_truck):
        truck=list(map(int,file.readline().split()))
        l_trucks.append(truck)
    file.close()
    return l_trucks

def glouton(k,W):
    file_trajet=open("input/routes."+str(k)+".in", "r")
    file_puissance=open("output/routes."+str(k)+".out","r")
    nb_trajet=list(map(int, file_trajet.readline().split()))[0]
    efficacite=[]
    for i in range(nb_trajet):
        src,dest,gain=list(map(int, file_trajet.readline().split()))
        power=list(map(int, file_puissance.readline().split()))[0]
        efficacite.append(gain/power,power,gain,i+1)
    efficacite.sort(key= lambda x:x[0])
    w_dep=0
    i=0
    while w_dep<W:
    



#for k in range(1,10):
#  temps_15(Graph.min_power_ameliore,k)
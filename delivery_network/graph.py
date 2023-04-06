from graphviz import Graph as gr

def graph_from_file(filename): #questions 1 et 4
    """
    Reads a text file and returns the graph as an object of the Graph class.

    The file should have the following format: 
        The first line of the file is 'n m'
        The next m lines have 'node1 node2 power_min dist' or 'node1 node2 power_min' (if dist is missing, it will be set to 1 by default)
        The nodes (node1, node2) should be named 1..n
        All values are integers.

    Parameters: 
    -----------
    filename: str
        The name of the file

    Outputs: 
    -----------
    g: Graph
        An object of the class Graph with the graph from file_name.
    """
    with open(filename, "r") as file:
        n, m = map(int, file.readline().split())
        g = Graph(range(1, n+1))
        for _ in range(m):
            edge = list(map(int, file.readline().split()))
            if len(edge) == 3:
                node1, node2, power_min = edge
                g.add_edge(node1, node2, power_min) # will add dist=1 by default
            elif len(edge) == 4:
                node1, node2, power_min, dist = edge
                g.add_edge(node1, node2, power_min, dist)
            else:
                raise Exception("Format incorrect")
    return g

class Graph:
    """
    A class representing graphs as adjacency lists and implementing various algorithms on the graphs. Graphs in the class are not oriented. 
    Attributes: 
    -----------
    nodes: NodeType
        A list of nodes. Nodes can be of any immutable type, e.g., integer, float, or string.
        We will usually use a list of integers 1, ..., n.
    graph: dict
        A dictionnary that contains the adjacency list of each node in the form
        graph[node] = [(neighbor1, p1, d1), (neighbor1, p1, d1), ...]
        where p1 is the minimal power on the edge (node, neighbor1) and d1 is the distance on the edge
    nb_nodes: int
        The number of nodes.
    nb_edges: int
        The number of edges. 
    """

    def __init__(self, nodes=[]):
        """
        Initializes the graph with a set of nodes, and no edges. 
        Parameters: 
        -----------
        nodes: list, optional
            A list of nodes. Default is empty.
        """
        self.nodes = nodes
        self.graph = dict([(n, []) for n in nodes])
        self.nb_nodes = len(nodes)
        self.nb_edges = 0
    

    def __str__(self):
        """Prints the graph as a list of neighbors for each node (one per line)"""
        if not self.graph:
            output = "The graph is empty"            
        else:
            output = f"The graph has {self.nb_nodes} nodes and {self.nb_edges} edges.\n"
            for source, destination in self.graph.items():
                output += f"{source}-->{destination}\n"
        return output
    
    def add_edge(self, node1, node2, power_min, dist=1): #question 1
        """
        Adds an edge to the graph. Graphs are not oriented, hence an edge is added to the adjacency list of both end nodes. 

        Parameters: 
        -----------
        node1: NodeType
            First end (node) of the edge
        node2: NodeType
            Second end (node) of the edge
        power_min: numeric (int or float)
            Minimum power on this edge
        dist: numeric (int or float), optional
            Distance between node1 and node2 on the edge. Default is 1.
        """
        if node1 not in self.graph:
            self.graph[node1] = []
            self.nb_nodes += 1
            self.nodes.append(node1)
        if node2 not in self.graph:
            self.graph[node2] = []
            self.nb_nodes += 1
            self.nodes.append(node2)

        self.graph[node1].append((node2, power_min, dist))
        self.graph[node2].append((node1, power_min, dist))
        self.nb_edges += 1
    
    def dfs(self,node,visited_nodes): #question 2
        """ connected_graph = {}for key, values in self.graph.items(): connected_graph[key]=[values[0]]
        on crée un dictionnaire qui prend comme clé le noeud et qui ajoute en valeur seulement le noeud voisin
        le noeud voisin est bien contenu dans values = (nodes2, power_min, dist) """
        """liste de liste : on va faire un dict"""
        component = [node]
        voisins = [node]
        visited_nodes[node] = True
        while component != []:
            node=component[0]
            component=component[1:]
            for neighbour in self.graph[node]:
                neighbour=neighbour[0]
                if not visited_nodes[neighbour]:
                    visited_nodes[neighbour] = True
                    component.append(neighbour)
                    voisins.append(neighbour)
        return voisins

    def connected_components(self): #question 2
        list_components = []
        visited_nodes = {noeud: False for noeud in self.nodes}

        """création d'un dictionnaire de noeuds avec false si non visité"""
        for noeud in self.nodes:
            if not visited_nodes[noeud]:
                list_components.append(Graph.dfs(self,noeud,visited_nodes))
        return list_components

    def connected_components_set(self): #question 2
        return set(map(frozenset, self.connected_components()))
        print(set(map(frozenset, self.connected_components())))
    
    def get_path_with_power(self, src, dest, power): #questions 3 et 5
        list = self.connected_components()
        i = 0
        while i < len(list) and src not in list[i]:
            i += 1
        if i == len(list): 
            return "pas de source"
        if dest not in list[i]:
            return "source et destination non connectées"
        return self.chemin(src, dest, power)

    def chemin(self, s, t, power): #dijkstra pour question 3
        Vu = set()
        d = {s: 0}
        predecesseurs = {}
        suivants = [(0, s)]  # Â tas de couples (d[x],x)
        while suivants != []:
            dx, x = suivants[0]
            suivants=suivants[1:]
            if x in Vu:
                continue
            Vu.add(x)
            for y, p, w in self.graph[x]:
                if y in Vu:
                    continue
                dy = dx + w
                if (y not in d or d[y] > dy) and power >= p:
                    d[y] = dy
                    suivants.append((dy, y))
                    predecesseurs[y] = x
        path = [t]
        if t not in d : return "pas de chemin possible avec cette puissance"
        x = t
        while x != s:
            x = predecesseurs[x]
            path.insert(0, x)
        return path
    
    def min_power_naif(self, src, dest):
        """
        Should return path, min_power.
        """
        p = 0
        while type(self.get_path_with_power(src, dest, p)) == str :
            p += 1
        return self.get_path_with_power(src, dest, p), p
    #on suppose ici que la puissance est toujours un entier naturel

    def min_power(self,src,dest): #question 6 : recherche dichotomique de puissance minimale
        pmin=0
        pmax=0
        for nodes in self.graph:
            for voisins in self.graph[nodes]:
                pmax=max(pmax,voisins[1])
        while pmin+1<pmax:
            p=(pmin+pmax)//2
            if type(Graph.get_path_with_power(self,src,dest,p))==str:
                pmin=p
            else:
                pmax=p
        return Graph.get_path_with_power(self,src,dest,pmax),pmax
    
    def representation(self, nom): #question 7 : représentation visuelle des graphes
        graphe = gr(format='png', engine="circo") 
        key=self.graph.keys()
        sauv=[]
        for i in key: # on crée tous les sommets
            print(i)
            graphe.node(f"{i}",f"{i}")
            for voisin in self.graph[i]:
                if voisin[0] not in sauv:
                    graphe.edge(f"{i}", f"{voisin[0]}", label=f"p={voisin[1]},\n d={voisin[2]}")
            sauv.append(i)
        graphe.render(f"{nom}.dot")
        print(graphe)
        return()
    
    def temps_10(f,k): #question 10
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
        h=graph_from_file("input/network."+str(k)+".in")
        for src,dest in trajets:
            t_start=time.perf_counter()
            solution.append(f(h,src,dest))
            t_stop=time.perf_counter()
            temps.append(t_stop-t_start)
        print("temps pour l'ensemble des trajets de la route"+str(k)+" en secondes:",nb_trajets*sum(temps)/len(temps))
        return solution

    def makeset(pik,rank,node): #pour implémenter Kruskal : question 12
        pik[node]=node
        rank[node]=0
        return None

    def find(pik,node): #pour implémenter Kruskal : question 12
        if pik[node] != node:
            pik[node]= Graph.find(pik,pik[node])
        return pik[node]

    def union(pik,rank,node1,node2): #pour implémenter Kruskal : question 12
        r1=Graph.find(pik,node1)
        r2=Graph.find(pik,node2)
        if r1==r2: return None
        if rank[r1]>rank[r2]:
            pik[r2]=r1
        else:
            pik[r1]=r2
            if rank[r1]==rank[r2]:
                rank[r2]+=1
        return None

    def kruskal(self): #question 12
        pik={}
        rank={}
        for node in self.nodes:
            Graph.makeset(pik,rank,node)
        X=Graph([])
        edges=[]
        for node in self.graph:
            for edge in self.graph[node]:
                edges.append((node,edge[0],edge[1]))
        edges.sort(key =lambda x: x[2])
        for edge in edges:
            if Graph.find(pik,edge[0])!=Graph.find(pik,edge[1]):
                Graph.add_edge(X,edge[0],edge[1],edge[2])
                Graph.union(pik,rank,edge[0],edge[1])
        return(X)
    
    def pre_travail(self): #pour implémenter la question 14
        list = self.connected_components()
        X=Graph.kruskal(self)
        visited_nodes={noeud: False for noeud in X.nodes}
        predecesseurs={}
        node_initial=X.nodes[0]
        for noeud in X.nodes:
            if len(X.graph[noeud])>len(X.graph[node_initial]):
                node_initial=noeud
        component = [node_initial]
        predecesseurs[node_initial]=[node_initial,0,0]
        visited_nodes[node_initial] = True
        while component != []:
            node=component[0]
            component=component[1:]
            for neighbour in X.graph[node]:
                power=neighbour[1]
                neighbour=neighbour[0]
                if not visited_nodes[neighbour]:
                    visited_nodes[neighbour] = True
                    component.append(neighbour)
                    predecesseurs[neighbour]=[node,power,predecesseurs[node][2]+1]
        return predecesseurs

    def min_power_ameliore(predecesseurs,src,dest): #question 14
        path_b=[]
        path_e=[]
        power=0
        profondeur_min=min([predecesseurs[src][2],predecesseurs[dest][2]])
        profondeur_max=max([predecesseurs[src][2],predecesseurs[dest][2]])
        while profondeur_max!=profondeur_min:
            if profondeur_max==predecesseurs[src][2]:
                path_b.append(src)
                power=max([power,predecesseurs[src][1]])
                src=predecesseurs[src][0]
            else:
                path_e.insert(0,dest)
                power=max([power,predecesseurs[dest][1]])
                dest=predecesseurs[dest][0]
            profondeur_max-=1
        while src!=dest:
            path_b.append(src)
            path_e.insert(0,dest)
            power=max([power,predecesseurs[src][1],predecesseurs[dest][1]])
            src=predecesseurs[src][0]
            dest=predecesseurs[dest][0]
        path=path_b+[src]+path_e
        return path,power
    
    def temps_15(f,k): #question 15
        import time
        solution=[]
        file=open("input/routes."+str(k)+".in", "r")
        nb_trajets=list(map(int, file.readline().split()))[0]
        h=graph_from_file("input/network."+str(k)+".in")
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
    
    def glouton(k_routes,k_camions,W):
        file_trajet=open("input/routes."+str(k_routes)+".in", "r")
        file_puissance=open("output/routes."+str(k_routes)+".out","r")
        nb_trajet=list(map(int, file_trajet.readline().split()))[0]
        efficacite=[]
        for i in range(nb_trajet):
            src,dest,gain=list(map(int, file_trajet.readline().split()))
            power=list(map(int, file_puissance.readline().split()))[0]
            efficacite.append([gain/(power+0.1),power,gain,i+1])
        efficacite.sort(key= lambda x:x[0])
        w_dep=0
        gain_tot=0
        l_trucks=Graph.trucks(k_camions)
        bon_camion=[]
        for trajet in efficacite:
            puissance=trajet[1]
            indice_truck=-1
            cout_truck=trajet[2]
            premier=True
            for j in range(len(l_trucks)):
                if l_trucks[j][0]<puissance:
                    continue
                else:
                    if premier or l_trucks[j][1]<cout_truck:
                        premier=False
                        indice_truck=j
                        cout_truck=l_trucks[j][1]
            bon_camion.append([indice_truck,cout_truck])
        i=0
        camion_et_trajet={trajet[3]: {} for trajet in efficacite}
        while len(bon_camion)>i and w_dep+bon_camion[i][1]<W:
            if bon_camion[i][0] not in camion_et_trajet[efficacite[i][3]].keys():
                camion_et_trajet[efficacite[i][3]][bon_camion[i][0]]=1
            else:
                camion_et_trajet[efficacite[i][3]][bon_camion[i][0]]+=1
            gain_tot+=efficacite[i][2]
            w_dep+=bon_camion[i][1]
            i+=1
        return gain_tot,camion_et_trajet
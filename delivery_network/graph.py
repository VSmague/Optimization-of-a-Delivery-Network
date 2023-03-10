from heapq import *

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
    
    def add_edge(self, node1, node2, power_min, dist=1):
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
    
        """parcours en largeur : utiliser pour le plus court chemin BFS"""
        """parcous en profondeur : utiliser pour une recherche de chemin DFS"""
        
    

    def get_path_with_power(self, src, dest, power):
        list = self.connected_components()
        i = 0
        while i < len(list) and src not in list[i]:
            i += 1
        if i == len(list): 
            return None
        if dest not in list[i] : 
            return None
        return self.dijkstra(src, dest, power)

    def dijkstra(self, s, t, power):
        Vu = set()
        d = {s: 0}
        prédecesseurs = {}
        suivants = [(0, s)]  # Â tas de couples (d[x],x)
        while suivants != []:
            dx, x = heappop(suivants)
            if x in Vu:
                continue
            Vu.add(x)
            for y, p, w in self.graph[x]:
                if y in Vu:
                    continue
                dy = dx + w
                if (y not in d or d[y] > dy) and power >= p:
                    d[y] = dy
                    heappush(suivants, (dy, y))
                    prédecesseurs[y] = x
        path = [t]
        if t not in d : return None
        x = t
        while x != s:
            x = prédecesseurs[x]
            path.insert(0, x)
        return path

    def connected_components(self):
        list_components = []
        visited_nodes = {noeud: False for noeud in self.nodes}

        """création d'un dictionnaire de noeuds avec false si non visité"""

        def dfs(node):
            """ connected_graph = {}for key, values in self.graph.items(): connected_graph[key]=[values[0]]
            on crée un dictionnaire qui prend comme clé le noeud et qui ajoute en valeur seulement le noeud voisin
            le noeud voisin est bien contenu dans values = (nodes2, power_min, dist) """
            """liste de liste : on va faire un dict"""
            component = [node]
            for neighbour in self.graph[node]:
                neighbour = neighbour[0]
                # on ne retient que la première composante de la value pour avoir le voisin
                if not visited_nodes[neighbour]:
                    visited_nodes[neighbour] = True
                    component += dfs(neighbour)
            return component

        for noeud in self.nodes:
            if not visited_nodes[noeud]:
                list_components.append(dfs(noeud))

        return list_components
        print(list_components)

    visited = set()

    def connected_components_set(self):
        return set(map(frozenset, self.connected_components()))
        print(set(map(frozenset, self.connected_components())))

    def min_power(self, src, dest):
        """
        Should return path, min_power.
        """
        p = 0
        while self.get_path_with_power(src, dest, p) == None :
            p += 1
        return self.get_path_with_power(src, dest, p), p
    """on suppose ici que la puissance est toujours un entier naturel"""


    def graph_from_file(filename): 
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

    def makeset(pik,rank,node):
        pik[node]=node
        rank[node]=0
        return None

    def find(pik,node):
        if pik[node] != node:
            pik[node]= find(pik[node])
        return pik[node]

    def union(pik,rank,node1,node2):
        r1=find(pik,node1)
        r2=find(pik,node2)
        if r1==r2: return None
        if rank[r1]>rank[r2]:
            pik[r2]=r1
        else:
            pik[r1]=r2
            if rank[r1]==rank[r2]:
                rank[r2]+=1
        return None

    def kruskal(self):
        pik={}
        rank={}
        for node in self.nodes:
            makeset(pik,rank,node)
        X=Graph([])
        edges=[]
        for node in self.graph:
            for edge in self.graph[node]:
                edges.append((node,edge[0],edge[1]))
        edges.sort(key =lambda x: x[2])
        for edge in edges:
            if find(pik,edge[0])!=find(pik,edge[1]):
                add_edge(X,edge[0],edge[1],edge[2])
                union(pik,rank,edge[0],edge[1])
        return(X)

    def power_min_ameliore(self,src,dest):
        list = self.connected_components()
        i = 0
        while i < len(list) and src not in list[i]:
            i += 1
        if i == len(list):
            return None
        if dest not in list[i]:
            return None
        X=kruskal(self)
        def power(self,node1,node2):
            voisins=self.graph[node1]
            n=len(voisins)
            k=0
            while voisins[k][0]!=node2:
                k+=1
            return voisins[k][1]
        def dijkstra_unique(self, s, t):
            Vu = set()
            prédecesseurs = {}
            suivants = [s]
            while suivants != []:
                x = heappop(suivants)
                if x in Vu:
                    continue
                Vu.add(x)
                for y, p, w in self.graph[x]:
                    if y in Vu:
                        continue
                    else:
                        heappush(suivants, y)
                        prédecesseurs[y] = x
            path = [t]
            x = t
            p_min=0
            while x != s:
                p_min=max(p_min,power(self,x,prédecesseurs[x]))
                x = prédecesseurs[x]
                path.insert(0, x)
            return path,p_min
        return dijkstra_unique(X, src, dest)
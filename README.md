(French below)

# ENSAE 1A : programming project

Through this programming project, we focus on optimizing a transportation network. The problem statement is as follows: consider a road network consisting of cities and routes between the cities. The objective of the project is to construct a delivery network capable of covering a set of routes between two cities with trucks. The difficulty lies in the fact that each route has a minimum power requirement, meaning a truck can only use this route if its power is greater than or equal to the route's minimum power requirement. Therefore, we need to determine for each pair of cities if a truck with a given power can find a possible path between these two cities; then, optimize the fleet of trucks to be purchased based on the routes to be covered.

The road network is represented by an undirected graph G = (V, E). The set of vertices V corresponds to the set of cities. The set of edges E corresponds to the set of existing routes between two cities.

We consider a set T of routes, where each route t is a pair of two distinct cities, i.e., t = (v, v0) where v ∈ V, v0 ∈ V. The set T represents the set of city pairs (v, v0) for which we want to have a truck that can transport between v and v0. Note that the graph is undirected and we do not distinguish the direction of the route. Each route t is also associated with a profit (or utility) ut ≥ 0, which will be earned by the delivery company if route t is covered.

Finally, the transportation is done by trucks. Each truck (denoted as K) has a power p and costs a price c. Transport on a route t = (v, v0) in T will be possible if and only if we can find in the graph G a path from v to v0 where the minimum power of each edge is less than or equal to p (i.e., the truck has sufficient power to pass everywhere on the path). It is then said that route t can be covered by the truck K considered.

To best address the problem, which is to maximize a company's profit based on the profit brought by each route and the cost of each truck depending on its power, we proceeded in two main parts: the implementation of algorithms to find the minimum power to travel a route; and the optimization of truck acquisition based on a list of routes associated with a profit.

## Organization of the repositery

This repository contains several folders and files:
- The delivery_network folder contains the main code. This is where the Graph class is located.
- The inputs folder contains datasets (graphs and sets of routes).
- The outputs folder contains datasets calculated from the inputs using functions from the delivery_network folder.
- The tests folder contains unit tests.
- The install_graphviz.sh file allows you to install Graphviz on sspcloud.

## Format of input files

The input folder contains 3 types of files: the network.x.in files ($x \in {00, 01, 02, 03, 04, 1, ..., 10}$) which contain the graphs, the routes.x.in files ($x \in {1, ..., 10}$) which contain sets of routes for the corresponding graphs of $x$, and the trucks.x.in files ($x \in{0, 1, 2\}) which contain trucks catalogs.

The structure of the network.x.in files is as follows:
- The first line consists of two integers separated by a space: the number of vertices (n) and the number of edges (m).
- The following m lines each represent an edge and are composed of 3 or 4 numbers separated by spaces: 'city1 city2 power [distance]', where 'city1' and 'city2' are the vertices of the edge, power is the minimum power required to traverse the edge, and distance (optional) is the distance between 'city1' and 'city2' on the edge.

The structure of the routes.x.in files is as follows:
- The first line contains an integer corresponding to the number of routes in the set (T).
- The following T lines each contain a route in the form 'city1 city2 utility', where utility is the profit gained if the corresponding route is covered.

The structure of the trucks.x.in files is as follows:
- The first line contains an integer corresponding to the number of trucks in the catalog.
- The following K lines each contain a truck in the form 'power price', where power is the power of the truck, and price is its price.

## Format of output files

The output folder contains files output.x.out ($x \in {1, 2, 3, ..., 9}$) which correspond to the input files input.x.in. They contain the minimum power required to complete each route in the corresponding input file, and these powers are calculated by the min_power_amélioré function.

# ENSAE 1A : projet de programmation

À travers ce projet de programmation, nous nous intéressons à l'optimisation d'un réseau de transport. L'énoncé du problème est le suivant : considérez un réseau routier composé de villes et de routes entre ces villes. L'objectif du projet est de construire un réseau de livraison capable de couvrir un ensemble de routes entre deux villes avec des camions. La difficulté réside dans le fait que chaque route a une puissance minimale requise, donc un camion ne peut emprunter cette route que si sa puissance est supérieure ou égale à la puissance minimale requise pour la route. Par conséquent, nous devons déterminer pour chaque paire de villes si un camion avec une puissance donnée peut trouver un chemin possible entre ces deux villes ; puis, optimiser la flotte de camions à acheter en fonction des routes à couvrir.

Le réseau routier est représenté par un graphe non orienté G = (V, E). L'ensemble des sommets V correspond à l'ensemble des villes. L'ensemble des arêtes E correspond à l'ensemble des routes existantes entre deux villes.

Nous considérons un ensemble T de routes, où chaque route t est une paire de deux villes distinctes, c'est-à-dire t = (v, v0) où v ∈ V, v0 ∈ V. L'ensemble T représente l'ensemble des paires de villes (v, v0) pour lesquelles nous voulons avoir un camion capable de transporter entre v et v0. Notez que le graphe est non orienté et nous ne distinguons pas la direction de la route. Chaque route t est également associée à un profit (ou utilité) ut ≥ 0, qui sera gagné par la société de livraison si la route t est couverte.

Enfin, le transport est effectué par des camions. Chaque camion (désigné par K) a une puissance p et coûte un prix c. Le transport sur une route t = (v, v0) dans T sera possible si et seulement si nous pouvons trouver dans le graphe G un chemin de v à v0 où la puissance minimale de chaque arête est inférieure ou égale à p (c'est-à-dire que le camion a une puissance suffisante pour passer partout sur le chemin). On dit alors que la route t peut être couverte par le camion K considéré.

Pour répondre au mieux au problème, qui consiste à maximiser le profit d'une entreprise en fonction du profit apporté par chaque route et du coût de chaque camion en fonction de sa puissance, nous avons procédé en deux parties principales : la mise en œuvre d'algorithmes pour trouver la puissance minimale pour parcourir une route ; et l'optimisation de l'acquisition de camions en fonction d'une liste de routes associée à un profit.

## Organisation du dépôt

Ce dépôt contient plusieurs dossiers et fichiers : 
- le dossier `delivery_network` contient le code principal. C'est là qu'est la classe Graph.
- le dossier 'inputs' contient des jeux de données (graphes et ensembles de trajets) 
- le dosser 'ouputs' contient des jeux de données calculés à partir des 'inputs' grâce aux  fonctions du 'delivery_network'
- le dossier 'tests' contient les tests unitaires
- le fichier `install_graphviz.sh` permet d'installer graphviz sur sspcloud

## Format des fichiers d'input

Le dossier input contient 3 types de fichiers : les fichiers network.x.in ($x \in \{00, 01, 02, 03, 04, 1, ..., 10\}$) qui contiennent les graphes, les fichiers routes.x.in ($x \in \{1, ..., 10\}$) qui contiennent des ensembles de trajets pour les graphes de $x$ correspondant, et les fichiers trucks.x.in ($x \in{0, 1, 2\}$) qui contiennent des catalogues de camions. 

La structure des fichiers network.x.in est la suivante : 
- la première ligne est composée de deux entiers séparés par un espace : le nombre de sommets (n) et le nombre d'arêtes (m)
- les m lignes suivantes représentent chacune une arête et sont composées de 3 ou 4 nombres séparés par des espaces : `ville1 ville2 puissance [distance]`, où `ville1` et `ville2` sont les sommets de l'arête, puissance est la puissance minimale requise pour passer sur l'arête, et distance (optionnel) est la distance entre `ville1` et `ville2` sur l'arête. 

La structure des fichiers routes.x.in est la suivante : 
- la première ligne contient un entier qui correspond aux nombres de trajets dans l'ensemble (T)
- les T lignes suivantes contiennent chacune un trajet sous la forme `ville1 ville2 utilité`, où utilité est le profit acquis si le trajet correspondant est couvert.

La structure des fichiers trucks.x.in est la suivante : 
- la première ligne contient un entier qui correspond aux nombres de camions dans le catalogue
- les K lignes suivantes contiennent chacune un camion et sont composées de 2 nombres séparés par des espaces : 'puissance prix' où puissance est la puissance du camion est prix le prix du camion.

## Format des fichiers d'output

Le dossier output contient des fichiers output.x.out ($x \in \{1, 2, 3, ..., 9\}$) qui correspondent aux fichiers input.x.in. Ils contiennt la puissance minimale nécessaire pour réaliser chaque trajet du fichier input correspondant, et ces puissances sont calculées par la fonction min_power_amélioré.


(French below)

# ENSAE 1A : programming project

This repository contains several folders and files:
- The delivery_network folder contains the main code. This is where the Graph class is located.
- The inputs folder contains datasets (graphs and sets of routes).
- The outputs folder contains datasets calculated from the inputs using functions from the delivery_network folder.
- The tests folder contains unit tests.
- The install_graphviz.sh file allows you to install Graphviz on sspcloud.

## Format of input files

The input folder contains 2 types of files: the network.x.in files ($x \in {00, 01, 02, 03, 04, 1, ..., 10}$) which contain the graphs, and the routes.x.in files ($x \in {1, ..., 10}$) which contain sets of routes for the corresponding graphs of $x$.

The structure of the network.x.in files is as follows:
- The first line consists of two integers separated by a space: the number of vertices (n) and the number of edges (m).
- The following m lines each represent an edge and are composed of 3 or 4 numbers separated by spaces: 'city1 city2 power [distance]', where 'city1' and 'city2' are the vertices of the edge, power is the minimum power required to traverse the edge, and distance (optional) is the distance between 'city1' and 'city2' on the edge.

The structure of the routes.x.in files is as follows:
- The first line contains an integer corresponding to the number of routes in the set (T).
- The following T lines each contain a route in the form 'city1 city2 utility', where utility is the profit gained if the corresponding route is covered.

# ENSAE 1A : projet de programmation

Ce dépôt contient plusieurs dossiers et fichiers : 
- le dossier `delivery_network` contient le code principal. C'est là qu'est la classe Graph.
- le dossier 'inputs' contient des jeux de données (graphes et ensembles de trajets) 
- le dosser 'ouputs' contient des jeux de données calculés à partir des 'inputs' grâce aux  fonctions du 'delivery_network'
- le dossier 'tests' contient les tests unitaires
- le fichier `install_graphviz.sh` permet d'installer graphviz sur sspcloud

## Format des fichiers d'input

Le dossier input contient 2 types de fichiers : les fichiers network.x.in ($x \in \{00, 01, 02, 03, 04, 1, ..., 10\}$) qui contiennent les graphes et les fichiers routes.x.in ($x \in \{1, ..., 10\}$) qui contiennent des ensembles de trajets pour les graphes de $x$ correspondant. 

La structure des fichiers network.x.in est la suivante : 
- la première ligne est composée de deux entiers séparés par un espace : le nombre de sommets (n) et le nombre d'arêtes (m)
- les m lignes suivantes représentent chacune une arête et sont composées de 3 ou 4 nombres séparés par des espaces : `ville1 ville2 puissance [distance]`, où `ville1` et `ville2` sont les sommets de l'arête, puissance est la puissance minimale requise pour passer sur l'arête, et distance (optionnel) est la distance entre `ville1` et `ville2` sur l'arête. 

La structure des fichiers routes.x.in est la suivante : 
- la première ligne contient un entier qui correspond aux nombres de trajets dans l'ensemble (T)
- les T lignes suivantes contiennent chacune un trajet sous la forme `ville1 ville2 utilité`, où utilité est le profit acquis si le trajet correspondant est couvert.
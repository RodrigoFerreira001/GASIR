# -*- coding: utf-8 -*-

import networkx as nx
import sys

output = sys.argv[1]
nodes = int(sys.argv[2])

g = nx.erdos_renyi_graph(nodes, .02)
#g = nx.watts_strogatz_graph(nodes, 4, .02)
nx.write_adjlist(g, output + "_" + str(nodes) + ".txt")
# -*- coding: utf-8 -*-
from sir_blackbox import SIRBB
from genetic_model import GeneticModel
import copy
import igraph
import random
import networkx as nx
import matplotlib.pyplot as plt
import sys

# def plot(adjacencyList):
# 	g = nx.Graph()
# 	for i,v in enumerate(adjacencyList):
# 		g.add_node(i)
# 		for e in v:
# 			g.add_edge(i,e)
#
# 	print nx.draw(g)
# 	plt.draw()
# 	plt.show()
# 	print "EOQ?"
#

if __name__ == '__main__':
	#transmission parameters (daily rates scaled to hourly rates)
	b = .02 / 24.0
	g = .05 / 24.0

	#initial conditions (# of people in each state)
	S = int(sys.argv[1])
	I = int(sys.argv[2])

	#network specific parameters
	p = .05 #this controls the likelihood that connections will be rewired
	nei = 10 #and this is the number of network neighbors each node has at t = 0

	#make a small world graph with as many nodes as we have individuals
	graph = igraph.Graph.Watts_Strogatz(1, S, nei=nei, p = p)
	#we do this to get rid of multiple edges and self-loops that the
	#randomly generated small-world graph might have
	graph.simplify()

	#Define a label for each vertex
	for i, v in enumerate(graph.vs):
		v['label'] = str(i)

	adjacencyList = []
	for i in range(S):
		adjacencyList.append([])

	#now we're going to unpack the info from the graph
	#into a more usable format

	#this is an efficient way of doing it bust shows you
	#how to turn the graph into an
	#adjacency list
	for edge in graph.es: #looping over the graph's edge sequence
		#indexing adjacency by node ID,so we can do quick lookups
		adjacencyList[edge.source].append(edge.target)
		adjacencyList[edge.target].append(edge.source)


	ag = GeneticModel(100, S)

	while ag.generation < 100:
		for ind in ag.population:
			

	for e, indiviual in enumerate(population):
		#S
		sAgentList = range(S)

		#R
		rAgentList = []

		#Realiza a vacinação
		for i in range(len(indiviual)):
			if(indiviual[i] == "1"):
				rAgentList.append(i)
				sAgentList.remove(i)

		random.shuffle(sAgentList)
		sirbb = SIRBB(adjacencyList, b, g, sAgentList, I, rAgentList)
		sirbb.run()

		print "Indivíduo: ",e," Infectados: ", sirbb.infectedCount

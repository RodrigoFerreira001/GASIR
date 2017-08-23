# -*- coding: utf-8 -*-
import sys
import igraph

graph_file = open(sys.argv[1],"w")
vertex_num = int(sys.argv[2])
neighbors =  int(sys.argv[3]) #4
p = float(sys.argv[4]) #0.2

#make a small world graph with as many nodes as we have individuals
graph = igraph.Graph.Watts_Strogatz(1, vertex_num, nei=neighbors, p = p)
#we do this to get rid of multiple edges and self-loops that the
#randomly generated small-world graph might have
graph.simplify()

#we're going to keep track of who is next to who using a list of lists
adjacencyList = []
for i in range(vertex_num):
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

graph_file.write(str(vertex_num) + "\n")
for i, vertex in enumerate(adjacencyList):
	for neighbor in vertex:
		graph_file.write(str(neighbor) + " ")

	if(i != (vertex_num - 1)):
		graph_file.write("\n")

graph_file.close()

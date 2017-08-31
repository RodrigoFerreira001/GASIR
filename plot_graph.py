# -*- coding: utf-8 -*-
import sys
from igraph import *

def graph_read(file_name):
	graph_file = open(file_name, "r")
	vertex_num = int(graph_file.readline())

	adjacencyList = []
	for i in range(vertex_num):
		adjacencyList.append([])

	for i in range(vertex_num):
		temp = graph_file.readline().strip()
		neighbors = temp.split(" ")
		for neighbor in neighbors:
			adjacencyList[i].append(int(neighbor))

	graph_file.close()

	return adjacencyList

#Infectados
def infecteds_read(file_name):
	infecteds_file = open(file_name, "r")

	infecteds = []
	temp = infecteds_file.readline().strip()

	for infected in temp.split(" "):
		infecteds.append(int(infected))

	infecteds_file.close()

	return infecteds

def vaccinateds_read(file_name):
	vaccinateds_file = open(file_name, "r")

	vaccinateds = []
	temp = vaccinateds_file.readline().strip()

	for vaccinated in temp.split(" "):
		vaccinateds.append(int(vaccinated))

	vaccinateds_file.close()

	return vaccinateds

if __name__ == '__main__':
	adjacencyList = graph_read(sys.argv[1])
	infecteds = infecteds_read(sys.argv[2])
	vaccinateds = vaccinateds_read(sys.argv[3])

	g = Graph()
	g.add_vertices(len(adjacencyList))

	for i, vertice in enumerate(adjacencyList):
		for neighbor in vertice:
			g.add_edges([(i,neighbor)])

	layout = g.layout("random")


	for i,v in enumerate(g.vs()):#loop over the nodes in the graph- in igraph the "vertex sequence"
            v['label'] = i #if you don't do this, nodes will be labeled with their indices, which
                                #can be visually confusing

            v['color'] = 'blue' #all nodes start blue
            if v.index in infecteds:
                v['color'] = 'red' #if they were infected during the run, color them red

            if v.index in vaccinateds: #color index cases green
                v['color'] = 'green'

	plot(g, layout = layout)

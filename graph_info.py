# -*- coding: utf-8 -*-
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random
from matplotlib import colors
import sys
import argparse

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	#required args
	parser.add_argument("graph", help = "Network graph representing community interactions")
	args = parser.parse_args()

	#graph
	graph = nx.read_adjlist(args.graph, nodetype = int)

	pr = nx.pagerank(graph)

	histogram = []
	for value in pr.values():
		histogram.append(value)

	highest_value = 0.0

	for value in histogram:
		if(value > highest_value):
			highest_value = float(value)

	ibar =  plt.bar(np.arange(len(histogram)), histogram, align='center', alpha=0.5)

	for i,element in enumerate(ibar):
		norm = colors.Normalize(0.0, 1.0)
		color = plt.cm.winter(norm(histogram[i]/highest_value))
		element.set_color(color)
	#plt.xticks(y_pos, objects)
	plt.xlabel('Individuo')
	plt.ylabel('Page Rank')
	plt.title('GASIR - Genetic Algorithm for SIR Model')
	plt.savefig(sys.argv[1].split(".")[0] + "_pagerank.svg", format="svg")
	plt.clf()

	nodes_degree = []
	for i in range(graph.number_of_nodes()):
		nodes_degree.append(graph.degree(i))

	highest_value = 0.0

	for value in nodes_degree:
		if(value > highest_value):
			highest_value = float(value)

	ibar =  plt.bar(np.arange(len(nodes_degree)), nodes_degree, align='center', alpha=0.5)

	for i,element in enumerate(ibar):
		norm = colors.Normalize(0.0, 1.0)
		color = plt.cm.winter(norm(nodes_degree[i]/highest_value))
		element.set_color(color)
	#plt.xticks(y_pos, objects)
	plt.xlabel('Individuo')
	plt.ylabel('Grau')
	plt.title('GASIR - Genetic Algorithm for SIR Model')
	plt.savefig(sys.argv[1].split(".")[0] + "_degree.svg", format="svg")
	plt.clf()

# -*- coding: utf-8 -*-
from sir_blackbox import SIRBB
from genetic_model import GeneticModel
import copy
import igraph
import random
import matplotlib.pyplot as plt
import sys

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

	return adjacencyList

def infecteds_read(file_name):
	infecteds_file = open(file_name, "r")

	infecteds = []
	temp = infecteds_file.readline().strip()

	for infected in temp.split(" "):
		infecteds.append(int(infected))

	return infecteds

if __name__ == '__main__':
	#transmission parameters (daily rates scaled to hourly rates)
	b = .02 / 24.0
	g = .05 / 24.0

	#lista de adjacencia
	adjacencyList = graph_read(sys.argv[1])
	iList = infecteds_read(sys.argv[2])
	gene_size = int(sys.argv[3])

	S = len(adjacencyList)

	ag = GeneticModel(S, gene_size)

	print "- GASIR -"
	print "Tamanho da população: ", S
	print "Tamanho do gene: ", gene_size
	print "Número de infectados: ", len(iList)

	for i, ind in enumerate(ag.population):
		print i,": ", ind


	while ag.generation < 2:
		for i, ind in enumerate(ag.population):

			#Susceptible
			sAgentList = range(S)

			#Recovered
			rAgentList = []

			#Infected
			iAgentList = iList[:]
			print "\n- Suscetíveis: "
			print sAgentList

			print "\n- Infectados:"
			print iAgentList

			print "\n- Recuperados:"
			print rAgentList

			print "\n- Vacinados:"
			print ind

			#realiza vacinação
			for v in ind:
				if(v in iAgentList):
					iAgentList.remove(v)
				if(v in sAgentList):
					sAgentList.remove(v)

				rAgentList.append(v)

			print "\n ---- Vacinação ----- "

			print "\n- Suscetíveis: "
			print sAgentList

			print "\n- Infectados:"
			print iAgentList

			print "\n- Recuperados:"
			print rAgentList

			#random.shuffle(sAgentList)
			sirbb = SIRBB(adjacencyList, sAgentList, iAgentList, b, g)

			sirbb.run()

			print "Performance de ", i, ": ", sirbb.infectedCount
			ag.individual_performance[i] = sirbb.infectedCount

		#realiza métodos do ag
		ag.parents_select()

print ag.best
print ag.best_performance

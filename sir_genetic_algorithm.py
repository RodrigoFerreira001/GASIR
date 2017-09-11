# -*- coding: utf-8 -*-
from sir_blackbox import SIRBB
from genetic_model import GeneticModel
import copy
from igraph import *
import random
import matplotlib.pyplot as plt
import sys

def graph_read(file_name):
	g = Graph.Read_Ncol(file_name)
	g.simplify()

	adjacencyList = []
	for i in range(g.vcount()):
		adjacencyList.append([])

	#adjacency list
	for edge in g.es: #looping over the graph's edge sequence
		#indexing adjacency by node ID,so we can do quick lookups
		adjacencyList[edge.source].append(edge.target)
		adjacencyList[edge.target].append(edge.source)

	print g.vcount()
	print g.ecount()

	return adjacencyList

def infecteds_read(file_name):
	infecteds_file = open(file_name, "r")

	infecteds = []
	temp = infecteds_file.readline().strip()

	for infected in temp.split(" "):
		infecteds.append(int(infected))

	infecteds_file.close()

	return infecteds

if __name__ == '__main__':

	# Argumentos:
	# 1 - Grafo
	# 2 - Porcentagem de infectados
	# 3 - Número de Vacinas

	#transmission parameters (daily rates scaled to hourly rates)
	b = .02 / 24.0
	g = .05 / 24.0
	# b = .02
	# g = .05

	#lista de adjacencia
	adjacencyList = graph_read(sys.argv[1])

	#pesos
	adjacencyListWeigth = []
	for i, neighbors in enumerate(adjacencyList):
		adjacencyListWeigth.append([])
		for neighbor in neighbors:
			adjacencyListWeigth[i].append(random.random())


	icount = int(len(adjacencyList) * float(sys.argv[2]))
	iList = random.sample(range(len(adjacencyList)), icount)
	gene_size = int(sys.argv[3])

	S = len(adjacencyList)

	ag = GeneticModel(100, gene_size, S, iList, selection_mode = 2)

	print "- GASIR -"
	print "Tamanho da população: ", ag.population_size
	print "Tamanho do gene: ", gene_size
	print "Número de infectados: ", len(iList)
	print " -- Início -- \n"

	while ag.generation < 100:
		for i, ind in enumerate(ag.population):

			#Susceptible
			sAgentList = range(S)

			#Recovered
			rAgentList = []

			#Infected
			iAgentList = iList[:]
			# print "\n- Suscetíveis: "
			# print sAgentList
			#
			# print "\n- Infectados:"
			# print iAgentList
			#
			# print "\n- Recuperados:"
			# print rAgentList
			#
			# print "\n- Vacinados:"
			# print ind

			#realiza vacinação
			for v in ind:
				if(v in sAgentList):
					sAgentList.remove(v)

				rAgentList.append(v)

			# #realiza vacinação
			# for v in ind:
			# 	if(v in iAgentList):
			# 		iAgentList.remove(v)
			# 	if(v in sAgentList):
			# 		sAgentList.remove(v)
			#
			# 	rAgentList.append(v)

			# print "\n ---- Vacinação ----- "
			#
			# print "\n- Suscetíveis: "
			# print sAgentList
			#
			# print "\n- Infectados:"
			# print iAgentList
			#
			# print "\n- Recuperados:"
			# print rAgentList

			random.shuffle(sAgentList)
			sirbb = SIRBB(adjacencyList, adjacencyListWeigth, sAgentList, iAgentList, b, g)

			sirbb.run()

			ag.individual_performance[i] = sirbb.infectedCount
			print sirbb.infectedCount
			#print i, ": ", sirbb.infectedCount
			#ag.individual_performance[i] = len(sAgentList) -  len(sirbb.sAgentList)
			#print len(sAgentList), " - ", len(sirbb.sAgentList), " = ",  len(sAgentList) -  len(sirbb.sAgentList)

		#realiza métodos do ag
		ag.parents_select()
		print "\nGeração: ", ag.generation
		print "Melhor: ", ag.best
		print "Infectados: ", ag.best_performance
		print " ------------------------ "

	print "GLOBAL:"
	print ag.global_best
	print ag.global_best_performance

	result = open(sys.argv[4], "a+")
	result.write(str(ag.global_best) + "\n")
	result.close()

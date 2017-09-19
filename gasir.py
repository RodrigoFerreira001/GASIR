# -*- coding: utf-8 -*-
import networkx as nx
import ndlib.models.ModelConfig as mc
#import ndlib.models.epidemics.SIRModel as sir
import SIRModel as sir
from genetic_model import GeneticModel
import random
import sys

if __name__ == '__main__':

	import argparse

	parser = argparse.ArgumentParser()
	#required args
	parser.add_argument("graph", help = "Network graph representing community interactions")
	parser.add_argument("population_size", help = "Genetic algorithm population size", type = int)
	parser.add_argument("gene_size", help = "Number of available vaccines", type = int)

	#optional args
	parser.add_argument("--selection_mode", help = "GA's parents select mode", type = int)
	parser.add_argument("--cross_points", help = "Crossover cross points number", type = int)
	parser.add_argument("--mutation", help = "Crossover mutation level", type = float)
	parser.add_argument("--cross_l", help = "Crossover cross probability", type = float)
	parser.add_argument("--generations", help = "Number of generations(ag's iterations)", type = int)
	parser.add_argument("-p", "--percentage_infected", help = "Initial number of infections", type = float)
	parser.add_argument("-b", "--beta", help = "Disease tranmission rate", type = float)
	parser.add_argument("-g", "--gamma", help = "Disease recovery rate", type = float)
	parser.add_argument("-r", "--result", help = "File with the best individual of the genetic algorithm", type = float)

	args = parser.parse_args()

	#graph
	graph = nx.read_adjlist(args.graph, nodetype = int)

	#population_size
	population_size = args.population_size

	#gene_size
	gene_size = args.gene_size

	#selecion mode
	selection_mode = 0

	#cross points
	cross_points = 2

	#mutation
	mutation = 0.05

	#cross level
	cross_l = 0.9

	#generations
	generations = 200

	#percentage_infected
	percentage_infected = 0.05

	#transmission parameters (daily rates scaled to hourly rates)
	beta = 0.2857
	gamma = 0.1428

	#arquivo de resultado
	result = None

	#selection_mode check
	if(args.selection_mode):
		selection_mode = args.selection_mode
	else:
		print " - Assumindo modo de seleção como 0"

	#cross_points check
	if(args.cross_points):
		cross_points = args.cross_points
	else:
		print " - Assumindo pontos de cruzamento como 2"

	#mutation check
	if(args.mutation):
		mutation = args.mutation
	else:
		print " - Assumindo probabilidade de mutação como 0.5%"

	#generations check
	if(args.cross_l):
		cross_l = args.cross_l
	else:
		print " - Assumindo probabilidade de cruzamento como 90%"

	#generations check
	if(args.generations):
		generations = args.generations
	else:
		print " - Assumindo número de gerações como 200"

	#percentage infected check
	if(args.percentage_infected):
		percentage_infected = args.percentage_infected
	else:
		print " - Assumindo Porcentagem inicial de infectados como 0.5%"

	#beta check
	if(args.beta):
		beta = args.beta
	else:
		print " - Assumindo beta como 0.2857"

	#gamma check
	if(args.gamma):
		gamma = args.gamma
	else:
		print " - Assumindo gamma como 0.1428"

	#result check
	if(args.result):
		result = open(args.result, "a+")
	else:
		print " - Assumindo arquivo de saída como ", args.graph.split(".")[0] + ".result"
		result = open(str(args.graph.split(".")[0] + ".result"), "a+")


	# ---------- Início -----------

	#lista de infectados
	infected_list = random.sample(range(graph.number_of_nodes()), int(graph.number_of_nodes() * percentage_infected))

	#cria o ag
	ag = GeneticModel(population_size, gene_size, graph.number_of_nodes(), infected_list, selection_mode , cross_points, mutation, cross_l)

	print "- GASIR -"
	print "Tamanho da população: ", ag.population_size
	print "Tamanho do gene: ", gene_size
	print "Número de infectados: ", len(infected_list)
	print "Tamanho da rede:", graph.number_of_nodes()

	while ag.generation < generations:
		best = 0
		for i, ind in enumerate(ag.population):
			# Model selection
			model = sir.SIRModel(graph)

			# Model Configuration
			cfg = mc.Configuration()
			cfg.add_model_parameter('beta', 0.2857)
			cfg.add_model_parameter('gamma', 0.1428)

			cfg.add_model_initial_configuration("Infected", infected_list)
			cfg.add_model_initial_configuration("Removed", ind)

			#set initial status for the model
			model.set_initial_status(cfg)

			#count each infected for each simulation
			infecteds_count = 0

			#first model iterarion
			iteration = model.iteration()

			while((iteration['node_count'][0] > 0) and (iteration['node_count'][1] > 0)):
				#print iteration['node_count']
				# for key, value in iteration['status'].items():
				# 	if(value == 1):
				# 		infecteds_count += 1

				iteration = model.iteration()

			#ag.individual_performance[i] = infecteds_count
			ag.individual_performance[i] = model.infecteds_count

		#realiza métodos do ag
		ag.parents_select()
		print "\nGeração: ", ag.generation
		print "Melhor: ", ag.best
		print "Infectados: ", ag.best_performance
		print " ------------------------ "

	print "GLOBAL:"
	print ag.global_best
	print ag.global_best_performance

	result.write(str(ag.global_best) + "\n")
	result.close()

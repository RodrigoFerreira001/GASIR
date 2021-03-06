# -*- coding: utf-8 -*-
import networkx as nx
import numpy as np
import ndlib.models.ModelConfig as mc
import ndlib.models.epidemics.SIRModel as sir
from genetic_model import GeneticModel
import random
from multiprocessing import Process, Array
import argparse

ag = None
graph = None
beta = None
gamma = None
infected_list = None

def initial_evaluation(process_id, num_process):
	ini = ((ag.population_size / num_process) * process_id)
	fim = 0

	if (process_id == (num_process - 1)):
		fim = ((ag.population_size / num_process) * process_id) + (ag.population_size / num_process) + (
					ag.population_size % num_process)
	else:
		fim = ((ag.population_size / num_process) * process_id) + (ag.population_size / num_process)

	for index in range(ini, fim):
		# Model selection
		model = sir.SIRModel(graph)

		# Model Configuration
		cfg = mc.Configuration()
		cfg.add_model_parameter('beta', beta)
		cfg.add_model_parameter('gamma', gamma)

		# cfg.add_model_parameter("percentage_infected", percentage_infected)
		cfg.add_model_initial_configuration("Infected", infected_list)
		cfg.add_model_initial_configuration("Removed", ag.population[index])

		# set initial status for the model
		model.set_initial_status(cfg)

		#model iterarion
		iteration = model.iteration_bunch(100)

		# atribui fitness
		ag.individual_performance[index] = iteration[len(iteration) - 1]['node_count'][1] + iteration[len(iteration) - 1]['node_count'][2]

def evaluate_population(process_id, num_process):
	# realiza avaliação dos filhos

	ini = ((ag.population_size / num_process) * process_id)
	fim = 0

	if(process_id == (num_process - 1)):
		fim = ((ag.population_size / num_process) * process_id) + (ag.population_size / num_process) + (ag.population_size % num_process)
	else:
		fim = ((ag.population_size / num_process) * process_id) + (ag.population_size / num_process)

	for index in range(ini, fim):
		# Model selection
		model = sir.SIRModel(graph)

		# Model Configuration
		cfg = mc.Configuration()
		cfg.add_model_parameter('beta', beta)
		cfg.add_model_parameter('gamma', gamma)

		# cfg.add_model_parameter("percentage_infected", percentage_infected)
		cfg.add_model_initial_configuration("Infected", infected_list)
		cfg.add_model_initial_configuration("Removed", ag.population2[index])

		# set initial status for the model
		model.set_initial_status(cfg)

		# model iterarion
		iteration = model.iteration_bunch(100)

		# atribui fitness
		ag.individual_performance2[index] = iteration[len(iteration) - 1]['node_count'][1] + \
										iteration[len(iteration) - 1]['node_count'][2]

		#ind_perf2 = iteration[len(iteration) - 1]['node_count'][1] + \
		#								iteration[len(iteration) - 1]['node_count'][2]
		model.reset()

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	#required args
	parser.add_argument("graph", help = "Network graph representing community interactions")
	parser.add_argument("population_size", help = "Genetic algorithm population size", type = int)
	parser.add_argument("gene_size", help = "Number of available vaccines", type = int)

	#optional args
	parser.add_argument("--infecteds", help = "Initial infecteds", type = int, nargs='*')
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
	#graph = nx.read_adjlist(args.graph, nodetype = int)
	graph = nx.read_edgelist(args.graph, nodetype = int)

	#population_size
	population_size = args.population_size

	#gene_size
	gene_size = args.gene_size

	#selecion mode
	selection_mode = 2

	#cross points
	cross_points = 2

	#mutation
	mutation = 0.05

	#cross level
	cross_l = 0.9

	#generations
	generations = 100

	#percentage_infected
	percentage_infected = 0.005

	#transmission parameters (daily rates scaled to hourly rates)
	beta = 0.2857
	gamma = 0.1428

	fixed = False

	#arquivo de resultado
	result = None
	result_detailed = None
	result_generation_detailed = None
	result_conv = None

	#selection_mode check
	if(args.selection_mode):
		selection_mode = args.selection_mode
	else:
		print " - Assumindo modo de seleção como 2"

	#cross_points check
	if(args.cross_points):
		cross_points = args.cross_points
	else:
		print " - Assumindo pontos de cruzamento como 2"

	#mutation check
	if(args.mutation):
		mutation = args.mutation
	else:
		print " - Assumindo probabilidade de mutação como 5%"

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
		result_detailed = open(args.result.split(".")[0] + "_detailed" + args.result.split(".")[1], "a+")
		result_generation_detailed = open(args.result.split(".")[0] + "_generation_detailed" + args.result.split(".")[1], "a+")
		result_conv = open(args.result.split(".")[0] + "_average" + args.result.split(".")[1], "a+")
	else:
		print " - Assumindo arquivo de saída como ", args.graph.split(".")[0] + ".result"
		result = open(str(args.graph.split(".")[0] + ".result"), "a+")
		result_detailed = open(str(args.graph.split(".")[0] + "_detailed.result"), "a+")
		result_generation_detailed = open(str(args.graph.split(".")[0] + "_generation_detailed.result"), "a+")
		result_conv = open(str(args.graph.split(".")[0] + "_average.result"), "a+")


	# ---------- Início -----------

	#lista de infectados
	infected_list = []
	if(args.infecteds):
		infected_list = args.infecteds[:]
	else:
		infected_list = random.sample(range(graph.number_of_nodes()), int(graph.number_of_nodes() * percentage_infected))

	#cria o ag
	ag = GeneticModel(population_size, gene_size, graph.number_of_nodes(), infected_list, selection_mode , cross_points, mutation, cross_l)

	print "- GASIR -"
	print "Tamanho da população: ", ag.population_size
	print "Tamanho do gene: ", gene_size
	print "Número de infectados: ", len(infected_list), ": ", infected_list
	print "Tamanho da rede:", graph.number_of_nodes()

	#iteração inicial
	process_list_init = []
	for pid in range(8):
		p0 = Process(target=initial_evaluation, args=(pid, 8))
		process_list_init.append(p0)
		p0.start()

	for pid in range(8):
		process_list_init[pid].join()


	while ag.generation < generations:
		best = 0

		result_generation_detailed.write(str(ag.generation) + " " + str(ag.best_performance) + " " + str(ag.best) + "\n")

		#realiza seleção dos pais
		ag.parents_select()

		print "\nGeração: ", ag.generation
		print "Melhor: ", ag.best
		print "Infectados: ", ag.best_performance
		print " ------------------------ "

		process_list = []
		for pid in range(8):
			p = Process(target=evaluate_population, args=(pid, 8))
			process_list.append(p)
			p.start()

		for pid in range(8):
			process_list[pid].join()

		#substitui os pais pelos novos filhos
		ag.replace()

		performance_average = 0.0
		for perf in ag.individual_performance:
			performance_average += perf

		result_conv.write(str(int(performance_average / ag.population_size)) + "\n")


	print "GLOBAL:"
	print ag.global_best
	print ag.global_best_performance

	result_generation_detailed.close()
	result_conv.close()

	result.write(str(ag.global_best) + "\n")
	result.close()

	result_detailed.write(str(ag.global_best) + "\n");
	result_detailed.write(str(ag.global_best_performance) + "\n");
	result_detailed.write(str(infected_list) + "\n");
	result_detailed.close()
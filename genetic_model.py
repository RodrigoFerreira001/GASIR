# -*- coding: utf-8 -*-
import random
import sys

class GeneticModel():
	def __init__(self, population_size, gene_size, selection_mode = 0, cross_points = 2, mutation = 0.05):
		self.population_size = population_size
		self.gene_size = gene_size
		self.selection_mode = selection_mode
		self.cross_points = cross_points
		self.mutation = mutation
		self.population = []
		self.individual_performance = []
		self.generation = 0

		pop_id = range(population_size)

		#cria a população inicial e inicializa a lista de avaliação de indivíduos
		for i in range(population_size):
			self.population.append(random.sample(pop_id, gene_size))
			self.individual_performance.append(0)


	def parents_select(self):
		#roleta-russa

		if(self.selection_mode == 0):

			#somatório de todos os desempenhos(invertidos)
			inverse_total_performance = 0.0
			for i in self.individual_performance:
				inverse_total_performance += i

			#calcula a proporção inversa
			inverse_performance = []
			for i in self.individual_performance:
				inverse_performance.append(1.0/(i/inverse_total_performance))

			#realiza a redistribuição
			total_performance = 0.0
			for i in inverse_performance:
				total_performance += i

			norm_individua_perf = []
			for i in inverse_performance:
				norm_individua_perf.append(i/total_performance)


			percentual_range = []
			for i, n in enumerate(norm_individua_perf):
				if(i == 0):
					percentual_range.append([0.0, n])
				# elif(i == self.population_size - 1):
				# 	percentual_range.append([n + percentual_range[i-1][1], 1.0])
				else:
					percentual_range.append([percentual_range[i-1][1], percentual_range[i-1][1] + n])

			#corrige 0.9999...
			percentual_range[-1][1] = 1.0

			for p in percentual_range:
				print p

			#pais selecionados
			parents_list = []

			#elitismo
			best_pos = 0
			smallest_value = sys.maxint

			for i, v in enumerate(self.individual_performance):
				if(v < smallest_value):
					smallest_value = v
					best_pos = i

			#adiciona o melhor pai
			parents_list.append(best_pos)

			#seleciona os pais baseado na roleta
			for i in range((self.population_size/2) - 1):
				x = random.random()
				for j, p in enumerate(percentual_range):
					if((x >= p[0]) and (x <= p[1])):
						parents_list.append(j)
						break

			#realiza o crossover
			self.__cross(parents_list)

			#realiza a mutação
			self.__mutate()

		#roleta
		elif(self.selection_mode == 1):

			#somatório de todos os desempenhos(invertidos)
			inverse_total_performance = 0.0
			for i in self.individual_performance:
				inverse_total_performance += i

			#calcula a proporção inversa
			inverse_performance = []
			for i in self.individual_performance:
				inverse_performance.append(1.0/(i/inverse_total_performance))

			#realiza a redistribuição
			total_performance = 0.0
			for i in inverse_performance:
				total_performance += i

			performance = []
			for i in inverse_performance:
				performance.append(i/total_performance)

			performance.sort()
			performance.reverse()

			#pais selecionados
			parents_list = []

			#elitismo
			best_pos = 0
			smallest_value = sys.maxint

			for i, v in enumerate(self.individual_performance):
				if(v < smallest_value):
					smallest_value = v
					best_pos = i

			#adiciona o melhor pai
			parents_list.append(best_pos)

			#seleciona os pais baseado na roleta
			for i in range((self.population_size/2) - 1):
				x = random.random()
				p = 0.0
				index = 0

				while p < x:
					p += performance[index]
					index += 1

				parents_list.append(index)

			#realiza o crossover
			self.__cross(parents_list)

			#realiza a mutação
			self.__mutate()

		#torneio
		else:

			#pais selecionados
			parents_list = []

			#elitismo
			best_pos = 0
			smallest_value = sys.maxint

			for i, v in enumerate(self.individual_performance):
				if(v < smallest_value):
					smallest_value = v
					best_pos = i

			#adiciona o melhor pai
			parents_list.append(best_pos)

			pop_id = range(self.population_size)

			#realiza o torneio
			for i in range((self.population_size/2) - 1):
				p1 = random.choice(pop_id)
				p2 = random.choice(pop_id)

				#garante que p1 e p2 são diferentes
				while(p1 != p2):
					p1 = random.choice(pop_id)
					p2 = random.choice(pop_id)

				if(self.individual_performance[p1] < self.individual_performance[p2]):
					parents_list.append(p1)
				else:
					parents_list.append(p2)

			#realiza o crossover
			self.__cross(parents_list)

			#realiza a mutação
			self.__mutate()

	def __cross(self, selected_parents):

		#reserva o melhor pai
		best_parent = self.population[selected_parents[0]]
		print "Selected Parents: ", selected_parents

		#cria a nova população
		new_population = []

		for i in range(0, len(selected_parents), 2):
			child1 = self.population[selected_parents[i]][ : self.gene_size/2] + \
				self.population[selected_parents[i + 1]][self.gene_size/2 : ]

			child2 = self.population[selected_parents[i]][self.gene_size/2 : ] + \
				self.population[selected_parents[i + 1]][ : self.gene_size/2]

			print "F1: ", child1, "\n"
			print "F2: ", child2, "\n"


			new_population.append(child1)
			new_population.append(child2)

		#retorna o melhor pai para a população
		new_population[0] = best_parent

		for p in new_population:
			print p

		self.population = new_population

	def __mutate(self):
		for i in range(len(self.population)):
			for g in range(self.gene_size):
				x = random.random()
				if(x < self.mutation):
					self.population[i][g] = (self.population[i][g] ** 2) % self.gene_size

		#avança a geração
		self.generation += 1

# -*- coding: utf-8 -*-
import random
import sys
from multiprocessing import Array

class GeneticModel():
	def __init__(self, pop_size, chromosome_size, graph_size, infecteds, selection_mode, cross_points, mutation, cross_l):
		self.population_size = pop_size
		self.chromosome_size = chromosome_size
		self.graph_size = graph_size
		self.selection_mode = selection_mode
		self.cross_points = cross_points
		self.mutation = mutation
		self.cross_l = cross_l
		self.population = []
		#self.individual_performance = []
		self.individual_performance  = Array('i', range(pop_size), lock=False)
		self.population2 = []
		#self.individual_performance2 = []
		self.individual_performance2 = Array('i', range(pop_size), lock=False)
		self.best = []
		self.best_performance = sys.maxint
		self.global_best = []
		self.global_best_performance = sys.maxint
		self.generation = 0
		self.infecteds = infecteds

		pop_id = range(self.graph_size - 1)

		#cria a população inicial e inicializa a lista de avaliação de indivíduos
		for i in range(self.population_size):
			temp = random.sample(pop_id, chromosome_size)

			#remove infectados
			for element in infecteds:
				if(element in temp):
					temp.remove(element)

			#completa os elementos restantes
			while((self.chromosome_size - len(temp)) > 0):
				x = random.randint(0, self.graph_size - 1)
				if((not x in temp) and (not x in infecteds)):
					temp.append(x)

			self.population.append(temp)
			#self.individual_performance.append(0)
			self.population2.append(temp)
			#self.individual_performance2.append(0)

	def parents_select(self):
		#print "- Seleção de Pais:"
		#roleta-russa

		if(self.selection_mode == 0):
			#print "- Método selecionado: 0"

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

			#pais selecionados
			parents_list = []

			#elitismo
			best_pos = 0
			smallest_value = sys.maxint

			for i, v in enumerate(self.individual_performance):
				if(v < smallest_value):
					smallest_value = v
					best_pos = i

			# reserva o melhor pai
			best_parent = self.population[best_pos][:]

			# remove duplicatas
			temp = list(set(best_parent))
			while ((self.chromosome_size - len(temp)) > 0):
				x = random.randint(0, self.graph_size - 1)
				if (x not in temp):
					temp.append(x)

			self.best = temp[:]
			self.best_performance = self.individual_performance[best_pos]

			#elitismo global
			if(smallest_value < self.global_best_performance):
				self.global_best_performance = smallest_value
				self.global_best = self.population[best_pos][:]

			#seleciona os pais baseado na roleta
			for i in range(self.population_size - 1):
				x = random.random()
				for j, p in enumerate(percentual_range):
					if((x >= p[0]) and (x <= p[1])):
						parents_list.append(j)
						break

			#realiza o crossover
			self.__cross(parents_list)

		#roleta
		elif(self.selection_mode == 1):
			#print "- Método selecionado: 1"

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

			# reserva o melhor pai
			best_parent = self.population[best_pos][:]

			# remove duplicatas
			temp = list(set(best_parent))
			while ((self.chromosome_size - len(temp)) > 0):
				x = random.randint(0, self.graph_size - 1)
				if (x not in temp):
					temp.append(x)

			self.best = temp[:]
			self.best_performance = self.individual_performance[best_pos]

			#elitismo global
			if(smallest_value < self.global_best_performance):
				self.global_best_performance = smallest_value
				self.global_best = self.population[best_pos][:]

			#seleciona os pais baseado na roleta
			for i in range(self.population_size - 1):
				x = random.random()
				p = 0.0
				index = 0

				while p < x:
					p += performance[index]
					index += 1

				parents_list.append(index - 1)

			#realiza o crossover
			self.__cross(parents_list)

		#torneio
		else:
			#print "- Método selecionado: 2"

			#pais selecionados
			parents_list = []

			#elitismo
			best_pos = 0
			smallest_value = sys.maxint

			for i, v in enumerate(self.individual_performance):
				if(v < smallest_value):
					smallest_value = v
					best_pos = i

			# reserva o melhor pai
			best_parent = self.population[best_pos][:]

			# remove duplicatas
			temp = list(set(best_parent))
			while ((self.chromosome_size - len(temp)) > 0):
				x = random.randint(0, self.graph_size - 1)
				if (x not in temp):
					temp.append(x)

			self.best = temp[:]
			self.best_performance = self.individual_performance[best_pos]

			#elitismo global
			if(smallest_value < self.global_best_performance):
				self.global_best_performance = smallest_value
				self.global_best = self.population[best_pos][:]

			pop_id = range(self.population_size)

			#realiza o torneio
			for i in range(self.population_size - 1):
				p1 = random.choice(pop_id)
				p2 = random.choice(pop_id)

				#garante que p1 e p2 são diferentes
				while(p1 == p2):
					p1 = random.choice(pop_id)
					p2 = random.choice(pop_id)

				if(self.individual_performance[p1] < self.individual_performance[p2]):
					parents_list.append(p1)
				else:
					parents_list.append(p2)

			#realiza o crossover
			self.__cross(parents_list)

	def __cross(self, selected_parents):

		#cria a nova população
		new_population = []

		while(len(new_population) < self.population_size):
			parent1 = 0
			parent2 = 0

			current_cross_l = random.random()
			if(current_cross_l < self.cross_l):
				#garante que os pais serão diferentes
				while(parent1 == parent2):
					parent1 = random.randint(0, len(selected_parents) - 1)
					parent2 = random.randint(0, len(selected_parents) - 1)

				points = random.sample(range(0, self.chromosome_size), self.cross_points)
				points.sort()

				#chromosome = list(set(self.population[selected_parents[parent1]]).union(self.population[selected_parents[parent2]]))
				# child1 = random.sample(chromosome, self.chromosome_size)
				# child2 = random.sample(chromosome, self.chromosome_size)

				child1_tmp = []
				child2_tmp = []

				for i in range(len(points)):
					if(i == 0):
						if((i % 2) == 0):
							child1_tmp += self.population[selected_parents[parent1]][ :points[i]]
							child2_tmp += self.population[selected_parents[parent2]][ :points[i]]
						else:
							child1_tmp += self.population[selected_parents[parent2]][ :points[i]]
							child2_tmp += self.population[selected_parents[parent1]][ :points[i]]
					else:
						if((i % 2) == 0):
							child1_tmp += self.population[selected_parents[parent1]][points[i-1] : points[i]]
							child2_tmp += self.population[selected_parents[parent2]][points[i-1] : points[i]]
						else:
							child1_tmp += self.population[selected_parents[parent2]][points[i-1] : points[i]]
							child2_tmp += self.population[selected_parents[parent1]][points[i-1] : points[i]]

				if((len(points) % 2) == 0):
					child1_tmp += self.population[selected_parents[parent1]][points[-1]: ]
					child2_tmp += self.population[selected_parents[parent2]][points[-1]: ]
				else:
					child1_tmp += self.population[selected_parents[parent2]][points[-1]: ]
					child2_tmp += self.population[selected_parents[parent1]][points[-1]: ]

				child1 = list(set(child1_tmp))
				child2 = list(set(child2_tmp))

				while(len(child1) < self.chromosome_size):
					gene = random.choice(child2)
					if(gene not in child1):
						child1.append(gene)

				while (len(child2) < self.chromosome_size):
					gene = random.choice(child1)
					if (gene not in child2):
						child2.append(gene)

				new_population.append(child1)
				new_population.append(child2)

		#remover ultimo filho?
		self.population2 = new_population[:]

		#inicializa mutação
		self.__mutate()

	def __mutate(self):
		#print "\n- Mutação: "
		for i in range(1, self.population_size):
			for g in range(self.chromosome_size):
				x = random.random()
				if(x < self.mutation):
					#print "i:", i, "| g:", g, "| LEN pop: ", len(self.population), "| LEN gene: ", len(self.population[i])
					r = random.randint(0, self.graph_size - 1);
					if((r not in self.population2[i]) and (r not in self.infecteds)):
						self.population2[i][g] = r
					else:
						while((r in self.population2[i]) or (r  in self.infecteds)):
							r = random.randint(0, self.graph_size - 1);
						self.population2[i][g] = r

	def replace(self):
		for i in range(self.population_size):
			if (self.individual_performance2[i] < self.individual_performance[i]):
				self.individual_performance[i] = self.individual_performance2[i]
				self.population[i] = self.population2[i][:]

		# avança a geração
		self.generation += 1




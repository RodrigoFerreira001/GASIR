# -*- coding: utf-8 -*-
import random
from genetic_model import GeneticModel

ag = GeneticModel(20, 20)

for i in range(ag.population_size):
	ag.individual_performance[i] = random.randint(1,30)

ag.parents_select()

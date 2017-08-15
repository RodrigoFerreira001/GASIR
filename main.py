# -*- coding: utf-8 -*-
import random
from genetic_model import GeneticModel

ag = GeneticModel(20, 20, selection_mode = 2)

print "Performance: "
for i in range(ag.population_size):
	ag.individual_performance[i] = random.randint(1,30)
	print i ,":\t", ag.individual_performance[i]


print "População inicial:"
for i, individual in enumerate(ag.population):
	print i ,": ", individual

print "\n ----------------------------------------- \n"
ag.parents_select()
print "\n ----------------------------------------- \n"

print "\nApós Mutação:\n"

print len(ag.population)
for i, individual in enumerate(ag.population):
	print i ,": ", individual

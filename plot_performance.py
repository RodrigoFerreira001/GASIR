# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
from matplotlib import colors
import numpy as np
import sys

num_iterations = int(sys.argv[1])
num_generations = int(sys.argv[2])

generation_detailed_source = open(sys.argv[3])
detailed_source = open(sys.argv[4])
m_value = int(sys.argv[5])

#p_matrix = np.zeros((num_iterations, num_generations), dtype = int)
p_matrix = []

for i in range(num_iterations):
    p_matrix.append([])
    for j in range(num_generations):
        line = generation_detailed_source.readline()
        values = line.split(" ")
        if(values[0] != '0'):
            p_matrix[i].append(int(values[1]))


avg_perf = np.zeros(len(p_matrix[0]), dtype=float).tolist()
for i in range(num_iterations):
    for j in range(len(p_matrix[0])):
        if(i == num_iterations - 1):
            avg_perf[j] += p_matrix[i][j]
            avg_perf[j] /= num_iterations
        else:
            avg_perf[j] += p_matrix[i][j]

performance = []
best_performance = sys.maxint
best_performance_pos = 0
wrost_performance = 0
wrost_performance_pos = 0

for i in range(0, num_iterations * 3, 3):
    detailed_source.readline()
    performance.append(int((detailed_source.readline())))
    detailed_source.readline()

for i,value in enumerate(performance):
    if(value < best_performance):
        best_performance = value
        best_performance_pos = i
    elif(value > wrost_performance):
        wrost_performance = value
        wrost_performance_pos = i


teto_b = 0
teto_w = 0
teto_m = 0

for i in p_matrix[best_performance_pos]:
    if(i > teto_b):
        teto_b = i

for i in p_matrix[wrost_performance_pos]:
    if (i > teto_w):
        teto_w = i

for i in avg_perf:
    if (i > teto_m):
        teto_m = i

#melhor caso
plt.plot(range(len(p_matrix[best_performance_pos])), p_matrix[best_performance_pos], 'ro')
plt.axis([0, len(p_matrix[best_performance_pos]), 0, teto_b])
plt.xlabel('Geracoes')
plt.ylabel('Individuos Infectados')
plt.title('GASIR - Genetic Algorithm for SIR Model - Melhor Caso')
plt.savefig(sys.argv[3].split(".")[0] + "_melhor_.svg", format="svg")
plt.clf()

#pior caso
plt.plot(range(len(p_matrix[wrost_performance_pos])), p_matrix[wrost_performance_pos], 'ro')
plt.axis([0, len(p_matrix[wrost_performance_pos]), 0, teto_w])
plt.xlabel('Geracoes')
plt.ylabel('Individuos Infectados')
plt.title('GASIR - Genetic Algorithm for SIR Model - Pior Caso')
plt.savefig(sys.argv[3].split(".")[0] + "_pior_.svg", format="svg")
plt.clf()

#média
plt.plot(range(len(avg_perf)), avg_perf, 'ro')
plt.axis([0, len(avg_perf), 0, teto_m])
plt.xlabel('Geracoes')
plt.ylabel('Individuos Infectados')
plt.title('GASIR - Genetic Algorithm for SIR Model - Media')
plt.savefig(sys.argv[3].split(".")[0] + "_media_.svg", format="svg")

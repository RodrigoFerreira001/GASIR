# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
from matplotlib import colors
import numpy as np
import sys

num_iterations = int(sys.argv[1])
num_generations = int(sys.argv[2])
source = open(sys.argv[3])

#p_matrix = np.zeros((num_iterations, num_generations), dtype = int)
p_matrix = []

for i in range(num_iterations):
    p_matrix.append([])
    for j in range(num_generations):
        line = source.readline()
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


print avg_perf

for i, item in enumerate(p_matrix):
    plt.plot(range(len(item)), item, 'ro')
    plt.axis([0, len(item), 0, 410])
    plt.xlabel('Geracoes')
    plt.ylabel('Individuos Infectados')
    plt.title('GASIR - Genetic Algorithm for SIR Model')
    plt.savefig(sys.argv[3].split(".")[0] + "_" + str(i) + "_.svg", format="svg")
    plt.clf()
    #plt.show()

plt.plot(range(len(avg_perf)), avg_perf, 'ro')
plt.axis([0, len(avg_perf), 0, 410])
plt.xlabel('Geracoes')
plt.ylabel('Individuos Infectados')
plt.title('GASIR - Genetic Algorithm for SIR Model - Media')
plt.savefig(sys.argv[3].split(".")[0] + "_media_.svg", format="svg")
#plt.show()

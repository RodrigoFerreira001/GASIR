# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
from matplotlib import colors
import numpy as np
import sys

max_value = int(sys.argv[1])

file1 = open(sys.argv[2])
file2 = open(sys.argv[3])
file3 = open(sys.argv[4])


histogram = np.zeros(max_value, dtype=int).tolist()
highest_value = 0.0

sample_size = 0.5
sample = []

for i,line in enumerate(file1.readlines()):
	values = line.strip().split(",")
	for j, value in enumerate(values):
		if(j == 0):
			histogram[int(value.split("[")[1])] += 1
		elif(j == len(values) - 1):
			histogram[int(value.split("]")[0])] += 1
		else:
			histogram[int(value)] += 1

for i,line in enumerate(file2.readlines()):
	values = line.strip().split(",")
	for j, value in enumerate(values):
		if(j == 0):
			histogram[int(value.split("[")[1])] += 1
		elif(j == len(values) - 1):
			histogram[int(value.split("]")[0])] += 1
		else:
			histogram[int(value)] += 1

for i,line in enumerate(file3.readlines()):
	values = line.strip().split(",")
	for j, value in enumerate(values):
		if(j == 0):
			histogram[int(value.split("[")[1])] += 1
		elif(j == len(values) - 1):
			histogram[int(value.split("]")[0])] += 1
		else:
			histogram[int(value)] += 1

for i in range(len(histogram)):
    histogram[i] = histogram[i] / 3.0

for value in histogram:
	if(value > highest_value):
		highest_value = float(value)

print highest_value
for i,value in enumerate(histogram):
	if(value >= (highest_value - (highest_value * sample_size))):
		sample.append(i)

sample_file = open(sys.argv[1].split("_mean.")[0] + ".sample", "w")
for value in sample:
	sample_file.write(str(value) + " ")
sample_file.close()

objects = []
for i in range(max_value):
	objects.append(str(i))

y_pos = np.arange(len(objects))

ibar =  plt.bar(y_pos, histogram, align='center', alpha=0.5)

for i,element in enumerate(ibar):
	norm = colors.Normalize(0.0, 1.0)
	color = plt.cm.winter(norm(histogram[i]/highest_value))
	element.set_color(color)
#plt.xticks(y_pos, objects)
plt.xlabel('Individuo')
plt.ylabel('Vezes Selecionado')
plt.title('GASIR - Genetic Algorithm for SIR Model')

plt.savefig(sys.argv[1].split(".")[0] + "_mean.svg", format="svg")
#plt.show()

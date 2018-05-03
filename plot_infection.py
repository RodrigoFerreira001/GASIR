# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt
import sys
import ndlib.models.epidemics.SIRModel as sir
import ndlib.models.ModelConfig as mc
import csv
import ast

#transmission parameters (daily rates scaled to hourly rates)
beta = 0.2857
gamma = 0.1428

infected_list = [21]
vaccinated_list = [17,18,29,30,38,49,52,53]
neighbors_list = []

#carrega o grafo
g = nx.read_edgelist(sys.argv[1], nodetype=int)

for node in vaccinated_list:
    neighbors_list += nx.neighbors(g, node)

neighbors_list =  list(set(neighbors_list) - set(vaccinated_list))

#vizinhos de vizinhos

#for node in nx.nodes(g):
#    print nx.get_node_attributes(g, 'pos')

#guarda a posição fixa dos nós
#pos = nx.spring_layout(g, iterations=100)

# w = csv.writer(open(sys.argv[1].split(".")[0] +".csv", "w"))
# for key, val in pos.items():
#     w.writerow([key, val])

reader = csv.reader(open('moreno_highschool/moreno_highschool.csv', 'r'))
pos = {}
for row in reader:
   k, v = row
   x, y = 0, 0

   tmp = v.replace('[','')
   tmp = tmp.replace(']','')
   tmp = tmp.strip()

   splited = tmp.split()

   # print k, splited[0], splited[1]
   # print k, float(splited[0]), float(splited[1])
   # print "#########"

   #x = ast.literal_eval(tmp.split(' ')[0])
   #y = ast.literal_eval(tmp.split(' ')[1])

   #print k, x, y

   pos[int(k)] = [float(splited[0]), float(splited[1])]

#configura cor inicial dos nós
color_map = []
for node in nx.nodes(g):
    color_map.append('blue')

# Model selection
model = sir.SIRModel(g)

# Model Configuration
cfg = mc.Configuration()
cfg.add_model_parameter('beta', beta)
cfg.add_model_parameter('gamma', gamma)

cfg.add_model_initial_configuration("Infected", infected_list)
#cfg.add_model_initial_configuration("Removed", vaccinated_list)
cfg.add_model_initial_configuration("Removed", neighbors_list)

# set initial status for the model
model.set_initial_status(cfg)
iteration = model.iteration()

while(iteration['node_count'][1] > 0):
    for key, value in iteration['status'].iteritems():
        if (value == 0):
            color_map[key] = 'blue'
        elif (value == 1):
            color_map[key] = 'red'
        else:
            color_map[key] = 'green'

    # desenha o grafo
    plt.clf()
    plt.cla()
    nx.draw(g, pos=pos, with_labels=True, node_color=color_map)
    plt.draw()
    #plt.show()
    plt.savefig(sys.argv[1].split(".")[0] + "_" + str(iteration['iteration']) +".png", format="png")

    iteration = model.iteration()
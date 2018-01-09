# -*- coding: utf-8 -*-
import sys
import networkx as nx
#from igraph import *
from operator import itemgetter

fsample = open(sys.argv[1], "r")
g = nx.read_adjlist(sys.argv[2], nodetype=int)
output = open(sys.argv[2].split(".")[0] + ".info", "w")

nodes = []
tnodes = fsample.readline().strip().split(" ")

for n in tnodes:
    nodes.append(int(n))

#Page Rank
page_rankt = nx.pagerank(g)

pr_values = sorted(page_rankt.iteritems(), key=lambda (k,v): (v,k))

# for key, value in sorted(page_rankt.iteritems(), key=lambda (k,v): (v,k)):
#     print "%s: %s" % (key, value)

page_rank = {}
for node in nodes:
    page_rank.update({node : page_rankt[node]})

spage_rank = sorted(page_rank.items(), key=itemgetter(1), reverse=False)
output.write("PageRank:\n")
for entry in spage_rank:
    pos = 0
    for value in pr_values:
        if(value[0] == entry[0]):
            break
        else:
            pos += 1
    output.write(str(pos) + "º: " + str(entry) + "\n")

#Betweenness
betweennesst = nx.betweenness_centrality(g)
betweenness = {}
for node in nodes:
    betweenness.update({node : betweennesst[node]})

sbetweenness = sorted(betweenness.items(), key=itemgetter(1), reverse=True)
output.write("\nBetweenness:\n")
for entry in sbetweenness:
    output.write(str(entry) + "\n")

#Grau
degreet = g.degree(nodes)
degree = {}

print "##################"
print type(degreet)
print "##################"



for key, value in degreet.iteritems():
    degree.update({key: value})

sdegree = sorted(degree.items(), key=itemgetter(1), reverse=True)
output.write("\nGraus:\n")
for entry in sdegree:
    print entry
    output.write(str(entry) + "\n")

output.close()
# -*- coding: utf-8 -*-

#a simple network-based SIR model written in Python
#Jon Zelner
#University of Michigan
#October 20, 2009

#import this file (networkSIRWithClasses) to use the model components
#or run as 'python networkSIRWithClasses.py' to do sample runs


import igraph
import random
import copy
import pylab as pl
import scipy
from scipy import random
import heapq
import sys

#model constructor
class simpleNetworkSIRModel():
	def __init__(self, adjacencyList, sAgentList, newIList, b = .2,  g = .01):

		#parameters
		self.b = b
		self.g = g
		self.t = 0

		self.infectedCount = 0

		self.adjacencyList = adjacencyList

		#to use iGraph's internal method to do this, comment
		#out above and uncomment the following:
		#self.adjacencyList = graph.get_adjlist()

		#going to use this to store the *indices* of agents in each state
		self.sAgentList = sAgentList[:]
		self.iAgentList = []
		self.rAgentList = []

		#and here we're going to store the counts of how many agents are in each
		#state @ each time step
		self.sList = []
		self.iList = []
		self.rList = []
		self.newIList = []

		#and we'll use this to keep track of recovery times in the more
		#efficient implementation
		self.recoveryTimesHeap = []

		#shuffle the list so there's no accidental correlation in agent actions
		#random.shuffle(allAgents)

		#start with everyone susceptible
		#self.sAgentList = copy.copy(allAgents)

		Ilist = newIList[:]

		#now infect a few to infect at t = 0
		self.indexCases = []
		for i in Ilist:
			self.indexCases.append(i)
			self.infectAgent(i)
			self.iAgentList.append(i)

		print "S: ",self.sAgentList
		print "I: ",self.iAgentList
		print "R: ",self.rAgentList

# heap-based method for recovering agents using an arbitrary distribution of recovery times

	def infectAgent(self,agent):
		self.sAgentList.remove(agent)
		self.infectedCount += 1

		#uncomment for exponentially distributed recovery times
		recoveryTime = self.t + scipy.random.exponential(1/self.g)

		#comment out above and uncomment below to try different recovery
		#distributions

		#lognormal with mean 1/g
		#recoveryTime = self.t + scipy.random.lognormal(mean = scipy.log(1/g), sigma = scipy.log(20) )
		#if recoveryTime <= self.t:
		#    recoveryTime = self.t + 1

		#gamma distributed times with mean 1/g
		#shape = 10.0
		#recoveryTime = self.t + scipy.random.gamma(shape, scale = 1/(shape*self.g))

		#normally distributed with mean 1/g
		#recoveryTime = self.t + scipy.random.normal(1/self.g, 10)
		#if recoveryTime <= self.t:
		#    recoveryTime = self.t + 1

		#constant
		#recoveryTime = self.t + (1/g)

		#note that we're pushing a tuple onto the heap where the first element
		#is the recovery time and the second one is the agent's unique ID
		heapq.heappush(self.recoveryTimesHeap, (recoveryTime, agent))

		return 1

	def recoverAgents(self):
		#when we recover agents, it's similar to the previous
		#non-network implementation
		recoverList = []
		if len(self.recoveryTimesHeap) > 0:
			while self.recoveryTimesHeap[0][0] <= self.t:
				#we take advantage of python's built-in sequence sorting methods
				#which compare starting from the first element in a sequence,
				#so if these are all unique, we can sort arbitary sequences
				#by their first element without a special comparison operator
				recoveryTuple = heapq.heappop(self.recoveryTimesHeap)
				recoverList.append(recoveryTuple[1])
				if len(self.recoveryTimesHeap) == 0:
					break

		return recoverList


	#again, the guts of the model
	def run(self):
		#same as while I > 0
		while len(self.iAgentList) > 0:
			tempIAgentList = []
			recoverList = []
			newI = 0
			#we only need to loop over the agents who are currently infectious
			for iAgent in self.iAgentList:
				#and then expose their network neighbors
				for agent in self.adjacencyList[iAgent]:
					#given that the neighbor is susceptible
					if agent in self.sAgentList:
						if (random.random() < self.b):
							#and then it's the same as the other models
							newI += self.infectAgent(agent)
							tempIAgentList.append(agent)


			#then get the list of who is recovering
			recoverList = self.recoverAgents()

			#and do the bookkeeping with agent indices

			#for recoveries
			for recoverAgent in recoverList:
				self.iAgentList.remove(recoverAgent)
				self.rAgentList.append(recoverAgent)

			#and new infections
			self.iAgentList.extend(tempIAgentList)

			#then track the number of individuals in each state
			self.sList.append(len(self.sAgentList))
			self.iList.append(len(self.iAgentList))
			self.rList.append(len(self.sAgentList))
			self.newIList.append(newI)

			#increment the time
			self.t += 1

			#reshuffle the agent list so they step in a random order the next time
			#around
			random.shuffle(self.iAgentList)

		#and when we're done, return all of the relevant information
		return [self.sList, self.iList, self.rList, self.newIList]


def graph_read(file_name):
	graph_file = open(file_name, "r")
	vertex_num = int(graph_file.readline())

	adjacencyList = []
	for i in range(vertex_num):
		adjacencyList.append([])

	for i in range(vertex_num):
		temp = graph_file.readline().strip()
		neighbors = temp.split(" ")
		for neighbor in neighbors:
			adjacencyList[i].append(int(neighbor))

	return adjacencyList

if __name__=='__main__':


	#transmission parameters (daily rates scaled to hourly rates)
	b = .02 / 24.0
	g = .05 / 24.0

	#initial conditions (# of people in each state)
	S = 20
	I = 4

	#lê o grafo
	adjacencyList = graph_read(sys.argv[1])

	newSAgent = []
	newSAgent = range(len(adjacencyList))

	newIAgent = []
	newIAgent.append(1)
	newIAgent.append(2)
	newIAgent.append(3)

	newRAgent = []
	newRAgent.append(5)
	newRAgent.append(1)

	for r in newRAgent:
		if(r in newIAgent):
			newIAgent.remove(r)

		if(r in newSAgent):
			newSAgent.remove(r)

	print "Local S: \n", newSAgent
	print "Local I: \n", newIAgent
	print "Local R: \n", newRAgent

	myNetworkModel = simpleNetworkSIRModel(adjacencyList, newSAgent, newIAgent, b = b, g = g)
	networkResults = myNetworkModel.run()
	print myNetworkModel.infectedCount

	# myNetworkModel.graphPlot()
	# numNetworkCases = sum(networkResults[3])
	# pl.figure()
	# pl.plot(networkResults[1], label = 'networked outbreak; ' + str(numNetworkCases) + ' cases')
	# pl.xlabel('time')
	# pl.ylabel('# infectious')

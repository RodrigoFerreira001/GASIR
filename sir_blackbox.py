import random
import scipy
from scipy import random
import heapq

#model constructor
class SIRBB():
	def __init__(self, adjacencyList, adjacencyListWeigth, S, I, b, g):

		#parameters
		self.b = b
		self.g = g
		self.t = 0

		self.infectedCount = 0

		self.adjacencyList = adjacencyList
		self.adjacencyListWeigth = adjacencyListWeigth

		#going to use this to store the *indices* of agents in each state
		self.sAgentList = S[:]
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

		#now infect a few to infect at t = 0
		for infected in I:
			self.infectAgent(infected)
			self.iAgentList.append(infected)

	# heap-based method for recovering agents using an arbitrary distribution of recovery times
	def infectAgent(self,agent):
		self.infectedCount += 1
		if(agent in self.sAgentList):
			self.sAgentList.remove(agent)

		#uncomment for exponentially distributed recovery times
		recoveryTime = self.t + scipy.random.exponential(1/self.g)

		#comment out above and uncomment below to try different recovery
		#distributions

		#lognormal with mean 1/g
		# recoveryTime = self.t + scipy.random.lognormal(mean = scipy.log(1/self.g), sigma = scipy.log(20) )
		# if recoveryTime <= self.t:
		#    recoveryTime = self.t + 1

		#gamma distributed times with mean 1/g
		# shape = 10.0
		# recoveryTime = self.t + scipy.random.gamma(shape, scale = 1/(shape*self.g))

		#normally distributed with mean 1/g
		# recoveryTime = self.t + scipy.random.normal(1/self.g, 10)
		# if recoveryTime <= self.t:
		#    recoveryTime = self.t + 1

		#constant
		#recoveryTime = self.t + (1/self.g)

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
				for j, agent in enumerate(self.adjacencyList[iAgent]):
					#given that the neighbor is susceptible
					if agent in self.sAgentList:
						if (random.random() < self.b):
						#if (self.adjacencyListWeigth[iAgent][j] < self.b):
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
			#print('t', self.t, 'numS', len(self.sAgentList), 'numI', len(self.iAgentList) )

			#reshuffle the agent list so they step in a random order the next time
			#around
			random.shuffle(self.iAgentList)

		#and when we're done, return all of the relevant information
		return [self.sList, self.iList, self.rList, self.newIList]

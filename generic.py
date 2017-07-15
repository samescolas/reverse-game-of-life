import numpy as np

class Population:

	def __init__(self, populationSize, initialize=False):
		self.individuals = []

		if initialize==True:
			for i in range(populationSize):
				newIndividual = Individual();
				self.individuals.append(newIndividual)

	def getIndividual(ix):
		return self.individuals[ix]

	def getFittest(self):
		fittest = self.individuals[0]

		for indiv in self.individuals:
			if fittest.getFitness() <= indiv.getFitness():
				fittest = indiv
		return fittest

	def	popSize(self):
		return len(self.individuals)

class Individual:

	def __init__(self, geneLength=56):
		self.geneLength = geneLength
		self.fitness = 0
		self.genes = [0] * self.geneLength

		for i in xrange(self.geneLength):
			self.genes[i] = np.random.random()

	def getGene(self,ix):
		return self.genes[ix]

	def geneLength(self):
		return self.geneLength

	def getFitness(self):
		if self.fitness == 0:
			self.fitness = FitnessCalc.getFitness(self)
		return self.fitness

	def __str__(self):
		return map((lambda x: '1' if x > 0.5 else '0'), self.genes)

class FitnessCalc:

	def __init__(self):
		self.solution = []

	def setSolution(self, solution):
		self.solution = solution

	def getFitness(self, individual):


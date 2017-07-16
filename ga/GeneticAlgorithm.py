import random
import FitnessCalc

# {00}[01,06) | population
# {06}[07,08) | alive?
# {08}[09,12) | corner,side,center
# {12}[13,19) | # of living neighbors
# {19}[20,25) | # of living cells
# {25}[26,31) | layers of isolation
# {31}[32,35) | distance to nearest edge
# {35}[36,40) | quadrant
# {40}[41,46) | quadrant population density
# {46}[47,52) | delta
# {52}[53,54) | prediction

class GeneticAlgorithm:	
	def __init__(self):
		self.genes = [
			(0,5), (6,1), (8,3), (12,6), (19,5),
			(25,5), (31,3), (35,4), (40,5), (46,5), (52,1)
		]
		self.chromosome_length = 53
		self.crossover_rate = 0.7
		self.mutation_rate = 0.001
		self.activation_rate = 0.3
		self.pop_size = 100
		self.max_allowable_generations = 400
		self.population = []

	def create_individual(self):
		return dict([
			('fitness', 0),
			('chromosome', self.create_random_chromosome())
		])

	def create_random_chromosome(self):
		chromosome = ['0']*(self.chromosome_length - 1)
		for (activator,length) in self.genes[:-1]:
			if random.random() > self.activation_rate:
				chromosome[activator] = '1'
                        if random.random() > float(1.0/(length+1)):
			    chromosome[activator + random.randint(0, length)] = '1'
		if random.random() < self.activation_rate:
			chromosome += '1'
		else:
			chromosome += '0'
		return "".join(chromosome)

	def create_initial_population(self):
		for i in xrange(self.pop_size):
			self.population.append(self.create_individual())


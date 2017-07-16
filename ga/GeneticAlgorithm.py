import random
import FitnessCalc

# {00}[01,05) | population
# {05}[06,07) | alive?
# {07}[08,10) | corner,side,center
# {10}[11,15) | # of living neighbors BINARY
# {17}[18,23) | # of living cells
# {23}[24,29) | layers of isolation
# {29}[30,33) | distance to nearest edge
# {33}[34,38) | quadrant
# {38}[39,44) | quadrant population density
# {44}[45,50) | delta
# {50}[51,52) | prediction

class GeneticAlgorithm:	
	def __init__(self):
		self.genes = [
			(0,4), (5,1), (7,2), (10,4), (15,5),
			(21,5), (27,3), (31,4), (36,5), (42,5), (48,1)
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
                if random.random() < 0.5:
			chromosome += '1'
		else:
			chromosome += '0'
		return "".join(chromosome)

	def create_initial_population(self):
		for i in xrange(self.pop_size):
			self.population.append(self.create_individual())


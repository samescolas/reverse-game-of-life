import random
import FitnessCalc

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
			if random.random() > 0.5:
				chromosome[activator] = '1'
			chromosome[activator + random.randint(0, length)] = '1'
		if random.random() < self.activation_rate:
			chromosome += '1'
		else:
			chromosome += '0'
		return "".join(chromosome)

	def create_initial_population(self):
		for i in xrange(self.pop_size):
			self.population.append(self.create_individual())

g = GeneticAlgorithm()

print 'genes: ' + str(g.genes)

print 'pop size: ' + str(g.pop_size)

print 'creating initial population...'
g.create_initial_population()
print 'success!'

f = FitnessCalc.FitnessCalc(["testtesttesttesttesttesttesttesttesttesttesttesttest"]*10)

f.calculate_fitness(g.population[0]['chromosome'])
print 'neeeeeeeeext'
print ''
f.calculate_fitness(g.population[42]['chromosome'])

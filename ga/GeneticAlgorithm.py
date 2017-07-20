import random
import FitnessCalc

# I should probably graph the bucketized values
# and distribute buckets evenly or something...

# {00}[01,02) | alive?
# {02}[03,12) | population: (BINARY)
# {12}[13,15) | corner,side,center
# {15}[16,20) | % of living neighbors (BINARY)
# {20}[21,30) | # of living cells (BINARY)
# {30}[31,35) | distance to nearest edge
# {35}[36,41) | quadrant population density
# {41}[42,47) | delta
# {47}[48,49) | prediction

class GeneticAlgorithm:	
	def __init__(self):
		self.genes = [
			(0,1), (2,9), (12,2), (15,4), (20,9),
			(30,4), (35,5), (41,5), (47,1)
		]
		self.chromosome_length = 48
		self.crossover_ix = 24
		self.mutation_rate = 0.01
		self.activation_rate = 0.042
		self.pop_size = 200
		self.population = []

	def create_individual(self):
		return dict([
			('fitness', 0),
			('chromosome', self.create_random_chromosome())
		])

	def create_random_chromosome(self):
		chromosome = ['0']*(self.chromosome_length - 1)
		for (activator,length) in self.genes[:-1]:
			if random.random() < (self.activation_rate * random.randint(1,5)):
				chromosome[activator] = '1'
			if activator == 2:
				chromosome[activator+1:activator+length+1] = self.create_binary_string(length, (0,200))
			elif activator == 15:
				chromosome[activator+1:activator+length+1] = self.create_binary_string(length, (0,10))
			elif activator == 20:
				chromosome[activator+1:activator+length+1] = self.create_binary_string(length, (0,100))
			elif activator == 30:
				chromosome[activator+1:activator+length+1] = self.create_binary_string(length, (0,10))
			else:
				chromosome[activator+1] = '1'
				random.shuffle(chromosome[activator+1:activator+length+1])
		if random.random() < 0.5:
			chromosome += '1'
		else:
			chromosome += '0'
		return "".join(chromosome)

	def create_initial_population(self):
		for i in xrange(self.pop_size):
			self.population.append(self.create_individual())

	def create_binary_string(self, length, boundaries):
		b = '{0:b}'.format(random.randint(boundaries[0], boundaries[1]))
		while len(b) < length:
			b = '0'+b
		print 'returning ' + b
		return list(b)

	def roulette_selection(self, total_fitness):
		threshold = random.randint(0, int(total_fitness))
		fitness_sum = 0.0
		for indiv in self.population:
			fitness_sum += indiv['fitness']
			if fitness_sum >= threshold:
				return indiv['chromosome']
		return indiv['chromosome']

	def crossover(self, parent1, parent2):
		offspring1 = parent1[0:self.crossover_ix] + parent2[self.crossover_ix:]
		offspring2 = parent2[0:self.crossover_ix] + parent[self.crossover_ix:]

	def mutate(self, chromosome):
		chromosome = list(chromosome)
		for gene_id,length in self.genes[:-1]:
			if random.random() < self.mutation_rate:
				print 'mutating activator!'
				if chromosome[gene_id] == '1':
					chromosome[gene_id] = '0'
				else:
					chromosome[gene_id] = '1'
			if random.random() < (self.mutation_rate * length):
				print 'mutating data!'
				if gene_id == 0:
					chromosome[gene_id+1:gene_id+length+1] = self.create_binary_string(length, (0,200))
				elif gene_id == 15:
					chromosome[gene_id+1:gene_id+length+1] = self.create_binary_string(length, (0,10))
				elif gene_id == 20:
					chromosome[gene_id+1:gene_id+length+1] = self.create_binary_string(length, (0,100))
				elif gene_id == 36:
					chromosome[gene_id+1:gene_id+length+1] = self.create_binary_string(length, (0,10))
				else:
					random.shuffle(chromosome[gene_id+1:gene_id+length+1])
		return ''.join(chromosome)

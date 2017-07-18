import random
import FitnessCalc

# I should probably graph the bucketized values
# and distribute buckets evenly or something...

# {00}[01,05) | population: 20%,40%,60%,80%,100%
# {05}[06,07) | alive?
# {07}[08,10) | corner,side,center
# {10}[11,15) | # of living neighbors (BINARY)
# {15}[16,25) | # of living cells (BINARY)
# {25}[26,31) | layers of isolation
# {31}[32,35) | distance to nearest edge
# {35}[36,39) | quadrant
# {39}[40,45) | quadrant population density
# {45}[46,51) | delta
# {51}[52,53) | prediction

class GeneticAlgorithm:	
	def __init__(self):
		self.genes = [
			(0,4), (5,1), (7,2), (10,4), (15,9),
			(25,5), (31,3), (35,3), (39,5), (45,5), (51,1)
		]
		self.chromosome_length = 52
		self.crossover_ix = 23
		self.mutation_rate = 0.002
		self.activation_rate = 0.3
		self.pop_size = 150
		self.population = []

	def create_individual(self):
		return dict([
			('fitness', 0),
			('chromosome', self.create_random_chromosome())
		])

	def create_random_chromosome(self):
		chromosome = ['0']*(self.chromosome_length - 1)
		for (activator,length) in self.genes[:-1]:
			if random.random() < self.activation_rate:
				chromosome[activator] = '1'
			if activator == 10:
				chromosome[activator+1:activator+length+1] = self.create_binary_string(length, (0,8))
			elif activator == 15:
				chromosome[activator+1:activator+length+1] = self.create_binary_string(length, (0,396))
			else:
				if random.random() > float(1.0/(length+1)):
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
				if gene_id == 10:
					b = '{0:b}'.format(random.randint(0,8))
					while len(b) < 4:
						b = '0'+b
					chromosome[gene_id+1:gene_id+length+1] = list(b)
				else:
					random.shuffle(chromosome[gene_id+1:gene_id+length+1])
		return ''.join(chromosome)

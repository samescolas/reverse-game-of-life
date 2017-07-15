from FitnessChecks import *

class FitnessCalc:

	def __init__(self, training_data):
		self.genes = [
			(0,5), (6,1), (8,3), (12,6), (19,5),
			(25,5), (31,3), (35,4), (40,5), (46,5), (52,1)
		]
		self.chromosome_length = 53
		self.training_data = training_data

	def calculate_fitness(self,chromosome):
		for example in self.training_data:
			self.test_chromosome(example, chromosome)


	def test_chromosome(self, example, chromosome):
		classification_met = True
		for ix,(activator,length) in enumerate(self.genes[:-1]):
			if chromosome[activator] == '1':
				res = self.test_gene(chromosome[activator+1:activator+length+1], example[ix], ix)

	def test_gene(self, gene, example, ix):
		test = {
			0: check_pop,
			1: check_alive,
			2: check_neighbors,
			3: check_living_neighbors,
			4: check_size,
			5: check_isolation_layers,
			6: check_nearest_edge,
			7: check_quadrant,
			8: check_quadrant_density,
			9: check_delta
		}[ix](gene, example)

from fitness_checks import *
import sys

# firness equation: w1*PA + w2*CPH+w3*S

class FitnessCalc:

	def __init__(self, training_data):
		self.w1 = 0.4
		self.w2 = 0.3
		self.w3 = 0.15
		self.w4 = 0.15
		self.genes = [
			(0,4), (5,1), (7,2), (10,4), (15,9),
			(25,5), (31,3), (35,3), (39,5), (45,5), (51,1)
		]
		self.chromosome_length = 52
		self.training_data = training_data
		self.num_examples = len(self.training_data.keys())

        # test chromosome against each example in training set
	def calculate_fitness(self,chromosome):
		results = 0,0,0,0
		for ix in xrange(1,self.num_examples + 1):
			results = [sum(x) for x in zip(results, self.test_chromosome(self.training_data[ix], chromosome))]
		tp,fp,tn,fn = results
		PA = float(tp) / max((tp+tn+fp+fn), 0.000001)
		C = float(tp+tn)/(tp+fp+fn+tn)
		S = float(tp) / max((tp + fn), 0.000001)
		CPH = 10 - reduce((lambda x,y:int(x)+int(y)), [chromosome[x] for x,y in self.genes])
		print 'score: ' + str(100 * float(tp+tn)/(tp+fp+fn+tn))
		print 'tp: {}'.format(tp)
		print 'tn: {}'.format(tn)
		print 'fp: {}'.format(fp)
		print 'fn: {}'.format(fn)
		if tp + fp == 0 or tn + fn == 0:
			return 0
		return self.w1*PA + self.w2*C + self.w3*CPH + self.w4*S

	def test_chromosome(self, example, chromosome):
		classification_results = {}
		classifications = []
		tp,fp,tn,fn = 0,0,0,0
		for gene_id,(activator,length) in enumerate(self.genes[:-1]):
			if chromosome[activator] == '1':
				classification_results[activator] = self.test_gene(chromosome[activator+1:activator+1+length], example, gene_id)

		for cell_result in xrange(400):
			classification_met = True
			for key in classification_results.keys():
				if classification_results[key][cell_result] == False:
					classifications.append(False)
					classification_met = False
					break
			if classification_met == True:
				classifications.append(True)
			else:
				classification_met = True

		for ix,c in enumerate(classifications):
			if c == True:
				if str(example['cells'][ix + 1]['outcome']) == str(chromosome[-1]):
					tp += 1
				else:
					fp += 1
			else:
				if str(example['cells'][ix + 1]['outcome']) == str(chromosome[-1]):
					fn += 1
				else:
					tn += 1
		return tp,fp,tn,fn

        # test chromosome against each cell in grid
	def test_gene(self, gene, data, gene_id):
		test = []
		if gene_id == 0:
			test = [check_pop(gene, data['population'])]*400
		elif gene_id == 9:
			test = [check_delta(gene, data['delta'])]*400
		else:
			for cell in xrange(1,401):
				test.append( {
					1: check_alive,
					2: check_neighbors,
					3: check_living_neighbors,
					4: check_size,
					5: check_isolation_layers,
					6: check_nearest_edge,
					7: check_quadrant,
					8: check_quadrant_density,
				}[gene_id](gene, data['cells'][cell]) )
		return test

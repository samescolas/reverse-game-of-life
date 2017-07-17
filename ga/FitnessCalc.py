from fitness_checks import *
import sys

class FitnessCalc:

	def __init__(self, training_data):
            self.genes = [
                    (0,4), (5,1), (7,2), (10,4), (15,5),
                    (21,5), (27,3), (31,4), (36,5), (42,5), (48,1)
            ]
            self.chromosome_length = 53
            self.training_data = training_data

        # test chromosome against each example in training set
	def calculate_fitness(self,chromosome):
            results = 0,0,0,0
            for ix in xrange(1,501):
                results = [sum(x) for x in zip(results, self.test_chromosome(self.training_data['42'], chromosome))]
            print 'tp: {}'.format(results[0])
            print 'fp: {}'.format(results[1])
            print 'tn: {}'.format(results[2])
            print 'fn: {}'.format(results[3])
            print 'total: {}'.format(results[0] + results[1] + results[2] + results[3])


	def test_chromosome(self, example, chromosome):
            classification_results = {}
            classifications = []
            tp,fp,tn,fn = 0,0,0,0
	    for ix,(activator,length) in enumerate(self.genes[:-1]):
		if chromosome[activator] == '1':
		    classification_results[activator] = self.test_gene(chromosome[activator+1:activator+1+length], example, ix)

            for ix in xrange(400):
                classification_met = True
                for activator in classification_results.keys():
                    if classification_results[activator][ix] == False:
                        classifications.append(False)
                        classification_met = False
                        break
                if classification_met == True:
                    classifications.append(True)
                else:
                    classification_met = True
            for ix,c in enumerate(classifications):
                if c == True:
                    if example['start.' + str(ix+1)] == chromosome[-1]:
                        tp += 1
                    else:
                        fp += 1
                else:
                    if example['start.' + str(ix+1)] == chromosome[-1]:
                        tn += 1
                    else:
                        fn += 1
            return tp,fp,tn,fn

        # test chromosome against each cell in grid
	def test_gene(self, gene, example, ix):
            test = []
            if ix == 0:
                test = [check_pop(gene, example, 0)] * 400
            else:
                for cell in xrange(1,401):
                    test.append( {
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
                    }[ix](gene, example, cell) )
            return test

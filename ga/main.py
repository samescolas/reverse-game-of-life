#!/usr/bin/python

from FitnessCalc import FitnessCalc
from GeneticAlgorithm import GeneticAlgorithm
from data_processing import process_data

# initialize empty collection
summary = process_data('../resources/train.csv', 500, True)

# create GA instance
ga = GeneticAlgorithm()

# load data into fitness calculator
fc = FitnessCalc(summary)

#create initial population
ga.create_initial_population()

for generations in xrange(1,11):
	max_fitness = 0.0
	print 'generation ' + str(generations)
	print 'max fitness: ' + str(max_fitness)
#assign fitness levels
	total_fitness = 0.0
	for i,indiv in enumerate(ga.population):
		fitness = fc.calculate_fitness(indiv['chromosome'])
		total_fitness += fitness
		indiv['fitness'] = fitness
		print str(round(fitness,2)) + ' ' + indiv['chromosome']
		print 'avg fitness: ' + str(float(total_fitness) / (i+1))

	#selection (ROULETTE STYLE)
	new_pop = []
	for pair in xrange(ga.pop_size / 2):
		c1,c2 = ga.roulette_selection(total_fitness),ga.roulette_selection(total_fitness)
		print 'combining '
		print c1
		print ' and '
		print c2
		new_pop.append({
			'fitness': 0,
			'chromosome': ga.mutate(c1)
		} )
		new_pop.append( {
			'fitness': 0,
			'chromosome': ga.mutate(c2)
		} )
	
	ga.population = new_pop

winner = ga.population[0]
for indiv in ga.population:
	if indiv['fitness'] > winner['fitness']:
		winner = indiv

print 'best chromosome: ' + winner['chromosome']
winner['fitness'] = fc.calculate_fitness(winner['chromosome'])
print 'fitness: ' + str(winner['fitness'])

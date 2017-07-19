#!/usr/bin/python

import csv
from FitnessCalc import FitnessCalc
from GeneticAlgorithm import GeneticAlgorithm
from data_processing import *

import sys

# initialize empty collection
summary = {}

print 'reading in data...'

# read data from csv
with open('../resources/train.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for i,record in enumerate(reader):
		if i == 0:
			keys = record
			continue
		elif i < 5000:
			continue
		elif i == 5501:
			break
		summary[i-4999] = {
			'population': reduce((lambda x,y: int(x)+int(y)), record[402:]),
			'delta': record[1],
			'cells': {}
		}
		print str(i)
		for j,cell in enumerate(keys[402:]):
			neighbors = get_neighbors(int(cell[5:]), record[401:])
			density = get_quadrant_densities(record[401:])
			summary[i-4999]['cells'][j+1] = {
				'status': record[j+2],
				'outcome': record[j+398],
				'neighbors': len(neighbors[0]),
				'living_neighbors': len(neighbors[1]),
				'quadrant': get_quadrant(int(cell[5:])),
				'quadrant_density': density[get_quadrant(int(cell[5:])) - 1],
				'nearest_edge': get_nearest_edge(int(cell[5:]))
			}
			if record[j+2] == '1':
				summary[i-4999]['cells'][j+1]['size'] = get_size(int(cell[5:]), record[401:])
			else:
				summary[i-4999]['cells'][j+1]['size'] = 0

# create GA instance
ga = GeneticAlgorithm()

# load data into fitness calculator
fc = FitnessCalc(summary)

#create initial population
ga.create_initial_population()

for generations in xrange(1,21):
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

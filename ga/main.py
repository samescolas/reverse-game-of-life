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
		elif i == 501:
			break
                summary[i] = {
					'population': reduce((lambda x,y: int(x)+int(y)), record[402:]),
					'delta': record[1],
					'cells': {}
				}
                print str(i/500.0*100) + '%'
                for j,cell in enumerate(keys[402:]):
					neighbors = get_neighbors(int(cell[5:]), record[401:])
					density = get_quadrant_densities(record[401:])
					summary[i]['cells'][j+1] = {
						'status': record[j+2],
						'neighbors': len(neighbors[0]),
						'living_neighbors': len(neighbors[1]),
						'quadrant': get_quadrant(int(cell[5:])),
						'quadrant_density': density[get_quadrant(int(cell[5:])) - 1],
						'nearest_edge': get_nearest_edge(int(cell[5:]))
					}
					if record[j+2] == '1':
						summary[i]['cells'][j+1]['size'] = get_size(int(cell[5:]), record[401:])
					else:
						summary[i]['cells'][j+1]['size'] = 0

# create GA instance
ga = GeneticAlgorithm()

# load data into fitness calculator
fc = FitnessCalc(summary)

#create initial population
ga.create_initial_population()

#assign fitness levels
total_fitness = 0.0
for indiv in ga.population:
	fitness = fc.calculate_fitness(indiv['chromosome'])
	total_fitness += fitness
	indiv['fitness'] = fitness
	print str(fitness) + ' ' + indiv['chromosome']

#selection (ROULETTE STYLE)
c1 = ga.roulette_selection(total_fitness)
c2 = ga.roulette_selection(total_fitness)

print c1
print c2

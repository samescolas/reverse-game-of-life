#!/usr/bin/python

import csv
from FitnessCalc import FitnessCalc
from GeneticAlgorithm import GeneticAlgorithm
from data_processing import *

import sys

def space_horiz(record, pos):
	space = 0
	x = pos + 1
	while True:
		if (x % 20 == 1 or record['stop.' + str(x)] == '1'):
			break
		space += 1
		x += 1
	x = pos - 1
	while True:
		if (x % 20 == 0 or record['stop.' + str(x)] == '1'):
			break
		space += 1
		x -= 1
	return space

def	space_vert(record, pos):
	space = 0
	x = pos + 20
	while True:
		if (x >= 400 or record['stop.' + str(x)] == '1'):
			break
		space += 1
		x += 20
	x = pos - 20
	while True:
		if (x <= 0 or record['stop.' + str(x)] == '1'):
			break
		space += 1
		x -= 20
	return space

# read data from csv
print 'reading in data...'

# initialize empty collection
summary = {}

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

print 'creating ga...'
ga = GeneticAlgorithm()


print 'ga created...'
print 'creating fitness calculator...'
fc = FitnessCalc(summary)

print 'fitness calculator created...'
print 'generating initial population...'
ga.create_initial_population()

print 'initiail population created...'
for indiv in ga.population:
	print 'testing chromosome ' + indiv['chromosome'] + '...'
	indiv['fitness'] = fc.calculate_fitness(indiv['chromosome'])

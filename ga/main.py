#!/usr/bin/python

import csv
from FitnessCalc import FitnessCalc
from GeneticAlgorithm import GeneticAlgorithm

def	get_living_neighbors(record, pos):
	(l,r,t,b) = (pos-1,pos+1,pos-20,pos+20)
	(tl,tr,bl,br) = (t-1,t+1,b-1,b+1)
	neighbors = 0
	if l > 0 and pos % 20 != 1:
		if record['stop.' + str(l)] == '1':
			neighbors += 1
	if r < 400 and pos % 20 != 0:
		if record['stop.' + str(r)] == '1':
			neighbors += 1
	if t > 0:
		if record['stop.' + str(t)] == '1':
			neighbors += 1
	if b < 400:
		if record['stop.' + str(b)] == '1':
			neighbors += 1
	if tl > 0 and pos % 20 != 1:
		if record['stop.' + str(tl)] == '1':
			neighbors += 1
	if tr > 0 and pos % 20 != 0:
		if record['stop.' + str(tr)] == '1':
			neighbors += 1
	if bl < 400:
		if record['stop.' + str(bl)] == '1':
			neighbors += 1
	if br < 400:
		if record['stop.' + str(br)] == '1':
			neighbors += 1
	return neighbors

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

def get_neighbors(pos):
	if pos == 1 or pos == 20 or pos == 381 or pos == 400:
		return 3
	elif pos < 20 or pos > 380 or pos % 20 < 2:
		return 5
	return 8

def min_edge(pos):
	if pos < 201:
		if pos % 20 < 11:
			return min(pos % 20, int(pos / 20))
		return min(20 - (pos % 20), int(pos / 20))
	else:
		if pos % 20 < 11:
			return min(pos % 20, 20 - (pos / 20))
	return min(20 - (pos % 20), 20 - (pos / 20))

def get_quadrant(pos):
	if pos < 201:
		if pos % 20 < 11:
			return 2
		return 1
	else:
		if pos % 20 < 11:
			return 3
	return 4

# initialize empty collection
data = {}

# read data from csv
row = -1

print 'reading in data...'

with open('../resources/train.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for record in reader:
		row += 1
		if row == 0:
			keys = record
			continue
		elif row == 1001:
			break
		data[record[0]] = {}
		for ix,field in enumerate(keys[1:]):
			data[record[0]][field] = record[ix + 1]
		data[record[0]]['population'] = reduce((lambda x,y: int(x)+int(y)), record[403:])
		row += 1

print 'creating ga...'

ga = GeneticAlgorithm()

print 'ga created...'
print 'creating fitness calculator...'

fc = FitnessCalc(data)

print 'fitness calculator created...'
print 'generating initial population...'

ga.create_initial_population()

print 'initiail population created...'

for indiv in ga.population:
	print 'testing chromosome ' + indiv['chromosome'] + '...'
	fc.calculate_fitness(indiv['chromosome'])

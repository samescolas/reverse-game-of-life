#!/usr/bin/python

import csv
from FitnessCalc import FitnessCalc
from GeneticAlgorithm import GeneticAlgorithm

import sys
  
def     get_neighbors(cell, example):
        (l,r,t,b) = (cell-1,cell+1,cell-20,cell+20)
        (tl,tr,bl,br) = (t-1,t+1,b-1,b+1)
        neighbors = []

	if l > 0 and cell % 20 != 1:
		if example[l] == '1':
                        neighbors.append(l)
	if r < 400 and cell % 20 != 0:
		if example[r] == '1':
                        neighbors.append(r)
	if t > 0:
		if example[t] == '1':
                        neighbors.append(t)
	if b < 400:
		if example[b] == '1':
                        neighbors.append(b)
	if tl > 0 and cell % 20 != 1:
		if example[tl] == '1':
                        neighbors.append(tl)
	if tr > 0 and cell % 20 != 0:
		if example[tr] == '1':
                        neighbors.append(tr)
	if bl < 400:
		if example[bl] == '1':
                        neighbors.append(bl)
	if br < 400:
		if example[br] == '1':
                        neighbors.append(br)
        return neighbors
 
def     get_size(cell, example):
        members = {}
        new = [cell]
        while len(new) != 0:
            to_add = new[:]
            new = []
            for c in to_add:
                members[c] = 1
                new += get_neighbors(c, example)
            new = [x for x in new if x not in members.keys()]
        return len(members.keys())

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
print 'reading in data...'

summary = {}
with open('../resources/train.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for i,record in enumerate(reader):
		if i == 0:
			keys = record
			continue
		elif i == 1001:
			break
                summary[i] = {}
                summary[i]['population'] = reduce((lambda x,y: int(x)+int(y)), record[403:])
                summary[i]['delta'] = record[1]
                summary[i]['cells'] = {}
                print str(i/1000.0*100) + '%'
                for j,cell in enumerate(keys[402:]):
                        summary[i]['cells'][j+1] = {}
                        summary[i]['cells'][j+1]['status'] = record[j+1]
                        summary[i]['cells'][j+1]['neighbors'] = get_neighbors(int(cell[5:]), record[401:])
                        if record[j+1] == '1':
                            summary[i]['cells'][j+1]['size'] = get_size(int(cell[5:]), record[401:])
                        else:
                            summary[i]['cells'][j+1]['size'] = 0


print summary[1]

sys.exit(0)

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

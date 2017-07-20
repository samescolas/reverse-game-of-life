#!/usr/bin/python

import matplotlib.pyplot as plt
from data_processing import process_data

import sys

sample_size = 15000

# initialize empty collection
data = process_data('../resources/train.csv', sample_size, True)

# read data from csv

alive = {}
dead = {}

aliveX = []
aliveY = []

deadX = []
deadY = []

deltas = []
pos = 1

for i in xrange(1,sample_size):
	for cell in xrange(1, 401):
		ratio = data[i]['cells'][cell]['living_neighbors'] / float(data[i]['cells'][cell]['neighbors'])
		if data[i]['cells'][cell]['outcome'] == '1':
			if ratio in alive.keys():
				alive[ratio] += 1
			else:
				alive[ratio] = 1
		else:
			if ratio in dead.keys():
				dead[ratio] += 1
			else:
				dead[ratio] = 1

total_alive = sum(alive.values())
total_dead =  sum(dead.values())

for key in alive.keys():
	aliveX.append(key)
	if key in dead.keys():
		aliveY.append(float(alive[key])/(alive[key]+dead[key]))
	else:
		aliveY.append(1)

for key in dead.keys():
	deadX.append(key)
	if key in alive.keys():
		deadY.append(float(dead[key])/(alive[key]+dead[key]))
	else:
		deadY.append(1)

plt.plot(deadX, deadY, 'rx')
plt.plot(aliveX, aliveY, 'bv')
plt.show()

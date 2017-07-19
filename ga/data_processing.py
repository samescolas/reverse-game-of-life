import csv
import sys

def		process_data(filepath, limit=100000, verbose=False):
	summary = {}
	with open(filepath, 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		for i,record in enumerate(reader):
			if i == 0:
				keys = record
				continue
			elif i == limit:
				break
			summary[i] = {
				'population': reduce((lambda x,y: int(x)+int(y)), record[402:]),
				'delta': record[1],
				'cells': {}
			}
			if verbose == True:
				print str(100 *(float(i)/limit)) + '%'
			for j,cell in enumerate(keys[402:]):
				neighbors = get_neighbors(int(cell[5:]), record[401:])
				density = get_quadrant_densities(record[401:])
				summary[i]['cells'][j+1] = {
					'status': record[j+402],
					'outcome': record[j+2],
					'neighbors': len(neighbors[0]),
					'living_neighbors': len(neighbors[1]),
					'quadrant': get_quadrant(int(cell[5:])),
					'quadrant_density': density[get_quadrant(int(cell[5:])) - 1],
					'nearest_edge': get_nearest_edge(int(cell[5:]))
				}
				if record[j+402] == '1':
					summary[i]['cells'][j+1]['size'] = get_size(int(cell[5:]), record[401:])
				else:
					summary[i]['cells'][j+1]['size'] = 0
	return summary


def     get_neighbors(cell, example):
        (l,r,t,b) = (cell-1,cell+1,cell-20,cell+20)
        (tl,tr,bl,br) = (t-1,t+1,b-1,b+1)
        living_neighbors = []
        neighbors = []

	if l > 0 and cell % 20 != 1:
		if example[l] == '1':
			living_neighbors.append(l)
		else:
			neighbors.append(l)
	if r < 400 and cell % 20 != 0:
		if example[r] == '1':
			living_neighbors.append(r)
		else:
			neighbors.append(r)
	if t > 0:
		if example[t] == '1':
			living_neighbors.append(t)
		else:
			neighbors.append(t)
	if b < 400:
		if example[b] == '1':
			living_neighbors.append(b)
		else:
			neighbors.append(b)
	if tl > 0 and cell % 20 != 1:
		if example[tl] == '1':
			living_neighbors.append(tl)
		else:
			neighbors.append(tl)
	if tr > 0 and cell % 20 != 0:
		if example[tr] == '1':
			living_neighbors.append(tr)
		else:
			neighbors.append(tr)
	if bl < 400:
		if example[bl] == '1':
			living_neighbors.append(bl)
		else:
			neighbors.append(bl)
	if br < 400:
		if example[br] == '1':
			living_neighbors.append(br)
		else:
			neighbors.append(br)
	return neighbors,living_neighbors
 
def     get_size(cell, example):
        members = {}
        new = [cell]
        while len(new) != 0:
            to_add = new[:]
            new = []
            for c in to_add:
                members[c] = 1
                new += get_neighbors(c, example)[1]
            new = [x for x in new if x not in members.keys()]
        return len(members.keys())

def get_quadrant(pos):
	if pos < 201:
		if pos % 20 < 11:
			return 2
		return 1
	else:
		if pos % 20 < 11:
			return 3
	return 4

def get_quadrant_densities(example):
	total = reduce((lambda x,y: int(x) + int(y)), example)
	densities = [0]*4
	for cell in xrange(1,401):
		if example[cell] == '1':
			densities[get_quadrant(cell) - 1] += 1
	return [x/total for x in densities]

def get_nearest_edge(cell):
	if cell < 201:
		if cell % 20 < 11:
			return min(cell % 20, int(cell / 20))
		return min(20 - (cell % 20), int(cell / 20))
	else:
		if cell % 20 < 11:
			return min(cell % 20, 20 - (cell / 20))
		return min(20 - (cell % 20), 20 - (cell / 20))


import pandas as pd
import pickle
import os

def process_data(filepath, num_examples=500):
	if os.path.exists(filepath[0:filepath.rfind('.')] + '.pkl'):
		return pd.read_pickle(filepath[0:filepath.rfind('.')] + '.pkl')
	train_df = pd.read_csv(filepath, nrows=num_examples)

	stop = ['stop.' + str(x) for x in xrange(1,401)]
	start = ['start.' + str(x) for x in xrange(1,401)]
	
	data = train_df[stop].stack()
	outcomes = train_df[start].stack()
	deltas = train_df['delta'].values
	types = ([1]+[2]*18+[1]) + ([2]+[3]*18+[2])*18 + ([1]+[2]*18+[1])
	
	cols = ['board', 'delta', 'position', 'size', 'type', 'alive', 'neighbors', 'population', 'outcome']
	
	processed_data = pd.DataFrame
	
	for board in xrange(num_examples):
		print str(100 * (float(board)/num_examples)) + '%'
		df = [
			[board]*400,
			[deltas[board]]*400,
			range(1,401),
			[get_size(x, data[board].values) for x in xrange(400)],
			[types[x] for x in xrange(400)],
			list(data[board].values.transpose()),
	                [get_neighbors(x, data[board].values) for x in xrange(400)],
			[sum(data[board])]*400,
			list(outcomes[board].values.transpose())
		]
		df = [list(l) for l in zip(*df)]
		df = pd.DataFrame(df, columns=cols)
		if processed_data.empty:
			processed_data = df
		else:
			processed_data = pd.concat([processed_data, df], ignore_index=True)
		processed_data.to_pickle(filepath[0:filepath.rfind('.')] + '.pkl')
	return processed_data


def	get_nghbs(cell, example):
        (l,r,t,b) = (cell-1,cell+1,cell-20,cell+20)
        (tl,tr,bl,br) = (t-1,t+1,b-1,b+1)
        living_neighbors = []
        neighbors = []

	if l >= 0 and (cell + 1) % 20 != 1:
		if example[l] == 1:
			living_neighbors.append(l)
		neighbors.append(l)
	if r < 400 and (cell + 1) % 20 != 0:
		if example[r] == 1:
			living_neighbors.append(r)
		neighbors.append(r)
	if t >= 0:
		if example[t] == 1:
			living_neighbors.append(t)
		neighbors.append(t)
	if b < 400:
		if example[b] == 1:
			living_neighbors.append(b)
		neighbors.append(b)
	if tl >= 0 and (cell + 1) % 20 != 1:
		if example[tl] == 1:
			living_neighbors.append(tl)
		neighbors.append(tl)
	if tr >= 0 and (cell + 1) % 20 != 0:
		if example[tr] == 1:
			living_neighbors.append(tr)
		neighbors.append(tr)
	if bl < 400:
		if example[bl] == 1:
			living_neighbors.append(bl)
		neighbors.append(bl)
	if br < 400:
		if example[br] == 1:
			living_neighbors.append(br)
		neighbors.append(br)
	return (neighbors,living_neighbors)

def     get_neighbors(cell, example):
	n = get_nghbs(cell, example)
	return float(len(n[1])) / len(n[0])

def     get_size(cell, example):
        members = {}
        new = [cell]
        while len(new) != 0:
            to_add = new[:]
            new = []
            for c in to_add:
                members[c] = 1
                new += get_nghbs(c, example)[1]
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


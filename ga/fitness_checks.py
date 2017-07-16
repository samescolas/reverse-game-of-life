import sys

# 5 buckets and 400 total == 80
def	check_pop(gene, val, cell):
	if '1' in gene:
		bucket = gene.index('1')
	else:
		bucket = 0
        if val['population'] >= bucket * 80 and val['population'] < (bucket + 1) * 80:
            return True
	return False

def	check_alive(gene, val, cell):
        if val['start.' + str(cell)] == gene:
            return True
	return False

def	check_neighbors(gene, val, cell):
        if cell == 1 or cell == 20 or cell == 381 or cell == 400:
            if '1' not in gene:
                return True
        elif cell % 20 < 2:
            if '1' in gene and gene.index('1') == 2:
                return True
        elif '1' in gene and gene.index('1') == 3:
            return True
	return False

def     get_neighbors(cell, example):
        (l,r,t,b) = (cell-1,cell+1,cell-20,cell+20)
        (tl,tr,bl,br) = (t-1,t+1,b-1,b+1)
        neighbors = []

	if l > 0 and cell % 20 != 1:
		if example['stop.' + str(l)] == '1':
                        neighbors.append(l)
	if r < 400 and cell % 20 != 0:
		if example['stop.' + str(r)] == '1':
                        neighbors.append(r)
	if t > 0:
		if example['stop.' + str(t)] == '1':
                        neighbors.append(t)
	if b < 400:
		if example['stop.' + str(b)] == '1':
                        neighbors.append(b)
	if tl > 0 and cell % 20 != 1:
		if example['stop.' + str(tl)] == '1':
                        neighbors.append(tl)
	if tr > 0 and cell % 20 != 0:
		if example['stop.' + str(tr)] == '1':
                        neighbors.append(tr)
	if bl < 400:
		if example['stop.' + str(bl)] == '1':
                        neighbors.append(bl)
	if br < 400:
		if example['stop.' + str(br)] == '1':
                        neighbors.append(br)
        return neighbors
        

def	check_living_neighbors(gene, val, cell):
        classification = int(gene,2)
        if classification > 8:
            return False
        actual = len(get_neighbors(cell, val))

        if classification == actual:
            return True
	return False

# Six buckets: 
#       1-2     00000   B = 0
#       3-4     10000   B = 1
#       5-7     01000   B = 2
#       8-11    00100   B = 3
#       9-15,   00010   B = 4
#       16+     00001   B = 5

def	check_size(gene, val, cell):
        members = {}
        bucket = 0
        if '1' in gene:
            bucket = gene.index('1') + 1
        new = [cell]
        while len(new) != 0:
            to_add = new[:]
            new = []
            for c in to_add:
                members[c] = 1
                new += get_neighbors(c, val)
            new = [x for x in new if x not in members.keys()]
        num_members = len(members.keys())

        if bucket == 0:
            if num_members < 3:
                return True
        elif bucket == 1:
            if num_members >= 3 and num_members < 5:
                return True
        elif bucket == 2:
            if num_members >= 5 and num_members < 8:
                return True
        elif bucket == 3:
            if num_members >= 8 and num_members < 12:
                return True
        elif bucket == 4:
            if num_members >= 12 and num_members < 16:
                return True
        elif bucket == 5:
            if num_members >= 16:
                return True
	return False

def	check_isolation_layers(gene, val, cell):
	return True

def	check_nearest_edge(gene, val, cell):
	return True

def	check_quadrant(gene, val, cell):
	return True

def	check_quadrant_density(gene, val, cell):
	return True

def	check_delta(gene, val, cell):
	return True

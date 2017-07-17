import sys

# 5 buckets and 400 total == 80
def	check_pop(gene, population):
	if '1' not in gene:
		bucket = 0
	else:
		bucket = gene.index('1') + 1
        if population >= bucket * 80 and population < (bucket + 1) * 80:
            return True
	return False

def	check_alive(gene, val, cell):
        if val['start.' + str(cell)] == gene:
            return True
	return False

def	check_neighbors(gene, data):
	if '1' not in gene and data['neighbors'] == 3:
		return True
	elif gene.index('1') == 0 and data['neighbors'] == 5:
		return True
	elif gene.index('1') == 1 and data['neighbors'] == 8:
		return True
	return False

def	check_living_neighbors(gene, data):
        classification = int(gene,2)
        if classification > 8:
            return False
        actual = data['living_neighbors']

        if int(classification) == int(actual):
            return True
	return False

# Six buckets: 
#       0-2     00000   B = 0
#       3-4     10000   B = 1
#       5-7     01000   B = 2
#       8-11    00100   B = 3
#       9-15,   00010   B = 4
#       16+     00001   B = 5

def	check_size(gene, data):
	if '1' not in gene:
		bucket = 0
	else:
		bucket = gene.index('1') + 1
	if bucket == 0 and data['size'] < 2:
		return True
	elif bucket == 1 and data['size'] < 5
		return True
	elif bucket == 2 and data['size'] < 8
		return True
	elif bucket == 3 and data['size'] < 12
		return True
	elif bucket == 4 and data['size'] < 16
		return True
	elif bucket == 5 and data['size'] >= 16
		return True
	return False

def	check_isolation_layers(gene, layers):
	return True

def	check_nearest_edge(gene, edge):
	return True

def	check_quadrant(gene, quadrant):
	return True

def	check_quadrant_density(gene, density):
	return True

def	check_delta(gene, delta):
	if '1' not in gene:
		d = 0
	else:
		d = gene.index('1') + 1
	if d == delta:
		return True
	return False

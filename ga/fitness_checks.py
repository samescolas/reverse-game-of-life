import sys

# 5 buckets and 400 total == 80
def	check_pop(gene, val, cell):
        print 'pop: ' + gene
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
        print 'neighbors: ' + gene
        if '1' not in gene:
            return False
        if cell == 1 or cell == 20 or cell == 381 or cell == 400:
            if gene.index('1') == 3:
                return True
        elif cell % 20 < 2:
            if gene.index('1') == 2:
                return True
        elif gene.index('1') == 3:
            return True
	return False

def	check_living_neighbors(gene, val, cell):
        print 'living neighbors: '  + gene
        if cell == 1 or cell == 20 or cell == 381 or cell == 400:
            neighbors = 3
        elif cell % 20 < 2:
            neighbors = 5
        else:
            neighbors = 8
        
	return True

def	check_size(gene, val, cell):
	return True

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

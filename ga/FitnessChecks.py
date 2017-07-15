import sys

def	check_pop(gene, val):
	if '1' in gene:
		bucket = gene.index('1')
	else:
		bucket = 0
	print 'checking gene ' + gene + ' to see if ' + str(val['population']) + ' is within ' + str(bucket) + '...'
	sys.exit(1)
	return True

def	check_alive(gene, val):
	return True

def	check_neighbors(gene, val):
	return True

def	check_living_neighbors(gene, val):
	return True

def	check_size(gene, val):
	return True

def	check_isolation_layers(gene, val):
	return True

def	check_nearest_edge(gene, val):
	return True

def	check_quadrant(gene, val):
	return True

def	check_quadrant_density(gene, val):
	return True

def	check_delta(gene, val):
	return True

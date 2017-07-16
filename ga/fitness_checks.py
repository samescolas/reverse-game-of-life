import sys

# 5 buckets and 400 total == 80
def	check_pop(gene, val):
	if '1' in gene:
		bucket = gene.index('1')
	else:
		bucket = 0
        if val['population'] >= bucket * 80 and val['population'] < (bucket + 1) * 80:
            return True
	return False

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

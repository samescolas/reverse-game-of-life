import sys

# 5 buckets and 400 total == 80
def	check_pop(gene, population):
	classification = int(gene,2)
	if classification > 396:
		return False
	if population <= classification:
		return True
	return False

def	check_alive(gene, data):
	if data['status'] == '1':
		return True
	return False

def	check_neighbors(gene, data):
	if '1' not in gene:
		if data['neighbors'] == 3:
			return True
		return False
	elif gene.index('1') == 0 and data['neighbors'] == 5:
		return True
	elif gene.index('1') == 1 and data['neighbors'] == 8:
		return True
	return False

def	check_living_neighbors(gene, data):
        classification = int(gene,2)
        if classification > 10:
			return False

        actual = data['living_neighbors']

        if actual*10.0 < float(classification):
			return True

	return False

def	check_size(gene, data):
	classification = int(gene,2)
	if classification > 396:
		return False
	if data['size'] < classification:
		return True
	return False

def	check_isolation_layers(gene, layers):
	return True

def	check_nearest_edge(gene, data):
	classification = int(gene,2)
	if classification > 10:
		return False
	if classification == data['nearest_edge']:
		return True
	return False

# Eight buckets:
# 0		00.0% - 12.5%
# 1		12.5% - 25.0%
# 2		25.0% - 37.5%
# 3		37.5% - 50.0%
# 4		50.0% - 62.5%
# 5		62.5% - 75.0%
# 6		75.0% - 87.5%
# 7		87.5%+

def	check_quadrant_density(gene, data):
	if '1' not in gene:
		bucket = 0
	else:
		bucket = gene.index('1') + 1
	d = data['quadrant_density']
	if d > 0.125*bucket and d < 0.125*(bucket+1):
		return True
	return False

def	check_delta(gene, delta):
	if '1' not in gene:
		d = 0
	else:
		d = gene.index('1') + 1
	if d == delta:
		return True
	return False

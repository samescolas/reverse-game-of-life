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
	elif bucket == 1 and data['size'] < 5:
		return True
	elif bucket == 2 and data['size'] < 8:
		return True
	elif bucket == 3 and data['size'] < 12:
		return True
	elif bucket == 4 and data['size'] < 16:
		return True
	elif bucket == 5 and data['size'] >= 16:
		return True
	return False

def	check_isolation_layers(gene, layers):
	return True

# Four buckets:
#		0-1		000 B = 0
#		2-3		100	B = 1
#		4-6		010 B = 2
#		7+		001	B = 3

def	check_nearest_edge(gene, data):
	if '1' not in gene:
		bucket = 0
	else:
		bucket = gene.index('1') + 1
	nearest = data['nearest_edge'];
	if bucket == 0 and nearest < 2:
		return True
	elif bucket == 1 and nearest > 1 and nearest < 4:
		return True
	elif bucket == 2 and nearest > 3 and nearest < 7:
		return True
	elif bucket == 3 and nearest > 6:
		return True
	return False


#	Q0 = 000
#	Q1 = 100
#	Q2 = 010
#	Q3 = 001

def	check_quadrant(gene, data):
	if '1' not in gene:
		q = 0
	else:
		q = gene.index('1') + 1
	if int(q) == int(data['quadrant']):
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

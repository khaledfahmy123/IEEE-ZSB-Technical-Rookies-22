def calc(n, a, b):
	x = sorted(set([sum([a*(n-1-i), b*i]) for i in range(n)]))
	return x

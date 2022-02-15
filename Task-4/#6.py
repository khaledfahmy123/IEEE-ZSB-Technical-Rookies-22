from math import floor as fl
def calc(n, c, m):
	x = fl(n/c)
	return int( x + fl( (x-1)/(m-1) ) )
def count(d, arr):
	c = 0
	for i in arr:
		if (i+d) in arr and (i+2*d) in arr:
			c += 1
	return c
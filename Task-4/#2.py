def count_rs(n):
	c  = (n//3)*2 + 1 if n%3 else 0
	return c

print(count_rs(10))
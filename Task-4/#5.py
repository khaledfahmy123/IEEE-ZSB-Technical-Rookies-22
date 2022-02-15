def check(n):
	c = 0
	x = n
	while x > 0:
		digit = x%10

		if (digit != 0 and n % digit == 0):
			c += 1
		x = x // 10
	return c

print(check(124))
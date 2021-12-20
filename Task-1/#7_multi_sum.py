def sum():
	n = int(input("enter the upper limit: "))
	m = n//3
	j = n//5
	R = n//15
	sum = 1.5*(m**2 + m) + 2.5*(j**2 + j) - 7.5*(R**2 + R)
	print(sum)

sum()
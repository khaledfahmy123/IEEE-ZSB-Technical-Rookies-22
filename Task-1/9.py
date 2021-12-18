def fibo():
	term = int(input("Number of Terms: "))
	arr = []
	n1, n2 = 0, 1
	count = 0

	if term <= 0:
		print("Enter A positive integer idiot: ")
	elif term == 1:
		print(n1)
	else:
		while count < term:
			arr.append(n1)
			nth = n1 + n2
			n1 = n2
			n2 = nth
			count += 1
	print(' '.join(map(str, arr)))

fibo()
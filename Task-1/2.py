def prime():
	n = input("enter the upper limit: ")
	arr = []
	for num in range(2, int(n)):
		if all(num % i != 0 for i in range(2,num)):
			arr.append(num)
	print(" ".join(map(str,arr)))

prime()

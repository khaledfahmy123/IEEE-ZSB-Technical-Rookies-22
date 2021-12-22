def diff():
	n = int(input("enter one dimension of the matrix: "))
	arr = []
	
	for i in range(n):
		arr.append([int(a) for a in input(f"enter row {i+1} numbers: ").split(" ")])

	sum1 = sum(arr[i][i] for i in range(n))
	sum2 = sum(arr[i][n-i-1] for i in range(n))
	print(abs(sum1-sum2))

diff()

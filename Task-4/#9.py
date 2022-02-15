def cav(arr, n):
	for i in range(len(arr)):
		arr[i] = list(arr[i])
	print(arr)
	c = 0
	for r in range(1, n - 1):
		for c in range(1, n - 1):
			if arr[r][c] > max(arr[r][c+1], arr[r][c-1], arr[r+1][c], arr[r-1][c]):
				arr[r][c] = "X"
	for i in range(n):
		arr[i] = "".join(arr[i])
	return arr

print(cav(['1112', '1912', '1892', '1234'], 4))
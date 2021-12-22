def stud():
	n = int(input("Enter number of students: \n"))
	arr = []
	for i in range(n):
		arr.append([input("Enter Student Name: \n"), float(input("Enter Student Grade: \n"))])



	arr.sort(key = lambda a: a[1])
	print(arr)
	lst = []
	z = arr[0][1]
	
	while arr[0][1] == z:
		arr.remove(arr[0])
	
	z = arr[0][1]

	for i in arr:
		if z == i[1]:
			lst.append(i)
		else:
			break
	
	lst.sort(key = lambda a: a[0])
	print(lst)

stud()
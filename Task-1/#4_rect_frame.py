def frame():
	sen=input("Enter your sentence: \n")
	arr = sen.split(" ")
	l = len(max(arr, key=len))
	print('*' * (l + 4))
	for word in arr:
		print("* {} *".format(word.ljust(l)))
	print('*' * (l + 4))

frame()

def clean():
	arr = input("enter your list : \n").split(" ")
	clnArr = list(dict.fromkeys(arr, True).keys())
	return clnArr

print(clean())
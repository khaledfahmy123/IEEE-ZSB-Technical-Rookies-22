def run(arr):
	arr = list(dict.fromkeys(arr, True).keys())
	arr.remove(max(arr))
	print(max(arr))

arr = [int(a) for a in input("enter the list: \n").split(" ")]
run(arr)

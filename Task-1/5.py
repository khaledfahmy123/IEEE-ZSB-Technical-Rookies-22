def for_sum(arr):
	sum = 0
	for x in arr:
		sum += x
	print(sum)

def while_sum(arr):
	sum = 0
	i = 0
	while i < len(arr):
		sum += arr[i]
		i += 1
	print(sum)

def rec_sum(arr):
	return arr[0] + rec_sum(arr[1:]) if arr else 0


def calc():
	n = input("")+"\n"
	lst = input("")
	arr = list(map(int, lst.split(" ")))
	for_sum(arr)
	while_sum(arr)
	print(rec_sum(arr))

calc()
def rotate(arr, k, p): ## not working for one case i don't know why it looks fine
	res = []
	x = len(arr)-k
	for i in p:
		try:
			val = arr[x+i]
		except:
			val = arr[i-k]
		res.append(val)
	return res

def rot(a, k, p): ## working
	lst = []
	for i in range(k):
		a.insert(0,a[len(a)-1])
		a.pop()

	for i in p:
		lst.append(a[i])

	return lst


print(rotate([1, 2, 3], 2, [0, 1, 2]))

print(rot([1, 2, 3], 2, [0, 1, 2]))
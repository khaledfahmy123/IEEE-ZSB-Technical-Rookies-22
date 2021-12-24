def check(arr):
	if sum(arr) <= 2:
		print("Yes")
	else:
		print("No")

n = int(input("Enter number of Bottles: \n"))
arr = []
for i in range(n):
	p = [int(a) for a in input().split(" ")]
	arr.append(p[0]/p[1])
check(arr)
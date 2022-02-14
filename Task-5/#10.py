def remove(n, k, arr): #space complexity failed
	arr = list(arr)
	if k:
		for i in range(n):
			if arr[i] < arr[i+1]:
				del arr[i]
				break
		remove(len(arr), k-1, arr)
	else:
		print(" ".join(map(str,arr)))


def delete(n,k,a):
	temp=[]
	for i in a:
		while k and temp and temp[-1]<i:
			temp.pop()
			k-=1
			temp.append(i)
	print(" ".join(map(str,temp)))


for i in range(int(input())):
	n,k=map(int,input().split())
	a=map(int,input().split())
	delete(n,k,a)
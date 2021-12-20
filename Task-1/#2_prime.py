def prime():
	n = input("enter the upper limit: ")
	arr = []
	for num in range(2, int(n)):
		if all(num % i != 0 for i in range(2,num)):
			arr.append(num)
	print(" ".join(map(str,arr)))

prime() ##Time Comp: approximately O(n^2)


def SOE():
	n = int(input("enter the upper limit: "))
	prime = [True for i in range(n+1)]
	p = 2
	while (p * p <= n):
		if (prime[p] == True):
			for i in range(p * p, n+1, p):
				prime[i] = False
		p += 1
	for p in range(2, n+1):
		if prime[p]:
			print(p, end =" ")

SOE() ##Time Comp: O(n*log(log(n)));
from itertools import combinations as comb
# version #1 time-comlexity failed
def calc(arr, t):
	m = 0
	val = 0
	counter = 0
	for i in list(comb(arr, 2)):
		for j in range(t):
			if (int(i[0][j]) + int(i[1][j])):
				val += 1
		print(f"{i} and {val}")
		if val > m:
			m = val
			counter = 1
		elif m == val:
			counter +=1 
		val = 0
	return [m, counter]


# version #2 time-complexity failed
def calc2(arr, t):
	col = []
	for i in list(comb(arr, 2)):
		lst = [sum([int(x[0]) or int(x[1]) for x in list(zip(*i))])]
		col.append(lst)
	m = max(col)
	counter = col.count(m)
	return [m[0] , counter]



# version 3 time-complexity succeded as a consequance of turning data into int when the user enter it to save time

from itertools import combinations
n,k = map(int,input().split())
teams = [list(map(int,list(input()))) for i in range(n)]
sums = [sum([x[0] or x[1] for x in list(zip(*i))]) for i in combinations(teams,2)]
print(max(sums),sums.count(max(sums)),sep='\n')

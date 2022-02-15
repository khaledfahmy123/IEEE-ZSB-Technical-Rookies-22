def money(b, k, u):
	arr = [ sum([x,y]) for x in k for y in u if (sum([x,y]) <= b)]
	return max(arr) if arr else -1

print(money(60, [40, 50, 60], [5, 8, 12]))


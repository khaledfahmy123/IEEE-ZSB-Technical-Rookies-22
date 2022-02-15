def kaprekar(n):
    l=1
    while l<=n : l*=10
    return n== (n*n)//l + (n*n)%l

def calc(s, e):
	x = [str(x) for x in range(s,e+1) if kaprekar(x)]
	if x:
		print(" ".join(x))
	else:
		print("INVALID RANGE")
	

calc(1, 1000)
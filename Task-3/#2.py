from functools import reduce

def factors(n):
	return set(reduce(lambda a,b: a+b , ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)
 

def gcdMulti(arr):
	c = reduce(lambda a,b: gcd(a, b), arr)
	return c

def colec(arr):
	n = gcdMulti(arr)
	fact = factors(n)
	return fact

def check(a, b):
	consid = 0
	facts = colec(b)
	for i in facts:
		if all(i % j == 0 for j in a):
			consid += 1
	return consid

a = [2,4]
b= [16,32,96]

print(check(a,b))
import random

def start():
	c = 0
	x = random.randint(1, 10)
	while True:
		num = int(input("Make a guess: "))
		c += 1
		if num == x:
			print("Congrats you got it right in {} trials".format(c))
			break
		else:
			print("nope that's wrong")

start()
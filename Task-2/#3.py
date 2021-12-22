import random 
def game():
	x = random.randint(100, 999)
	x = [int(i) for i in str(x)]
	lst = x.copy()
	count = 0

	while True:
		count += 1
		hits = 0
		misses = 0
		num = [int(i) for i in input("guess the number: ")]
		numF = num.copy();
		if num == x:
			print("that's correct you guessed it in {}".format(count))
			break

		for i in range(3):
			if lst[i] == numF[i]:
				hits += 1
				num.remove(numF[i])
				x.remove(numF[i])

		for i in num:
			if i in x:
				misses += 1
				x.remove(i)
				# num.remove(i)

		print(f"{hits} hits {misses} misses")
		x = lst.copy()

game()

def valleys(txt):
	sea = 0
	count = 0
	for i in txt:
		if i == "D":
			sea -= 1
		else:
			sea += 1

		if(sea == 0 and i == "U"):
			count += 1

	return count


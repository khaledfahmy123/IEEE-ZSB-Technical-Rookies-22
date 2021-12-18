def rect():
	dimension = ""
	print("Enter Width and Height: ")
	for i in range(2):
		dimension+=input()+"\n"
	x,y = dimension.split("\n")[0:2]
	try:
		area = int(x) * int(y)
		param = 2 * ( int(x) + int(y) ) 
	except:
		print("Enter valid Dimensions")
		rect()
	print("Parameter: {}\nArea: {}".format(param, area))


rect()
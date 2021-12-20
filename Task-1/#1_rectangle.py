def rect():
	print("Enter Width and Height: ")
	x,y = [int(input()) for i in range(2)]
	try:
		area = int(x) * int(y)
		param = 2 * ( int(x) + int(y) ) 
	except:
		print("Enter valid Dimensions")
		rect()
	print("Parameter: {}\nArea: {}".format(param, area))


rect()
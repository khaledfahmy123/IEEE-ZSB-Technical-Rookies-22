def check():
	txt = lower(input("enter your word \n"))
	return "yes" if txt==txt[::-1] else "no"


print(check())
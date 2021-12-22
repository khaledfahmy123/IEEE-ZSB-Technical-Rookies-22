def check(txt, subT):
	n = txt.find(subT)
	if n != -1:
		return 1+check(txt[n+1:], subT)
	else:
		return 0

txt = input("enter your whole string: \n")
sub = input("enter your substring: \n")
print(check(txt, sub))
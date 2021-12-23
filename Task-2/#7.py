def check(txt, subT):
	n = txt.find(subT)
	if n != -1:
		return 1+check(txt[n+1:], subT)
	else:
		return 0

txt = input("enter your whole string: \n")
sub = input("enter your substring: \n")
print(check(txt, sub))


## Hacker Rank Version

def count_substring(txt, subT):
    n = txt.find(subT)
    if n != -1:
        return 1+count_substring(txt[n+1:], subT)
    else:
        return 0


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
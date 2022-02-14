import re


def contains(text, seq):
    pattern = seq[0] + ''.join(map(lambda c: '[^' + c + ']*' + c, list(seq[1:])))
    if re.search(pattern, text):
    	return "YES"
    else:
    	return "NO"


print(contains("hereiamstackerrank", "hackerrank"))

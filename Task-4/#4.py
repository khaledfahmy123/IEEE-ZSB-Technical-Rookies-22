def fine(d1, m1, y1, d2, m2, y2):
	if y1 > y2:
		return 10000
	elif y1 < y2:
		return 0

	if (m1<m2):
		return 0
	if(m1>m2):
		return (m1-m2)*500
	if(d1>d2):
		return (d1-d2)*15
	return 0

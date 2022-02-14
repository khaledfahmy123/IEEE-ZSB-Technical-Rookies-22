def days(t, arr):
	d = 0
	while (t > 0):
		x = 86400 - arr[d]
		t = t - x
		d += 1
	print(d)

days(86400, [0, 86400])
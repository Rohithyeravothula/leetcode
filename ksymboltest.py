test = []
s="0"
for i in range(0, 10):
	new = ""
	for i in s:
		if i == "0":
			new += "01"
		else:
			new += "10"
	test.append(new)
	s = new
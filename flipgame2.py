def canwin(a):
	l = len(a)
	for i in range(0, l-1):
		if a[i] == "+" and a[i+1] == "+":
			a[i] = "-"
			a[i+1] = "-"
			win = not canwin(a)
			print(a)
			print(win)
			a[i] = "+"
			a[i+1] = "+"
			if win:
				return True
	return False

a="++++++"
print(canwin(list(a)))
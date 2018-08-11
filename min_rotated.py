def min_rotated(a):
	if a[0] < a[-1]:
		return 0
	else:
		i = 0
		l = len(a)
		j = l-1
		while i<=j:
			if i==j:
				return i
			m = (i+j)//2
			if m==i:
				if a[i] < a[j]:
					return i
				return j
			if a[m] < a[m+1] and a[m] < a[m-1]:
				return m
			elif a[m] > a[0]:
				i = m+1
			else:
				j = m-1

def min_ele(a):
	mini = min_rotated(a)
	return a[mini]

print(min_ele([7,2,3,4,5,6]))
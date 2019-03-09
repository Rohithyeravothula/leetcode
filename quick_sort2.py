def quicksort(a, s, e):
	if s>=e:
		return None
	i,j = s, e-1
	while i<=j:
		if a[i] >= a[e]:
			a[i], a[j] = a[j], a[i]
			j-=1
		else:
			i+=1
	a[i], a[e] = a[e], a[i]
	quicksort(a, s, i-1)
	quicksort(a, i+1, e)

def quick_sort(a):
	quicksort(a, 0, len(a)-1)

a = []
quick_sort(a)
print(a)


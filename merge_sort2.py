def mergesort(a, i, j):
	if i<j:
		m = i + (j-i)//2
		mergesort(a, i, m)
		mergesort(a, m+1, j)
		join(a, i, m, j)

def join(a, i, m, j):
	ans = []
	x,y = i, m+1
	while x<=m and y<=j:
		if a[x] < a[y]:
			ans.append(a[x])
			x+=1
		else:
			ans.append(a[y])
			y+=1

	while x<=m:
		ans.append(a[x])
		x+=1
	while y<=j:
		ans.append(a[y])
		y+=1

	for x in range(i, j+1):
		a[x] = ans[x-i]


def merge_sort(a):
	mergesort(a, 0, len(a)-1)

a = [4,3,2]
merge_sort(a)
print(a)
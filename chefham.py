

def dist(a, ans):
	c = 0
	for i in range(0, n):
		if a[i] == ans[i]:
			c+=1
	return c

t=int(input())
for iteration in range(0, t):
	n = int(input())
	a = list(map(int, input().split(" ")))
	ans = [i for i in a]
	c = dist(a, ans)
	for i in range(0, n):
		if a[i]==ans[i]:
			for j in range(0, n):
				if i!=j and a[i] != ans[j] and a[j] != ans[i]:
					ans[i], ans[j] = ans[j], ans[i]
	c=dist(a,ans)

	print(n-c)
	print(" ".join(list(map(lambda x: str(x), ans))))
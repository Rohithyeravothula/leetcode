def getUmbrellas(n, p):
	pl = len(p)
	sack = [(float("inf"),0)]*(n+1)
	sack[0] = (0, 0)
	for i in range(0, pl):
		newsack = []
		for j in range(0, n+1):
			ans = sack[j]
			if p[i] <= j and sack[j - p[i]][0] + 1 < ans[0]:
				ans = (sack[j-p[i]][0]+1, sack[j-p[i]][1] + p[i])
			if p[i] <= j and newsack[j - p[i]][0] + 1 < ans[0]:
				ans = (newsack[j-p[i]][0]+1, newsack[j-p[i]][1] + p[i])
			newsack.append(ans)
		sack = newsack
		print(newsack)
	print(sack)
	if sack[n][0] == float("inf"):
		return -1
	return sack[n][0]



n = 0
p = [4,5]
getUmbrellas(n, p)



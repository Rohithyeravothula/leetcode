# def readingArticles(intellectual, pages, p):
# 	n=len(intellectual)
# 	opt = [0]*n
# 	for i in range(0, p):
# 		opt.append([0]*p)

# 	for i in range(0, n):
# 		for j in range(0, p):
# 			if j>=2*pages[i]:
# 				opt[i, j] = max(opt[i-1, j], intellectual[i]+opt[i-1, j-2*pages[i]])
# 			else:
# 				opt[i, j] = opt[i-1, j]
# 	print(opt)



def readingArticles(intellectual, pages, p):
	n = len(intellectual)
	K = []
	for i in range(0, n+1):
		d=[]
		for j in range(0, p+1):
			d.append(0)
		K.append(d)

	for i in range(0, n+1):
		for w in range(0, p+1):
			if (i == 0 or w == 0):
				K[i][w] = 0
			elif (2 * pages[i - 1] <= w):
				K[i][w] = max(intellectual[i - 1] + K[i - 1][w - 2 * pages[i - 1]], K[i - 1][w])
			else:
				K[i][w] = K[i - 1][w]
	return K[n][p]

intg =[3,3,3,2]
pages = [3,3,2,2]
p = 10
print(readingArticles(intg, pages, p))

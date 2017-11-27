class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        def spiral(m, ls, le, bs, be):
        	print(ls, le, bs, be)
        	if ls>le or bs>be:
        		return []
        	cur = []
        	if ls == le -1 and bs == be -1 :
        		return [m[ls][bs]]

        	if ls == le or bs == be:
        		return []

        	elif ls == le-1:
        		for i in range(bs, be):
        			cur.append(m[ls][i])
        		return cur
        	elif bs == be-1:
        		for i in range(ls, le):
        			cur.append(m[i][be])
        		return cur

        	for i in range(bs, be):
        		cur.append(m[ls][i])
        	for j in range(ls+1, le):
        		cur.append(m[j][be-1])
        	for i in range(bs, be-1):
        		cur.append(m[le-1][be-2-i])
        	for j in range(ls+1, le-1):
        		cur.append(m[le-i-2][bs])
        	# print(cur)
        	return cur + spiral(m, ls+1, le-1, bs+1, be-1)

        l = len(matrix)
        b = len(matrix[0])
        return spiral(matrix, 0, l, 0, b)



def printMat(a):
	for i in range(0, len(a)):
		for j in range(0, len(a[0])):
			print(a[i][j], end = "")
		print()
import random
a=[]
l = random.randint(3, 4)
r = random.randint(3, 4)

for i in range(0, l):
	a.append([0]*r)
for i in range(0, l):
	for j in range(0, r):
		a[i][j] = random.randint(0, 9)

# a=[[2,1,4,2], [1,5,2,3]]

printMat(a)


s = Solution()
print(s.spiralOrder(a))


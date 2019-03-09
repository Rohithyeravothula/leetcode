from collections import Counter 
class Solution:
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        rc = [N]*N
        cc = [N]*N
        rcounter = Counter([m for m,n in mines])
        ccounter = Counter([n for m,n in mines])
        for key,val in rcounter.items():
        	rc[key] -= val
        for key,val in ccounter.items():
        	cc[key] -= val
        mines = {(m,n) for m,n in mines}
        opt = [0]*N
        for j in range(b):
        	opt[j] = 0 if (0,j) in mines else 1
        curmax = 0
        for i in range(1, N-1):
        	cur = [0]*N
        	cur[0] = 0 if (i,0) in mines else 1
        	for j in range(1, N-1):
        		cur[j] = min([cur[j-1], opt[j], rc-currc,cc-curcc])
        	cur[N-1] = 0 if (i, N-1) in mines else 0
        




n,mines = 3,[[0,0],[0,1],[0,2]]
Solution().orderOfLargestPlusSign(n, mines)

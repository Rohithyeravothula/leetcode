class Solution:
    def minKBitFlips(self, a: 'List[int]', k: 'int') -> 'int':
    	if k==1:
    		return len(a) - sum(a)
    	l = len(a)
    	count = 0
    	i=0
    	while i<(l-k+1):
    		if a[i] == 0:
    			while i<l and i<(i+k):
    				a[i] = a[i]^1
    				i+=1
    			count += 1
    		else:
    			i+=1
    	for i in range(l-k, l):
    		if a[i] == 0:
    			return -1
    	return count

inp,k = [1,1,0], 2
inp,k = [0,1,0], 1
inp,k = [0,0,0,0],3
inp,k = [0],2
inp,k = [0,0,0,1,0,1,1,0],3
print(Solution().minKBitFlips(inp,k))


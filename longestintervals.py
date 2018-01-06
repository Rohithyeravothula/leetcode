class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        l = len(pairs)
        if l == 0:
        	return 0
        if l==1:
        	return 1
        c=1
        sorted_pairs = sorted(pairs, key = lambda x: x[1])
        cur_end = sorted_pairs[0][1]
        for i in range(1, l):
        	single_pair = sorted_pairs[i]
        	if single_pair[0] > cur_end:
        		cur_end = single_pair[1]
        		c+=1
        return c

a=[[1,2], [4,5], [2,3], [8,9], [5,10]]
s=Solution()
print(s.findLongestChain(a))

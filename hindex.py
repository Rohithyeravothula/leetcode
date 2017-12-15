class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        l = len(citations)
        ans = i
        for i in range(1,l+1):
        	count = 0
        	for j in range(0, l):
        		if citations[j] > i:
        			break
        	if n-j == i:
        		ans = i
        return ans


ary=[3,1,0,5,6]
[50,60,1]
s=Solution()
s.hIndex(ary)


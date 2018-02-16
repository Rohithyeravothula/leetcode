class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        cur = 0
        l = len(arr)
        if l == 1:
        	return l
        chunks = 0
        while cur < l:
        	limit = arr[cur]
        	while cur <= limit:
        		limit = max(limit, arr[cur])
        		cur += 1
        	chunks+=1
        return chunks

a=[0,1,2,3,4,5,6]
s=Solution()
print(s.maxChunksToSorted(a))
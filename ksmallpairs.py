from heapq import heappush, heappop
class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        l1 = len(nums1)
        l2 = len(nums2)
        if l1==0 or l2==0:
        	return []
        pqueue = []
        for i in range(0, min(l1, k)):
        	for j in range(0, min(l2, k)):
        		heappush(pqueue, (nums1[i]+nums2[j], (nums1[i], nums2[j])))
        result = []
        while k and len(pqueue) > 0:
        	(cur, (i,j)) = heappop(pqueue)
        	result.append([i, j])
        	k-=1
        return result


a=[]
b=[]
s=Solution()
print(s.kSmallestPairs(a,b,2))
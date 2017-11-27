import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ele = {}
        for i in nums:
            if i in ele:
                ele[i]+=1
            else:
                ele[i] = 1
        pq = []
        for i in ele:
            heapq.heappush(pq, (-1*ele[i], i))
        ans = []
        for i in range(0, k):
            ans.append(heapq.heappop(pq)[1])
        print(ans)

s=Solution()
a=[1,1,1,1]
s.topKFrequent(a, 1)

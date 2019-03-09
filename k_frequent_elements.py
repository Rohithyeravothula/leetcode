from heapq import heappush, heappop, heapify
from collections import Counter
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        counter = [(val, key) for key,val in Counter(nums).items()]
        cl = len(counter)
        h = list(counter[:k])
        heapify(h)
        for cur_val, cur_key in counter[k:]:
            cur_val, cur_key = counter[k]
            top_val, top_key = heappop(h)
            if top_val < cur_val:
                heappush(h, (cur_val, cur_key))
            else:
                heappush(h, (top_val, top_key))
        
        ans = []
        while h:
            ans.append(heappop(h)[1])
        return ans[::-1]

inp = [4,1,2,-1,-1]
print(Solution().topKFrequent(inp, 2))
from heapq import heappush, heappop, heapify
from collections import Counter
class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counter = [(-val, key) for key, val in Counter(words).items()]
        heapify(counter)
        ans = []
        i = 0
        # print(counter)
        while i<k and counter:
        	_, key = heappop(counter)
        	ans.append(key)
        	i+=1
        return ans


s = Solution()
words = ["i", "love", "leetcode", "i", "love", "coding"]
words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 2
k = 44
# words = []
print(s.topKFrequent(words, k))
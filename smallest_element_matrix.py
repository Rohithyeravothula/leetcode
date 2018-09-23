from heapq import heappush, heappop
class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        h = []
        for row in matrix:
            for ele in row:
                heappush(h, ele)
        for _ in range(k-1):
            heappop(h)
        return heappop(h)
        

s = Solution()
print(s.kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))


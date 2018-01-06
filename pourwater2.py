class Solution(object):
    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        l = len(heights)
        K_index = K
        K_capicity = heights[K_index]
        left_min_heap = [(float("inf"), -1)]
        right_min_heap = [(float("inf"), -1)]
        
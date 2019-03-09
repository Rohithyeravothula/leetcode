class Solution:
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """


        l = len(A)
        right_min = [0]*l
        right_min[l-1] = A[l-1]
        for i in range(l-2, -1, -1):
        	right_min[i] = min(right_min[i+1], A[i])

        left_max = A[0]
        for i in range(0, l-1):
        	if left_max <= right_min[i+1]:
        		return i+1
        	left_max = max(left_max, A[i])

inp = [5,0,3,8,6]
inp = [1,1,1,1,1,0,2,3,4]
inp = [5,4,2]
inp = [1,1]
print(Solution().partitionDisjoint(inp))
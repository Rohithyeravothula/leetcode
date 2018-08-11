class Solution:
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        l = len(A)
        check = {}
        def swaps(i):
        	if i == l-1:
        		return 0
        	else:
        		if (A[i] <= A[i+1] and A[i] <= B[i+1]) and (B[i] < B[i+1] and B[i] < A[i+1]):
        			return min(swaps(i+1), swaps(i+2))

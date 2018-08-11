class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for i,v in enumerate(A[1:]):
            if A[i] > A[i+1]:
                return i
        return len(A)-1

s = Solution()
print(s.peakIndexInMountainArray([0,1,2,3,4,0]))
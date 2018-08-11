class Solution:
    def longestMountain(self, a):
        """
        :type A: List[int]
        :rtype: int
        """
        left = [0]
        for i, v in enumerate(a[1:]):
            if v > a[i]:
                left.append(left[i]+1)
            else:
                left.append(0)
        l = len(a)
        right = [0]*l
        for i in range(1, l):
            if a[l-i-1] > a[l-i]:
                right[l-i-1] = right[l-i] + 1
        max_height = 0
        for i, j in zip(left, right):
            if i > 0 and j>0:
                max_height = max(max_height, i+j+1)
        return max_height

info = [1,2,3,4]
s = Solution()
print(s.longestMountain(info[::-1]))
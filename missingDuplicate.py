class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def single(a, i, j):
            print(i, j)
            if i == j:
                return a[i]
            if (j-i)%2 == 0:
                m = int((j-i)/2)
                if m!=i and (m-i)%2 == 0 and a[m] != a[m-1]:
                    return single(a, i, m)
                if m<j and (j-m-1)%2 == 0 and a[m] != a[m+1]:
                    return single(a, m+1, j)
            return None

        return single(nums, 0, len(nums)-1)

a=[1,2,2]
s=Solution()
print(s.singleNonDuplicate(a))



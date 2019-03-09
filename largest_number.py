import functools
class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def compare(x, y):
            if (x+y) > (y+x):
                return 1
            return -1
        # print(compare("989", "98"))
        nums = [str(val) for val in nums]
        nums = sorted(nums, key=functools.cmp_to_key(compare), reverse=True)
        ans = "".join(nums)
        # print(ans)
        return ans

inp = [3,30,34,5,9]
inp = [10,2]
inp = [1,2,3,4]
inp = []
inp = [98, 989]
inp = [98, 984, 989]
inp = [0,0,9,0,0,8,3]
Solution().largestNumber(inp)



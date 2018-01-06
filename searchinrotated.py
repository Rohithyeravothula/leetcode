class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return -1
        if l == 1:
            if nums[0] == target:
                return 0
            return -1
        s=0
        e=l-1
        m=0
        if nums[e-1] > nums[e]:
            m=e
        elif nums[s] > nums[e]:
            while s<e:
                m = (s+e)//2
                # print(s, e, m)
                if (m>0 or m<l-1) and nums[m] < nums[m-1] and nums[m] < nums[m+1]:
                    break
                if nums[m] > nums[0] and nums[m] > nums[l-1]:
                    s=m+1
                elif nums[m] < nums[0] and nums[m] < nums[l-1]:
                    e=m
            # print(m)
            # nums = nums[m:] + nums[0:m]
        def get_index(numbers, target):
            if len(numbers) == 0:
                return -1
            s=0
            e=len(numbers)-1
            while s<e:
                # print(s,e)
                m = (s+e)//2
                if numbers[m] < target:
                    s=m+1
                else:
                    e=m
            if numbers[s] != target:
                return -1
            return s
        # print(m)
        i = get_index(nums[m:], target)
        if i == -1:
            return get_index(nums[0:m], target)
        return m+i


import random
from collections import deque
s=Solution()

nums = [2,1]
target = 2
ans = s.search(nums, target)
print(ans)

# for i in range(0, 1000):
#     nms = deque(list(range(1, random.randint(10, 20))))
#     nms.rotate(random.randint(0,19))
#     # print(nms)
#     target = random.randint(1,len(nms))
#     ans = s.search(list(nms), target)
#     if ans != list(nms).index(target):
#         print(nms, target, ans)
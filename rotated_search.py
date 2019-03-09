class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def pivot_index(a):
            l = len(a)
            if a[0] < a[-1]:
                return 0
            start = 0
            end = l-1
            while start <= end:
                mid = end + (start - end)//2
                if a[mid] < a[0]:
                    end = mid-1
                else:
                    start = mid+1
            return start
        
        def binary_search(a, i, j, key):
            start = i
            end = j
            while start <= end:
                mid = end + (start - end)//2
                if a[mid] == key:
                    return mid
                elif a[mid] > key:
                    end = mid-1
                else:
                    start = mid+1
            return -1
        
        l = len(nums)
        if l < 2:
            if target in nums:
                return nums.index(target)
            return -1
        
        pi = pivot_index(nums)
        # print(pi)
        left = binary_search(nums, 0, pi-1, target)
        if left != -1:
            return left
        right = binary_search(nums, pi, l-1, target)
        if right != -1:
            return right
        return -1

inp = [7,8,4]
print(Solution().search(inp, 9))

"""



"""
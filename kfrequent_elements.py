from collections import Counter
from heapq import heappush, heappop, heapify
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = [(val, key) for key, val in list(Counter(nums).items())]
        def k_th_split(a, left, right, k):
            if left > right or right == k:
                return 
            mid = (left + right) >> 1
            a[mid], a[right] = a[right], a[mid]
            i = left
            j = right-1
            while i<=j:
                if a[i] >= a[right]:
                    a[i], a[j] = a[j], a[i]
                    j-=1
                else:
                    i+=1
            a[i], a[right] = a[right], a[i]
            print(a, a[i], left, right, k)
            if i==k+1:
                return 
            elif i<k:
                return k_th_split(a, i, right, k-i)
            else:
                return k_th_split(a, left, i-1, k)
        info = [4,5,1,8,9,3,2,10,12]
        k_th_split(info, 0, len(info)-1, 3)
        print(info)

Solution().topKFrequent([], 4)


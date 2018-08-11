from heapq import heappush, heappop
class Solution:
    def kthSmallestPrimeFraction(self, a, k):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        a.sort()
        l = len(a)
        k = ((l*(l-1))/2) - k
        heap = []
        heappush(heap, (a[0]/a[l-1], (0, l-1)))
        heappush(heap, (a[0]/a[l-2], (0, l-2)))
        count = 0
        index = 0
        if count == 0:
            return [0, l-1]
        # smallest = []
        while heap:
            print(heap)
            p, (i,j) = heappop(heap)
            # smallest.append(p)
            count += 1
            if count == k:
                return [a[i], a[j]]
            if i<l-1:
                heappush(heap, (a[i+1]/a[j], (i+1, j)))
            if i==l-1 and index<l-2:
                index += 1
                heappush(heap, (a[index]/a[l-1], (index, l-1)))
        # print(smallest)
s=Solution()
print(s.kthSmallestPrimeFraction([1,7], 1))



        
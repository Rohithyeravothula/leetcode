class Solution:
    def sortColors(self, a):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(a)
        i = 0
        j = 0
        k = l-1
        while j<=k:
            if a[j] == 0:
                a[i], a[j] = a[j], a[i]
                i+=1
                j+=1
            elif a[j] == 1:
                j+=1
            elif a[j] == 2:
                a[j], a[k] = a[k], a[j]
                k-=1
        
s = Solution()
a = [0,1,0]
s.sortColors(a)
print(a)
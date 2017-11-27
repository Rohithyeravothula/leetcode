a=[0,0,1,0]
class Solution:
    def sortColors(self, a):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        l=len(a)
        i0 = 0
        i1 = 0
        i2 = l-1
        while i1<=i2:
            print(a, i0, i1, i2)
            if a[i1] == 0:
                a[i0],a[i1] = a[i1],a[i0]
                i0+=1
                i1+=1
            elif a[i1] == 1:
                i1+=1
            else:
                a[i1],a[i2] = a[i2],a[i1]
                i2-=1

s=Solution()
s.sortColors(a)
print("sol:", a)


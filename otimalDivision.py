
class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        n=len(nums)
        
        a=[]
        for i in range(0, n):
            d=[0.0]*n
            a.append(d)
        
        for i in range(0, n):
            a[i][i] = nums[i]
        l=1
        while l<n:
            for i in range(0, n-l):
                maxV = 0
                for j in range(i, i+l):
                    print(i, j, i+l, a[i][j], a[j+1][i+l])
                    cur = (a[i][j]/(a[j+1][i+l]))
                    if maxV < cur:
                        maxV = cur
                a[i][i+l] = maxV
            l+=1
        print(a)
        print(a[0][n-1])

a=[1000, 100,10, 2]
s=Solution()
s.optimalDivision(a)
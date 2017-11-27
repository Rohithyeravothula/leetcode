class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        a=[]
        ans=[]
        for i in nums:
            print(a)
            if len(a) == 0:
                a.append(i)
            else:
                if a[-1]+1 == i:
                    a.append(i)
                else:
                    if len(a) == 1:
                        ans.append(str(a[0]))
                    else:
                        ans.append(str(a[0]) + "->" + str(a[-1]))
                    a=[i]
        if len(a) == 1:
            ans.append(str(a[0]))
            a=[]
        if len(a) > 1:
            ans.append(str(a[0]) + "->" + str(a[-1]))
            a=[]
        return ans

d=[0,1,2,4,5,7]
s=Solution()
print(s.summaryRanges(d))
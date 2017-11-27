class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        l=len(strs)
        minL=len(strs[0])
        for s in strs:
            if minL > len(s):
                minL = len(s)
        
        i=0
        ans = False
        while i<minL:
            for j in range(1, l):
                if strs[j][i] != strs[j-1][i]:
                    ans = True
                    break
            if ans:
                break
            i+=1
        # print(i)
        return strs[0][0:i]

# 
a=["hello", "hella", "hell no way"]
s=Solution()
print(s.longestCommonPrefix(a))


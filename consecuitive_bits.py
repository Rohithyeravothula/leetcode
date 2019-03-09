class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        ans,i,j=0,0,0
        while j<l and s[j] == s[i]:
            j+=1
        prev = (j-i)
        i=j
        while i<l:
            k = i
            while k<l and s[i] == s[k]:
                k+=1
            ans += min(prev, k-i)
            prev = k-i
            i = k
        return ans
print(Solution().countBinarySubstrings("11100"))
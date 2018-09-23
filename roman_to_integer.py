class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        s = s[::-1]
        l = len(s)
        i = 0
        ans = mapping[s[i]]
        prev = mapping[s[i]]
        i+=1 
        while i<l:
            cur_val = mapping[s[i]]
            if cur_val < prev:
                ans -= cur_val
            else:
                ans += cur_val
            prev = cur_val
            i+=1
        return ans

s = Solution()
print(s.romanToInt("MCMXCIV"))
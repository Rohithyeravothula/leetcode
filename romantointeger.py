class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=="":
        	return 0
        s=s[::-1]
        romap = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ans = romap[s[0]]
        prev = s[0]
        l = len(s)
        for i in range(1, l):
        	if romap[s[i]] < romap[prev]:
        		ans -= romap[s[i]]
        	else:
        		ans += romap[s[i]]
        	prev = s[i]
        return ans

s=Solution()
print(s.romanToInt(""))
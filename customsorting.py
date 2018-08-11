from collections import Counter
class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        ans = ""
        counter = Counter(T)
        for char in S:
        	c = counter[char]
        	ans += char*c 
        	del counter[char]
        for char in counter.keys():
        	ans += char*counter[char]
        return ans

a="zxy"
b="abcdfas"
s=Solution()
print(s.customSortString(a,b))


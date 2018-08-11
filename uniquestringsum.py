from collections import Counter
class Solution:
    def uniqueLetterString(self, S):
        """
        :type S: str
        :rtype: int
        """
        mod_num = (10**9)+7
        u = len(Counter(S))
        table = []
        start = u
        for i in range(1, u+1):
        	table.append(start)
        	start *= u-i

        l = len(S)
        count = 0
        for i in range(1, l):
        	for j in range(1, u):
        		if i >= j:
        			count = (count + table[u-1]) % mod_num
        		else:
        			count = (count + table[j]) % mod_num
        return count

s=Solution()
print(s.uniqueLetterString("abc"))

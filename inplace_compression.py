class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        l = len(chars)
        i = 0
        repl_i = 0
        while i<l:
        	cur = chars[i]
        	count = 0
        	while i<l and chars[i] == cur:
        		i+=1
        		count += 1
        	chars[repl_i] = cur
        	repl_i += 1
        	if count > 1:
        		for c in str(count):
        			chars[repl_i] = c
        			repl_i += 1
        # print(repl_i)
        # print(chars[:repl_i])
        return repl_i

s = Solution()
s.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])

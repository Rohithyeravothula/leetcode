class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def get_next(input_str):
        	l = len(input_str)
        	ans = ""
        	i=0
        	while i<l:
        		c=1
        		j = i+1
        		while j<l and input_str[i] == input_str[j]:
        			j+=1
        			c+=1
        		ans += str(c) + input_str[i]
        		i=j
        	return ans

        prev = "1"
        for i in range(1, n):
        	cur = get_next(prev)
        	# print(cur)
        	prev = cur
        return prev

s=Solution()
s.countAndSay(10)

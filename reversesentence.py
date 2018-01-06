class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        def reverse(input_str, si, ei):
        	for i in range(si, (si+ei)//2):
        		input_str[i], input_str[si+ei-i-1] = input_str[si+ei-i-1], input_str[i]
        
        inp = list(s)
        l = len(inp)
        reverse(inp, 0, l)
        i=0
        while i<l and inp[i] == " ":
        	i+=1
        j=i+1
        while i<l and j<l:
        	if inp[j] == " ":
        		reverse(inp, i, j)
        		j+=1
        		i=j
        	j+=1
        reverse(inp, i,j)
        s="".join(inp)
        return s



s=Solution()
inp = "   a   b "  
ans = s.reverseWords(inp)
print(ans, len(ans), len(inp))
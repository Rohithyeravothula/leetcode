class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        keeper = []
        i = 0
        l = len(s)
        while i<l:
        	if s[i] == "]":
        		cur = []
        		while keeper and keeper[-1] != "[":
        			cur.append(keeper.pop())
        		keeper.pop() # remove [
        		num = []
        		while keeper and keeper[-1].isnumeric():
        			num.append(keeper.pop())
        		num = int("".join(num[::-1]))
        		cur = cur[::-1]
        		keeper.append("".join(cur)*num)
        	else:
        		keeper.append(s[i])
        	i+=1
        return "".join(keeper)


s = Solution()
# s.decodeString("3[a]2[bc]")
# s.decodeString("2[abc]3[cd]ef")
print(s.decodeString("10[a]"))
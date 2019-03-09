class Solution:
    def dailyTemperatures(self, t):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        if not t:
        	return []
        stk = [0]
        i = 1
        l = len(t)
        ans = [0]*l
        while i<l:
        	while stk and t[stk[-1]] < t[i]:
        		ans[stk[-1]] = i-stk[-1]
        		stk.pop()
        	stk.append(i)
        	i+=1
        return ans

s = Solution()
inp = [73, 74, 75, 71, 69, 72, 76, 73]
inp = [1,2,3,4,5]
print(s.dailyTemperatures(inp[::-1]))
        
class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stk = []
        i = 0
        l = len(temperatures)
        ans = [0]*l
        while i<l:
        	if len(stk) == 0:
        		stk.append(i)
        		i+=1
        	else:
        		if temperatures[i] > temperatures[stk[-1]]:
        			ans[stk[-1]] = i - stk[-1]
        			stk.pop()
        		else:
        			stk.append(i)
        			i+=1
        return ans

temp = [3]
s=Solution()
print(s.dailyTemperatures(temp))
class Solution:
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        def remove_digit(num):
        	numlist = list(str(num))
        	if not numlist or not num:
        		return "0"
        	l = len(numlist)
        	found = False
        	for i in range(0, l-1):
        		if numlist[i] > numlist[i+1]:
        			found = True
        			break
        	if not found:
        		max_val = max(numlist, key=lambda x: int(x))
        		for j,v in enumerate(numlist):
        			if v == max_val:
        				break
        		del numlist[j]
        		if not numlist:
        			return "0"
        		return "".join(numlist)

        	else:
        		del numlist[i]
        		if not numlist:
        			return "0"
        		return "".join(numlist)

        for i in range(0, k):
        	num = int(remove_digit(num))
        	if not num:
        		break
        return num


s = Solution()
print(s.removeKdigits(9, 1))



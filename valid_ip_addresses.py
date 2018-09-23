class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def to_int(r):
        	if r == "":
        		return -1
        	return int(r)

        valid_range = range(256)
        l = len(s)
        response = []
        for i in range(0, l):
        	for j in range(i+1, l):
        		for k in range(j+1, l):
        			a1 = to_int(s[:i])
        			a2 = to_int(s[i:j])
        			a3 = to_int(s[j:k])
        			a4 = to_int(s[k:])
        			if a1 in valid_range and a2 in valid_range and a3 in valid_range and a4 in valid_range:
        				ans = "{}.{}.{}.{}".format(a1, a2, a3, a4)
        				if len(ans)-3 == l:
	        				response.append(ans)
        return response


s = Solution()
print(s.restoreIpAddresses("010010"))




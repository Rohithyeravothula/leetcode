class Solution:
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = len(s)
        seen = set([0])
        for i in s:
        	next_seen = set()
        	if i == "(":
        		for v in list(seen):
        			next_seen.add(v+1)
        	elif i == ")":
        		for v in list(seen):
        			if i==l-1:
        				next_seen.add(v-1)
        			elif v > 0:
        				next_seen.add(v-1)
        	elif i == "*":
        		for v in list(seen):
        			next_seen.add(v)
        			next_seen.add(v+1)
        			if i==l-1:
        				next_seen.add(v-1)
        			elif v > 0:
        				next_seen.add(v-1)
        	seen = next_seen
        	# print(seen)
        if 0 in seen:
        	return True
        return False
s = Solution()
print(s.checkValidString("(*)"))


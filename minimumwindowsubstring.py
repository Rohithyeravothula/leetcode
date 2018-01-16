from collections import Counter
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dt = Counter(t)
        start = 0
        end = 0
        l = len(s)
        minl = l+1
        minls = l+1
    	copy = dt.copy()
        while start <= end and end < l:
        	while end < l:
        		if len(copy) == 0: # can build entire t
        			minl = min(minl, end-start+1)
        			break
        		else:
        			if s[end] in copy:
        				if copy[s[end]] == 1:
        					del copy[s[end]]
    					else:
    						copy[s[end]] -= 1
    				elif s[end] not in copy and in dt:
    					copy[s[end]] = -1

				end += 1

			while start <= end s[start] not in dt:
				start += 1

			copy[s[start]] = 1
			start += 1

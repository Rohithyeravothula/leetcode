from collections import Counter
class Solution:
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        
        index with ages
        iterate over indices with conditions, 
        take care of self friendship case
        """
        d = Counter(ages)        
        fc = 0
        age_keys = list(d.keys())
        for a in age_keys:
        	for b in age_keys:
        		if b>a:
        			continue
        		elif b > 100 and a < 100:
        			continue
        		elif b <= (a/2) + 7:
        			continue
        		else:
        			if a == b:
        				if d[a] > 1:
        					fc += d[a]*(d[a]-1)
        			else:
        				fc += d[a] * d[b]
        return fc


ggs = []
s = Solution()
print(s.numFriendRequests(ggs))
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        l1 = list(range(0, l))
        l2 = [(i, i+1) for i in range(0, l-1) if s[i] == s[i+1]]
        l3 = [(i,i+2) for i in range(0, l-2) if s[i] == s[i+2]]
        ans = [l1, l2, l3]
        prev = None
        cur = l2 
        cur_odd = l3
        while cur or cur_odd:
        	local = []
        	for pal in cur:
        		if (pal[0]-1) >= 0 and (pal[1]+1) < l and s[pal[0]-1] == s[pal[1]+1]:
        			local.append((pal[0]-1, pal[1]+1))

        	if local:
	        	ans.append(local)
        	cur = local

        	local_odd = []
        	for pal in cur_odd:
        		if (pal[0]-1) >= 0 and (pal[1]+1) < l and s[pal[0]-1] == s[pal[1]+1]:
        			local_odd.append((pal[0]-1, pal[1]+1))

        	if local_odd:
        		ans.append(local_odd)

        	cur_odd = local_odd
        return sum(list(map(lambda x: len(x), ans)))

a="a"*1000
s=Solution()
print(s.countSubstrings(a))


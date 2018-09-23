class Solution:
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        def get_hash(s):
        	s1 = []
        	s2 = []
        	l = len(s)
        	i = 0
        	while i<l:
        		s1.append(s[i])
        		i+=1
        		if i==l:
        			break
        		s2.append(s[i])
        		i+=1
        	s1.sort()
        	s2.sort()
        	return "{}_{}".format("".join(s1), "".join(s2))

        seen = set()
        for s in A:
        	hid = get_hash(s)
        	seen.add(hid)
        print(len(seen))
        return len(seen)

s = Solution()
# inp = ["a","b","c","a","c","c"]
# inp = ["aa","bb","ab","ba"]
# inp = ["abc","acb","bac","bca","cab","cba"]
# inp = ["abcd","cdab","adcb","cbad"]
inp = ["a", "b"]
s.numSpecialEquivGroups(inp)
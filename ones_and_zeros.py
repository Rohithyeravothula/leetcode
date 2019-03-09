class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        def get_count(val, c):
        	return sum([1 if v==c else 0 for v in list(val)])
        def find(i, w, seen, values, zc, oc):
        	if i == 0:
        		# print(w, zc, oc)
        		if w[0] >= zc[values[0]] and w[1] >= oc[values[0]]:
        			return 1
        		return 0

        	if (i, w) in seen:
        		return seen[(i, w)]
        	left = find(i-1, w, seen, values, zc, oc)
        	wu = (w[0] - zc[values[i]], w[1] - oc[values[i]])
        	if wu[0] < 0 or wu[1] < 0:
        		seen[(i, w)] = left
        		return seen[(i, w)]
        	right = find(i-1, wu, seen, values, zc, oc)
        	seen[(i, w)] = max(left, 1+right)
        	return seen[(i, w)]

        if not strs:
        	return 0
        zc = {val:get_count(val, '0') for val in strs}
        oc = {val:get_count(val, '1') for val in strs}
        seen = {}
        ans = find(len(strs)-1, (m,n), seen, strs, zc, oc)
        return ans

strs, m, n = ["10", "0", "1"],1,1
strs,m,n = ["10", "0001", "111001", "1", "0"], 5, 3
strs, m, n = [],0,0
print(Solution().findMaxForm(strs, m, n))
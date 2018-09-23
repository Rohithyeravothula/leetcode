class Solution(object):
    def smallestRangeII(self, a, k):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        maxa = max(a)
        mina = min(a)
        mindiff = maxa - mina
        l = len(a)
        umina = float("inf")
        umaxa = a[l-1]
        for i in range(l-1):
        	umina = min(umina, max(a[i] + k, a[i+1]))
        	umaxa = max(umaxa, min(a[i] - k, a[i+1]))
        mindiff = min(mindiff, abs(maxa - mina))
        return mindiff

inp,k = [20, 100, 110], 60
inp,k = [20, 70, 100, 150], 60
inp,k = [10,20,30,40],4
inp,k = [1,3,6], 3
print(Solution().smallestRangeII(inp, k))
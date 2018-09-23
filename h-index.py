class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        l = len(citations)
        a = [0]*(2+l)
        for c in citations:
            if c<=l:
                a[c] += 1
            else:
                a[1+l] += 1

        h = 0
        c = 0
        for i in range(1+l):
            rc = l-c
            if i <= rc and (l-i) <= (c+a[i]):
                h = i
            c += a[i]
        return h
print(Solution().hIndex([3,0,6,1,5]))

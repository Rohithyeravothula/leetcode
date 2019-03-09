class Solution:
    def numsSameConsecDiff(self, n, k):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        cur = [str(i) for i in range(1, 10)]
        if n==1:
            return [0]+cur
        depth = 1
        while cur and depth < n:
            nxt = []
            for node in cur:
                d = int(node[-1])
                if d-k >= 0:
                    nxt.append(node+str(d-k))
                if k!=0 and d+k <= 9:
                    nxt.append(node+str(d+k))
            cur = nxt
            depth += 1
        return [int(node) for node in cur]

print(Solution().numsSameConsecDiff(5,1))

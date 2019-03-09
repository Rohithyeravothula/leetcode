class Solution:
    def countArrangement(self, n):
        """
        :type N: int
        :rtype: int
        """
        def dfs(idx, cur, n):
            if idx==n:
                p = next(iter(cur))
                if p%n==0 or n%p==0:
                    return 1
                return 0
            count = 0
            for i in cur:
                if i%idx == 0 or idx%i == 0:
                    cur.remove(i)
                    count += dfs(idx+1, cur, n)
                    cur.add(i)
            return count
        return dfs(1, set(list(range(1, n+1))), n)

print(Solution().countArrangement(15)) 


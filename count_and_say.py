class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def get_next(s):
            ans = []
            l = len(s)
            i = 0
            while i<l:
                cur = s[i]
                count = 0
                while i<l and s[i] == cur:
                    i+=1
                    count += 1
                ans.append("{}{}".format(count, cur))
            return "".join(ans)
        prev = "1"
        n-=1
        while n:
            cur = get_next(prev)
            n-=1
            prev = cur
        print(prev)
        return prev

s = Solution()
s.countAndSay(5)
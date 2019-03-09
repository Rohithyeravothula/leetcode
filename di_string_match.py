class Solution:
    def diStringMatch(self, s):
        """
        :type S: str
        :rtype: List[int]
        """
        def build(cur, trend, idx, left, right):
            # print(idx, left, right)
            if abs(left - right) == 1:
                term = [cur[left], cur[right]]
                return term if trend[idx] == "I" else term[::-1]
            if trend[idx] == "I":
                m = cur[left]
                left += 1
            if trend[idx] == "D":
                m = cur[right]
                right -= 1
            return [m] + build(cur, trend, idx+1, left, right)
        l = len(s)
        cur = range(l+1)
        return build(cur, s, 0, 0, l)
        


inp = "DDI"
inp = ""
inp = "IDID"
inp = "DDD"
inp = "III"
inp = "DDIIDIDIID"
inp = "IIDDIIDD"
print(Solution().diStringMatch(inp))
class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        mapper = {}
        for i, c in enumerate(S):
            mapper[c] = i

        start = 0
        l = len(S)
        parts = []
        count = 0
        while start < l:
            end = mapper[S[start]]
            while start < l  and start <= end and end < l:
                newend = mapper[S[start]]
                end = max(end, newend)
                start += 1
                count += 1
            parts.append(count)
            count = 0
        return parts

s = Solution()
inp = "abcdef"
print(s.partitionLabels(inp))

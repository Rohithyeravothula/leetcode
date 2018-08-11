class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        if S=="":
            return [0,0]

        lines = 1
        current = 100
        for char in S[:-1]:
            cw = widths[ord(char) - ord('a')]
            if cw > current:
                current = 100 - cw
                lines += 1
            else:
                current -= cw
        cw = widths[ord(S[-1]) - ord('a')]
        if cw > current:
            lines += 1
            return [lines, cw]
        else:
            current -= cw
            return [lines, 100-current]



wtd = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
s=Solution()
print(s.numberOfLines(wtd, "a"))
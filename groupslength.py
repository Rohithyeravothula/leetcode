class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        ans = []
        l = len(S)
        start = 0
        while start < l:
            end = start+1
            count = 1
            while end < l and S[start] == S[end]:
                end += 1
                count += 1

            if count >= 3:
                ans.append([start, end-1])
            start = end
        # print(ans)
        return ans

s=Solution()
s.largeGroupPositions("aa")

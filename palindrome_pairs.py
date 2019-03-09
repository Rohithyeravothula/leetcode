class Solution:
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        def build_hashs(cur):
            l = len(cur)
            i = l
            ans = []
            while i>0:
                curp = cur[i:]
                if curp == curp[::-1]:
                    ans.append(cur[:i] + cur[i:] + cur[:i][::-1])
                i-=1
            return ans

        ans = []
        wset = {word:index for index, word in enumerate(words)}
        for index, val in enumerate(words):
            for whash in build_hashs(val):
                print(whash )
                if whash in wset:
                    ans.append([index, wset[whash]])
        return ans

s = Solution()
words = ["abcd","dcba","lls","s","sssll"]
print(s.palindromePairs(words))




        
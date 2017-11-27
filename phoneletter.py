class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        digstr=["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        def digit_to_str(n):
            if len(n) == 1:
                return list(digstr[int(n)])
            else:
                cur = list(digstr[int(n[0])])
                prev = digit_to_str(n[1:])
                ans = []
                for p in prev:
                    for c in cur:
                        ans.append(c+p)
                return ans
        return digit_to_str(digits)

s=Solution()
# print(s.letterCombinations("10"))
for i in range(0, 100):
    print(i, s.letterCombinations(str(i)))
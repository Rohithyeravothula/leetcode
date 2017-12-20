class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        def construct(word):
            d={}
            for j in word:
                i = j.lower()
                if i.isalpha():
                    if i in d:
                        d[i] += 1
                    else:
                        d[i] = 1
            return d
        def compare_ds(a, b):
            keys = a.keys()
            for k in keys:
                if k not in b or a[k] > b[k]:
                    return False
            return True
        ans = []
        lpd = construct(licensePlate)
        for word in words:
            word_d = construct(word)
            if compare_ds(lpd, word_d):
                ans.append(word)
        minL = min(list(map(lambda x: len(x), ans)))
        min_ans = list(filter(lambda x: len(x) == minL, ans))
        return min_ans[0]

licensePlate = "wo"
words = ["looks", "pest", "stew", "show"]
s=Solution()
print(s.shortestCompletingWord(licensePlate, words))

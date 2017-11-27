class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        w1l = len(words1)
        w2l = len(words2)

        if w1l != w2l:
            # print("asfd")
            return False

        d = {}
        for i in pairs:
            left, right = i
            if left in d:
                d[left].append(right)
            else:
                d[left] = [right]
            if right in d:
                d[right].append(left)
            else:
                d[right] = [left]

        # for i in d:
        #     print(i, d[i])
        for i in range(0, w1l):
            if words1[i] != words2[i]:
                prs = d.get(words1[i])
                if words1[i] not in d:
                    return False
                elif words1[i] in d and words2[i] not in prs:
                    print(words1[i], words2[i])
                    return False
        return True


w1 = ["one","excellent","meal"]
w2 = ["one","good","dinner"]
pars = [["great","good"],["extraordinary","good"],["well","good"],["wonderful","good"],["excellent","good"],["fine","good"],["nice","good"],["any","one"],["some","one"],["unique","one"],["the","one"],["an","one"],["single","one"],["a","one"],["truck","car"],["wagon","car"],["automobile","car"],["auto","car"],["vehicle","car"],["entertain","have"],["drink","have"],["eat","have"],["take","have"],["fruits","meal"],["brunch","meal"],["breakfast","meal"],["food","meal"],["dinner","meal"],["super","meal"],["lunch","meal"],["possess","own"],["keep","own"],["have","own"],["extremely","very"],["actually","very"],["really","very"],["super","very"]]

# w1 = "great acting skills".split()
# w2 = "                   ".split()
# pars = []
s = Solution()
ans = s.areSentencesSimilar(w1, w2, pars)
print(ans)
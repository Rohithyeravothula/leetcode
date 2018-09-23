class Solution:
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        replacements = {}
        for i, source, target in zip(indexes, sources, targets):
            if i in replacements:
                replacements[i].append((source, target))
            else:
                replacements[i] = [(source, target)]

        ans = []
        l = len(S)
        i = 0
        while i<l:
            if i in replacements:
                found_replacement = False
                for (source, target) in replacements[i]:
                    sl = len(source)
                    if S[i:i+sl] == source:
                        ans.append(target)
                        i += sl
                        found_replacement = True
                        break
                if not found_replacement:
                    ans.append(S[i])
                    i+=1
            else:
                ans.append(S[i])
                i+=1
        return "".join(ans)

S = ""
indexes = [0,2]
sources = ["a","ecd"]
targets = ["eee","ffff"]
s = Solution()
print(s.findReplaceString(S, indexes, sources, targets))
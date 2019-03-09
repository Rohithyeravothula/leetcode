from collections import defaultdict
class Solution:
    def numMatchingSubseq(self, s: 'str', words: 'List[str]') -> 'int':
        def bin_search(a, k):
            if k<a[0]:
                return a[0]
            elif k>=a[-1]:
                return -1
            i,j = 0, len(a)-1
            response = None
            while i<j:
                m = i+(j-i)//2
                if a[m] == k:
                    return a[m+1]
                elif a[m] < k:
                    i=m+1
                else:
                    response = a[m]
                    j=m-1
            return response if k >= a[j] else a[j]

        def compare(w, seen):
            prev = -1
            for c in w:
                if c in seen:
                    cur = bin_search(seen[c], prev)
                    if prev > cur:
                        return False
                    prev = cur
                else:
                    return False
            return True


        seen = defaultdict(list)
        for i,c in enumerate(s):
            seen[c].append(i)

        count = 0
        positive = set()
        negative = set()
        for w in words:
            if (w in positive) or (w not in negative and compare(w, seen)):
                count += 1
                positive.add(w)
            else:
                negative.add(w)
        return count

s, wds = "abcde", ["a","bb","acd","ace"]
s,wds = "abcde", ["aeb", "e", "ea", "a", "acd", "ace", "ac", "bde", "de"]
s,wds = "", ["a", "b", "c"]
print(Solution().numMatchingSubseq(s, wds))

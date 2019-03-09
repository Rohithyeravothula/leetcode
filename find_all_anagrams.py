from collections import Counter, defaultdict
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        lp = len(p)
        ls = len(s)
        if lp == 0 or ls == 0 or ls < lp:
            return []
        seen = Counter(p)
        l = len(seen)
        ans = []
        cur_seen = defaultdict(int)
        c = 0 # cur character counts
        
        for i in range(0, lp):
            cur_seen[s[i]] += 1
            if cur_seen[s[i]] == seen[s[i]]:
                c+=1
        if c==l:
            ans.append(0)

        end = lp
        while end<ls:
            i = end - lp
            if cur_seen[s[i]] > 0 and cur_seen[s[i]] == seen[s[i]]:
                c-=1
            cur_seen[s[i]] = max(0, cur_seen[s[i]]-1)

            cur_seen[s[end]] += 1
            if cur_seen[s[end]] > 0 and cur_seen[s[end]] == seen[s[end]]:
                c+=1

            if c==l:
                ans.append(i+1)

            # print(i, end, cur_seen, c, s[i+1:end+1])
            end += 1
        return ans

s,p = "",""
s,p = "cbaebabacd", "abc"
s,p = "abcdefg", 'dec'
print(Solution().findAnagrams(s, p))
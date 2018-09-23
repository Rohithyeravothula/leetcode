from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        def decr_or_remove(a, v):
            if v not in a:
                return 
            if a[v] == 1:
                del a[v]
            else:
                a[v]-=1
        dt = Counter(t)
        st = set(t)
        dtc = dict(dt) # current state of t
        dsc = defaultdict(int)
        i, j, l = 0, 0, len(s)
        max_length, max_string = float("inf"), ""
        if not t:
            return max_string
        while i<=j and j<l:
            # print(i, j)
            while dtc and j<l:
                decr_or_remove(dtc, s[j])
                dsc[s[j]] += 1
                j+=1

            if dtc:
                break

            while i<j:
                if s[i] in dt and dsc[s[i]] <= dt[s[i]]:
                    dtc[s[i]] = 1
                    decr_or_remove(dsc, s[i])
                    i+=1
                    break
                decr_or_remove(dsc, s[i])
                i+=1

            cur_length = j-i+2
            # print("after:" ,i, j, dtc)
            if cur_length <= max_length:
                max_length = cur_length
                max_string = s[i-1:j]
        return max_string

s = Solution()
print(s.minWindow("", "ABC"))










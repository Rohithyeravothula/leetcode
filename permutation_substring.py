from collections import Counter, defaultdict
class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        sl1 = len(s1)
        sl2 = len(s2)
        s1_unique = len(set(list(s1)))
        if sl2 < sl1:
            return False
        i,j = 0,0
        s1counter = Counter(s1)
        counter = 0
        cur_counter = defaultdict(int)
        
        # initial dict construction
        while j<sl1:
            cur_counter[s2[j]] += 1
            if s2[j] in s1counter and cur_counter[s2[j]] == s1counter[s2[j]]:
                counter += 1
            j+=1

        if counter == s1_unique:
            return True

        while j<sl2:
            # remove i char, incr i
            cur_counter[s2[i]] -= 1
            if s2[i] in s1counter and cur_counter[s2[i]] == s1counter[s2[i]]-1:
                counter-=1
            # print(s2[i], s2[j], counter, s1counter[s2[j]])
            i+=1

            # add j char, incr j
            cur_counter[s2[j]] += 1
            if s2[j] in s1counter and cur_counter[s2[j]] == s1counter[s2[j]]:
                counter += 1
            j+=1

            if counter == s1_unique:
                return True
        return False

s = Solution()
print(s.checkInclusion("a", ""))

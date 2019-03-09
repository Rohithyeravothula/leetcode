from collections import defaultdict
class Solution(object):
    def subarraysWithKDistinct(self, a, k):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        def remove(a, key):
            if key in a:
                if a[key]==1:
                    del a[key]
                else:
                    a[key] -= 1
        l = len(a)
        i,j = 0,0
        seen = defaultdict(int)
        ans = 0
        while j<l:
            x,y = 0,1
            while j<l and len(seen) < k:
                seen[a[j]] += 1
                j+=1
            il = j

            if len(seen) < k:
                break

            while j<l and a[j] in seen:
                seen[a[j]] += 1
                j+=1
                y+=1

            # print(i,j)
            while i<(il-1) and len(seen) == k:
                remove(seen, a[i])
                i+=1
                x+=1
                # print(seen)
            print(x,y,i,j,len(seen))

            ans += x*y
        return ans
inp = [1,2,1,2,3]
print(Solution().subarraysWithKDistinct(inp, 2))





        
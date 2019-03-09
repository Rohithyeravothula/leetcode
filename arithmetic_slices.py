from typing import List
class Solution:
    def numberOfArithmeticSlices(self, a: List[int]) -> int:
        l = len(a)
        if l<3:
            return 0
        prev = a[0]
        i = 1
        ans = 0
        while i<l:
            cur = a[i]
            diff = cur - prev
            num = cur + diff
            count = 2
            while (i+1) < l and a[i+1] == num:
                i+=1
                num += diff
                count += 1
            if count == 2:
                prev = a[i]
                i+=1
            else:
                ans += ((count-1)*(count-2))//2
                prev = a[i-1]
        return ans

inp = [1,2,3,4,5,7,8]
inp = []
print(Solution().numberOfArithmeticSlices(inp))

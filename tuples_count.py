from collections import Counter
class Solution:
    def threeSumMulti(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        mod=(10**9)+7
        a = []
        l = len(A)
        i = 0
        while i<l:
            j = i
            while j<l and A[j] == A[i]:
                j+=1
            a.append((A[i], j-i))
            i=j
        
        def two_sum(a, k, t):
            seen = Counter()
            seen[0]=1
            count = 0
            for val,valc in a[:k]:
                count += (valc*seen[t-val])
                seen[val] += valc
            return count
        
        print(a)
        l = len(a)
        ans = 0
        for k in range(l):
            curval, curcount = a[k]
            ans += (curcount*two_sum(a, k, target-curval))
            print(curval, curcount, two_sum(a, k, target-curval))
        return ans%mod


inp, t = [1,2,3,4], 1234
inp, t = [1,1,2,2,3,3,4,4,5,5],8
inp, t = [1,1,2,2,2,2],5
print(Solution().threeSumMulti(inp, t))

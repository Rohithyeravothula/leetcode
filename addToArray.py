class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        def strip(num):
            l = len(num)
            i = 0
            while i<l and num[i] == 0:
                i+=1
            return num[i:] if num[i:] else [0]
        def add(s1, s2):
            s1 = s1[::-1]
            s2 = s2[::-1]
            l1, l2 = len(s1), len(s2)
            i,j = 0,0
            ans = []
            c = 0
            while i<l1 or j<l2 or c:
                d1 = s1[i] if i<l1 else 0
                d2 = s2[j] if j<l2 else 0
                cursum = d1 + d2 + c
                ans.append(cursum%10)
                c = cursum//10
                i+=1
                j+=1
            return ans[::-1]
        K = [int(val) for val in list(str(K))]
        return strip(add(A, K))

a,b = [1,2,0,0], 34
a,b = [2,7,4],181
a,b = [9,9,9,9,9,9,9,9,9,9],1
a,b = [2,1,5],0
print(Solution().addToArrayForm(a,b))
from collections import Counter
class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        def get_sum_dict(A, B):
            return Counter(a+b for a in A for b in B)
            
        sum1 = get_sum_dict(A,B)
        return sum(sum1[-c-d] for c in C for d in D)

a = [-1,2]
b = [2,-1]
c = [-1,2]
d = [0,2]
s=Solution()
print(s.fourSumCount(a,b,c,d))


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
            s1 = {}
            la = len(A)
            lb = len(B)
            for i in range(0, la):
                for j in range(0, lb):
                    cursum = A[i]+B[j]
                    if cursum in s1:
                        s1[cursum] += 1
                    else:
                        s1[cursum] = 1
            return s1

        sum1 = get_sum_dict(A,B)
        sum2 = get_sum_dict(C,D)
        result = 0
        for p in sum1.keys():
            if -1*p in sum2:
                result += sum1[p] * sum2[-1*p]
        return result

a = []
b = []
c = []
d = []
s=Solution()
print(s.fourSumCount(a,b,c,d))


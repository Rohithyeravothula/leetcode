class Solution:
    # @param A : list of integers
    # @return an integer
    def cntBits(self, A):
        count = 0 
        l = len(A)
        iter_count = 0
        while iter_count < 32:
            iter_count += 1
            ones = 0
            zeros = 0
            break_con = True
            for i in range(0, l):
                b = A[i]&1
                if b==1:
                    ones +=1
                else:
                    zeros+=1
                A[i] = A[i] >> 1
            count += ones*zeros
        return 2*count

s=Solution()
print(s.cntBits([1,3,5]))

class Solution:
    def kthGrammar2(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        N=N-1
        K=K-1
        ans = ["0", "01", "0110"]
        if N > 2:
            s="01101001"
            N = N-3
            l = 8
            new = s
            while N:
                new = s[:]
                a,b = s[0:l//2], s[l//2:l]
                new = new + b+a
                s=new
                N=N-1
                l = l*2
            # print(new)
            return int(new[K])
        else:
            return int(ans[N][K])
    def kthGrammarHelper(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        print(N,K, 2**(N-1))
        ans = ["0", "01", "0110", "01101001"]
        if N > 3:
            l = 2 ** (N-1)
            if K < l:
                return self.kthGrammarHelper(N-1, K)
            else:
                K = K - l
                if K >= l//2:
                    return self.kthGrammarHelper(N-1, K - l//2)
                else:
                    return self.kthGrammarHelper(N-1, K + l//2)
        else:
            return int(ans[N][K])

    def kthGrammar(self, N, K):
        return self.kthGrammarHelper(N-1, K-1)



s=Solution()
i=30
j=43499199
# j=19
print(s.kthGrammar(i,j), s.kthGrammar2(i,j))
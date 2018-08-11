class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        def get_val(n, k):
            # print(n, k)
            if n == 1:
                return "0"

            if n == 2:
                return "01"[k]

            if n == 3:
                return "0110"[k]

            if n == 4:
                return "01101001"[k]

            else:
                l = 1<<(n-1)
                if k >= 0 and k < l//2:
                    return get_val(n-1, k)
                elif k >= l//2 and k < (3*l)//4:
                    return get_val(n-1, k-(l//4))
                else:
                    return get_val(n-1, k-3*(l//4))
        return int(get_val(N, K-1))


s = Solution()
n = 6
ans = ""

for i in range(1, 1 + (1 << (n-1))):
    print(n, i)
    ans += str(s.kthGrammar(n, i))
print(ans)
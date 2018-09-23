class Solution:
    def convert(self, s, n):
        if n==1:
            return s
        response = []
        l = len(s)
        for i in range(l):
            index = 2*i*(n-1)
            if index >= l:
                break
            response.append(s[index])

        for i in range(1, n-1):
            for j in range(0, l):
                index = i + 2*j*(n-1) - 2*i
                if index >= 0 and index < l:
                    response.append(s[index])
                index += 2*i
                if index < l:
                    response.append(s[index])
        
        if n>1:
            for i in range(l):
                index = (n-1)*(2*i+1)
                if index >= l:
                    break
                response.append(s[index])

        return "".join(response)

s = Solution()
print(s.convert("BAB", 2))

class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        
        def check(a,b,c, seen):
            print(a,b,c,seen)
            if (a,b) in seen:
                return seen[(a,b)]

            if a=="" or b=="":
                if a=="" and b==c:
                    seen[(a,b)] = True
                    return True
                elif b=="" and a==c:
                    seen[(a,b)] = True
                    return True
                return False
            
            c1,c2 = False, False
            if a[-1] == c[-1]:
                c1 = check(a[:-1], b, c[:-1], seen)
            if b[-1] == c[-1]:
                c2 = check(a, b[:-1], c[:-1], seen)
            r = c1 or c2 
            seen[(a,b)] = r 
            return r

        return check(s1, s2, s3, {})

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
s1 = ""
s2 = "" 
s3 = ""
s1="aabc"
s2="abad"
s3="aabadabc"
print(Solution().isInterleave(s1, s2, s3))


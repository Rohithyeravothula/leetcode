class Solution:
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        i = 0
        l = len(s)
        j = l-1
        while i<j:
        	if s[i].isalpha() and s[j].isalpha():
        		s[i],s[j] = s[j], s[i]
        		i+=1
        		j-=1
        	while i<l and not s[i].isalpha():
        		i+=1
        	while j>=0 and not s[j].isalpha():
        		j-=1
        return "".join(s)

print(Solution().reverseOnlyLetters("hello_"))
print(Solution().reverseOnlyLetters("ab-cd"))
print(Solution().reverseOnlyLetters("a-bC-dEf-ghIj"))
print(Solution().reverseOnlyLetters("Test1ng-Leet=code-Q!"))
print(Solution().reverseOnlyLetters(""))
print(Solution().reverseOnlyLetters("abc"))
print(Solution().reverseOnlyLetters("abcd"))

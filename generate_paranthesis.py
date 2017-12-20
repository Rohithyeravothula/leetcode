class Solution:
    def valid_parenthesis(self, input_string):
        count = 0
        for i in input_string:
            if i == "(":
                count += 1
            else:
                count -= 1
            if count < 0:
                return False
        return count == 0
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        cur = [""]
        count = 0
        max_count = 2*n
        while count < max_count:
            count += 1
            local = []
            for i in cur:
                local.append(i + "(")
                local.append(i + ")")
            cur = local
        return [i for i in cur if self.valid_parenthesis(i)]
        

s=Solution()
print(s.generateParenthesis(0))
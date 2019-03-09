class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        def get_type(d):
            for val in d:
                if not val.isnumeric():
                    return False
            return True

        alphs = []
        numeric = []
        for log in logs:
            idf, *rest = log.split()
            if get_type(rest):
                numeric.append(log)
            else:
                alphs.append((" ".join(rest), idf, log))
        alphs.sort()
        alphs = [log for _,_,log in alphs]
        return alphs + numeric
        

inp = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
inp = ["g2 act car", "g1 act car"]
print(Solution().reorderLogFiles(inp))
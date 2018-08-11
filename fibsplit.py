class Solution:
    def splitIntoFibonacci(self, fibstr):
        """
        :type S: str
        :rtype: List[int]
        """
        lmt = (2**31) - 1
        def check(a):
            for i in a:
                if i < 0 or i > lmt:
                    return []
            return a
        def recr_split(f1, f2, curstr):
            # print(f1, f2, curstr)
            s = str(f1+f2)
            l = len(s)
            splits = [f1,f2]
            if curstr[0:l] == s:
                splits.append(int(curstr[0:l]))
                if l < len(curstr):
                    next_list = recr_split(f2, int(curstr[0:l]), curstr[l:])
                    if not next_list:
                        return None
                    splits.extend(next_list[2:])
                return splits
            else:
                return None
            


        l = len(fibstr)
        for i in range(1, l):
            for j in range(i, l):
                f1 = fibstr[0:i]
                f2 = fibstr[i:j+1]
                if str(int(f1)) != f1 or str(int(f2)) != f2:
                    break
                f1 = int(f1)
                f2 = int(f2)

                possplit = recr_split(f1, f2, fibstr[j+1:])
                # print(possplit)
                if possplit:
                    return check(possplit)
        return []


# fibs = "11235813"
# fibs = "123456579"
# fibs = "112358130"
# fibs = "0123"
# fibs = "1101111"
# fibs = "189"
fibs = ""
s=Solution()
print(s.splitIntoFibonacci(fibs))

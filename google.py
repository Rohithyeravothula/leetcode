def solution(A,B):
    la = len(A)
    lb = len(B)
    if la<lb:
        count = int((lb-la)/la)
        if (lb-la) % la > 0:
            count += 2
        else:
            count += 1
        s=""
        for i in range(0, count):
            s+=A
        if B in s:
            return count
        else:
            s=s+A
            if B in s:
                return count+1
    else:
        if B in A:
            return 1
        else:
            if B in A+A:
                return 2
    return -1

a = solution("abaabaa", "abaababaab")
print(a)
# "abaabaa"


# class Solution(object):
    # def repeatedStringMatch(self, A, B):
    #     """
    #     :type A: str
    #     :type B: str
    #     :rtype: int
    #     """
    #     la = len(A)
    #     lb = len(B)
    #     if la<lb:
    #         count = int((lb-la)/la)
    #         if (lb-la) % la > 0:
    #             count += 2
    #         else:
    #             count += 1
    #         s=""
    #         for i in range(0, count):
    #             s+=A
    #         if B in s:
    #             return count
    #         else:
    #             s=s+B
    #             if B in s:
    #                 return count+1
    #     else:
    #         if B in A:
    #             return 1
    #         else:
    #             if B in A+A:
    #                 return 2
    #     return -1
    #         
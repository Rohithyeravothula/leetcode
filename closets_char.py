# Complete the closest function below.
from collections import defaultdict
def binary_search(inp, num):
    l = len(inp)
    if l == 1:
        return None, None
    if num == inp[0]:
        return None, inp[1]
    if num == inp[-1]:
        return inp[-2], None

    i = 0
    j = l-1
    ans = None
    while i<=j:
        m = (i+j) >> 1
        if num == inp[m]:
            return inp[m-1], inp[m+1]
        elif inp[m] > num:
            j = m-1
        else:
            i = m+1


def search(inp, num):
    if len(inp) == 1:
        return None, None
    if num == inp[0]:
        return None, inp[1]
    if num == inp[-1]:
        return inp[-2], None
    for i, v in enumerate(inp):
        if v == num:
            return inp[i-1], inp[i+1]



def closest(s, queries):
    char_index = defaultdict(list)
    for i, c in enumerate(list(s)):
        char_index[c].append(i)

    ans = []
    for q in queries:
        left, right = binary_search(char_index[s[q]], q)
        # print(q, left, right, q-left, right-q)
        if left is None and right is None:
            ans.append(-1)
        elif left is None:
            ans.append(right)
        elif right is None:
            ans.append(left)
        elif (q - left) <= (right - q):
            # print(q, left, right, q-left, right-q)
            ans.append(left)
        else:
            # print(q-left, right-q)
            ans.append(right)
    return ans

ss = "aaaa"
q = [0, 1, 2, 3]
print(closest(ss, q))

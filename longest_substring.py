def get_max(a):
    max_l = 0
    max_e = None
    for index, val in enumerate(a):
        if max_l < val:
            max_l = val
            max_e = index
    return max_l, max_e
def substring(s1, s2):
    if not s1 or not s2:
        return ""
    if len(s1) < len(s2):
        s1, s2 = s2, s1
    ls1 = len(s1)
    ls2 = len(s2)
    opt = [1 if s1[0] == s2[i] else 0 for i in range(ls2)]
    max_l, max_e = get_max(opt)
    i = 1
    while i<ls1:
        cur = [0]*ls2
        if s1[i] == s2[0]:
            cur[0] = 1
        for j in range(1, ls2):
            if s1[i] == s2[j]:
                cur[j] = 1 + opt[j-1]
        opt = cur
        cur_l, cur_e = get_max(opt)
        if max_l < cur_l:
            max_l = cur_l
            max_e = cur_e
        i+=1
    if max_l > 0:
        return s2[max_e - max_l+1: max_e+1]
    return ""






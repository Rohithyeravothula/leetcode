def replace(inp):
    c = 0
    count = 0
    for i in inp:
        if i=="<":
            c+=1
        else:
            if c==0:
                count += 1
            else:
                c-=1
    return count if c == 0 else float("inf")

def balancedOrNot(expressions, maxReplacements):
    return [1 if replace(exp) <= expm else 0 for exp, expm in zip(expressions, maxReplacements)]

expinp = ["<<<>"]
maxinp = [2]
print(balancedOrNot(expinp, maxinp))


"""
"""
# Complete the getShiftedString function below.
def getShiftedString(s, leftShifts, rightShifts):
    l = len(s)
    slist = list(s)
    leftShifts = leftShifts % l
    rightShifts = rightShifts % l
    if leftShifts > rightShifts:
        leftShifts -= rightShifts
        left = slist[0:leftShifts][::-1]
        right = slist[leftShifts:][::-1]
        ans = "".join(left) + "".join(right)
        return ans[::-1]
    else:
        rightShifts -= leftShifts
        right = slist[-rightShifts:][::-1]
        left = slist[:-rightShifts][::-1]
        ans = "".join(left) + "".join(right)
        return ans[::-1]
   

def ncr(n, r):
   r = min(r, n-r)
   numer = reduce(op.mul, range(n, n-r, -1), 1)
   denom = reduce(op.mul, range(1, r+1), 1)
   return numer//denom     

print(getShiftedString("abc", 2, 1))
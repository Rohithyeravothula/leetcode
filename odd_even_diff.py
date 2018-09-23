# Complete the maxDifferenceOddEven function below.
def maxDifferenceOddEven(a):
    cur_max = -1*float("inf")
    prev_min = float("inf")
    for val in a:
        if (val & 1):
            prev_min = min(prev_min, val)
        else:
            cur_max = max(cur_max, val-prev_min)
    if prev_min != float("inf"):
        return prev_min
    return -1
        

a = [2,3,10,1,4,8,1]
maxDifferenceOddEven(a)
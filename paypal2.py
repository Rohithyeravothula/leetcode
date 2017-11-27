import math
def maxSubsetSum(k):
    # Complete this function
    def multiples_sum(n):
        if n==1:
            return 1
        elif n==2:
            return 3
        elif n==3:
            return 4
        s=int(math.sqrt(n)+1)
        a=[]
        for i in range(2, s):
            if n%i==0:
                if i*i!=n:
                    a.append(i)
                    a.append(int(n/i))
                else:
                    a.append(i)
        a.append(n)
        print(a)
        return sum(a)+1
    ans = []
    for num in k:
        ans.append(multiples_sum(num))
    for i in ans:
        print(i)
    return []

te=[1]
maxSubsetSum(te)

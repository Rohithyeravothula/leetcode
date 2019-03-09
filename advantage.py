class Solution:
    def advantageCount(self, a,b):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        c = list(a)
        b = [(val, idx) for idx,val in enumerate(b)]
        c.sort()
        b.sort()
        l = len(a)
        i=0
        j=0
        updated = set()
        while i<l and j<l:
            if c[i] > b[j][0]:
                a[b[j][1]] = c[i]
                updated.add(b[j][1])
                j+=1
            i+=1
        j=0
        for i in range(l):
            if i not in updated:
                a[i] = c[j]
                j+=1
        return a

a,b=[2,7,11,15],[1,10,4,11]
a,b=[12,24,8,32],[13,25,32,11]
a,b=[1,2,3,4,5],[4,5,6,7,8]
a,b=[],[]
a,b=[1,2,3,4,5],[4,5,3,3,3]
print(Solution().advantageCount(a,b))


        
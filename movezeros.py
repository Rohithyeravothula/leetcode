a=[1, 1, 1, 0]
l=len(a)
s=0
e=-1
while s<l and e<l:
    while s<l and a[s]!=0:
        s+=1
    if e == -1:
        e=s
    while e<l and a[e]==0:
        e+=1
    if e<l and s<l:
        d=a[s]
        a[s]=a[e]
        a[e] = d

print(a)


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l=len(a)
        s=0
        e=-1
        while s<l and e<l:
            while s<l and a[s]!=0:
                s+=1
            if e == -1:
                e=s
            while e<l and a[e]==0:
                e+=1
            if e<l and s<l:
                d=a[s]
                a[s]=a[e]
                a[e] = d

        
            
            
        

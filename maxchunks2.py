class Solution:

    def maxchunks(self, arr):
        cur = 0
        l = len(arr)
        if l == 1:
            return l
        chunks = 0
        prev = cur
        while cur < l:
            limit = arr[cur]
            while cur <= limit:
                limit = max(limit, arr[cur])
                cur += 1
            chunks+=1
            if prev == cur:
                cur += 1
            prev=cur
        return chunks

    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        indexmap = {}
        l = len(arr)
        dum = arr[:]
        dum.sort()
        for i in range(0, l):
            if dum[i] in indexmap:
                indexmap[dum[i]].append(i)
            else:
                indexmap[dum[i]] = [i]
        mapped = []
        for i in range(0, l):
            mapped.append(indexmap[arr[i]][0])
            indexmap[arr[i]] = indexmap[arr[i]][1:]
        print(mapped)
        return self.maxchunks(mapped)

a=[2,1,3,4,4]
s=Solution()
print(s.maxChunksToSorted(a))

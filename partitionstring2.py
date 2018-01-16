class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        a={}
        l = len(S)
        for i in range(0, l):
            a[S[i]] = i
        print(a)
        start = 0
        ans = []
        while start<l:
            index = start
            cur = a[S[start]]
            while start<cur and start<l:
                start+=1
                cur=max(cur, a[S[start]])
            ans.append(cur-index+1)
            start+=1
        return ans



input_string="daba"
s=Solution()
print(s.partitionLabels(input_string))

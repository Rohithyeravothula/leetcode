class Solution:
    def shiftingLetters(self, input_str, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        s = sum(shifts)
        shift_sums = [s]
        l = len(shifts)
        for i in range(1, l):
        	shift_sums.append(s - shifts[i-1])
        	s = s - shifts[i-1]

        ans = ""
        for i in range(0, l):
        	newc = 97 + (ord(input_str[i]) - 97 + (shift_sums[i])%26)%26
        	ans += chr(newc)
        return ans


        


s = Solution()
ss = "z"
shifts = [3]
print(s.shiftingLetters(ss, shifts))
class Solution:
    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        def avg(a, l):
            if l==0:
                return float("inf")*-1
            return sum(a)/l

        total_length = len(A)
        if total_length == 0:
            return False
        s = sum(A)
        final_avg = s/(1.0*total_length)
        half_sum = s/2

        def check(left, i, track):
            # print(left, i, track)
            left_length = len(left)
            right_length = total_length - left_length
            if left_length == total_length or i==total_length:
                print(left)
                return False
            left_sum = sum(left)
            left_avg = avg(left, left_length)
            right_avg = (s - left_sum)/right_length
            right_sum = s - left_sum
            if left_avg == right_avg:
                return True
            # if left_sum > half_sum:
            #     track[(left_sum, left_length)] = False
            #     track[(right_sum, right_length)] = False
            #     return False
            if (left_sum, left_length) in track:
                return track[(left_sum, left_length)]
            if (right_sum, right_length) in track:
                return track[(right_sum, right_length)]
            new_left = left + [A[i]]
            val = check(new_left, i+1, track) or check(left, i+1, track)
            track[(left_sum, left_length)] = val
            track[(right_sum, right_length)] = val
            return val
        
        A.sort()
        dp = {}
        return check([], 0, dp) or check([A[0]], 0, dp)

# aa=[0,13,13,7,5,0,10,19,5]
# aa=[1,2,3,4,5,6,7,8]
# aa=[4,4,4]
aa = [73,37,34,95,4,97,22,53,55,52,46,44,71,24,26,35,96,3]
# aa=[5,5,5]
s=Solution()
print(s.splitArraySameAverage(aa))
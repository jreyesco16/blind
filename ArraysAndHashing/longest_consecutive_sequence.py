from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums) # set

        m, t = 0, 0 # max, temp
        for n in nums:
            # check if n is the beginning of sequence
            if n-1 not in s:
                t = 1
                
                c = n + 1 # current
                while c in s:
                    t += 1
                    c +=1

                if m < t:
                    m = t

        return m
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0

        for n in nums:
            c = 0

            if n-1 not in s:
                c += 1
                t = n

                while t+1 in s:
                    c += 1
                    t += 1
                    
            ans = max(c, ans)
            
        return ans
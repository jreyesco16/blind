from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new = set(nums)
        ans = 0

        for num in nums:
            count = 0
            if num-1 not in new:
                count += 1
                temp = num
                while temp+1 in new:
                    count += 1
                    temp += 1
                    
            ans = max(count, ans)
            
        return ans
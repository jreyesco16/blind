from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, pos = 1, 1

        pre_nums, pos_nums = [None]*len(nums), [None]*len(nums)

        for i in range(len(nums)):
            pre *= nums[i]

            pre_nums[i] = pre

        for i in range(len(nums)-1, -1, -1):
            pos *= nums[i]
            
            pos_nums[i] = pos
        
        for i in range(len(nums)):
            if i == 0:
                nums[i] = pos_nums[i+1]
            elif i == len(nums)-1:
                nums[i] = pre_nums[i-1]
            else:
                nums[i] = pre_nums[i-1] * pos_nums[i+1]

        return nums
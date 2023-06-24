from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, pos = 1, 1

        pre_list, pos_list = [None]*len(nums), [None]*len(nums)

        for i in range(len(nums)): 
            pre *= nums[i]
            pre_list[i] = pre

            pos *= nums[len(nums)-1-i]
            pos_list[len(nums)-1-i] = pos

        for i in range(len(nums)):
            if i == 0:
                nums[i] = pos_list[i+1]
            elif i == len(nums)-1:
                nums[i] = pre_list[i-1]
            else:
                nums[i] = pre_list[i-1]*pos_list[i+1]

        return nums
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, pos = 1,1

        pre_list, pos_list = [None] * len(nums), [None] * len(nums)

        for i in range(len(nums)):
            pre_list[i] = pre * nums[i]

            pre = pre_list[i]


            pos_list[(len(nums)-1)-i] = pos * nums[(len(nums)-1)-i]

            pos = pos_list[(len(nums)-1)-i]

        res_list = [1] * len(nums)

        for i in range(len(res_list)):
            if i == 0:
                res_list[i] = pos_list[i+1]
                continue
            elif i == len(nums)-1:
                res_list[i] = pre_list[i-1]
                continue

            res_list[i] = pre_list[i-1] * pos_list[i+1]


        return res_list
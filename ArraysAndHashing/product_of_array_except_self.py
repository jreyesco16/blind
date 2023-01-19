from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        pre, pos = 1, 1
        pa = [1]*l

        for i in range(l):
            pa[i] *= pre
            pre = pre*nums[i]
            pa[l-i-1] *= pos
            pos *= nums[l-i-1]

        return pa
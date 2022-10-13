class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[:-1]), self.helper(nums[1:]))

    def helper(self, nums):
        prevRob, currRob = 0, 0
    
        for n in nums:
            tmp = max(n + prevRob, currRob)
            prevRob = currRob
            currRob = tmp

        return currRob
    
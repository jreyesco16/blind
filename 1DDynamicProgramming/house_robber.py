class Solution:
    def rob(self, nums: List[int]) -> int:
       
        prevRob = currRob = 0
    
        for n in nums:
            tmp = max(n + prevRob, currRob)
        
            prevRob = currRob
        
            currRob = tmp
    
        return currRob
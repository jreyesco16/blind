class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        threeSums = []
        
        nums.sort()
        
        for i, n in enumerate(nums):
            if n == nums[i-1] and i != 0:
                continue
            
            l, r = i+1, len(nums)-1
            
            while l < r:
                v = n + nums[l] + nums[r]
                
                # too high
                if v > 0:
                    r-=1
                # too low
                elif v < 0:
                    l+=1
                else:
                    threeSums.append([n, nums[l], nums[r]])
                
                    l+=1
                    
                    while nums[l-1] == nums[l] and l < r:
                        l+=1
        
        return threeSums
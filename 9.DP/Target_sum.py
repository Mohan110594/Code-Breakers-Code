# Memoization
#TIme comp --> o(len(nums) * sum)
#space comp --> o(len(nums) * sum)
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        
        if sum(nums)<S:
            return 0
        
        
        cache=dict()
        
        return self.helper(0,nums,S,cache)
        
        
        
        
    def helper(self,curr, nums,S,cache):
        key = (curr, tuple(nums))
        if key in cache: 
            return cache[key]
        if not nums: return 1 if curr == S else 0           
        
        res = self.helper(curr - nums[0], nums[1:],S,cache) + self.helper(curr + nums[0], nums[1:],S,cache)
        cache[key] = res
        return res
        
        
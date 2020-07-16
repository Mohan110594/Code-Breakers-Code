class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max=0
        maxi=float('-inf')
        for i in range(len(nums)):
            curr_max=max(nums[i],curr_max+nums[i])
            
            maxi=max(maxi,curr_max)
            
        return maxi
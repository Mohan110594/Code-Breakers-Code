#Time comp --> o(n)
#space comp --> o(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=float('-inf')
        curr_max=0
        for i in range(len(nums)):
            curr_max=max(nums[i],curr_max+nums[i])
            maxi=max(maxi,curr_max)
        return maxi
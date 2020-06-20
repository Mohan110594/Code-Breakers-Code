#Time comp --> o(n)
#space comp --> o(1)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dest=0
        
        for i in range(len(nums)):
            if i>dest:
                return False
            dest=max(dest,nums[i]+i)
        return True
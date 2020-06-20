#Time comp --> o(n)
#space comp --> o(1)
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dest=len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if i+nums[i]>=dest:
                dest=i
            
        return dest==0
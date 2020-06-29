#Time commp --> o(log n)
#space comp --> o(1)

class Solution(object):
    def bs_first_pos(self,target,nums):
        start=0
        end=len(nums)-1
        while start<=end:
            mid=start+((end-start)//2)
            # print(start,end,mid)
            if nums[mid]==target:
                while mid-1>=0 and nums[mid]==nums[mid-1]:
                    mid=mid-1
                return mid
            elif nums[mid]>target:
                end=mid-1
            else:
                start=mid+1
        return -1

    def bs_last_pos(self,target,nums):
        start=0
        end=len(nums)-1
        while start<=end:
            mid=start+((end-start)//2)
            # print(start,end,mid)
            if nums[mid]==target:
                while mid+1<len(nums) and nums[mid]==nums[mid+1]:
                    mid=mid+1
                return mid
            elif nums[mid]>target:
                end=mid-1
            else:
                start=mid+1
        return -1
    
    
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums)==0:
            return [-1,-1]
        
        first_pos=self.bs_first_pos(target,nums)
        last_pos=self.bs_last_pos(target,nums)
        
        return [first_pos,last_pos]
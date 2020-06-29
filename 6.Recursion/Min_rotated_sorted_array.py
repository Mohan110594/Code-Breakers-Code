#Time comp --> o(logn )
#space comp --> o(1)
# Template 2:
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low=0
        high=len(nums)-1
        
        if len(nums)==1:
            return nums[0]
        # when the elements are in ascending order
        
        if nums[high]>nums[low]:
            return nums[low]
        
        while low<=high:
            mid=low+((high-low)//2)
            
            # if middle element is greater than the next mid element(Inflection point)
            if nums[mid]>nums[mid+1]:
                return nums[mid+1]
            
            # If the mid element is less than prev mid element
            if nums[mid]<nums[mid-1]:
                return nums[mid]
            # else move the low and high pointers
            if nums[mid]>nums[low]:
                low=mid+1
                
            else:
                high=mid-1
        
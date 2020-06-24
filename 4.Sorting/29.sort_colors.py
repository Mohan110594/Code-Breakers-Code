#Time comp -->o(n)
#space comp -->o(1)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low=0
        mid=0
        high=len(nums)-1
        if len(nums)==0:
            return nums
        while mid<=high:
            if nums[mid]==2:
                nums[mid],nums[high]=nums[high],nums[mid]
                high=high-1
            elif nums[mid]==1:
                mid=mid+1
            else:
                nums[low],nums[mid]=nums[mid],nums[low]
                low=low+1
                mid=mid+1
        
        return nums
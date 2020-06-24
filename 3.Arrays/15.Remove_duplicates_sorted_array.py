#Time comp --> o(n)
#space comp --> o(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start=0
        i=1
        while i<len(nums):
            if nums[start]!=nums[i]:
                start=start+1
                nums[start]=nums[i]
                
            i=i+1
        
        return start+1
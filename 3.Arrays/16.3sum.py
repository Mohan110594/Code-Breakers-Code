#Time comp --> o(n**2)
#space comp --> o(n)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                i=i+1
                continue
            target=-(nums[i])
            low=i+1
            high=len(nums)-1
            while low<high:
                if nums[low]+nums[high]==target:
                    res.append([nums[i],nums[low],nums[high]])
                    low=low+1
                    high=high-1
                    while 0<=low-1<len(nums)-1 and nums[low]==nums[low-1]:
                        low=low+1
                    while 0<=high+1<len(nums)-1 and  nums[high+1]==nums[high]:
                        high=high-1
                elif nums[low]+nums[high]<target:
                    low=low+1
                else:
                    high=high-1
        return res
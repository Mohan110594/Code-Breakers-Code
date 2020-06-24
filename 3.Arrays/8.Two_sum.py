#Time comp --> o(n)
#space comp --> o(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited=dict()
        if len(nums)==0:
            return []
        for i in range(len(nums)):
            if target-nums[i] in visited:
                return [visited[target-nums[i]],i]
            visited[nums[i]]=i